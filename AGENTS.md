# Antigravity Agents Rules

## 核心原则
- **优先技能与 MCP**：在执行复杂任务（如排版检查、文件扫描、多模型协作）时，必须优先调用 `skills` 或 `mcp` 工具。
- **极简高效**：保持输出精简，直接解决问题。
- **规范执行**：严格遵循各 Skill 定义的命令格式与流程。

## 可用技能

### 1. [read - 文档分析](file:///.agents/skills/read-project-tools/SKILL.md)
- **功能**：目录扫描、标题提取、内容预览、文件分割。
- **关键命令**：`node .agents/skills/read-project-tools/dir_h1.js`, `file_headings.js`, `file_prelimit.js`。

### 2. [review - 排版审查](file:///.agents/skills/review-workflow/SKILL.md)
- **功能**：执行 Lint、修复错别字、检查公式规范。
- **关键命令**：`node .agents/skills/review-workflow/review.js lint -- --file <file>`。
- **规范参考**：[style.md](file:///.agents/rules/style.md)。

## 提示框语法 (Admonition)
使用 `{admonition="type" title="Title"}` 语法：
```md {admonition="note" title="注意"}
内容支持 Markdown。
```
类型支持：`note`, `tip`, `warning`, `details` (默认收缩)。

## L-Hub MCP 委派
遇到文案创作、翻译、多文件代码实现等任务，必须通过 `mcp_lhub_ai_ask` 或 `ai_codex_task` 委派给专家模型。

---
* rules 目录同步由 `scripts/onstart.js` 自动维护。*
