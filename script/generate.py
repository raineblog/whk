import os
import yaml
import json

def parse_yaml(yaml_path):
    with open(yaml_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return yaml.load(text, Loader=yaml.FullLoader)

def extract_title(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('# '):
                return line[2:].strip()
    return "无标题"

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def write_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

intro = [
    {
        '简介': [
            'index.md',
            'intro/format.md',
            'intro/usage.md',
            'intro/discussion.md',
            'madoka.md'
        ]
    }
]

def get_site_nav():
    nav = load_json('info.json')['nav']
    return intro + [{item['title']: item['children']} for item in nav]

if __name__ == "__main__":
    info = load_json('info.json')
    template = info['project'] | parse_yaml('script/template.yml') | parse_yaml('docs/assets/extra.yml')
    template['extra'] = { 'giscus': info['giscus'] }
    template['nav'] = get_site_nav()
    with open('mkdocs.yml', 'w', encoding='utf-8') as file:
        yaml.dump(template, file, allow_unicode=True, indent=4, sort_keys=False)
