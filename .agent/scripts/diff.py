import os
import subprocess
import re

# 定义我们要匹配的特殊字符：逗号、单引号、双引号、左括号、右括号
TARGET_PATTERN = re.compile(r"""[,'"\(\)]""")

# ANSI 颜色转义码，用于在终端中高亮显示输出
class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'

def colorize(line):
    """为 diff 的每一行添加颜色，类似 git diff 控制台效果"""
    if line.startswith('+') and not line.startswith('+++'):
        return f"{Colors.GREEN}{line}{Colors.RESET}"
    elif line.startswith('-') and not line.startswith('---'):
        return f"{Colors.RED}{line}{Colors.RESET}"
    return line

def main():
    diff_file = "temp_diff_output.txt"

    print(f"{Colors.YELLOW}正在执行 git diff (仅筛选 .md 文件)...{Colors.RESET}")
    try:
        # 【修改点 1】：在 git diff 命令后方添加 "--", "*.md"，让 git 只输出 Markdown 文件的变动
        subprocess.run(["git", "diff", f"--output={diff_file}", "--", "*.md"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"{Colors.RED}执行 git diff 失败: {e}{Colors.RESET}")
        return
    except FileNotFoundError:
        print(f"{Colors.RED}未找到 git 命令，请确保已安装 git。{Colors.RESET}")
        return

    # 如果文件不存在，或者体积为 0（代表没有关于 .md 文件的改动）
    if not os.path.exists(diff_file) or os.path.getsize(diff_file) == 0:
        print(f"{Colors.RED}当前没有针对 .md 文件的未提交更改。{Colors.RESET}")
        if os.path.exists(diff_file):
            os.remove(diff_file)
        return

    print(f"{Colors.YELLOW}正在解析 diff 文件...{Colors.RESET}\n")

    # 使用 errors='replace' 避免遇到各种奇葩文件编码导致的读取崩溃
    try:
        with open(diff_file, 'r', encoding='utf-8', errors='replace') as f:
            lines = f.read().splitlines()
    except Exception as e:
        print(f"{Colors.RED}读取 diff 文件失败: {e}{Colors.RESET}")
        return

    hunks =[]
    current_file = None
    current_hunk = None
    current_line_num = 0

    for line in lines:
        if line.startswith("diff --git "):
            # 保存前一个文件的 hunk
            if current_file and current_hunk:
                hunks.append((current_file, current_hunk))
            current_file = None
            current_hunk = None
            continue

        if line.startswith("+++ "):
            filepath = line[4:].strip()
            # 去掉 git 默认的 b/ 前缀
            if filepath.startswith("b/"):
                filepath = filepath[2:]
            
            # 【修改点 2】：双重保险，如果解析到的不是 .md 文件则直接忽略
            if not filepath.lower().endswith('.md'):
                current_file = None
                continue
                
            current_file = filepath
            continue

        if line.startswith("@@ "):
            if current_file and current_hunk:
                hunks.append((current_file, current_hunk))
            
            current_hunk =[]
            # 解析新文件的起始行号，格式类似 @@ -10,3 +15,4 @@
            m = re.match(r"@@ -\d+(?:,\d+)? \+(\d+)(?:,\d+)? @@", line)
            if m:
                current_line_num = int(m.group(1))
            continue

        # 处理在 hunk 内部的具体代码行
        if current_file is not None and current_hunk is not None:
            if line.startswith("+") and not line.startswith("+++"):
                # 检查去掉 '+' 前缀后的实际代码是否包含目标字符
                has_target = bool(TARGET_PATTERN.search(line[1:]))
                current_hunk.append({
                    'raw': line,
                    'is_added': True,
                    'line_num': current_line_num,
                    'has_target': has_target
                })
                current_line_num += 1
            elif line.startswith("-") and not line.startswith("---"):
                current_hunk.append({
                    'raw': line,
                    'is_added': False,
                    'line_num': None, # 删除的行在当前新文件中没有真正的行号
                    'has_target': False
                })
            elif line.startswith(" "):
                current_hunk.append({
                    'raw': line,
                    'is_added': False,
                    'line_num': current_line_num,
                    'has_target': False
                })
                current_line_num += 1
            elif line.startswith("\\"): # \ No newline at end of file
                current_hunk.append({
                    'raw': line,
                    'is_added': False,
                    'line_num': None,
                    'has_target': False
                })
            else:
                # 遇到其他不属于 hunk 的行，结束当前 hunk
                if current_hunk:
                    hunks.append((current_file, current_hunk))
                current_hunk = None

    # 保存最后一个 hunk
    if current_file and current_hunk:
        hunks.append((current_file, current_hunk))

    # 遍历所有解析到的 hunks 并输出匹配的结果
    match_count = 0
    for file_name, hunk in hunks:
        for idx, item in enumerate(hunk):
            if item['is_added'] and item['has_target']:
                match_count += 1
                
                # 获取上一行和下一行 (基于 diff 块的上下文)
                prev_line = hunk[idx-1]['raw'] if idx > 0 else "<位于 Diff 块顶部，无上一行上下文>"
                next_line = hunk[idx+1]['raw'] if idx < len(hunk) - 1 else "<位于 Diff 块底部，无下一行上下文>"
                curr_line = item['raw']
                line_num = item['line_num']

                print(f"{Colors.CYAN}文件: {file_name} (第 {line_num} 行){Colors.RESET}")
                print(f"  上一行: {colorize(prev_line)}")
                print(f"  当前行: {colorize(curr_line)}")
                print(f"  下一行: {colorize(next_line)}")
                print("-" * 60)

    if match_count == 0:
        print(f"{Colors.YELLOW}没有在 .md 文件中找到包含 , ' \" ( ) 的新增或修改行。{Colors.RESET}")
    else:
        print(f"{Colors.GREEN}共找到 {match_count} 处匹配。{Colors.RESET}")

    # 清理产生的临时 diff 文件
    try:
        os.remove(diff_file)
    except OSError:
        pass

if __name__ == "__main__":
    main()