import httpx
from urllib.parse import quote
import xmlrpc.client

RPC_LIST = [
    "http://rpc.pingomatic.com",
    "http://blogsearch.google.com/ping/RPC2",
    "http://ping.feedburner.com",
]


def submit_sitemap_ping(site_name: str, site_url: str, sitemap_url: str) -> None:
    """
    使用 HTTP GET 向搜索引擎的 Sitemap 接收接口发送通知。
    """
    encoded_sitemap = quote(sitemap_url)
    encoded_url = quote(site_url)
    encoded_name = quote(site_name)

    ping_list = {
        "Google": f"http://www.google.com/ping?sitemap={encoded_sitemap}",
        "Bing": f"https://www.bing.com/ping?sitemap={encoded_sitemap}",
        "Sogou": f"http://ping.sogou.com/ping?sitemap={encoded_sitemap}",
        "FeedBurner": f"http://www.feedburner.com/fb/a/pingSubmit?bloglink={encoded_url}",
        "Yandex": f"http://blogs.yandex.ru/pings/?blogname={encoded_name}&blogurl={encoded_url}",
    }

    print("[Sitemap Ping] 开始发送 Sitemap 接收接口的 HTTP 请求...")
    for name, endpoint in ping_list.items():
        try:
            response = httpx.get(endpoint, follow_redirects=True, timeout=10.0)
            print(f"[Sitemap Ping] ✅ {name} 响应状态码: HTTP {response.status_code}")
        except Exception as e:
            print(f"[Sitemap Ping] ❌ {name} 接口请求异常: {e}")


def submit_rpc_ping(site_name: str, site_url: str) -> None:
    """
    通过 XML-RPC 对博客目录服务发送更新通知。
    """
    print("[RPC Ping] 开始发送 XML-RPC 更新请求...")
    for endpoint in RPC_LIST:
        try:
            server = xmlrpc.client.ServerProxy(endpoint, encoding="utf-8")
            result = server.weblogUpdates.ping(site_name, site_url)
            print(f"[RPC Ping] ✅ {endpoint} 成功: {result}")
        except Exception as e:
            print(f"[RPC Ping] ❌ {endpoint} 失败: {e}")
