import os
import json
import shutil
import download
from toc import *

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def write_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def process_top_level(info, sub_nav, site_url):
    first_title = info['title']
    first_out = os.path.join('cache', first_title)

    print(first_title)
    os.makedirs(first_out, exist_ok=True)

    toc = {
        "title": info["title"],
        "subtitle": info["subtitle"],
        "authors": info["authors"],
        "info": info["info"],
        "content": []
    }

    pdf_tasks = [] 
    sections_map = {}

    for item in sub_nav:
        for second_title, third_list in item.items():
            second_out = os.path.join(first_out, second_title)
            os.makedirs(second_out, exist_ok=True)
            sections_map.setdefault(second_title, [])
            for third_file in third_list:
                md_path = os.path.join('docs', third_file.replace('/', os.sep))
                third_title = extract_title(md_path)
                pdf_path = os.path.join(first_out, second_title, third_title + ".pdf")
                html_url = site_url.rstrip('/') + "/" + third_file.replace('.md', '/index.html').replace('index/index.html', 'index.html') + "?export=true"
                pdf_tasks.append([html_url, pdf_path])
                sections_map[second_title].append((third_title, pdf_path))

    download.convertHtmlToPdf(pdf_tasks)

    original_dir = os.getcwd()

    for second_title, items in sections_map.items():
        section = {"title": second_title, "sections": []}
        for third_title, pdf_path in items:
            pdf_dir = os.path.dirname(pdf_path)
            temp_pdf = os.path.join(pdf_dir, "test.pdf")
            shutil.copy(pdf_path, temp_pdf)
            os.chdir(pdf_dir)
            os.system(f"pdf2svg test.pdf {third_title}.%04d.svg all")
            os.chdir(original_dir)
            os.remove(temp_pdf)
            svg_files = sorted([f for f in os.listdir(pdf_dir) if f.startswith(third_title) and f.endswith('.svg')])
            section["sections"].append({
                "title": third_title,
                "pages": [os.path.join(first_title, second_title, svg) for svg in svg_files]
            })
        toc["content"].append(section)

    shutil.copy('script/main.typ', 'cache/main.typ')
    write_json('cache/toc.json', toc)

    typst_in = os.path.join('cache', "main.typ")
    typst_out = os.path.join('cache', info['filename'])
    print(f"typst compile {typst_in} {typst_out}")
    os.system(f"typst compile {typst_in} {typst_out}")

    shutil.rmtree(first_out)
    os.remove('cache/main.typ')
    os.remove('cache/toc.json')

if __name__ == "__main__":
    os.system('export TYPST_FONT_PATHS="./script/fonts"')
    info = load_json('info.json')
    site_url = info['project']['site_url']
    for item in info['nav']:
        if not 'export' in item:
            continue
        process_top_level(item['export'], item['children'], site_url)
