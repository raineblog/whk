# Supplement 文件夹内容整合工作流程

## 概述

本工作流程用于将 `dev/supplement` 文件夹中的内容整理成笔记形式，并补充到 `docs` 文件夹下的相应文章中。这是一个需要高度组织性和写作技巧的任务，需要严格遵循项目的写作风格和排版规范。

## 前置条件

### 必需技能和资源

1. **阅读并理解 AGENTS.md**：必须首先阅读项目根目录下的 `AGENTS.md` 文件，了解可用的技能和工具
2. **使用 read skill**：使用 `scripts/skills/read/` 中的工具来分析文档结构
3. **使用 review skill**：使用 `scripts/skills/review/` 中的工具来检查排版格式
4. **熟悉项目规范**：阅读并理解 `scripts/rules/styleguide.md` 中的排版规范

### 环境准备

```bash
# 切换到 git 的 dev 分支
git checkout dev

# 确保在项目根目录
cd d:/Github/blog/whk
```

## 详细工作流程

### 第一阶段：分析和规划

#### 步骤 1：查看 supplement 文件夹内容

**目标**：了解 `dev/supplement` 文件夹中的所有文件及其大小

**执行命令**：
```bash
# 列出 supplement 文件夹中的所有文件
node scripts/skills/read/dir_h1.js
```

**预期输出**：获取所有文件的标题列表，了解每个文件的大致内容

**最佳实践**：
- 不要直接读取 supplement 文件夹中的文件内容，因为文件可能很大
- 使用 read skill 工具来获取概览信息
- 记录每个文件的大小，以便合理分配 subagent 任务

#### 步骤 2：分析文档结构

**目标**：了解 docs 文件夹的结构，确定每个 supplement 文件应该插入到哪个文档中

**执行命令**：
```bash
# 查看 docs 文件夹的结构
node scripts/skills/read/dir_h1.js

# 查看 supplement 文件夹的结构
node scripts/skills/read/dir_h1.js dev/supplement
```

**分析要点**：
- 每个 supplement 文件的第一行通常指明了应该插入的 docs 文件
- 使用 `file_prelimit.js` 读取文件开头内容，确认目标文件路径
- 识别 supplement 文件与 docs 文件的对应关系
- 规划每个文件的整合策略

**重要说明**：
- 不要直接读取 supplement 文件的第一行，因为第一行可能不准确
- 使用 `file_prelimit.js` 读取文件开头内容，确认用户指定的目标文件
- 确保用户在前几行写的内容正确，避免用户误操作导致人工智能瞎写

#### 步骤 3：制定任务分配计划

**目标**：根据文件大小和复杂度，制定合理的 subagent 任务分配

**分配原则**：
- 每个 subagent 处理 2-5 个文件（根据文件大小调整）
- 大文件（>10KB）单独分配一个 subagent
- 相关文件可以分组处理，保持上下文连贯性
- 对于超大文件，使用 file_split.js 进行分割后再分配

**分析目标文档结构**：
```bash
# 查看目标 .md 文件的标题结构
node scripts/skills/read/file_headings.js docs/[路径]/[文件名].md

# 查看目标 .md 文件的开头内容
node scripts/skills/read/file_prelimit.js docs/[路径]/[文件名].md
```

**分析要点**：
- 使用 `file_headings.js` 查看目标文档的标题结构，进行有机融合的初步推断
- 分析目标文档的章节安排和逻辑结构
- 确定 supplement 内容应该插入到哪个章节或段落
- 规划如何保持原文的叙述风格和架构思想

**大文件处理策略**：
```bash
# 对于超大文件，先进行分割
node scripts/skills/read/file_split.js dev/supplement/[大文件名]

# 分割后会生成多个临时文件，可以分别分配给不同的 subagent
# 例如：dev/supplement/[大文件名].001.tmp, dev/supplement/[大文件名].002.tmp 等
```

**输出格式**：
```
任务分配表：
1. Subagent 1: 文件 A, 文件 B (目标: docs/xxx/1.md)
2. Subagent 2: 文件 C (目标: docs/xxx/2.md)
3. Subagent 3: 文件 D, 文件 E (目标: docs/xxx/3.md)
4. Subagent 4: 大文件 F 分割后的部分 1 (目标: docs/xxx/4.md)
5. Subagent 5: 大文件 F 分割后的部分 2 (目标: docs/xxx/4.md)
```

### 第二阶段：内容整合

#### 步骤 4：启动写作编辑 subagent

**目标**：使用 subagent 进行实际的写作编辑工作

