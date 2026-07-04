from openai import OpenAI
import os

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.environ.get("NVIDIA_API_KEY"),
)

counter = 0

import time
from concurrent.futures import ThreadPoolExecutor, TimeoutError
from tenacity import retry, stop_after_attempt, retry_if_exception_type

# 1. 定义一个用于单次执行超时的包装函数
def run_with_timeout(func, file, options, timeout_seconds):
    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(func, file, options)
        # 在这里设置单次请求的超时时间
        return future.result(timeout=timeout_seconds)

@retry(
    stop=stop_after_attempt(3),  # 达到 3 次停止
    retry=retry_if_exception_type(TimeoutError) # 仅针对超时异常重试
)
def get_description(file: str, options):
    return run_with_timeout(_get_description, file, options, 30)

def _get_description(file: str, options):
    file_content = f"``````markdown\n{file}\n``````"
    user_content = ""

    for key, value in options.items():
        user_content += f"{key}：{value}\n"

    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": "给下面的文章，拟一个纯文本的描述 Description 字段，用于 SEO/GEO，必须是简体中文，75～100 字左右，不要输出其他任何内容。",
            },
            {
                "role": "user",
                "content": f"给下面的文章，拟一个纯文本的描述 Description 字段，用于 SEO/GEO，必须是简体中文，75～100 字左右，不要输出其他任何内容。\n\n{file_content}\n\n{user_content}",
            },
        ],
        temperature=1,
        top_p=1,
        max_tokens=4096,
        stream=True,
    )

    global counter
    counter += 1

    result = ""

    print(counter, end=": ")

    for chunk in completion:
        if not getattr(chunk, "choices", None):
            print(".", end="")
            continue
        reasoning = getattr(chunk.choices[0].delta, "reasoning_content", None)
        if reasoning:
            print("*", end="")
        elif chunk.choices and chunk.choices[0].delta.content is not None:
            result += chunk.choices[0].delta.content
            print("#", end="")
        else:
            print("-", end="")

    print("")

    return result
