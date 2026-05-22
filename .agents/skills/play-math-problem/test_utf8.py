#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试 UTF-8 编码处理的辅助脚本
"""

import sys
import io

# 强制设置 UTF-8 编码
sys.stdout = io.TextIOWrapper(
    sys.stdout.buffer, encoding='utf-8', errors='replace', line_buffering=True
)
sys.stderr = io.TextIOWrapper(
    sys.stderr.buffer, encoding='utf-8', errors='replace', line_buffering=True
)

# Windows 专用处理
if sys.platform == 'win32':
    import ctypes
    ctypes.windll.kernel32.SetConsoleOutputCP(65001)
    ctypes.windll.kernel32.SetConsoleCP(65001)

print("测试中文输出: 成功")
print("测试 LaTeX: $x^2 + y^2 = 1$")
print(f"Python 版本: {sys.version}")
print(f"当前输码: {sys.stdout.encoding}")
print(f"是否为 TTY: {sys.stdout.isatty()}")
