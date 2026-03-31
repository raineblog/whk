import os
import shutil
import sys
import functools
import subprocess
import argparse
import importlib.util
from pathlib import Path

print = functools.partial(print, flush=True)

import yaml
import json
from jinja2 import Environment, FileSystemLoader

script_dir = Path(__file__).resolve().parent
current_dir = Path.cwd()


def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_sidebar(raw_path):
    return load_json(Path("docs") / raw_path.lstrip("/"))


def get_nav():
    nav_config = load_json("docs/nav.json")
    nav = []
    for item in nav_config:
        children = item["children"]
        if type(children) is str:
            children = get_sidebar(children)
        nav.append({item["title"]: children})
    return nav


def check_social_dependencies():
    """
    检查 social 插件的依赖 (cairosvg 和 pillow) 是否可用。
    不仅要检查是否能 import，还要检查是否能正常加载（处理 libcairo-2.dll 缺失等问题）。
    """
    if importlib.util.find_spec("cairosvg") is None:
        return False
    if importlib.util.find_spec("PIL") is None:
        return False

    try:
        import cairosvg
        from PIL import Image

        return True
    except ImportError, OSError, Exception:
        return False


def to_yaml(value, indent=0):
    """将 Python 对象转换为 YAML 格式字符串"""
    text = yaml.dump(
        value, allow_unicode=True, sort_keys=False, default_flow_style=False
    )
    if indent > 0:
        prefix = " " * indent
        lines = text.rstrip().split("\n")
        text = "\n".join(prefix + line if line else line for line in lines)
    return text.rstrip()


def parse_args():
    parser = argparse.ArgumentParser(
        description="我的自定义脚本 CLI", formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument("--build", action="store_true", help="执行构建动作")
    parser.add_argument("--serve", action="store_true", help="启动本地预览服务")

    parser.add_argument(
        "--disable_giscus",
        type=str,
        default="false",
        help="是否禁用 Giscus，默认为 false",
    )

    parser.add_argument(
        "--site_url",
        type=str,
        default="https://example.com",
        help="网站的 URL，包括 https",
    )

    parser.add_argument("--port", type=int, default=8000, help="服务端口，默认为 8000")

    return parser.parse_args()


def main():
    args = parse_args()
    project = load_json("project.json")

    if args.build or args.serve:
        has_social_dependencies = check_social_dependencies()
        if not has_social_dependencies:
            print(
                "[PREBUILD] 未检测到 cairosvg 或 pillow (或相关库缺失)，自动禁用 social 插件。"
            )

        # 准备 Jinja2 上下文
        extra = project.get("extra", {}).copy()
        disable_giscus = args.disable_giscus.lower() in ("true", "1", "yes")
        if disable_giscus:
            extra.pop("giscus", None)

        context = {
            "info": project["info"],
            "extra": extra,
            "site_url": args.site_url,
            "nav": get_nav(),
            "has_social_dependencies": has_social_dependencies,
        }

        # 创建 Jinja2 环境并注册自定义过滤器
        env = Environment(
            loader=FileSystemLoader(script_dir / "templates"),
            keep_trailing_newline=True,
        )
        env.filters["to_yaml"] = to_yaml

        template = env.get_template("build.yml.jinja2")
        output = template.render(context)

        # 写入 mkpandocs.yml
        with open("mkpandocs.yml", "w", encoding="utf-8") as f:
            f.write(output)

        print("[PREBUILD] mkpandocs.yml 已更新。")

        # 判断是否使用 uv
        use_uv = os.path.exists("uv.lock")
        cmd_prefix = ["uv", "run"] if use_uv else []

        if args.build:
            print(f"[BUILD] 执行 {' '.join(cmd_prefix)} mkpandocs build...")
            try:
                subprocess.run(
                    cmd_prefix + ["mkpandocs", "build"], check=True
                )
                print("[FINAL] 构建成功！")
            except subprocess.CalledProcessError as e:
                print(f"[ERROR] 构建失败: {e}")
                sys.exit(1)
        elif args.serve:
            print(
                f"🚀 启动 {' '.join(cmd_prefix)} mkpandocs serve (端口: {args.port})..."
            )
            # try:
            #     subprocess.run(
            #         cmd_prefix
            #         + ["mkdocs", "serve", "--dev-addr", f"0.0.0.0:{args.port}"],
            #         check=True,
            #     )
            # except KeyboardInterrupt:
            #     print("\n[FINAL] 服务已停止。")
            # except subprocess.CalledProcessError as e:
            #     print(f"[ERROR] 服务启动失败: {e}")
            #     sys.exit(1)

    else:
        print("⚠️ 错误: 请指定要执行的操作，例如 --build 或 --serve")
        sys.exit(1)


if __name__ == "__main__":
    main()
