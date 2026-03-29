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

所有文档必须遵循 `scripts/rules/style-v2.md` 中定义的排版规范。

## 工作流程

### 文档阅读

1. 使用 `read` skill 快速了解文档结构
2. 根据需要选择合适的工具进行深入分析

### 文档审查

1. 阅读 `REVIEW.md` 了解详细审查规则
2. 使用 `review` skill 进行格式检查
3. 严格遵循 `style-v2.md` 规范
4. 深度理解内容，纠正实质性错误
5. 反复检查，确保修改没有引入新的问题
