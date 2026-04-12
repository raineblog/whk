---
name: review
description: Markdown 文章审阅与排版检查专家，能够执行 lint 检查、修复错别字和格式问题，确保文章符合项目规范。
---

对于用户指定的文件，你需要按照下面的步骤进行（**在项目根目录下执行 `node .agents/skills/review-workflow/review.js <command>`**）：

## 审查流程

1. 执行 `node .agents/skills/review-workflow/review.js lint -- --file <file_path>`，结果会写入 `<file_path>.log`（源文件名 + .log）中，你需要阅读这个文件获取 lint 详情。

2. 手动复查并修复 lint 的错误和警告，尽量修复所有错误，除了一些你认为是误判的错误。如果源文件中有大段显然是格式完全混乱的，请你跳过，因为文件可能仍在 draft 阶段。

3. 重复执行 `node .agents/skills/review-workflow/review.js lint -- --file <file_path>`，继续检查，直到你认为没有能够修复的错误。

4. 阅读整个文章，修复错别字、严重的病句等，同时纠正一些低级错误（例如手误、公式错误、运算错误等等），你需要深度理解文章和文章所讲解的内容。

5. 重新执行 `node .agents/skills/review-workflow/review.js lint -- --file <file_path>` 并修复，确保你的修改没有引入新的格式错误或不规范。

## 命令格式

```bash
# 对指定文件进行排版检查
node .agents/skills/review-workflow/review.js lint -- --file <file_path>

# 查看待提交 Markdown 文件的变更及其潜在排版问题
node .agents/skills/review-workflow/review.js diff
```

## 排版规范说明

审查时必须严格遵循 `scripts/rules/style.md`（或 `AGENTS.md` 中的链接）定义的规范：

- **图片引用**：`![](filepath)` 中 filepath 中有中英文连续，autocorrect 会识别并为其添加空格，这可能导致引用失效。这种问题不需要修改。
- **代码块**：对于大量英文代码的情况，autocorrect 可能会误判，请谨慎处理。
- **多余空格**：修复中文之间的多余空格（例如 `中 文` -> `中文`）。
- **KaTeX 公式**：保留自定义宏，公式与正文之间必须有空行。
- **缩进**：严格使用 4 空格缩进。
- **标点**：使用全角中文标点，数字使用半角字符。

## 忽略规则

进行审阅时要忽略以下 patterns：

- `dev/supplement/*`
- `dev/finished/*`
- `.agents`, `.clinerules`, `.gemini`, `.kilo`, `.kilocode`, `.qwen`
- `.gitignore` 中的文件

## Workflows

### /diff

// turbo

- 1. 执行 `node .agents/skills/review-workflow/review.js diff` 以查看待提交 Markdown 文件的变更及其潜在排版问题。

### /lint

// turbo

1. 执行 `node .agents/skills/review-workflow/review.js lint -- --file <file_path>` 对指定 Markdown 文件进行排版检查。

2. 查看生成的 `<file_path>.log` 文件以获取详细报告。
