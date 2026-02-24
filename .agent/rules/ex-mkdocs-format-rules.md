---
trigger: glob
globs: docs/**/*.md
---

用户使用的 Markdown 标准和扩展参考下面的 mkdocs 配置文件：

```yaml
markdown_extensions:
- abbr
- admonition
- attr_list
- def_list
- footnotes
- md_in_html
- tables
-   pymdownx.arithmatex:
        generic: true
- pymdownx.caret
- pymdownx.keys
- pymdownx.mark
- pymdownx.tilde
- pymdownx.betterem
- pymdownx.blocks.admonition
- pymdownx.blocks.details
- pymdownx.blocks.caption
- pymdownx.blocks.tab
-   pymdownx.highlight:
        anchor_linenums: true
        line_spans: __span
        pygments_lang_class: true
        linenums: true
- pymdownx.inlinehilite
- pymdownx.snippets
- pymdownx.superfences
- pymdownx.magiclink
- pymdownx.smartsymbols
- pymdownx.tasklist
- pymdownx.tabbed
extra_javascript:
- assets/jquery.min.js
- assets/katex/katex.min.js
- assets/katex/contrib/mhchem.min.js
- assets/katex/contrib/auto-render.min.js
- assets/katex/contrib/copy-tex.min.js
extra_css:
- assets/katex/katex-swap.min.css
```

```
katex_options:
            trust: true
            macros:
                # 下面是一些符号的兼容性定义
                "\\RR": "\\mathbb{R}"
                "\\i": "\\mathrm{i}"
                "\\d": "\\mathrm{d}"
                "\\C": "\\mathbb{C}"
                "\\R": "\\mathbb{R}"
                "\\Q": "\\mathbb{Q}"
                "\\Z": "\\mathbb{Z}"
                "\\N": "\\mathbb{N}"
                "\\P": "\\mathbb{P}"
                "\\degree": "^\\circ"
                "\\rank": "\\operatorname{rank}" # 矩阵的秩
                # 下面是一些简写的定义
                "\\op": "\\operatorname"
                "\\paren": "\\left({#1}\\right)"
                "\\bracket": "\\left[{#1}\\right]"
                "\\brace": "\\left\\{{#1}\\right\\}"
                "\\ceil": "\\left\\lceil{#1}\\right\\rceil"
                "\\floor": "\\left\\lfloor{#1}\\right\\rfloor"
                "\\vert": "\\left\\lvert{#1}\\right\\rvert"
                "\\vec": "\\bm" # 默认使用粗体表示向量
                "\\vecc": "\\overrightarrow" # 默认使用上标箭头表示有向线段
                # 下面是一些文化课用的定义
                "\\poly": "\\ce{-\\!\\!\\![ #1 ]_n\\!\\!\\!\\!\\!-}" # 有机化学 聚合物
                "\\el": "#1\\mathrm{#2}^{#3}" # 结构化学 能级
                "\\pH": "p\\ce{H}"
                "\\pOH": "p\\ce{OH}"
                "\\con": "\\left[\\ce{#1}\\right]" # 化学计量 一般表示摩尔浓度
                # 下面都是一些不标准的 Unicode 转移
                "’": "'"
                "，": ","
                "。": "."
                "；": ";"
                "：": ":"
                "！": "!"
                "？": "?"
                "【": "["
                "】": "]"
                "（": "("
                "）": ")"
                "、": ","
                "—": "-"
                "…": "\\dots"
                "·": "\\cdot"
                "->": "\\to"
                "<-": "\\gets"
```

在具体书写上，下面提供一个较为完整的写法提示：

```md
# 一级标题只能有一个

## 可以有多个二级标题

### 最多使用三级标题作为文档的目录

#### 四级标题仅用于表示一个过于复杂的三级标题下的一些较小的分类，你需要注意四级标题不会被包含在文档的目录之中

数学公式书写如下：

$$
\ce{H2 + O2 ->[点燃] H2O}
$$

一些标识使用方法如下：

<div class="grid" markdown>

每一行是一个元素，使用这种写法时，每一行应当是较为简单的段，通常来说这个写法用来放图片。

放图片的适合，一般情况下 grid 是两栏的，这个写法用于将两张图片并排放置。

</div>

<div class="grid cards" markdown>

- 这种写法里面放无序列表，每个元素是一个“卡片”，有时会加一个 note 之类的，具体看下面 note 的解释。

- **经常会这么表示标题**

    ---

    这里是正文内容。

</div>

/// note | 这里是提示的标题
这里是提示的内容
///

这里的 note 还可以替换为 pymdownx 的其他方式，我们不建议使用 mkdocs 所建议的 `!!! note` 写法，尽管我们也支持这种渲染。

/// details | 这里是详细标题
里面的内容默认是收起的、不展开的，虽然可以指定默认展开，但是我们建议如果要默认展开就用 note 而不是 details
///

对于引用图片，可以用 markdown 标准的语法：

![](xxx.png)

也可以指定图片的宽度，一般来说，我们建议必须指定图片的宽度，如果要满屏就设为 `100%`：

![](xxx.png){ width="100%" }

我们还支持将图片左右对齐作为嵌入式，但是我们不推荐你写这种形式，如果你认为需要，请告诉用户让用户自己调整。

```

数学公式内尽量避免使用中文，如果公式里面有很多中文，可以用下面的方式书写：

<center>
输入 $=$ 输出（有效）$+$ 损耗（无效）
</center>

**请谨记这条要求**，尤其是在生物文档中的公式，通常需要用这种格式书写，以及比如说 $+$ 能量的写法：

<center>
$\ce{H2 + O2 -> H2O}+$ 能量
</center>

<center>
同化量（GPP）$=$ 净初级生产量（NPP）$+$ 呼吸消耗（R）
</center>

同时这意味着 HTML 的块可以写，也要与段落之间有空行，尽量避免使用太多无用的 <p> <a> 标签等，如果能用原生的 Markdown 语法，避免使用 HTML 标签。

注意：请严格按照 4 空格缩进有无序列表等。