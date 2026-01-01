import subprocess
import sys
import os
import shutil
import mlib_download
from mlib_load import *
import mlib_server as server

def clean_url(baseurl, filepath):
    return baseurl.rstrip('/') + '/' + filepath.replace('.md', '/index.html').replace('index/index.html', 'index.html') + "?export=true"

def compile_latex(tex_filename, output_pdf_filename=None):
    if not os.path.exists(tex_filename):
        print(f"Error: Input file '{tex_filename}' not found!")
        sys.exit(1)
    
    base_dir = os.path.dirname(tex_filename)
    file_stem = os.path.splitext(os.path.basename(tex_filename))[0]
    default_pdf_path = os.path.join(base_dir if base_dir else '.', f"{file_stem}.pdf")

    cmd = [
        "latexmk",
        "-cd",
        "-lualatex",
        "-interaction=nonstopmode",
        "-file-line-error",
        "-halt-on-error",
        "-g",
        "-gg",
        tex_filename
    ]

    print(f"[*] Compiling: {tex_filename} ...")
    print(f"[*] Command: {' '.join(cmd)}")

    try:
        # subprocess.run(cmd, check=True, stdout=None, stderr=None)
        subprocess.run(cmd)
        print(f"[*] Compilation successful: {default_pdf_path}")
        
    except subprocess.CalledProcessError as e:
        print("\n==============================")
        print("❌ LaTeX Compilation Failed!")
        print(f"Exit code: {e.returncode}")
        print("Please check the log output above for details.")
        print("==============================")
        subprocess.run([
            "cat",
            "cache/main.log",
            "-n",
            "-s"
        ])
        sys.exit(e.returncode)

    if output_pdf_filename:
        if os.path.abspath(default_pdf_path) != os.path.abspath(output_pdf_filename):
            print(f"[*] Renaming output to: {output_pdf_filename}")
            output_dir = os.path.dirname(output_pdf_filename)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)
            try:
                shutil.move(default_pdf_path, output_pdf_filename)
                print(f"[*] File ready at: {output_pdf_filename}")
            except OSError as e:
                print(f"❌ Error renaming file: {e}")
                sys.exit(1)

def process_top_level(info, sub_nav, baseurl):
    first_title = info['title']
    first_out = os.path.join('cache', first_title)
    os.makedirs(first_out, exist_ok=True)

    sections = []
    for item in sub_nav:
        for second_title, third_list in item.items():
            second_out = os.path.join(first_out, second_title)
            os.makedirs(second_out, exist_ok=True)
            section = { "title": second_title, "sections": [] }
            for third_file in third_list:
                third_title = extract_title(os.path.join('docs', third_file.replace('/', os.sep)))
                pdf_path = os.path.join(first_out, second_title, third_title + ".pdf")
                html_url = clean_url(baseurl, third_file)
                mlib_download.add_task([html_url, pdf_path])
                section["sections"].append({ "title": third_title, "path": pdf_path })
            sections.append(section)

    mlib_download.start_tasks()

    # 路径处理：将 cache/toc.json 中的路径改为相对于 cache/ 的路径
    relative_sections = []
    for section in sections:
        rel_sec = { "title": section["title"], "sections": [] }
        for sub in section["sections"]:
            rel_sec["sections"].append({
                "title": sub["title"],
                "path": sub["path"].replace('cache/', '', 1).replace('\\', '/')
            })
        relative_sections.append(rel_sec)

    write_json('cache/toc.json', {
        "title": info["title"],
        "subtitle": info["subtitle"],
        "authors": info["authors"],
        "info": info["info"],
        "sections": relative_sections
    })

    shutil.copy('script/template.tex', 'cache/main.tex')
    compile_latex('cache/main.tex', 'cache/' + info['filename'])
    
    shutil.rmtree('cache/toc.json')
    shutil.rmtree('cache/main.tex')

if __name__ == "__main__":
    info = load_json('info.json')
    site_url = server.start_local_server('./site')
    for item in info['nav']:
        if 'export' in item:
            process_top_level(item['export'], item['children'], site_url)
    server.stop_local_server()
