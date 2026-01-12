#!/usr/bin/env python3
"""
自动替换 Markdown 文件中的重定向链接
警告：此脚本会直接修改 Markdown 文件，请谨慎使用
建议先运行 process-lychee-report.py 生成 redirects.txt 后再运行此脚本
"""

import re
import sys
from pathlib import Path
from typing import Dict


def load_redirect_mapping(mapping_file: Path) -> Dict[str, str]:
    """
    从映射文件加载重定向信息
    格式: original_url --> final_url
    """
    redirects = {}
    
    if not mapping_file.exists():
        print(f"⚠️  映射文件不存在: {mapping_file}")
        return redirects
    
    with open(mapping_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # 跳过注释和空行
            if line.startswith('#') or not line:
                continue
            
            # 解析映射
            if ' --> ' in line:
                original, final = line.split(' --> ', 1)
                redirects[original.strip()] = final.strip()
    
    print(f"📊 加载了 {len(redirects)} 个重定向映射")
    return redirects


def replace_urls_in_file(file_path: Path, redirects: Dict[str, str]) -> int:
    """
    替换文件中的 URL
    返回：替换次数
    """
    if not file_path.exists():
        return 0
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ 读取文件失败 {file_path}: {e}")
        return 0
    
    original_content = content
    replace_count = 0
    
    for original_url, final_url in redirects.items():
        # 转义特殊字符用于正则表达式
        escaped_original = re.escape(original_url)
        
        # 替换 Markdown 链接中的 URL: [text](url)
        pattern1 = rf'\[([^\]]+)\]\({escaped_original}\)'
        replacement1 = rf'[\1]({final_url})'
        new_content, count1 = re.subn(pattern1, replacement1, content)
        
        # 替换纯 URL
        pattern2 = rf'(?<!\()(?<!])\b{escaped_original}\b(?!\))'
        replacement2 = final_url
        new_content, count2 = re.subn(pattern2, replacement2, new_content)
        
        if count1 + count2 > 0:
            replace_count += count1 + count2
            content = new_content
            print(f"  ✅ {file_path.name}: 替换 {count1 + count2} 处")
            print(f"     {original_url} -> {final_url}")
    
    # 如果有替换，保存文件
    if content != original_content:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            print(f"❌ 写入文件失败 {file_path}: {e}")
            return 0
    
    return replace_count


def process_markdown_files(docs_dir: Path, redirects: Dict[str, str]) -> None:
    """处理所有 Markdown 文件"""
    if not docs_dir.exists():
        print(f"❌ 文档目录不存在: {docs_dir}")
        return
    
    total_replacements = 0
    files_modified = 0
    
    # 递归查找所有 .md 文件
    md_files = list(docs_dir.rglob('*.md'))
    print(f"\n📁 找到 {len(md_files)} 个 Markdown 文件")
    
    for md_file in md_files:
        count = replace_urls_in_file(md_file, redirects)
        if count > 0:
            total_replacements += count
            files_modified += 1
    
    print(f"\n✨ 处理完成！")
    print(f"📝 修改了 {files_modified} 个文件")
    print(f"🔄 总共替换了 {total_replacements} 处链接")


def main():
    """主函数"""
    # 默认路径
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent.parent
    mapping_file = script_dir / 'redirects.txt'
    docs_dir = repo_root / 'docs'
    
    # 命令行参数
    if len(sys.argv) > 1:
        mapping_file = Path(sys.argv[1])
    if len(sys.argv) > 2:
        docs_dir = Path(sys.argv[2])
    
    print("🔄 开始自动替换重定向链接...")
    print(f"📄 映射文件: {mapping_file}")
    print(f"📁 文档目录: {docs_dir}")
    
    # 加载重定向映射
    redirects = load_redirect_mapping(mapping_file)
    
    if not redirects:
        print("⚠️  没有重定向映射，退出")
        return
    
    # 确认操作
    print("\n⚠️  警告：此操作将直接修改 Markdown 文件！")
    if len(sys.argv) <= 1:  # 交互模式
        response = input("是否继续？[y/N]: ")
        if response.lower() != 'y':
            print("❌ 操作已取消")
            return
    
    # 处理文件
    process_markdown_files(docs_dir, redirects)


if __name__ == '__main__':
    main()
