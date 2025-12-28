import os
import toc
import json
import yaml

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    info = load_json('info.json')
    template = info['project'] | toc.parse_yaml('script/template.yml') | toc.parse_yaml('docs/assets/extra.yml')
    template['extra'] = { 'giscus': info['giscus'] }
    template['nav'] = toc.get_site_nav()
    with open('mkdocs.yml', 'w', encoding='utf-8') as file:
        yaml.dump(template, file, allow_unicode=True, indent=4, sort_keys=False)
    try:
        os.system("git rev-parse --short HEAD | xargs -I % sed -i \"s/githash: ''/githash: '%'/g\" mkdocs.yml")
    except Exception as e:
        print(f"无法创建 githash.txt: {e}")
