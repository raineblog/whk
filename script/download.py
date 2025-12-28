import os
import queue
import concurrent.futures
from playwright.sync_api import sync_playwright

def pdf_worker(worker_id: int, task_queue: queue.Queue):
    print(f"[Worker-{worker_id}] 启动")

    # 在线程内部初始化 Playwright
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        
        # 持续从队列中获取任务，直到收到 "None" 这个哨兵信号
        while True:
            try:
                # 从队列中获取一个任务，如果队列为空则阻塞等待
                task = task_queue.get()
                
                # 收到哨兵信号，表示所有任务已完成，可以退出循环
                if task is None:
                    break

                url, filename = task
                print(f"[Worker-{worker_id}] 开始处理: {url}")

                page = None
                try:
                    page = context.new_page()
                    page.goto(url, wait_until="networkidle")
                    
                    page.pdf(
                        path=filename,
                        format="A4",
                        margin={
                            "top": "25.5mm",
                            "bottom": "25.5mm",
                            "left": "19mm",
                            "right": "19mm"
                        },
                        print_background=True,
                    )
                    print(f"[Worker-{worker_id}] 成功创建文件: {filename}")
                except Exception as e:
                    print(f"[Worker-{worker_id}] 错误: 处理 {url} 失败: {e}")
                finally:
                    if page:
                        page.close()
                    # 标记任务完成
                    task_queue.task_done()

            except Exception as e:
                print(f"[Worker-{worker_id}] 发生严重错误: {e}")
                # 确保即使发生意外，也能标记任务完成，避免主线程死锁
                task_queue.task_done()

        # 关闭长期存在的浏览器实例
        browser.close()
        print(f"[Worker-{worker_id}] 关闭浏览器，任务完成。")

def convertHtmlToPdf(url_list, max_threads: int = 4):
    print(f"--- 任务开始: 共 {len(url_list)} 个 URL，最大并发数 {max_threads} ---")

    # 创建一个线程安全的队列来存放所有任务
    task_queue = queue.Queue()
    for item in url_list:
        task_queue.put(item)
        if os.path.exists(item[1]):
            os.remove(item[1])

    # 使用 ThreadPoolExecutor 来管理我们的工作线程
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        # 启动 max_threads 个工作线程
        # 每个工作线程都会运行 pdf_worker 函数
        for i in range(max_threads):
            executor.submit(pdf_worker, i, task_queue)
    
        # 等待队列中的所有任务都被处理完毕
        # task_queue.join() 会阻塞，直到队列中每个 item 都被 get() 并且调用了 task_done()
        task_queue.join()

        # 所有任务处理完毕后，向队列中放入哨兵信号 (None)
        # 以便每个工作线程都能退出其 while True 循环
        for _ in range(max_threads):
            task_queue.put(None)

    print("--- 所有任务完成 ---")

def Main():
    print("test download")
    convertHtmlToPdf([
        ["https://blog.rainppr.dns-dynamic.net/whk/science/sequence/1/", "数列 1.pdf"],
        ["https://blog.rainppr.dns-dynamic.net/whk/science/sequence/2/", "数列 2.pdf"],
        ["https://blog.rainppr.dns-dynamic.net/whk/science/sequence/3/", "数列 3.pdf"],
        ["https://blog.rainppr.dns-dynamic.net/whk/science/sequence/4/", "数列 4.pdf"],
    ])

if __name__ == "__main__":
    Main()
