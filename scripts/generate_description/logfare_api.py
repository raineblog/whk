from openai import OpenAI
import os

client = OpenAI(
    base_url="https://logfare.ai/v1",
    api_key=os.environ.get("LOGFARE_API_KEY"),
)


def get_description(file: str, options):
    file_content = f"``````markdown\n{file}\n``````"
    user_content = ""

    for key, value in options.items():
        user_content += f"{key}：{value}\n"

    completion = client.chat.completions.create(
        model="logfare/auto",
        messages=[
            {
                "role": "system",
                "content": "给下面的文章，拟一个纯文本的描述 Description 字段，用于 SEO/GEO，必须是简体中文，75～100 字左右，不要输出其他任何内容。",
            },
            {
                "role": "user",
                "content": f"{file_content}\n\n---\n\n给上面的文章，拟一个纯文本的描述 Description 字段，用于 SEO/GEO，必须是简体中文，75～100 字左右，不要输出其他任何内容。\n\n{user_content}",
            },
        ],
        stream=True,
    )

    result = ""

    for chunk in completion:
        if not getattr(chunk, "choices", None):
            continue
        reasoning = getattr(chunk.choices[0].delta, "reasoning_content", None)
        if reasoning:
            print(reasoning, end="")
        if chunk.choices and chunk.choices[0].delta.content is not None:
            result += chunk.choices[0].delta.content
            print("#", end="")

    print("")

    return result
