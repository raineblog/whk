import os
import json
import shutil
from toc import parse_yaml, extract_nav, extract_title
from download import convertHtmlToPdf

def get_site_url(yaml_path):
    """
    Read the site_url from mkdocs.yml after filtering out invalid tokens.
    """
    with open(yaml_path, 'r', encoding='utf-8') as file:
        text = file.read()\
            .replace('!!', '__')\
            .replace('.github.io', 'githubio')\
            .replace('.md', '_md')\
            .replace('.', '-')\
            .replace('_md', '.md')\
            .replace('githubio', '.github.io')
    data = __import__('yaml').load(text, Loader=__import__('yaml').FullLoader)
    return data.get("site_url", "").strip(), data

def find_info_path_for_top(sub_nav, docs_path):
    """
    Iterate through the sub_nav to locate an info.json file.
    Returns the path to info.json and the candidate folder.
    """
    for item in sub_nav:
        if isinstance(item, dict):
            for _, third_list in item.items():
                for third_file in third_list:
                    folder = third_file.split('/')[0]
                    candidate = os.path.join(docs_path, folder, "info.json")
                    if os.path.exists(candidate):
                        return candidate, folder
    return None, None

def process_top_level(top_title, sub_nav, docs_path, site_url, script_dir):
    """
    Process one top-level section:
    - Read info.json and build output directory.
    - Gather PDF download tasks and organize sections.
    - Convert PDFs to SVG files.
    - Build and write the toc.json file (placed in script_dir).
    """
    info_path, _ = find_info_path_for_top(sub_nav, docs_path)
    if info_path is None:
        return
    with open(info_path, 'r', encoding='utf-8') as f:
        info_data = json.load(f)
    
    print(top_title)
        
    top_out = os.path.join(script_dir, top_title)
    os.makedirs(top_out, exist_ok=True)

    # Build toc structure and collect PDF download tasks
    toc = {
        "title": info_data["title"],
        "subtitle": info_data["subtitle"],
        "authors": info_data["authors"],
        "info": info_data["info"],
        "content": []
    }
    pdf_tasks = []  # Each element: [html_url, pdf_path]
    sections_map = {}  # Key: second-level title, Value: list of (third_title, pdf_path)

    # Iterate over second-level sections in the nav structure
    for item in sub_nav:
        if isinstance(item, dict):
            for second_title, third_list in item.items():
                second_out = os.path.join(top_out, second_title)
                os.makedirs(second_out, exist_ok=True)
                sections_map.setdefault(second_title, [])
                for third_file in third_list:
                    md_path = os.path.join(docs_path, third_file.replace('/', os.sep))
                    if os.path.exists(md_path):
                        third_title = extract_title(md_path)
                        pdf_path = os.path.join(top_out, second_title, third_title + ".pdf")
                        # Build HTML URL (handle index.md special case)
                        html_part = third_file.replace('.md', '/index.html')
                        html_part = html_part.replace('index/index.html', 'index.html')
                        html_url = site_url.rstrip('/') + "/" + html_part + "?export=true"
                        pdf_tasks.append([html_url, pdf_path])
                        sections_map[second_title].append((third_title, pdf_path))

    # Download all PDFs in one batch
    if pdf_tasks:
        print("PDF tasks:", pdf_tasks)
        convertHtmlToPdf(pdf_tasks)

    # Convert downloaded PDFs to SVGs and build toc sections
    for second_title, items in sections_map.items():
        section = {"title": second_title, "sections": []}
        for third_title, pdf_path in items:
            current_dir = os.path.dirname(pdf_path)
            temp_pdf = os.path.join(current_dir, "test.pdf")  # Use test.pdf as temporary file
            if os.path.exists(pdf_path):
                shutil.copy(pdf_path, temp_pdf)
                # Change directory to convert PDF using relative paths
                original_dir = os.getcwd()
                try:
                    os.chdir(current_dir)
                    out_svg_pattern = f"{third_title}.%04d.svg"
                    os.system(f"pdf2svg test.pdf {out_svg_pattern} all")
                finally:
                    os.chdir(original_dir)
                os.remove(temp_pdf)
                svg_files = sorted([f for f in os.listdir(current_dir)
                                    if f.startswith(third_title) and f.endswith('.svg')])
                # Include top-level directory in pages path
                section["sections"].append({
                    "title": third_title,
                    "pages": [os.path.join(top_title, second_title, svg) for svg in svg_files]
                })
        toc["content"].append(section)

    # Write the combined toc.json to script_dir
    toc_path = os.path.join(script_dir, "toc.json")
    with open(toc_path, 'w', encoding='utf-8') as f:
        json.dump(toc, f, ensure_ascii=False, indent=4)
    print(json.dumps(toc, ensure_ascii=False, indent=4))
    
    # Compile main.typ (assumed to be in script_dir) into main.pdf
    typst_in = os.path.join(script_dir, "main.typ")
    typst_out = os.path.join(script_dir, info_data['filename'])
    print(f"typst compile {typst_in} {typst_out}")
    os.system(f"typst compile {typst_in} {typst_out}")

    # shutil.rmtree(top_out)

def generate_toc_and_export():
    """
    Main function:
    - Parse mkdocs.yml to get nav and site_url.
    - Process each top-level section.
    - Compile main.typ to main.pdf.
    """
    base_dir = os.path.abspath(".")  # Base directory (whk folder)
    yaml_path = os.path.join(base_dir, "mkdocs.yml")
    docs_path = os.path.join(base_dir, "docs")
    site_url, _ = get_site_url(yaml_path)

    # Set output to current script directory
    script_dir = os.path.abspath(os.path.dirname(__file__))
    
    print(script_dir)

    nav = extract_nav(parse_yaml(yaml_path))
    for item in nav:
        if isinstance(item, dict):
            for top_title, sub_nav in item.items():
                process_top_level(top_title, sub_nav, docs_path, site_url, script_dir)

if __name__ == "__main__":
    generate_toc_and_export()