**subagent 配置要求**：

1. **传递系统提示词**：将本体代理的系统提示词传入 subagent，确保其具备相同的指导能力

2. **传递必需的规则文件**：
   - `scripts/rules/styleguide.md`：排版规范
   - `.kilocode/rules/ex-copywriting-guidelines.md`：写作指南（如果存在）
   - `.kilocode/rules/ex-` 开头的其他规则文件

3. **传递上下文信息**：
   - 当前处理的 supplement 文件路径
   - 目标 docs 文件路径
   - 写作风格指导（阅读整个文件获取风格特点）

**subagent 指令模板**：

```
你是写作编辑 subagent，负责将 supplement 内容整合到 docs 文档中。

## 任务详情

### 源文件
- 文件路径：dev/supplement/[文件名]
- 文件大小：[大小]

### 目标文件
- 文件路径：docs/[路径]/[文件名].md
- 插入位置：[具体位置描述]

### 执行步骤

1. **阅读规则文件**（按顺序）：
   - 先读取 scripts/rules/styleguide.md，理解排版要求
   - 再读取 .kilocode/rules/ex-copywriting-guidelines.md（如果存在）
   - 最后读取其他 ex- 开头的规则文件

2. **分析目标文档**：
   - 使用 node scripts/skills/read/file_headings.js 查看目标文档的标题结构
   - 使用 node scripts/skills/read/file_prelimit.js 预览文档开头内容
   - 理解文档的整体架构和写作风格

3. **阅读源文件内容**：
   - 仔细阅读 dev/supplement/[文件名] 的完整内容
   - 理解内容的核心要点和逻辑结构

4. **规划整合策略**：
   - 确定内容应该插入到目标文档的哪个位置
   - 规划如何将新内容有机地融入原文
   - 尽量不新增标题（最多添加几个三级标题）
   - 不要使用 `/// note` 这种语法

5. **执行编辑**：
   - 将内容插入到目标文档的合适位置
   - 保持原文的写作风格和叙述特点
   - 确保格式符合排版规范

6. **质量检查**：
   - 运行 node scripts/skills/review/review.js lint -- --file [目标文件路径]
   - 修复任何格式错误
   - 确保修改没有引入新的问题

### 重要限制

- 尽量不新增 Headings，最多添加几个三级标题
- 不要使用 `/// note` 这种语法
- 需要将内容有机插入原文中的合适位置
- 保持原文的写作风格和叙述特点

### 排版规范摘要

- 中英文之间需要增加空格
- 中文与数字之间需要增加空格
- 使用全角中文标点
- 数字使用半角字符
- 公式与正文之间必须有空行
- 列表项之间必须有空行
- 所有缩进必须用四个空格，不能用 TAB
```

#### 步骤 5：监控和协调 subagent

**目标**：确保 subagent 正确执行任务，避免冲突

**监控要点**：
- 每个目标 .md 文件只同时启动一个 subagent
- 多个目标 .md 文件可以同时并发启动
- 避免同时写入同一个文件造成混乱

**协调策略**：
- 使用文件锁或队列机制管理并发写入
- 定期检查 subagent 的进度和状态
- 及时处理 subagent 遇到的问题

#### 步骤 6：提交 commit

**目标**：每修改完一个文件就提交一个 commit，避免丢失工作成果

**执行命令**：
```bash
# 添加修改的文件
git add [文件路径]

# 提交 commit
git commit -m "docs: 整合 supplement 内容到 [文件名]"

# 推送到远程仓库
git push origin dev
```

**最佳实践**：
- 每个文件修改后立即提交
- commit message 清晰描述修改内容
- 定期推送到远程仓库，确保工作不丢失

### 第三阶段：质量保证

#### 步骤 7：执行 review skill 的 lint 检查

**目标**：使用 review skill 的 lint 功能对所有修改的 .md 文件进行排版检查

**执行命令**：
```bash
# 对特定文件进行 lint 检查
node scripts/skills/review/review.js lint -- --file docs/[路径]/[文件名].md

# 对整个文件夹进行检查（逐个文件）
node scripts/skills/review/review.js lint -- --file docs/[路径]/1.md
node scripts/skills/review/review.js lint -- --file docs/[路径]/2.md
```

**最佳实践**：
- 使用 review skill 的 lint 功能，而不是 markdownlint-cli2
- 查看生成的 `<file_path>.log` 文件获取详细报告
- 分析排版错误，但不要直接读取目标 .md 文件
- 将错误信息传递给 subagent 进行修复

#### 步骤 8：启动修复 subagent

**目标**：使用 subagent 修复 review skill 的 lint 发现的排版问题

**subagent 指令模板**：

```
你是排版修复 subagent，负责修复 review skill 的 lint 发现的排版问题。

