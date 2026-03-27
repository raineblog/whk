import os
from jinja2 import Environment, FileSystemLoader

def generate_prompt():
    # 获取脚本所在目录的绝对路径
    script_dir = os.path.dirname(os.path.abspath(__file__))
    prompt_dir = os.path.join(script_dir, "prompt")
    
    # 设置 Jinja2 环境，加载 prompt 目录下的模板
    env = Environment(loader=FileSystemLoader(prompt_dir))
    
    try:
        # 加载主模板 main.md
        template = env.get_template("main.md")
        
        # 渲染模板（目前不需要传入动态变量，include 会自动处理）
        output = template.render()
        
        # 定义输出路径
        output_path = os.path.join(script_dir, "SKILL.md")
        
        # 写入生成的内容
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(output)
            
        print(f"成功生成 Prompt 文件: {output_path}")
        
    except Exception as e:
        print(f"生成过程中出现错误: {e}")

if __name__ == "__main__":
    generate_prompt()
