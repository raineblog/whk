import os
import shutil
import sys
import subprocess
import argparse
import importlib.util
from pathlib import Path

import yaml
import json

script_dir = Path(__file__).resolve().parent
current_dir = Path.cwd()


def load_yaml(yaml_path):
    with open(yaml_path, "r", encoding="utf-8") as file:
        text = file.read()
    return yaml.load(text, Loader=yaml.FullLoader)


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
        # 尝试调用一个简单的函数来验证动态链接库是否正常
        # 如果 libcairo-2.dll 缺失，这里会抛出 OSError
        cairosvg.svg2png(bytestring=b"<svg></svg>")
        return True
    except (ImportError, OSError, Exception):
        return False


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
        "--site_url", type=str, default="null", help="网站的 URL，包括 https"
    )

    parser.add_argument("--port", type=int, default=8000, help="服务端口，默认为 8000")

    return parser.parse_args()


def main():
    args = parse_args()
    project = load_json("project.json")
    config_map = project["info"]

    if args.build or args.serve:
        if (site_url := args.site_url).lower() != "null":
            config_map["site_url"] = site_url

        if "extra" in project:
            config_map["extra"] = project["extra"]
            if args.disable_giscus.lower() in ("true", "1", "yes"):
                config_map["extra"].pop("giscus", None)

        template_defaults = load_yaml(script_dir / "template.yml")
        config_map["nav"] = get_nav()

        # 合并配置
        final_config = template_defaults | config_map

        # 确保 site_url 存在 (llmstxt 等插件需要)
        if not final_config.get("site_url"):
            final_config["site_url"] = "https://example.com" # 临时默认值，通常会被覆盖

        # 检查 social 插件依赖
        if not check_social_dependencies():
            print("[PREBUILD] 未检测到 cairosvg 或 pillow (或相关库缺失)，自动禁用 social 插件。")
            if "plugins" in final_config:
                new_plugins = []
                for p in final_config["plugins"]:
                    if isinstance(p, str) and p == "social":
                        continue
                    if isinstance(p, dict) and "social" in p:
                        continue
                    new_plugins.append(p)
                final_config["plugins"] = new_plugins

        # 写入 mkdocs.yml
        with open("mkdocs.yml", "w", encoding="utf-8") as f:
            yaml.dump(final_config, f, allow_unicode=True, indent=4, sort_keys=False)
        
        print("[PREBUILD] mkdocs.yml 已更新。")

        # 判断是否使用 uv
        use_uv = os.path.exists("uv.lock")
        cmd_prefix = ["uv", "run"] if use_uv else []

        if args.build:
            print(f"[BUILD] 执行 {' '.join(cmd_prefix)} mkdocs build...")
            try:
                subprocess.run(cmd_prefix + ["mkdocs", "build"], check=True)
                print("[FINAL] 构建成功！")
            except subprocess.CalledProcessError as e:
                print(f"[ERROR] 构建失败: {e}")
                sys.exit(1)
        elif args.serve:
            print(f"🚀 启动 {' '.join(cmd_prefix)} mkdocs serve (端口: {args.port})...")
            try:
                subprocess.run(cmd_prefix + ["mkdocs", "serve", "--dev-addr", f"0.0.0.0:{args.port}"], check=True)
            except KeyboardInterrupt:
                print("\n[FINAL] 服务已停止。")
            except subprocess.CalledProcessError as e:
                print(f"[ERROR] 服务启动失败: {e}")
                sys.exit(1)

    else:
        print("⚠️ 错误: 请指定要执行的操作，例如 --build 或 --serve")
        sys.exit(1)


if __name__ == "__main__":
    main()
