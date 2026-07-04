#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_answer.py

高端数学问题解答生成器。

使用 OpenAI 兼容 API 通过 POE 平台调用模型（支持 kimi-k2.5-fw、gemma-4-31b 等），
采用 Jinja2 模板引擎模拟构建系统提示词。

强制使用流式输出（stream），所有内容实时输出到终端。
"""

import sys
import io

# ========== Windows UTF-8 编码修复 ==========
# 在导入其他模块之前，强制设置 stdout/stderr 为 UTF-8 编码
# 这是处理 Windows 终端乱码问题的关键

# 1. 强制设置 Python 输出编码为 UTF-8
sys.stdout = io.TextIOWrapper(
    sys.stdout.buffer, encoding="utf-8", errors="replace", line_buffering=True
)
sys.stderr = io.TextIOWrapper(
    sys.stderr.buffer, encoding="utf-8", errors="replace", line_buffering=True
)

# 2. Windows 专用：强制切换终端代码页为 UTF-8 (65001)
if sys.platform == "win32":
    import ctypes

    # 设置输出代码页为 UTF-8
    ctypes.windll.kernel32.SetConsoleOutputCP(65001)
    # 设置输入代码页为 UTF-8
    ctypes.windll.kernel32.SetConsoleCP(65001)

import argparse
import os
from pathlib import Path
from typing import Optional, List

# 尝试加载 .env 文件（如果存在）
try:
    from dotenv import load_dotenv

    # 加载脚本所在目录的 .env 文件
    script_dir = Path(__file__).parent
    env_path = script_dir / ".env"
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)
    # 同时尝试加载当前工作目录的 .env
    load_dotenv()
except ImportError:
    pass  # 如果没有安装 python-dotenv，忽略

from jinja2 import Environment, FileSystemLoader, TemplateError
from openai import OpenAI, APIError, AuthenticationError

# 尝试加载 .env 文件（如果存在）
try:
    from dotenv import load_dotenv

    # 加载脚本所在目录的 .env 文件
    script_dir = Path(__file__).parent
    env_path = script_dir / ".env"
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)
    # 同时尝试加载当前工作目录的 .env
    load_dotenv()
except ImportError:
    pass  # 如果没有安装 python-dotenv，忽略

from jinja2 import Environment, FileSystemLoader, TemplateError
from openai import OpenAI, APIError, AuthenticationError


# 配置常量
DEFAULT_MODEL = "kimi-k2.5-fw"
DEFAULT_TEMPERATURE = 0.7
TEMPLATE_FILE = "prompt.md.jinja2"
EXPLORATION_TEMPLATE_FILE = "exploration.md.jinja2"

# 支持的模型列表（控制成本：只允许使用免费/便宜的模型）
# 注意: 使用时应该调用所有可用模型，然后人工智能整合结果
SUPPORTED_MODELS = [
    "gemma-4-31b",  # Google Gemma 4 31B - 轻量级/免费
    "kimi-k2.5-fw",  # Kimi K2.5 - 默认模型，数学推理强
]


def get_poe_client() -> OpenAI:
    """初始化 POE OpenAI 兼容客户端。"""
    api_key = os.environ.get("POE_API_KEY")
    if not api_key:
        raise ValueError(
            "POE_API_KEY 环境变量未设置。\n"
            "请设置 POE_API_KEY 环境变量后重试。\n"
            "示例: set POE_API_KEY=your_api_key  (Windows)\n"
            "      export POE_API_KEY=your_api_key  (Linux/Mac)"
        )

    # POE 平台的 OpenAI 兼容端点
    # 根据官方文档: https://creator.poe.com/docs/external-applications/openai-compatible-api
    # 正确的 base_url 是 https://api.poe.com/v1
    api_base = os.environ.get("POE_API_BASE", "https://api.poe.com/v1")

    return OpenAI(
        api_key=api_key,
        base_url=api_base,
    )


def render_prompt(
    problem: str,
    exploration_content: Optional[str] = None,
    template_dir: Optional[Path] = None,
) -> str:
    """
    使用 Jinja2 模板引擎渲染系统提示词。

    Args:
        problem: 数学问题文本
        exploration_content: 探索日志内容（可选）
        template_dir: 模板目录路径（默认为脚本所在目录）

    Returns:
        渲染后的完整提示词
    """
    if template_dir is None:
        template_dir = Path(__file__).parent

    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    template = env.get_template(TEMPLATE_FILE)

    # 如果没有提供 exploration内容，尝试从 exploration.md.jinja2 加载
    if exploration_content is None:
        exploration_content = load_default_exploration(template_dir)

    try:
        rendered = template.render(
            problem=problem,
            exploration=exploration_content,
        )
    except TemplateError as e:
        raise RuntimeError(f"模板渲染失败: {e}") from e

    return rendered


def load_exploration_files(template_dir: Path) -> list[dict]:
    """
    加载 exploration 目录下所有 .md 文件的内容。

    返回列表，每个元素包含 filename 和 content。
    """
    exploration_dir = template_dir / "exploration"
    files = []

    if exploration_dir.exists() and exploration_dir.is_dir():
        for md_file in sorted(exploration_dir.glob("*.md")):
            try:
                content = md_file.read_text(encoding="utf-8")
                files.append({"filename": md_file.name, "content": content})
            except Exception as e:
                print(f"[警告] 无法读取文件 {md_file}: {e}", file=sys.stderr)

    return files


def load_default_exploration(template_dir: Path) -> str:
    """
    从默认探索模板加载内容，机械聚合 exploration 目录下的所有 .md 文件。"""
    exploration_path = template_dir / EXPLORATION_TEMPLATE_FILE

    if not exploration_path.exists():
        return ""

    # 加载所有 exploration 文件
    exploration_files = load_exploration_files(template_dir)

    # 使用 Jinja2 渲染 exploration 模板
    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    try:
        template = env.get_template(EXPLORATION_TEMPLATE_FILE)
        rendered = template.render(exploration_files=exploration_files)
        return rendered
    except TemplateError as e:
        print(f"[警告] 模板渲染失败: {e}", file=sys.stderr)
        # 如果渲染失败，直接返回原始模板内容
        return exploration_path.read_text(encoding="utf-8")


def stream_answer(
    problem: str,
    model: str = DEFAULT_MODEL,
    temperature: float = DEFAULT_TEMPERATURE,
    exploration_content: Optional[str] = None,
) -> str:
    """
    流式生成数学问题的解答，实时输出到终端。

    包括思考过程（reasoning_content）和最终答案都输出到终端。

    Args:
        problem: 数学问题文本
        model: 使用的模型名称（支持 kimi-k2.5-fw, gemma-4-31b, glm-5.1-t, glm-5-t 等）
        temperature: 模型温度参数
        exploration_content: 探索内容（可选）

    Returns:
        完整的响应内容
    """
    # 渲染提示词
    prompt = render_prompt(problem, exploration_content)

    # 初始化客户端
    client = get_poe_client()

    full_response = []
    in_reasoning = False

    try:
        print(f"[使用模型: {model}, temperature: {temperature}]\n", flush=True)
        print("=" * 60, flush=True)

        response_stream = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "你是一位资深的高中数学专家和竞赛导师。请以专业、严谨且富有洞察力的方式解答数学问题，展示深度的思维和多元的解题路径。",
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=temperature,
            stream=True,  # 强制启用流式输出
            # 其余使用默认参数
        )

        # 流式接收并输出
        for chunk in response_stream:
            if not chunk.choices:
                continue

            delta = chunk.choices[0].delta
            if not delta:
                continue

            # 处理思考过程（reasoning_content）
            if hasattr(delta, "reasoning_content") and delta.reasoning_content:
                if not in_reasoning:
                    in_reasoning = True
                    print("\n[思考过程]", flush=True)
                    print("-" * 40, flush=True)
                content = delta.reasoning_content
                full_response.append(content)
                print(content, end="", flush=True)

            # 处理正式回复内容
            if delta.content:
                if in_reasoning:
                    in_reasoning = False
                    print("\n" + "-" * 40, flush=True)
                    print("[正式解答]\n", flush=True)
                content = delta.content
                full_response.append(content)
                print(content, end="", flush=True)

        # 输出换行符（最后）
        print(flush=True)

        return "".join(full_response)

    except AuthenticationError as e:
        raise RuntimeError(f"API 认证失败: {e}") from e
    except APIError as e:
        raise RuntimeError(f"API 调用错误: {e}") from e
    except Exception as e:
        raise RuntimeError(f"生成答案时发生错误: {e}") from e


def main():
    """命令行入口函数。"""
    parser = argparse.ArgumentParser(
        description="生成高端数学问题的深度解答（强制流式输出）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
支持的模型（AI使用时应调用所有模型整合结果）:
  - kimi-k2.5-fw (默认) - 数学推理强
  - gemma-4-31b - Google 轻量级模型

AI 使用工作流程:
  1. 首先使用 --print-prompt 查看构建好的 prompt
  2. 使用 --all-models 让所有模型同时解答
  3. AI 整合各模型结果，输出最终答案

环境变量配置:
  Windows CMD:   set POE_API_KEY=your_api_key
  Windows PS:    $env:POE_API_KEY="your_api_key"
  Linux/Mac:     export POE_API_KEY="your_api_key"

示例:
  # 查看构建好的 prompt
  python generate_answer.py -p "求导数" --print-prompt
  
  # 所有模型同时解答（AI使用）
  python generate_answer.py -p "不等式证明" --all-models
  
  # 使用单个模型
  python generate_answer.py -p "函数极值" -m gemma-4-31b
  
  # 保存到文件
  python generate_answer.py -p "解析几何" -o output.md
        """,
    )

    parser.add_argument(
        "--problem", "-p", type=str, help="数学问题文本（也可从标准输入读取）"
    )
    parser.add_argument(
        "--model",
        "-m",
        type=str,
        default=DEFAULT_MODEL,
        help=f"使用的模型名称（默认: {DEFAULT_MODEL}）",
    )
    parser.add_argument(
        "--temperature",
        "-t",
        type=float,
        default=DEFAULT_TEMPERATURE,
        help=f"模型温度参数（默认: {DEFAULT_TEMPERATURE}）",
    )
    parser.add_argument(
        "--exploration",
        "-e",
        type=str,
        help="探索内容文件路径（可选，默认使用内置模板）",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        help="输出文件路径（可选，完整内容会同时保存到文件）",
    )
    parser.add_argument(
        "--list-models", "-l", action="store_true", help="列出所有支持的模型"
    )
    parser.add_argument(
        "--print-prompt",
        action="store_true",
        help="输出构建好的 prompt（不调用 API，AI 使用）",
    )
    parser.add_argument(
        "--all-models", action="store_true", help="使用所有模型同时解答（AI 整合结果）"
    )

    args = parser.parse_args()

    # 列出支持的模型
    if args.list_models:
        print("支持的模型列表（AI使用时应调用所有模型）:")
        for i, model in enumerate(SUPPORTED_MODELS, 1):
            marker = " *" if model == DEFAULT_MODEL else ""
            desc = ""
            if model == "kimi-k2.5-fw":
                desc = " - 数学推理强"
            elif model == "gemma-4-31b":
                desc = " - 轻量级模型"
            print(f"  {i}. {model}{marker}{desc}")
        print("\n* 表示默认模型")
        print(
            "\nAI 使用建议: 先用 --print-prompt 查看 prompt，然后用 --all-models 让所有模型同时解答，最后整合结果。"
        )
        return

    # 获取问题内容
    if args.problem:
        problem = args.problem
    elif not sys.stdin.isatty():
        # 从标准输入读取
        problem = sys.stdin.read().strip()
    else:
        parser.error("需要提供 --problem 参数或从标准输入提供问题")

    if not problem.strip():
        parser.error("问题内容不能为空")

    # 加载自定义探索内容（如果有）
    exploration_content = None
    if args.exploration:
        exploration_path = Path(args.exploration)
        if not exploration_path.exists():
            print(f"错误: 探索文件不存在: {exploration_path}", file=sys.stderr)
            sys.exit(1)
        exploration_content = exploration_path.read_text(encoding="utf-8")

    # AI 模式：输出构建好的 prompt
    if args.print_prompt:
        prompt = render_prompt(problem, exploration_content)
        print("=" * 60)
        print("【构建好的 Prompt】")
        print("=" * 60)
        print(prompt)
        print("=" * 60)
        print(f"\nPrompt 长度: {len(prompt)} 字符")
        return

    # AI 模式：所有模型同时解答
    if args.all_models:
        print("【AI 多模型协同模式】")
        print("将使用以下所有模型同时解答，AI 需要整合结果:")
        for model in SUPPORTED_MODELS:
            print(f"  - {model}")
        print("-" * 60)

        all_results = {}
        for model in SUPPORTED_MODELS:
            print(f"\n\n{'=' * 60}")
            print(f"[模型: {model}]")
            print(f"{'=' * 60}")
            try:
                result = stream_answer(
                    problem=problem,
                    model=model,
                    temperature=args.temperature,
                    exploration_content=exploration_content,
                )
                all_results[model] = result
            except Exception as e:
                print(f"[错误] 模型 {model} 调用失败: {e}")
                all_results[model] = f"[Error: {e}]"

        # 输出结果摘要，供 AI 整合
        print(f"\n\n{'=' * 60}")
        print("【所有模型解答完成 - 请 AI 整合以下结果】")
        print(f"{'=' * 60}")
        for model, result in all_results.items():
            print(f"\n--- {model} ---")
            print(result[:500] + "..." if len(result) > 500 else result)

        # 如果指定了输出文件，保存完整结果
        if args.output:
            output_path = Path(args.output)
            full_content = f"# 问题: {problem}\n\n"
            for model, result in all_results.items():
                full_content += f"## 模型: {model}\n\n{result}\n\n---\n\n"
            output_path.write_text(full_content, encoding="utf-8")
            print(f"\n[所有结果已保存到: {output_path}]")
        return

    # 普通模式：单个模型解答
    try:
        full_answer = stream_answer(
            problem=problem,
            model=args.model,
            temperature=args.temperature,
            exploration_content=exploration_content,
        )

        # 如果指定了输出文件，保存完整内容
        if args.output:
            output_path = Path(args.output)
            output_path.write_text(full_answer, encoding="utf-8")
            print(f"\n[解答已保存到: {output_path}]")

    except ValueError as e:
        print(f"配置错误: {e}", file=sys.stderr)
        sys.exit(1)
    except RuntimeError as e:
        print(f"运行错误: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"未知错误: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