## 任务详情

### 目标文件
- 文件路径：docs/[路径]/[文件名].md

### 错误信息
[粘贴 review skill lint 的输出]

### 执行步骤

1. **阅读排版规则**：
   - 读取 scripts/rules/styleguide.md，理解排版要求
   - 分析 review skill lint 的错误信息

2. **分析错误**：
   - 理解每个错误的具体含义
   - 确定修复策略

3. **执行修复**：
   - 修复所有发现的排版问题
   - 确保修复不会引入新的问题

4. **验证修复**：
   - 重新运行 review skill lint 检查
   - 确认所有问题都已修复

### 注意事项

- 不要读取目标 .md 文件的完整内容
- 只根据错误信息进行修复
- 保持原文的写作风格和内容不变
- 只修复格式问题，不修改内容
```

#### 步骤 9：最终验证

**目标**：确保所有修改都符合项目规范

**执行命令**：
```bash
# 使用 review skill 的 diff 功能进行最终提交前审阅
node scripts/skills/review/review.js diff
```

**验证清单**：
- [ ] 所有 supplement 内容都已整合到 docs 中
- [ ] 所有修改的文件都已提交 commit
- [ ] 所有文件都通过 review skill 的 lint 检查
- [ ] 使用 review skill 的 diff 功能进行最终提交前审阅
- [ ] 写作风格与原文保持一致
- [ ] 排版格式符合 styleguide.md 要求

**重要说明**：
- 使用 review skill 的 diff 功能进行不完全审查，确保没有遗漏的问题
- diff 功能可以查看待提交 Markdown 文件的变更及其潜在排版问题
- 这是提交前的最后检查步骤，确保所有修改都符合项目规范

### 第四阶段：完成和提交

#### 步骤 10：创建 Pull Request

**目标**：将所有修改提交到主分支

**执行命令**：
```bash
# 确保所有修改都已提交
git status

# 推送所有修改
git push origin dev

# 创建 Pull Request
gh pr create --base main --head dev --title "docs: 整合 supplement 内容到文档" --body "整合 dev/supplement 文件夹中的内容到 docs 文档中"
```

**最佳实践**：
- PR 标题清晰描述修改内容
- PR body 详细说明修改的文件和内容
- 确保所有 CI 检查都通过

## 最佳实践总结

### 提示词工程最佳实践

1. **明确的任务描述**：每个 subagent 都有清晰的任务描述和执行步骤
2. **详细的上下文信息**：提供完整的文件路径、规则文件、写作风格指导
3. **分步骤的指令**：将复杂任务分解为简单的步骤，便于执行
4. **质量检查机制**：每个步骤都有相应的检查和验证

### 工作流程最佳实践

1. **先规划后执行**：在开始工作前，先分析和规划任务
2. **使用工具辅助**：充分利用 read skill 和 review skill 提高效率
3. **及时提交**：每完成一个文件就提交 commit，避免工作丢失
4. **并发处理**：合理使用 subagent 并发处理多个任务
5. **质量保证**：使用 review skill 的 lint 和 diff 功能确保质量

### 写作编辑最佳实践

1. **保持风格一致**：仔细阅读原文，模仿写作风格和叙述特点
2. **有机整合**：将新内容自然地融入原文，不破坏原有结构
3. **最小化修改**：尽量不新增标题，不使用特殊语法
4. **严格遵循规范**：确保所有修改都符合排版规范

## 故障排除

### 常见问题及解决方案

1. **subagent 执行失败**
   - 检查是否正确传递了所有必需的规则文件
   - 确认文件路径是否正确
   - 检查是否有权限问题

2. **排版检查失败**
   - 仔细阅读 review skill lint 的错误信息
   - 对照 styleguide.md 检查具体问题
   - 使用 review skill 进行详细检查

3. **commit 冲突**
   - 确保每个文件只由一个 subagent 处理
   - 使用 git pull 更新最新代码
   - 解决冲突后重新提交

4. **上下文窗口满**
   - 将任务分解为更小的块
   - 使用子代理处理大文件
   - 及时释放不需要的上下文

## 相关资源

- **AGENTS.md**：项目根目录下的代理指南，包含可用技能和工具
- **scripts/rules/styleguide.md**：排版规范详细说明
- **scripts/skills/read/**：文档读取和分析工具
- **scripts/skills/review/**：排版检查和修复工具