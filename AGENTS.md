---
trigger: always_on
---

# 人工智能代理指南

## 可用技能

本项目提供了以下技能（skills）供人工智能使用：

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

**工具说明**：
- `review.js`：主要的审查工具，支持 lint 和 diff 命令

**命令格式**：
```bash
# 对指定文件进行排版检查
node scripts/skills/review/review.js lint -- --file <file_path>

# 查看待提交 Markdown 文件的变更及其潜在排版问题
node scripts/skills/review/review.js diff
```

**审查流程**：
1. 执行 lint 命令检查文件
2. 查看生成的 `<file_path>.log` 文件获取详细报告
3. 手动复查并修复错误和警告
4. 重复执行 lint 直到没有能够修复的错误
5. 阅读整个文章，修复错别字、严重的病句等
6. 重新执行 lint 确保修改没有引入新的格式错误

**特殊说明**：
- 图片引用中的中英文连续问题不需要修改
- 代码块中的文字问题可酌情忽略
- 需要修复中文之间多余空格的问题
- 请严格按照 4 空格缩进有无序列表等

## AI Review 规则

当人工智能执行 review 任务时，必须：

1. **使用 review skill**：通过 `node scripts/skills/review/review.js lint -- --file <file_path>` 进行检查
2. **严格遵循 styleguide.md 规范**：所有修改必须符合 `scripts/rules/styleguide.md` 中定义的排版规范
3. **深度理解文章内容**：不仅修复格式问题，还要理解文章内容，纠正实质性的错误
4. **确保修改质量**：修复后需要重新运行 lint 检查，确保没有引入新的问题

## 排版规范摘要

根据 `scripts/rules/styleguide.md` 的要求，主要包括：

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

## 工作流程

### 文档阅读

1. 使用 `read` skill 快速了解文档结构
2. 根据需要选择合适的工具进行深入分析

### 文档审查

1. 使用 `review` skill 进行格式检查
2. 严格遵循 `styleguide.md` 规范
3. 深度理解内容，纠正实质性错误
4. 反复查</parameter>