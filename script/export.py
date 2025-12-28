import os
import shutil
import mlib_download
from mlib_load import *
import mlib_server as server

def clean_url(baseurl, filepath):
    return baseurl.rstrip('/') + '/' + filepath.replace('.md', '/index.html').replace('index/index.html', 'index.html') + "?export=true"

def process_top_level(info, sub_nav, baseurl):
    first_title = info['title']
    first_out = os.path.join('cache', first_title)
    os.makedirs(first_out, exist_ok=True)

    sections_map = {}
    for item in sub_nav:
        for second_title, third_list in item.items():
            second_out = os.path.join(first_out, second_title)
            os.makedirs(second_out, exist_ok=True)
            sections_map.setdefault(second_title, [])
            for third_file in third_list:
                third_title = extract_title(os.path.join('docs', third_file.replace('/', os.sep)))
                pdf_path = os.path.join(first_out, second_title, third_title + ".pdf")
                html_url = clean_url(baseurl, third_file)
                mlib_download.add_task([html_url, pdf_path])
                sections_map[second_title].append((third_title, pdf_path))

    mlib_download.start_tasks()

    toc = {
        "title": info["title"],
        "subtitle": info["subtitle"],
        "authors": info["authors"],
        "info": info["info"],
        "content": []
    }

    for second_title, items in sections_map.items():
        section = {"title": second_title, "sections": []}
        for third_title, pdf_path in items:
            svg_files = [f for f in os.listdir(os.path.dirname(pdf_path)) if f.startswith(third_title) and f.endswith('.svg')]
            output_pages = [os.path.join(first_title, second_title, svg) for svg in sorted(svg_files)]
            section["sections"].append({ "title": third_title, "pages": output_pages })
        toc["content"].append(section)

    shutil.copy('script/main.typ', 'cache/main.typ')
    write_json('cache/toc.json', toc)

    os.system(f"typst compile cache/main.typ cache/{info['filename']}")

    shutil.rmtree(first_out)
    os.remove('cache/main.typ')
    os.remove('cache/toc.json')

if __name__ == "__main__":
    info = load_json('info.json')
    site_url = server.start_local_server('./site')
    for item in info['nav']:
        if 'export' in item:
            process_top_level(item['export'], item['children'], site_url)
    server.stop_local_server()
