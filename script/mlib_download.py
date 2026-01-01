import os
import sys
import queue
import subprocess
import uuid
from concurrent.futures import ThreadPoolExecutor
from playwright.sync_api import sync_playwright

task_list = []

# def convert_pdf_to_svg(pdf_full_path: str, final_file_name: str):
#     directory = os.path.dirname(pdf_full_path)
#     current_temp_name = os.path.basename(pdf_full_path)
#     stem_name = os.path.splitext(final_file_name)[0]

#     subprocess.run(
#         [
#             "pdf2svg", 
#             current_temp_name, 
#             f"{stem_name}.%04d.svg", 
#             "all"
#         ], 
#         cwd=directory, 
#         check=True, 
#         stdout=subprocess.DEVNULL,
#         stderr=subprocess.PIPE
#     )

def pdf_worker(worker_id: int, task_queue: queue.Queue):
    print(f"[Worker-{worker_id}] 启动")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-setuid-sandbox"])
        context = browser.new_context()

        processed_count = 0
        while True:
            if processed_count > 0 and processed_count % 50 == 0:
                context.close()
                context = browser.new_context()
                
            task = task_queue.get()
            if task is None:
                break
            url, final_path = task

            target_dir = os.path.dirname(final_path)
            # final_name = os.path.basename(final_path)
            if not os.path.exists(target_dir):
                os.makedirs(target_dir, exist_ok=True)
    
            temp_filename = f"tmp_{uuid.uuid4().hex[:8]}.pdf"
            temp_full_path = os.path.join(target_dir, temp_filename)
    
            page = context.new_page()
            page.goto(url, wait_until="load")

            page.evaluate("""
                () => Promise.all([
                    document.fonts.ready,
                    new Promise(resolve => {
                        if (document.readyState === 'complete') resolve();
                        else window.addEventListener('load', resolve);
                    }),
                    new Promise(resolve => {
                        requestAnimationFrame(() => {
                            requestAnimationFrame(resolve);
                        });
                    })
                ])
            """)

            page.pdf(
                path=temp_full_path,
                format="A4",
                margin={"top": "25.5mm", "bottom": "25.5mm", "left": "19mm", "right": "19mm"},
                print_background=True,
            )

            page.close()

            # convert_pdf_to_svg(temp_full_path, final_name)

            if os.path.exists(final_path):
                os.remove(final_path)
            os.rename(temp_full_path, final_path)
            
            processed_count += 1
            task_queue.task_done()

        context.close()
        browser.close()
        
        print(f"[Worker-{worker_id}] 完成。")

def add_task(task):
    task_list.append(task)

def start_tasks(max_threads: int = 4):
    print(f"--- 任务开始: 共 {len(task_list)} 个 URL，最大并发数 {max_threads} ---")
    task_queue = queue.Queue()
    for item in task_list:
        if os.path.exists(item[1]):
            os.remove(item[1])
        task_queue.put(item)
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        for i in range(max_threads):
            executor.submit(pdf_worker, i, task_queue)
        task_queue.join()
        for _ in range(max_threads):
            task_queue.put(None)
    print("--- 所有任务完成 ---")
