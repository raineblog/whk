import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/indexing"]


def submit_to_google_indexing(tasks: list[dict]) -> list[dict]:
    """
    使用 google-api-python-client 的 BatchHttpRequest 提交任务列表。
    每个 task 是: {"url": str, "action": "URL_UPDATED"|"URL_DELETED", "file_path": str}
    返回任务列表，其中已填充 'success': bool
    """
    if not tasks:
        print("[Google Indexing] 没有待提交的任务。")
        return []

    # 默认全部初始化为 success = False
    for t in tasks:
        t["success"] = False

    creds_json = os.environ.get("GOOGLE_INDEXING_CREDENTIALS")
    if not creds_json:
        print(
            "[Google Indexing] ⚠️ 未配置 GOOGLE_INDEXING_CREDENTIALS 环境变量，跳过 Google Indexing 提交。"
        )
        return tasks

    try:
        creds_data = json.loads(creds_json)
        credentials = service_account.Credentials.from_service_account_info(
            creds_data, scopes=SCOPES
        )
        # cache_discovery=False 能够防止在无写权限的临时目录中生成缓存文件警告
        service = build(
            "indexing", "v3", credentials=credentials, cache_discovery=False
        )
    except Exception as e:
        print(f"[Google Indexing] ❌ 凭证加载或 API 客户端初始化失败: {e}")
        return tasks

    success_ids = set()

    # 回调函数：处理批处理中每个请求的返回结果
    def batch_callback(request_id, response, exception):
        if exception is not None:
            print(f"[Google Indexing] ❌ 子任务 {request_id} 提交失败: {exception}")
        else:
            print(f"[Google Indexing] ✅ 子任务 {request_id} 提交成功")
            success_ids.add(request_id)

    try:
        # 创建批处理请求
        batch = service.new_batch_http_request(callback=batch_callback)

        # 将各任务添加进 batch
        for idx, task in enumerate(tasks):
            req_id = str(idx)
            body = {"url": task["url"], "type": task["action"]}
            request_obj = service.urlNotifications().publish(body=body)
            batch.add(request_obj, request_id=req_id)

        print(
            f"[Google Indexing] 正在使用 Google API 官方 Batch 方式发送 {len(tasks)} 个 URL 任务..."
        )
        batch.execute()

    except Exception as e:
        print(f"[Google Indexing] ❌ Batch 执行时发生异常: {e}")
        return tasks

    # 统计成功数并更新 success 状态
    for idx, task in enumerate(tasks):
        if str(idx) in success_ids:
            task["success"] = True
        else:
            task["success"] = False

    success_count = sum(1 for t in tasks if t["success"])
    print(f"[Google Indexing] 本轮 Batch 结束。成功: {success_count}/{len(tasks)}")

    return tasks
