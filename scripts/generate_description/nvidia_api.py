from openai import OpenAI
import os

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = os.environ.get("NVIDIA_API_KEY")
)

counter = 0

def get_description(file: str, options):
    file_content = "``````markdown\n{file}\n``````"
    user_content = ""
    
    for key, value in options.items():
        user_content += f"{key}：{value}\n"
    
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": "给下面的文章，拟一个纯文本的描述 Description 字段，用于 SEO/GEO，100～200 字左右，不要输出其他任何内容。"
            }
            {
                "role": "user",
                "content": f"给下面的文章，拟一个纯文本的描述 Description 字段，用于 SEO/GEO，100～200 字左右，不要输出其他任何内容。\n\n{file_content}\n\n{user_content}"
            }
        ],
        temperature=1,
        top_p=1,
        max_tokens=4096,
        stream=True
    )
    
    global counter
    counter += 1
    
    result = ''
    
    print(counter, end=':')

    for chunk in completion:
        if not getattr(chunk, "choices", None):
            continue
        reasoning = getattr(chunk.choices[0].delta, "reasoning_content", None)
        if reasoning:
            print('r', end='')
        if chunk.choices and chunk.choices[0].delta.content is not None:
            result += chunk.choices[0].delta.content
            print('w', end='')
    
    print('')
    
    return result
