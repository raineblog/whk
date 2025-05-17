import os
import yaml

def parse_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().replace('!!', '__').replace('.md', '_md').replace('.', '-').replace('_md', '.md')
        data = yaml.load(text, Loader=yaml.FullLoader)
    return data

def extract_nav(data):
    return data.get('nav', [])

def build_tree(nav, base_path, indent=0):
    tree = ""
    for item in nav:
        if isinstance(item, dict):
            for folder, sub_nav in item.items():
                tree += " " * indent + f"📁 {folder}\n"
                tree += build_tree(sub_nav, base_path, indent + 4)
        elif isinstance(item, str):
            file_path = os.path.join(base_path, item.replace('/', os.sep))
            if os.path.exists(file_path):
                title = extract_title(file_path)
                tree += " " * indent + f"📝 {item} - {title}\n"
    return tree

def extract_title(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('# '):  # 一级标题
                return line[2:].strip()
    return "无标题"

def main():
    yaml_path = './mkdocs.yml'
    docs_path = './docs'
    data = parse_yaml(yaml_path)
    nav = extract_nav(data)
    tree = build_tree(nav, docs_path)
    print(tree)

if __name__ == "__main__":
    main()
