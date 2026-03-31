# 人工智能代理指南

## 概述

本项目提供了多种技能（skills）供人工智能使用。AI Review 的详细规则请参考 `REVIEW.md`。

## 可用技能

### 1. read - Markdown 文件读取与分析工具集

**功能**：提供目录扫描、标题提取、内容预览等功能，帮助快速了解文档结构和内容概要。

**使用场景**：

- 快速浏览整个文档库的标题分布
- 检查文档命名规范
- 生成文档目录索引
- 查看文档的结构层次
- 快速定位特定章节
- 检查标题层级是否合理
- 快速预览文档内容
- 检查文档开头是否包含必要的元数据
- 判断文档是否符合写作规范

**工具说明**：

- `dir_h1.js`：遍历 `docs` 文件夹下的所有 `.md` 文件，输出每个文件的第一个 H1 标题
- `file_headings.js`：提取指定文件的所有标题（所有 `#` 开头的行），并在前面加上行号
- `file_prelimit.js`：输出文件内容的前 1000 个字符（计算字数时不含空行和空格，但输出包含），用于快速预览文档内容
- `file_split.js`：将文件按照 20000 个字符分割成多个临时文件，便于处理大型文档

**命令格式**：

```bash
node scripts/skills/read/dir_h1.js
node scripts/skills/read/file_headings.js <file_path>
node scripts/skills/read/file_prelimit.js <file_path>
node scripts/skills/read/file_split.js <file_path>
```

### 2. review - Markdown 文章审阅与排版检查专家

**功能**：能够执行 lint 检查、修复错别字和格式问题，确保文章符合项目规范。

**使用场景**：

- 检查 Markdown 文件的排版格式
- 修复错别字、严重的病句
- 纠正低级错误（手误、公式错误、运算错误等）
- 确保文章符合项目规范

**命令格式**：

```bash
# 对指定文件进行排版检查
node scripts/review/review.js lint -- --file <file_path>

# 查看待提交 Markdown 文件的变更及其潜在排版问题
node scripts/review/review.js diff
```

**详细规则**：请参考 `REVIEW.md`。

## 排版规范

所有文档必须遵循 `scripts/rules/style.md` 中定义的排版规范。

## 提示框语法更新

### 标准语法格式

使用带有 `admonition` 属性的 `md` 或 `markdown` 代码块，所有属性均需包裹在 `{}` 内：

````markdown
```md {admonition="类型" title="区块标题"}
这里是内部正文内容，支持各类 Markdown 语法。
```
````

**参数说明**：

- **admonition="xxx"**（必填）：指定区块的类型。如果填入 `note`, `warning`, `tip` 等，会渲染为对应的高亮提示语块；如果填入特殊的 `details`，则会渲染为**默认收缩**的折叠详情区块。
- **title="xxx"**（可选）：区块显示的标题。

**使用示例 1：常规高亮提示块**

````markdown
```md {admonition="warning" title="注意：请勿除以 $0$"}
在进行上述计算时，请确保分母 **绝对不为零**，否则会引发 `ZeroDivisionError`。
```
````

**使用示例 2：详情折叠块 (Details)**

````markdown
```md {admonition="details" title="点击查看 $E=mc^2$ 的详细推导过程"}
根据相对论，我们可以推导出：

1. 质量和能量是等价的
2. 具体的推导公式如下...
```
````

**最佳实践与避坑指南**：

- **规范书写属性**：必须确保使用键值对加引号的标准格式（如 `{admonition="note"}`），切勿将属性写在括号外，也不要混用原生类名写法（绝对不要写成 `.admonition`）。
- **标题引号转义**：如果你的 `title` 文本中本身包含双引号 `"`，请将其替换为单引号 `'` 或中文双引号 `""`，避免破坏底层属性解析树（例如正确写法：`title="关于'测试'的说明"`）。
- **发挥 Markdown 的能力**：组件的 `title` 属性以及内部的正文区域，均已被深度接管并支持二次 Markdown 解析。请尽情在标题中使用加粗 `**`、行内代码 `` ` ``、数学公式 `$X^2$` 等复杂格式，它们都能被完美渲染。
- **保持空行隔离**：在 ` ```md ` 代码块的上方和下方，建议各保留一个**空行**，这能确保 Markdown 解析树的结构最稳固，防止由于紧贴上下文引起的渲染异常。

## 规则文件维护说明

### 自动维护的规则文件

以下目录中的规则文件由 precommit 钩子自动维护和同步，**请勿手动修改**：

- `.clinerules/` - Cline IDE 规则
- `.gemini/` - Gemini IDE 规则  
- `.kilo/` - Kilo IDE 规则
- `.kilocode/` - KiloCode IDE 规则

### 需要手动修改的规则文件

如果你需要更新项目规范，请修改以下文件：

- `scripts/rules/style.md` - 主要排版规范文件

修改后，precommit 钩子会自动将更新同步到上述自动维护的规则目录中。

## 工作流程

### 文档阅读

1. 使用 `read` skill 快速了解文档结构
2. 根据需要选择合适的工具进行深入分析

### 文档审查

1. 阅读 `REVIEW.md` 了解详细审查规则
2. 使用 `review` skill 进行格式检查
3. 严格遵循 `style.md` 规范
4. 深度理解内容，纠正实质性错误
5. 反复检查，确保修改没有引入新的问题
