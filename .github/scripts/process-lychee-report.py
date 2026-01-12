#!/usr/bin/env python3
"""
处理 Lychee 链接检查报告的脚本
功能：
1. 清理报告中的 403 错误、SSL 证误和已解决的重定向
2. 提取重定向信息用于手动或自动替换
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple


def extract_redirect_info(line: str) -> Tuple[str, str] | None:
    """
    从重定向行中提取原始 URL 和目标 URL
    示例: * [200] https://example.com | Redirect: ... --> https://final.com
    """
    # 匹配重定向模式
    redirect_pattern = r'\* \[200\] (https?://[^\s]+) \| .*?--> (https?://[^\s]+)'
    match = re.search(redirect_pattern, line)
    if match:
        return match.group(1), match.group(2)
    return None


def should_remove_line(line: str) -> bool:
    """
    判断是否应该从报告中删除此行
    删除条件：
    1. 403 错误
    2. 412 错误（Precondition Failed，常见于 B站等网站）
    3. SSL 证书验证失败错误
    4. 200 状态的重定向（已经跟随成功）
    """
    # 403 错误
    if '[403]' in line and 'Forbidden' in line:
        return True
    
    # 412 错误
    if '[412]' in line and 'Precondition Failed' in line:
        return True
    
    # SSL 证书错误
    if '[ERROR]' in line and 'SSL certificate verification failed' in line:
        return True
    
    # 200 状态的重定向（已成功跟随）
    if '[200]' in line and 'Redirect:' in line and 'Followed' in line:
        return True
    
    return False


def clean_report(report_path: Path) -> Tuple[List[str], Dict[str, str]]:
    """
    清理报告文件
    返回：(清理后的行列表, 重定向映射字典)
    """
    if not report_path.exists():
        print(f"❌ 报告文件不存在: {report_path}")
        return [], {}
    
    cleaned_lines = []
    redirects = {}
    removed_count = 0
    
    with open(report_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for line in lines:
        # 提取重定向信息
        redirect_info = extract_redirect_info(line)
        if redirect_info:
            original_url, final_url = redirect_info
            redirects[original_url] = final_url
        
        # 判断是否应该删除
        if should_remove_line(line):
            removed_count += 1
            continue
        
        cleaned_lines.append(line)
    
    print(f"✅ 已从报告中移除 {removed_count} 行（403/SSL错误/成功的重定向）")
    print(f"📊 检测到 {len(redirects)} 个重定向链接")
    
    return cleaned_lines, redirects


def save_cleaned_report(report_path: Path, cleaned_lines: List[str]) -> None:
    """保存清理后的报告"""
    with open(report_path, 'w', encoding='utf-8') as f:
        f.writelines(cleaned_lines)
    print(f"💾 已保存清理后的报告: {report_path}")


def save_redirect_mapping(output_path: Path, redirects: Dict[str, str]) -> None:
    """保存重定向映射到文件（即使为空也创建文件）"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# 链接重定向映射\n")
        f.write("# 格式: 原始URL --> 最终URL\n")
        f.write("# 此文件由自动化脚本生成，用于跟踪检测到的重定向链接\n\n")
        
        if redirects:
            for original, final in redirects.items():
                f.write(f"{original} --> {final}\n")
            print(f"💾 已保存 {len(redirects)} 个重定向映射: {output_path}")
        else:
            f.write("# 当前没有检测到重定向链接\n")
            print(f"💾 已创建空的重定向映射文件: {output_path}")


def main():
    """主函数"""
    # 默认路径
    report_path = Path(__file__).parent.parent / 'lychee.md'
    redirect_map_path = Path(__file__).parent.parent / 'redirects.txt'

    print(report_path)
    print(redirect_map_path)
    
    # 如果提供了命令行参数，使用参数路径
    if len(sys.argv) > 1:
        report_path = Path(sys.argv[1])
    
    print("🔧 开始处理 Lychee 报告...")
    print(f"📄 报告路径: {report_path}")
    
    # 清理报告并提取重定向
    cleaned_lines, redirects = clean_report(report_path)
    
    # 保存清理后的报告
    if cleaned_lines:
        save_cleaned_report(report_path, cleaned_lines)
    
    # 保存重定向映射
    if redirects:
        save_redirect_mapping(redirect_map_path, redirects)
        print("\n📝 重定向链接列表：")
        for original, final in redirects.items():
            print(f"  {original}")
            print(f"    └─> {final}")
    
    print("\n✨ 处理完成！")


if __name__ == '__main__':
    main()
