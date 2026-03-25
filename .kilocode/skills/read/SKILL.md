---
name: read
description: Markdown 文件读取与分析工具集，提供目录扫描、标题提取、内容预览等功能，帮助快速了解文档结构和内容概要。
---

对于 Markdown 文件的读取和分析，你需要按照下面的工具说明进行（**在项目根目录下执行 `node scripts/skills/read/<tool>.js`**）：

## 工具说明

### dir_h1 - 目录 H1 扫描器

遍历 `docs` 文件夹下的所有 `.md` 文件，输出每个文件的第一个 H1 标题。

**命令格式**：

```bash
node scripts/skills/read/dir_h1.js
```

**参数**：无

**输出格式**：

```
docs\science\probability\2.md 统计学概述
docs\science\reaction\1.md 化学反应原理
docs\science\solid\1.md 空间几何基础
```

**使用场景**：

- 快速浏览整个文档库的标题分布
- 检查文档命名规范
- 生成文档目录索引

/// note | 注意事项
第一个 H1 不一定在文件第一行，但一定是第一个 `# ` 开头的行。如果文件中有多个 H1，只输出第一个。
///

### file_headings - 文件标题提取器

提取指定文件的所有标题（所有 `#` 开头的行），并在前面加上行号。

**命令格式**：

```bash
node scripts/skills/read/file_headings.js <file_path>
```

**参数**：

- `file_path`：文件相对路径（例如 `docs/science/probability/2.md`）

**输出格式**：

```
[2] # H1
[4] ## H2
[7] ### H3
[10] ## H2 2
```

**使用场景**：

- 查看文档的结构层次
- 快速定位特定章节
- 检查标题层级是否合理

/// note | 标题识别规则
只识别 `#` 后面紧跟空格的行作为标题，例如 `# Title` 会被识别，但 `#Title` 不会被识别。
///

### file_prelimit - 文件内容预览器

输出文件内容的前 1000 个字符（计算字数时不含空行和空格，但输出包含），用于快速预览文档内容。

**命令格式**：

```bash
node scripts/skills/read/file_prelimit.js <file_path>
```

**参数**：

- `file_path`：文件相对路径（例如 `docs/science/probability/2.md`）

**输出格式**：

```
[1] ---
[2] title: 统计学概述
[3] ---
[5] 统计学是一门研究数据收集、分析、解释和呈现的学科。
[6] 它在科学研究、商业决策和社会发展中扮演着重要角色。
```

**特殊处理**：

- 如果文件的第一个非空行是 `---`（YAML frontmatter），则跳过到第二个 `---` 之后开始计数
- 输出包含空行，但计算 1000 字符限制时不包含空行和空格
- 因为排除空行计数，所以输出的行号不一定连续

**使用场景**：

- 快速预览文档内容
- 检查文档开头是否包含必要的元数据
- 判断文档是否符合写作规范

/// note | 字符计算规则
1000 字符限制是指去除空行和空格后的实际内容字符数，但输出时会保留原始格式（包括空行和空格）。
///

## 工作流程

### /overview

// turbo

1. 执行 `node scripts/skills/read/dir_h1.js` 获取所有文档的标题列表。

2. 根据标题列表，选择需要深入了解的文档。

3. 执行 `node scripts/skills/read/file_headings.js <file_path>` 查看文档结构。

4. 执行 `node scripts/skills/read/file_prelimit.js <file_path>` 预览文档内容。

### /inspect

// turbo

1. 执行 `node scripts/skills/read/file_headings.js <file_path>` 查看文档的标题结构。

2. 执行 `node scripts/skills/read/file_prelimit.js <file_path>` 预览文档开头内容。

3. 根据需要，使用其他工具进一步分析文档。

## 其他说明

- **路径格式**：所有文件路径均使用相对路径，相对于项目根目录。

- **编码支持**：工具支持 UTF-8 编码的 Markdown 文件。

- **性能考虑**：`dir_h1` 工具会遍历整个 `docs` 目录，在文件较多时可能需要一定时间。

- **错误处理**：如果文件不存在或无法读取，工具会输出错误信息并继续处理其他文件。
