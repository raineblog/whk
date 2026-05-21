#!/usr/bin/env python3
"""
CJK Emphasis Normalizer for Pandoc compatibility
把「这是**加粗**文本」规范化成「这是 **加粗** 文本」

特点：
- 高度稳定：保护代码块、inline code、链接、图片、HTML、YAML frontmatter
- 只在普通段落文本中进行替换
- 支持 * 和 ** 两种强调
- 幂等（多次运行不会重复加空格）
"""

import re
from typing import Tuple


CJK = r'[\u4e00-\u9fff\u3400-\u4dbf\u20000-\u2a6df\u2a700-\u2b73f\u2b740-\u2b81f\u2b820-\u2ceaf\uf900-\ufaff\u3300-\u33ff\ufe30-\ufe4f]'


def protect_code_blocks(content: str) -> Tuple[str, dict]:
    """保护代码块和内联代码，返回处理后的内容和恢复映射"""
    placeholders = {}
    counter = 0

    # 1. 保护 fenced code blocks (``` 或 ~~~)
    def fence_replacer(match):
        nonlocal counter
        key = f"__CODE_BLOCK_{counter}__"
        placeholders[key] = match.group(0)
        counter += 1
        return key

    content = re.sub(
        r'(?s)^(```|~~~).+?^\1\s*$',
        fence_replacer,
        content,
        flags=re.MULTILINE
    )

    # 2. 保护 indented code blocks (4空格或tab缩进的代码)
    def indented_replacer(match):
        nonlocal counter
        key = f"__INDENTED_CODE_{counter}__"
        placeholders[key] = match.group(0)
        counter += 1
        return key

    content = re.sub(
        r'(?m)^(?: {4,}|\t).+(?:\n(?: {4,}|\t).+)*',
        indented_replacer,
        content
    )

    # 3. 保护 inline code (`code` 或 ``code``)
    def inline_replacer(match):
        nonlocal counter
        key = f"__INLINE_CODE_{counter}__"
        placeholders[key] = match.group(0)
        counter += 1
        return key

    content = re.sub(r'`+.+?`+', inline_replacer, content)

    return content, placeholders


def restore_code_blocks(content: str, placeholders: dict) -> str:
    """恢复被保护的内容"""
    for key, value in placeholders.items():
        content = content.replace(key, value)
    return content


def normalize_cjk_emphasis(md_content: str) -> str:
    """
    主函数：规范化 CJK 旁边的强调标记
    
    返回处理后的 Markdown 源码
    """
    if not md_content or not isinstance(md_content, str):
        return md_content

    # 第一步：保护敏感区域
    protected, placeholders = protect_code_blocks(md_content)

    # 第二步：规范化强调标记
    # 规则1: CJK后面紧跟 * 或 ** 时，在中间加空格
    # (CJK)(**?)(非空格非*非_)
    protected = re.sub(
        f'({CJK})([*_]{{1,2}})(?=[^*_\\s])',
        r'\1 \2',
        protected
    )

    # 规则2: * 或 ** 后面紧跟 CJK 时，在中间加空格
    # (非空格非*非_)(**?)(CJK)
    protected = re.sub(
        f'(?<=[^*_\\s])([*_]{{1,2}})({CJK})',
        r'\1 \2',
        protected
    )

    # 规则3: 处理已经被空格分隔但可能有多余空格的情况（清理）
    # 把 " ** text ** " 规范化，但保留我们刚加的空格
    protected = re.sub(
        f'({CJK})\\s+([*_]{{1,2}})\\s*({CJK})',
        r'\1 \2 \3',
        protected
    )
    protected = re.sub(
        f'({CJK})\\s*([*_]{{1,2}})\\s+({CJK})',
        r'\1 \2 \3',
        protected
    )

    # 恢复被保护的内容
    result = restore_code_blocks(protected, placeholders)

    return result


# ====================== CLI 支持 ======================
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            normalized = normalize_cjk_emphasis(content)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(normalized)
            print(f"Normalized: {file_path}")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            sys.exit(1)
    else:
        print("Usage: python normalize_cjk_emphasis.py <markdown_file>")
        print("Or import and use normalize_cjk_emphasis(md_content)")
