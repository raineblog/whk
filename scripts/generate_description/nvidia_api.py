from openai import OpenAI
import os

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.environ.get("NVIDIA_API_KEY"),
)


def get_description(file: str, options):
    file_content = f"``````markdown\n{file}\n``````"
    user_content = ""

    for key, value in options.items():
        user_content += f"{key}：{value}\n"

    completion = client.chat.completions.create(
        model="nvidia/ising-calibration-1.5-31b",
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
        max_tokens=32768,
        stream=True,
        # extra_body={"chat_template_kwargs": {"enable_thinking": True}},
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
