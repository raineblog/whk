import os
import io
import shutil
import argparse
import sys
from pathlib import Path

import yaml
import json
import toml

from mkdocs.config import load_config
from mkdocs.commands.build import build
from mkdocs.commands.serve import serve

script_dir = Path(__file__).resolve().parent


# def copy_public_to_site():
#     # 使用 pathlib 定义路径更加优雅和安全
#     src = Path("public")
#     dst = Path("site")

#     # 确保源目录存在，避免报错
#     if not src.exists() or not src.is_dir():
#         print(f"⚠️ 源目录 {src} 不存在或不是文件夹！")
#         return

#     print(f"📂 正在将 {src} 的内容复制到 {dst} ...")

#     # 完美等价于 cp -af public/. site/
#     shutil.copytree(
#         src, 
#         dst, 
#         symlinks=True,           # 对应 -a: 保留软链接而不只是复制内容
#         dirs_exist_ok=True,      # 对应 -f 和 /.: 如果 site 目录已存在，不报错，直接合并/覆盖文件
#         copy_function=shutil.copy2 # 对应 -a: 保留文件的元数据（如修改时间、权限等）
#     )
    
#     print("✅ 复制完成！")

def parse_yaml(yaml_path):
    with open(yaml_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return yaml.load(text, Loader=yaml.FullLoader)

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def get_nav():
    nav_config = load_json('config/nav.json')
    nav = []
    for item in nav_config:
        nav.append({item['title']: item['children']})
    return nav

def get_template(template_path):
    template_defaults = parse_yaml(template_path)
    project_config = load_json('config/project.json')
    template_defaults['theme'] |= project_config['theme']
    return template_defaults

def parse_args():
    parser = argparse.ArgumentParser(
        description="我的自定义脚本 CLI",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument("--build", action="store_true", help="执行构建动作")
    parser.add_argument("--serve", action="store_true", help="启动本地预览服务")

    parser.add_argument(
        "--disable_giscus", 
        type=str, 
        default="false", 
        help="是否禁用 Giscus，默认为 false"
    )

    parser.add_argument(
        "--site_url", 
        type=str, 
        default="null", 
        help="网站的 URL，包括 https"
    )

    parser.add_argument("--port", type=int, default=8000, help="服务端口，默认为 8000")

    return parser.parse_args()

def main():
    args = parse_args()

    disable_giscus = args.disable_giscus.lower() in ("true", "1", "yes")

    info = load_json('config/project.json')['info']

    if args.build:
        if (site_url := args.site_url).lower() != "null":
            info['site_url'] = site_url
        
        nav = { 'nav': get_nav() }

        info['extra'] = load_json('config/extra.json')
        if disable_giscus:
            info['extra'].pop('giscus', None)
        
        template_defaults = get_template(script_dir / 'template.yml')
        config_map = info | template_defaults | nav

        with open(os.path.join(os.getcwd(), "mkdocs.yml"), 'w', encoding='utf-8') as file:
            yaml.dump(config_map, file, allow_unicode=True, indent=4, sort_keys=False)

        dummy_file = io.StringIO(yaml.dump(config_map, allow_unicode=True, indent=4, sort_keys=False))
        dummy_file.name = os.path.join(os.getcwd(), "mkdocs.yml")
        config = load_config(config_file=dummy_file)
        config["plugins"].run_event("startup", command="build", dirty=False)
        try:
            build(config)
            # copy_public_to_site()
            print("✅ 构建成功！")
            
        except Exception as e:
            print(f"❌ 构建失败: {e}")
            raise
            
        finally:
            config["plugins"].run_event("shutdown")
    elif args.serve:
        print('serve')
        # write_site_template('mkdocs.yml', False, 'template.serve.yml')
    else:
        print("⚠️ 错误: 请指定要执行的操作，例如 --build 或 --serve")
        sys.exit(1)

if __name__ == "__main__":
    main()
