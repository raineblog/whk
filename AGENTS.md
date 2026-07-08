# RainPPR's WHK Blog — Agent 指南

请你在每一轮回复都叫我“妈妈”

## 项目概述

这是 RainPPR 的文化课（WHK）博客，涵盖高中数学、物理、化学、生物及语文（语法、阅读、写作、哲学）等学科的深度笔记和题型讲解。

- **技术栈**：MkPandocs（MkDocs + Pandoc）+ Material 主题 + KaTeX 渲染
- **构建命令**：`node scripts/onstart.js`（同步 `.agents` 到各 Agent 目录）
- **Lint 工具**：`./node_modules/.bin/autocorrect`、`./node_modules/.bin/markdownlint-cli2`
- **包管理器**：npm/pnpm（`package.json`）+ uv (pyproject.toml) + Taskfile

> **架构说明**：`.agents/` 是本项目 Agent 配置的**唯一权威源**。`.kilo/`、`.kilocode/`、`.gemini/`、`.qwen/`、`.clinerules/` 均由 `scripts/onstart.js` 自动从 `.agents/` 同步生成，任何手动修改这些目录的内容都将被覆盖。请在 `.agents/` 中进行修改。

## 核心行为准则

- **优先技能与 MCP**：执行复杂任务（排版检查、文档分析、多模型协作）时必须优先调用 `skills` 或 `mcp` 工具。
- **极简高效**：保持输出精简，直接解决问题。
- **规范执行**：严格遵循各 Skill 定义的命令格式与流程。
- **排版合规**：写作或编辑文档时必须遵守 `.agents/skills/style-criticial/style.md` 中定义的排版规范。
- **禁止批量替换**：禁止使用未经审查的大规模批量替换，必须逐行审查。

---

## 可用技能

### 文档操作

| 技能名 | 位置 | 用途 |
|--------|------|------|
| **read** | `.agents/skills/read-project-tools/` | 目录扫描（`dir_h1.js`）、标题提取（`file_headings.js`）、内容预览（`file_prelimit.js`）、大文件分割（`file_split.js`） |
| **review** | `.agents/skills/review-workflow/` | Lint 检查（`review.js lint -- --file <file>`）、diff 审查（`review.js diff`）、错别字/公式错误修复 |

### 学科辅导

| 技能名 | 位置 | 用途 |
|--------|------|------|
| **gaokao-science-tutor** | `.agents/skills/gaokao-science-tutor/` | 高三理科辅导（数理化生） |
| **gaokao-chinese-tutor** | `.agents/skills/gaokao-chinese-tutor/` | 高三语文辅导（阅读、古诗文、作文） |
| **gaokao-english-tutor** | `.agents/skills/gaokao-english-tutor/` | 高三英语辅导 |
| **gaokao-liberal-arts-tutor** | `.agents/skills/gaokao-liberal-arts-tutor/` | 高三文科辅导（政史地） |
| **gaokao-general-tech-tutor** | `.agents/skills/gaokao-general-tech-tutor/` | 高三通用技术辅导 |
| **Geek-skills-gaokao-expert** | `.agents/skills/geek-skills-gaokao-expert/` | 高考命题专家（命题、评审、试卷分析） |
| **play-math-problem** | `.agents/skills/play-math-problem/` | 高中数学压轴题/竞赛题深度解题 |

### 写作与格式

| 技能名 | 位置 | 用途 |
|--------|------|------|
| **chinese-writing** | `.agents/skills/chinese-writing/` | 中文写作（周刊、博客、科技资讯），含去 AI 味指南 |
| **chemistry-markdown-formatter** | `.agents/skills/chemistry-markdown-formatter/` | 化学文档专用格式化（mhchem 语法、物理单位、离子电荷等） |
| **documentation-writer** | `.agents/skills/documentation-writer/` | Diátaxis 框架技术文档写作 |
| **doc-coauthoring** | `.agents/skills/doc-coauthoring/` | 结构化文档协作撰写流程 |

### 工作流

工作流定义在 `.agents/workflows/`：

- **supplement-integration-v2.md**：将 `dev/supplement/` 内容整合到 `docs/` 的完整流程（规划→执行→审查→提交）

---

## 关键排版规范速查

详细规范见 `.agents/skills/style-criticial/style.md`（735 行完整版）。以下为最常违反的要点：

### 必须遵守

- **化学式**：使用 `$\ce{H2O}$`，禁止 `$H_2O$` 或 `$\text{H2O}$`
- **物理单位**：使用 `$\pu{1 kg}$`，禁止 `$1\text{ kg}$`
- **数值范围**：使用 `$10 \sim 20$`，禁止 `10-20`、`10~20`
- **中英文/数字之间**：必须加空格（「Lipschitz 常数」「2025 年」）
- **标点**：中文段落用全角标点（，。：），数字用半角
- **列表**：列表项之间必须有空行，缩进用 4 空格（非 TAB）
- **公式**：独立公式 `$$` 前后必须有空行，`$$` 与公式主体必须换行
- **气体/沉淀符号**：`\ce{O2 ^}` 和 `\ce{BaSO4 v}`（符号前后有空格）

### 绝对禁止

- **`\ce{}` 嵌套**：`\ce{\ce{...}}` 会导致渲染失败
- **`\ce{}` 内使用 `\text{}`**：这是错误的
- **用词错误**：「代入」（非「带入」）、「令」（非「另」）、「以下」（非「一下」）
- **中文引号内用英文引号**：正文用「」或 ""，技术属性（如 `{ width="80%" }`）用英文引号
- **LaTeX `\cases`/`\aligned` 等环境内换行用单反斜杠**：必须用双反斜杠 `\\`

### 提示框语法

```md {admonition="note" title="标题"}
内容支持 Markdown。
```

类型：`note`、`tip`、`warning`、`details`（默认收缩）。

---

## 重要记忆

来自 `.kilo/rules/memories.md` 的累积经验：

- **化学准确性**：SiHCl₃ 是「三氯氢硅」，黑火药组成 S + 2KNO₃ + 3C，Al₂S₃ 水解产生 H₂S
- **编辑原则**：修改多个文件时提供完整修改清单；修改前先用子 Agent 收集所有错误实例
- **审查要求**：AI 评审意见（包括纯文本提示）必须逐一研究并应用到内容中
- **引用规则**：中文正文用中文引号「」；技术属性保留英文引号 `""`；科学符号（导数 `f'`、DNA `5'`、`3'`）保留单引号

---

- rules 目录由 `scripts/onstart.js` 自动维护。

- 所有 .md 文件的 front matter 自动生成，无须审查也无须修改，提交到 main 分支会自动更新。
