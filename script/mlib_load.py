import os
import yaml
import json

def parse_yaml(yaml_path):
    with open(yaml_path, 'r', encoding='utf-8') as file:
        text = file.read()
    data = yaml.load(text, Loader=yaml.FullLoader)
    return data

def extract_title(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('# '):  # 一级标题
                return line[2:].strip()
    return "无标题"

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def write_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def get_site_nav():
    nav = load_json('info.json')['nav']
    return [
        {
            '简介': [
                'index.md',
                'intro/format.md',
                'intro/usage.md',
                'intro/discussion.md',
                'madoka.md'
            ]
        }
    ] + [{item['title']: item['children']} for item in nav]

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

if __name__ == "__main__":
    nav = get_site_nav()
    tree = build_tree(nav, 'docs')
    print(tree)
