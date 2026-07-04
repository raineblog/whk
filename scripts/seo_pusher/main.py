import os
import json
import hashlib
from pathlib import Path
from datetime import datetime, timezone

# 导入子模块
from _googleapis import submit_to_google_indexing
from _indexnow import submit_to_indexnow
from _ping import submit_sitemap_ping, submit_rpc_ping
from _other import submit_other

def calculate_md5(file_path: Path) -> str:
    """计算文件的 MD5 哈希"""
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        print(f"[main] 计算 {file_path} MD5 失败: {e}")
        return ""

def md_path_to_url(file_path: str, site_url: str) -> str:
    """将本地 docs 相对路径转换为绝对 URL"""
    if file_path.startswith("docs/"):
        rel_path = file_path[5:]
    elif file_path.startswith("docs\\"):
        rel_path = file_path[5:]
    else:
        rel_path = file_path

    rel_path = rel_path.replace('\\', '/')

    if rel_path.endswith('.md'):
        rel_path = rel_path[:-3]

    if rel_path.endswith('/index'):
        rel_path = rel_path[:-5]
    elif rel_path == 'index':
        rel_path = ''

    if rel_path and not rel_path.endswith('/'):
        rel_path += '/'

    base_url = site_url.rstrip('/') + '/'
    return base_url + rel_path

def main():
    # 1. 获取基础配置
    site_host = os.environ.get("SITE_HOST", "raineblog.dpdns.org")
    site_name = os.environ.get("SITE_NAME", "RainPPR's WHK Wiki")
    site_project = os.environ.get("SITE_PROJECT", "whk")
    site_base = os.environ.get("SITE_BASE", f"https://{site_host}")
    
    site_url = f"{site_base}/{site_project}".rstrip('/') + '/'
    sitemap_url = f"{site_url}sitemap.xml"
    
    print("=" * 60)
    print(f"[SEO Pusher] 开始运行...")
    print(f"[SEO Pusher] SITE_NAME: {site_name}")
    print(f"[SEO Pusher] SITE_URL: {site_url}")
    print(f"[SEO Pusher] SITEMAP_URL: {sitemap_url}")
    print("=" * 60)

    # 2. 读取并初始化数据库
    db_path = Path("google_indexing.json")
    if db_path.exists():
        try:
            with open(db_path, "r", encoding="utf-8") as f:
                db = json.load(f)
            print(f"[main] 成功加载数据库，共 {len(db)} 条记录。")
        except Exception as e:
            print(f"[main] ❌ 警告: 加载数据库失败 ({e})，将重新初始化。")
            db = {}
    else:
        db = {}
        print("[main] 数据库文件不存在，将重新创建。")

    # 3. 扫描本地 docs 目录下的所有 .md 文件
    docs_dir = Path("docs")
    if not docs_dir.exists():
        print("[main] ❌ 错误: docs 目录不存在，停止运行。")
        return

    current_files = {}
    for p in docs_dir.glob("**/*.md"):
        if any(part.startswith('.') for part in p.parts):
            continue
        
        file_path_str = p.as_posix()
        md5_val = calculate_md5(p)
        if md5_val:
            current_files[file_path_str] = md5_val

    print(f"[main] 扫描 docs 完毕，找到 {len(current_files)} 个有效 Markdown 文件。")

    # 4. 比对状态，收集待处理任务
    all_tasks = []
    
    # 4.1 检测新增与更新
    for file_path, current_md5 in current_files.items():
        db_item = db.get(file_path)
        is_changed = False
        
        if not db_item:
            is_changed = True
            last_submitted = "1970-01-01T00:00:00+00:00"
        else:
            last_submitted = db_item.get("last_submitted", "1970-01-01T00:00:00+00:00")
            if db_item.get("md5") != current_md5:
                is_changed = True

        if is_changed:
            all_tasks.append({
                "file_path": file_path,
                "action": "URL_UPDATED",
                "url": md_path_to_url(file_path, site_url),
                "current_md5": current_md5,
                "last_submitted": last_submitted
            })

    # 4.2 检测已删除文件
    for file_path, db_item in db.items():
        if file_path not in current_files:
            last_submitted = db_item.get("last_submitted", "1970-01-01T00:00:00+00:00")
            all_tasks.append({
                "file_path": file_path,
                "action": "URL_DELETED",
                "url": md_path_to_url(file_path, site_url),
                "current_md5": None,
                "last_submitted": last_submitted
            })

    print(f"[main] 共检测到 {len(all_tasks)} 个待处理的变更 (更新/删除)。")

    if not all_tasks:
        print("[main] 🎉 暂无变更，所有文档均已是最新状态。")
        submit_sitemap_ping(site_name, site_url, sitemap_url)
        submit_rpc_ping(site_name, site_url)
        return

    # 5. 按照 last_submitted 排序并限制每次 100 个
    all_tasks.sort(key=lambda x: (x["last_submitted"], x["file_path"]))
    
    batch_tasks = all_tasks[:100]
    ignored_tasks_count = len(all_tasks) - len(batch_tasks)
    print(f"[main] 本次处理前 100 个最老的变更，剩余 {ignored_tasks_count} 个变更将留到下次运行。")

    # 6. 推送至 Google Indexing API Batch
    processed_tasks = submit_to_google_indexing(batch_tasks)

    # 7. 根据推送结果更新数据库
    now_str = datetime.now(timezone.utc).isoformat()
    success_urls = []
    
    for task in processed_tasks:
        file_path = task["file_path"]
        if task.get("success"):
            success_urls.append(task["url"])
            if task["action"] == "URL_UPDATED":
                db[file_path] = {
                    "md5": task["current_md5"],
                    "last_submitted": now_str
                }
            elif task["action"] == "URL_DELETED":
                if file_path in db:
                    del db[file_path]

    # 8. 保存数据库
    try:
        with open(db_path, "w", encoding="utf-8") as f:
            json.dump(db, f, indent=2, ensure_ascii=False, sort_keys=True)
        print("[main] google_indexing.json 数据库已成功保存。")
    except Exception as e:
        print(f"[main] ❌ 错误: 保存 google_indexing.json 失败: {e}")

    # 9. 将成功的 URL 推送至 IndexNow
    if success_urls:
        submit_to_indexnow(success_urls)
    else:
        print("[main] 本次没有成功提交的 URL，跳过 IndexNow 提交。")

    # 10. 触发传统 sitemap 及 RPC Ping
    submit_sitemap_ping(site_name, site_url, sitemap_url)
    submit_rpc_ping(site_name, site_url)

    # 11. 触发预留的其他推送
    submit_other(success_urls)

    print("[main] 🎉 本轮 SEO 推送及状态同步任务执行完毕。")

if __name__ == "__main__":
    main()
