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

# 兼容 mkdocs-material 的 blog 插件及内部组件对 AMP_SUBSTITUTE 的引用
try:
    from markdown.util import AMP_SUBSTITUTE
except ImportError:
    AMP_SUBSTITUTE = "\x02amp\x03"

if not hasattr(pages, "AMP_SUBSTITUTE"):
    pages.AMP_SUBSTITUTE = AMP_SUBSTITUTE

# 为兼容 mkdocs-material 的 blog 插件（如 Excerpt / _ExcerptRelativePathTreeprocessor），
# 注入完整的 MkDocs 官方规范 _RelativePathTreeprocessor 实现
if not hasattr(pages, "_RelativePathTreeprocessor"):

    class _RelativePathTreeprocessor(markdown.treeprocessors.Treeprocessor):
        """
        兼容性处理器：解析并重写 Markdown 元素中的相对路径。
        遵循 MkDocs 官方标准实现规范，供 Material 博客插件等依赖 MkDocs 内部机制的扩展使用。
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

        @classmethod
        def _target_uri(cls, src_path: str, dest_path: str) -> str:
            return posixpath.normpath(
                posixpath.join(posixpath.dirname(src_path), dest_path).lstrip("/")
            )

        @classmethod
        def _possible_target_uris(
            cls, file, path: str, use_directory_urls: bool, suggest_absolute: bool = False
        ):
            """
            根据给定的相对路径，推测并生成文档源文件候选路径（如 index.md, README.md, .md 等），
            供后续在 files 集合中匹配真实物理文件对象。
            """
            target_uri = cls._target_uri(file.src_uri, path)
            yield target_uri

            if posixpath.normpath(path) == ".":
                yield file.src_uri
                return
            tried = {target_uri}

            prefixes = [target_uri, cls._target_uri(file.url, path)]
            if prefixes[0] == prefixes[1]:
                prefixes.pop()

            suffixes = []
            if use_directory_urls:
                suffixes.append(lambda p: p)
            if not posixpath.splitext(target_uri)[-1]:
                suffixes.append(lambda p: posixpath.join(p, "index.md"))
                suffixes.append(lambda p: posixpath.join(p, "README.md"))
            if (
                not target_uri.endswith(".")
                and not path.endswith(".md")
                and (use_directory_urls or not path.endswith("/"))
            ):
                suffixes.append(lambda p: (p[:-5] if p.endswith(".html") else p) + ".md")

            for pref in prefixes:
                for suf in suffixes:
                    guess = posixpath.normpath(suf(pref))
                    if guess not in tried and not guess.startswith("../"):
                        yield guess
                        tried.add(guess)

        def path_to_url(self, url: str) -> str:
            scheme, netloc, path, query, anchor = urlsplit(url)

            # 忽略外部链接或绝对路径
            if scheme or netloc:
                return url
            elif url.startswith(("/", "\\")):
                return url
            elif AMP_SUBSTITUTE in url:
                return url
            elif not path:
                if anchor and self.file:
                    self.links_to_anchors.setdefault(self.file, {}).setdefault(anchor, url)
                return url

            path = urlunquote(path)
            use_directory_urls = (
                getattr(self.config, "use_directory_urls", True) if self.config else True
            )
            possible_target_uris = self._possible_target_uris(
                self.file, path, use_directory_urls
            )

            target_file = None
            for target_uri in possible_target_uris:
                target_file = self.files.get_file_from_path(target_uri)
                if target_file is not None:
                    break

            if target_file is None:
                return url

            if anchor:
                self.links_to_anchors.setdefault(target_file, {}).setdefault(anchor, url)

            rel_url = utils.get_relative_url(target_file.url, self.file.url)
            return urlunsplit(("", "", rel_url, query, anchor))

        def _register(self, md):
            md.treeprocessors.register(self, "relpath", 0)

    pages._RelativePathTreeprocessor = _RelativePathTreeprocessor

# 同步确保 sys.modules 中的 mkdocs.structure.pages 也具有相应属性
if "mkdocs.structure.pages" in sys.modules:
    sys.modules["mkdocs.structure.pages"]._RelativePathTreeprocessor = pages._RelativePathTreeprocessor
    sys.modules["mkdocs.structure.pages"].AMP_SUBSTITUTE = pages.AMP_SUBSTITUTE

from properdocs.__main__ import cli

if __name__ == "__main__":
    cli()
