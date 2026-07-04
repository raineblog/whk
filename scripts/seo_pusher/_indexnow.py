import os
import httpx

INDEXNOW_LIST = {
    "IndexNow": "https://api.indexnow.org/indexnow",
    "Bing": "https://www.bing.com/indexnow",
    "Yandex": "https://yandex.com/indexnow",
    "Naver": "https://searchadvisor.naver.com/indexnow",
    "Seznam": "https://search.seznam.cz/indexnow",
    "Yep": "https://indexnow.yep.com/indexnow"
}

def submit_to_indexnow(site_host: str, urls: list[str]) -> None:
    """
    使用 IndexNow API 推送 URL 列表。
    """
    if not urls:
        print("[IndexNow] 没有待提交的 URL。")
        return

    indexnow_key = os.environ.get("INDEXNOW_KEY")
    
    if not indexnow_key:
        print("[IndexNow] ⚠️ 未配置 INDEXNOW_KEY 环境变量，跳过 IndexNow 提交。")
        return

    key_location = f"https://{site_host}/{indexnow_key}.txt"

    payload = {
        "host": site_host,
        "key": indexnow_key,
        "keyLocation": key_location,
        "urlList": urls
    }
    
    headers = {"Content-Type": "application/json; charset=utf-8"}
    
    print(f"[IndexNow] 开始向 IndexNow 接口提交 {len(urls)} 个 URL...")
    for name, endpoint in INDEXNOW_LIST.items():
        try:
            response = httpx.post(endpoint, json=payload, headers=headers, timeout=15.0)
            if response.status_code in (200, 202):
                print(f"[IndexNow] ✅ {name} 提交成功 (HTTP {response.status_code})")
            else:
                print(f"[IndexNow] ❌ {name} 提交失败: HTTP {response.status_code}: {response.text}")
        except Exception as e:
            print(f"[IndexNow] ❌ {name} 请求异常: {e}")
