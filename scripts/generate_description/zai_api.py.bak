from openai import OpenAI
import os

client = OpenAI(
    base_url="https://api.z.ai/api/paas/v4/",
    api_key=os.environ.get("ZAI_API_KEY"),
)


def get_description(file: str, options):
    file_content = f"``````markdown\n{file}\n``````"
    user_content = ""

    for key, value in options.items():
        user_content += f"{key}：{value}\n"

    completion = client.chat.completions.create(
        model="glm-4.7-flash",
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
        max_tokens=131072,
        stream=True,
        extra_body={"thinking": {"type": "enabled", "clear_thinking": False}},
    )

    result = ""
    for chunk in completion:
        if not getattr(chunk, "choices", None):
            continue
        reasoning = getattr(chunk.choices[0].delta, "reasoning_content", None)
        if reasoning:
            print("*", end="", flush=True)
        if chunk.choices and chunk.choices[0].delta.content is not None:
            result += chunk.choices[0].delta.content
            print("#", end="", flush=True)
    print("", flush=True)

    return result
