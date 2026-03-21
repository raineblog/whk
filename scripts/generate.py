import os
import io
import shutil
import sys

import argparse
from pathlib import Path

import yaml
import json
import toml

from mkdocs.config import load_config
from mkdocs.commands.build import build
from mkdocs.commands.serve import serve

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
    path = current_dir / "docs" / raw_path
    return load_json(path)


def get_nav():
    nav_config = load_json("docs/nav.json")
    nav = []
    for item in nav_config:
        children = item["children"]
        if type(children) is str:
            children = get_sidebar(children)
        nav.append({item["title"]: children})
    return nav


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

    if args.build:
        if (site_url := args.site_url).lower() != "null":
            config_map["site_url"] = site_url

        if "extra" in project:
            config_map["extra"] = project["extra"]
            if args.disable_giscus.lower() in ("true", "1", "yes"):
                config_map["extra"].pop("giscus", None)

        template_defaults = load_yaml(script_dir / "template.yml")
        config_map["nav"] = get_nav()

        dummy_file = io.StringIO(
            yaml.dump(
                config_map | template_defaults,
                allow_unicode=True,
                indent=4,
                sort_keys=False,
            )
        )

        dummy_file.name = os.path.join(os.getcwd(), "mkdocs.yml")

        config = load_config(config_file=dummy_file)
        config["plugins"].run_event("startup", command="build", dirty=False)

        try:
            build(config)
            print("✅ 构建成功！")
        except Exception as e:
            print(f"❌ 构建失败: {e}")
            raise
        finally:
            config["plugins"].run_event("shutdown")

    elif args.serve:
        print("serve")
        # write_site_template('mkdocs.yml', False, 'template.serve.yml')
    else:
        print("⚠️ 错误: 请指定要执行的操作，例如 --build 或 --serve")
        sys.exit(1)


if __name__ == "__main__":
    main()
