import os
import mlib_load
import yaml

if __name__ == "__main__":
    info = mlib_load.load_json('info.json')
    template = info['project'] | mlib_load.parse_yaml('script/template.yml') | mlib_load.parse_yaml('docs/assets/extra.yml')
    template['extra'] = { 'giscus': info['giscus'] }
    template['nav'] = mlib_load.get_site_nav()
    with open('mkdocs.yml', 'w', encoding='utf-8') as file:
        yaml.dump(template, file, allow_unicode=True, indent=4, sort_keys=False)
    try:
        os.system("git rev-parse --short HEAD | xargs -I % sed -i \"s/githash: ''/githash: '%'/g\" mkdocs.yml")
    except Exception as e:
        print(f"无法创建 githash.txt: {e}")
