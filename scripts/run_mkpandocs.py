import sys
import logging
import posixpath
from urllib.parse import urlsplit, urlunsplit, unquote as urlunquote

# 确保 properdocs 的 replacement 模块生效（mkdocs -> properdocs 重定向）
import properdocs.replacement
import properdocs.structure.pages as pages
from properdocs import utils
import markdown.treeprocessors

log = logging.getLogger(__name__)

# 为兼容 mkdocs-material 的 blog 插件及 preview 扩展，补充缺失的 _RelativePathTreeprocessor
if not hasattr(pages, "_RelativePathTreeprocessor"):

    class _RelativePathTreeprocessor(markdown.treeprocessors.Treeprocessor):
        """
        兼容性处理器：解析并重写 Markdown 元素中的相对路径。
        供 material.plugins.blog.structure.Excerpt 等依赖 mkdocs 内部接口的组件使用。
        """

        def __init__(self, file=None, files=None, config=None):
            self.file = file
            self.files = files
            self.config = config
            self.links_to_anchors = {}

        def run(self, root):
            if not self.file or not self.files:
                return root
            for element in root.iter():
                if element.tag == "a":
                    key = "href"
                elif element.tag == "img":
                    key = "src"
                else:
                    continue

                url = element.get(key)
                if url is not None:
                    element.set(key, self.path_to_url(url))
            return root

        def path_to_url(self, url: str) -> str:
            scheme, netloc, path, query, anchor = urlsplit(url)
            if scheme or netloc or not path:
                return url
            path = urlunquote(path)
            target_uri = posixpath.normpath(
                posixpath.join(posixpath.dirname(self.file.src_uri), path).lstrip("/")
            )
            target_file = self.files.get_file_from_path(target_uri)
            if target_file is None:
                return url
            rel_url = utils.get_relative_url(target_file.url, self.file.url)
            return urlunsplit(("", "", rel_url, query, anchor))

    pages._RelativePathTreeprocessor = _RelativePathTreeprocessor

from properdocs.__main__ import cli

if __name__ == "__main__":
    cli()
