def submit_other(urls: list[str]) -> None:
    """
    预留给其他平台的推送接口（如百度推送、自定义webhook等）。
    """
    if not urls:
        return
    print(f"[Other Pusher] 预留接口：接收到 {len(urls)} 个待推送的 URL，当前无额外推送任务。")
