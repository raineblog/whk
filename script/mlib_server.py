import os
import socket
import random
import threading
import asyncio
from aiohttp import web

# 保存服务器实例的全局变量，用于关闭
_server_runner = None
_server_thread = None
_server_loop = None

def get_free_port(start=10000, end=60000):
    """
    在指定范围内随机寻找一个可用端口。
    """
    range_size = end - start
    # 尝试一定次数，避免死循环
    for _ in range(100):
        port = random.randint(start, end)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            # 尝试绑定
            sock.bind(('127.0.0.1', port))
            sock.close()
            return port
        except OSError:
            # 端口被占用，继续尝试
            continue
    raise RuntimeError("无法找到可用的端口，请检查端口范围或系统状态。")

async def _high_perf_middleware(app, handler):
    """
    中间件：深度优化 HTTP 响应头
    1. 允许 CORS (解决字体/资源跨域问题)
    2. 强制缓存 (极大幅度提升 Playwright 批量打印速度)
    """
    async def middleware_handler(request):
        response = await handler(request)
        
        # --- 优化 1: CORS 设置 ---
        # 允许所有来源，防止 Playwright 加载外部 HTTPS 字体时被拦截
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        
        # --- 优化 2: 强缓存策略 (关键性能点) ---
        # 对于 Playwright 打印，静态文件通常不会变。
        # 设置强缓存可以让 1500 个页面复用同一个 CSS/Logo 文件，
        # 减少 99% 的 I/O 和网络请求。
        # max-age=86400 (1天)
        response.headers['Cache-Control'] = 'public, max-age=86400'
        
        return response
    return middleware_handler

def _run_aiohttp_server(host, port, site_path, ready_event):
    """
    在子线程中运行 aiohttp 服务器
    """
    global _server_runner, _server_loop
    
    # 创建一个新的事件循环用于该线程
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    _server_loop = loop

    app = web.Application(middlewares=[_high_perf_middleware])
    
    # 静态文件路由
    # chunk_size 默认即可，aiohttp 内部已经对大文件传输做了 sendfile 零拷贝优化
    app.router.add_static('/', site_path, show_index=True, follow_symlinks=True)

    # 配置启动器
    # access_log=None 是关键优化，在大批量并发时，
    # 避免向控制台打印数万条日志导致的 I/O 阻塞。
    runner = web.AppRunner(app, access_log=None) 
    
    try:
        loop.run_until_complete(runner.setup())
        site = web.TCPSite(runner, host, port)
        loop.run_until_complete(site.start())
        
        # 保存 runner 以便后续关闭
        _server_runner = runner
        
        # 通知主线程服务器已启动
        ready_event.set()
        
        # 保持运行直到被停止
        loop.run_forever()
    except Exception as e:
        print(f"Server Error: {e}")
    finally:
        # 清理工作会在 stop_server 中处理
        pass

def start_local_server(site_path='./site'):
    """
    启动本地高性能 HTTP 服务器。
    
    :param site_path: 静态网站根目录
    :return: 服务器 URL (例如 http://127.0.0.1:12345)
    """
    global _server_thread
    
    # 1. 检查目录是否存在，不存在则自动创建，防止报错
    if not os.path.exists(site_path):
        os.makedirs(site_path)
        # 创建一个测试文件，方便验证
        with open(os.path.join(site_path, 'index.html'), 'w', encoding='utf-8') as f:
            f.write('<h1>High Performance Server Running</h1>')

    # 2. 获取随机端口
    host = '127.0.0.1'
    port = get_free_port()
    
    # 3. 线程同步事件，用于等待服务器真正启动后再返回
    ready_event = threading.Event()
    
    # 4. 在独立线程中启动服务器
    _server_thread = threading.Thread(
        target=_run_aiohttp_server,
        args=(host, port, site_path, ready_event),
        daemon=True  # 设置为守护线程，主程序退出时它也会强制退出
    )
    _server_thread.start()
    
    # 5. 阻塞等待，直到服务器线程发出“准备就绪”信号
    # 这样可以确保函数返回时，服务器一定是可以访问的
    ready_event.wait()
    
    url = f"http://{host}:{port}"
    print(f"🚀 本地服务器已启动 (高性能模式): {url}")
    print(f"📂 根目录: {os.path.abspath(site_path)}")
    print(f"⚡ 优化: 日志已关闭, 强缓存已开启, CORS 已允许")
    
    return url

def stop_local_server():
    """
    关闭服务器并释放资源
    """
    global _server_runner, _server_loop, _server_thread
    
    print("🛑 正在关闭服务器...")
    
    if _server_runner and _server_loop:
        # 跨线程停止 asyncio 循环需要使用 call_soon_threadsafe
        # 定义一个异步清理函数
        async def shutdown():
            await _server_runner.cleanup()
            _server_loop.stop()

        future = asyncio.run_coroutine_threadsafe(shutdown(), _server_loop)
        try:
            future.result(timeout=5) # 等待清理完成
        except Exception as e:
            print(f"关闭时发生警告 (通常可忽略): {e}")

    # 等待线程结束
    if _server_thread and _server_thread.is_alive():
        _server_thread.join(timeout=2)
        
    print("✅ 服务器已关闭")
