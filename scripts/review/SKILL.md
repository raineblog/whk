---
name: review
description: Markdown 文章审阅与排版检查专家，能够执行 lint 检查、修复错别字和格式问题，确保文章符合项目规范。
---

对于用户指定的文件，你需要按照下面的步骤进行（**在项目根目录下执行 `node scripts/review/review.js <command>`**）：

## 流程指令

1. 执行 `node scripts/review/review.js lint -- --file docs/xxx/xxx.md`，结果会写入 `docs/xxx/xxx.md.log`（源文件名 + .log）中，你需要阅读这个文件获取 lint 详情。

2. 你需要手动进行复查，并进一步修复 lint 的错误和警告，尽量修复所有错误，除了一些你认为是误判的错误。如果源文件中有大段显然是格式完全混乱的，请你跳过，因为文件可能仍在 draft 阶段。

3. 重复执行 `node scripts/review/review.js lint -- --file docs/xxx/xxx.md`，继续检查，直到你认为没有能够修复的错误。

4. 执行完最基础的 lint 后，你需要阅读整个文章，修复错别字、严重的病句等，同时纠正一些低级错误（例如手误、公式错误、运算错误等等），你需要深度理解文章和文章所讲解的内容。

5. 然后，你需要重新执行 `node scripts/review/review.js lint -- --file docs/xxx/xxx.md` 并修复，确保你的修改没有引入新的格式错误或不规范。

## 其他说明

- **图片引用**：`![](filepath)` 中 filepath 中有中英文连续，autocorrect 会识别并为其添加空格，这是错误的，为了避免引用失效，为了避免不必要的麻烦，这种问题不需要修改，更不需要修改文件名。

- **代码块**：对于 Markdown codeblock 中的文字，默认开启了 autocorrect 中相应配置，但是对于大量英文代码的情况，可能会有问题，如果问题过多，或者你认为可能引起不必要的麻烦，请忽略这类问题。

- **多余空格**：对于中文之间有多余空格，目前的 lint 无法识别，例如从 PDF 中拷贝进去的文字，有 `中 文 之 间 多 余 空 格` 的问题，请你修复为例如 `中文之间多余空格`。

- **KaTeX 公式**：部分 KaTeX 公式使用了自定义宏，尽管我们不建议你使用，但是用户使用就不要动了。请在执行任何命令之前阅读 rules 中的所有内容，确保你掌握整个项目。

- **缩进**：请严格按照 4 空格缩进有无序列表等。

## Workflows

### /diff

// turbo

- 1. 执行 `node scripts/review/review.js diff` 以查看待提交 Markdown 文件的变更及其潜在排版问题。

### /lint

// turbo

1. 执行 `node scripts/review/review.js lint -- --file <file_path>` 对指定 Markdown 文件进行排版检查。

2. 查看生成的 `<file_path>.log` 文件以获取详细报告。
