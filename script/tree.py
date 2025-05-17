import os

def get_md_title(file_path):
    """获取 .md 文件的一级标题"""
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith("# "):  # 找到第一个一级标题
                return line[2:]  # 去掉 "# " 前缀
    return "无标题"  # 如果没有一级标题，返回默认值

def generate_tree(directory, prefix=""):
    """生成目录树"""
    entries = []
    for entry in os.listdir(directory):
        full_path = os.path.join(directory, entry)
        if os.path.isfile(full_path) and entry.endswith((
            '.md', '.pdf', '.json',
            '.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx'
        )):
            entries.append(entry)
        elif os.path.isdir(full_path):
            sub_entries = generate_tree(full_path, prefix + "    ")
            if sub_entries:  # 如果子文件夹有内容，才添加
                entries.append((entry, sub_entries))
    
    if not entries:  # 如果当前文件夹没有符合条件的文件或子文件夹，返回空
        return []
    
    result = []
    for entry in entries:
        if isinstance(entry, tuple):  # 子文件夹
            folder_name, sub_entries = entry
            result.append(f"{prefix}📁 {folder_name}")
            result.extend(sub_entries)
        else:  # 文件
            if entry.endswith(".md"):
                title = get_md_title(os.path.join(directory, entry))
                result.append(f"{prefix}📝 {entry} - {title}")
            elif entry.endswith(".pdf"):
                result.append(f"{prefix}📘 {entry}")
            elif entry.endswith(('.xls', '.xlsx')):
                result.append(f"{prefix}📊 {entry}")
            elif entry.endswith(('.doc', '.docx')):
                result.append(f"{prefix}📓 {entry}")
            elif entry.endswith(('.ppt', '.pptx')):
                result.append(f"{prefix}📽️ {entry}")
            else:
                result.append(f"{prefix}📄 {entry}")
    return result

def print_tree(directory):
    """打印目录树"""
    tree = generate_tree(directory)
    if tree:
        return "\n".join(tree)
    return "没有符合条件的文件或文件夹。"

# 调用函数
print(print_tree("./docs"))
