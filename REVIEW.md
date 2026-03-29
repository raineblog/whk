# AI Review 规则

本文档定义了 AI 执行 Markdown 文章审查时的流程、规则和注意事项。

## 审查工具

使用 `scripts/review/` 目录下的审查工具（**在项目根目录下执行 `node scripts/review/review.js <command>`**）。

## 审查流程

1. 执行 `node scripts/review/review.js lint -- --file <file_path>`，结果会写入 `<file_path>.log`（源文件名 + .log）中，你需要阅读这个文件获取 lint 详情。

2. 手动复查并修复 lint 的错误和警告，尽量修复所有错误，除了一些你认为是误判的错误。如果源文件中有大段显然是格式完全混乱的，请你跳过，因为文件可能仍在 draft 阶段。

3. 重复执行 `node scripts/review/review.js lint -- --file <file_path>`，继续检查，直到你认为没有能够修复的错误。

4. 阅读整个文章，修复错别字、严重的病句等，同时纠正一些低级错误（例如手误、公式错误、运算错误等等），你需要深度理解文章和文章所讲解的内容。

5. 重新执行 `node scripts/review/review.js lint -- --file <file_path>` 并修复，确保你的修改没有引入新的格式错误或不规范。

## 命令格式

```bash
# 对指定文件进行排版检查
node scripts/review/review.js lint -- --file <file_path>

# 查看待提交 Markdown 文件的变更及其潜在排版问题
node scripts/review/review.js diff
```

## 其他说明

- **图片引用**：`![](filepath)` 中 filepath 中有中英文连续，autocorrect 会识别并为其添加空格，这是错误的，为了避免引用失效，为了避免不必要的麻烦，这种问题不需要修改，更不需要修改文件名。

- **代码块**：对于 Markdown codeblock 中的文字，默认开启了 autocorrect 中相应配置，但是对于大量英文代码的情况，可能会有问题，如果问题过多，或者你认为可能引起不必要的麻烦，请忽略这类问题。

- **多余空格**：对于中文之间有多余空格，目前的 lint 无法识别，例如从 PDF 中拷贝进去的文字，有 `中 文 之 间 多 余 空 格` 的问题，请你修复为例如 `中文之间多余空格`。

- **KaTeX 公式**：部分 KaTeX 公式使用了自定义宏，尽管我们不建议你使用，但是用户使用就不要动了。请在执行任何命令之前阅读 rules 中的所有内容，确保你掌握整个项目。

- **缩进**：请严格按照 4 空格缩进有无序列表等。

## 排版规范引用

审查时必须严格遵循 `scripts/rules/style-v2.md` 中定义的排版规范。主要包括：

- 中英文、中文与数字之间需要增加空格
- 使用全角中文标点
- 数字使用半角字符
- 不使用过多重复的标点符号
- 公式与正文之间必须有空行
- 列表项之间必须有空行
- 所有缩进必须用四个空格，不能用 TAB
- 一级标题只能有一个
- 最多使用三级标题作为文档的目录
- 数学公式内尽量避免使用中文

## 忽略规则

进行审阅时要忽略以下 patterns：

- `dev/supplement/*`
- `dev/finished/*`
- `.agents`
- `.clinerules`
- `.gemini`
- `.kilo`
- `.kilocode`
- `.qwen`
- `.gitignore` 中的文件

## Workflows

### /diff

// turbo

- 1. 执行 `node scripts/review/review.js diff` 以查看待提交 Markdown 文件的变更及其潜在排版问题。

### /lint

// turbo

1. 执行 `node scripts/review/review.js lint -- --file <file_path>` 对指定 Markdown 文件进行排版检查。

2. 查看生成的 `<file_path>.log` 文件以获取详细报告。
