---
name: play-math-problem
description: 当用户需要解决高中数学、特别是高考压轴题或竞赛入门级别的数学问题时，使用本技能。本技能负责生成深度、多角度的数学解题方案，包括常规解法、进阶技巧和思想模型总结。用于处理函数、导数、不等式、极值点偏移、数列放缩等类型的问题。
---

# Play Math Problem - 高端数学问题解答技能

## 简介

本技能专为解决高中数学（特别是高考压轴题和竞赛入门）问题而设计。它通过模拟构建方式生成专业级的数学解题方案，提供：

- **深度特征透视**：识别题目背后的结构母题
- **多维解法对撞**：同时展示常规和进阶解法
- **精密代数演算**：确保每一步的准确性
- **思想模型提炼**：形成可复用的解题认知 Schema

## 使用场景

当用户需要以下内容时，此技能将被触发：

- 解答高考数学压轴题（函数与导数、解析几何、数列放缩等）
- 提供多种解法对比（基准路径 vs 高维路径）
- 进行不等式证明、极值点偏移分析
- 数列求和与放缩推导
- 定位题目的结构特征和同构变换

## 文件结构

```
play-math-problem/
├── SKILL.md                  # 技能文档（本文件）
├── generate_answer.py        # 核心解题脚本
├── prompt.md.jinja2          # 系统提示词模板（Jinja2）
├── exploration.md.jinja2     # 探索日志模板
├── exploration/
│   └── function.md           # 函数探索技能库（参考资料）
├── pyproject.toml            # Python 项目配置
└── .venv/                    # 虚拟环境
```

## 核心实现

### 1. generate_answer.py

该脚本负责：

- 使用 OpenAI 兼容 API 调用 `kimi-k2.5-fw` 模型
- 通过 Jinja2 模板引擎渲染 `prompt.md.jinja2`
- 设置模型参数：`temperature=0.7`，其余使用默认配置
- 处理错误情况（API 失败、模板渲染异常等）

### 2. Prompt 模板（prompt.md.jinja2）

采用模拟构建模式，关键变量：

- `{{ exploration }}` - 动态插入探索内容（来自 `exploration.md.jinja2` 或其他探索文件）

### 3. 探索库（exploration/function.md）

包含高端数学解题的专业技能：

- 反函数性质、Lambert W 函数
- 参变分离、端点效应、切线放缩
- 同构变换（指对同构、复合同构、混合结构）
- 极值点偏移与对数均值不等式
- 齐次化与变量消元
- 导数指纹识别与积分因子
- 极限论与数列放缩

## 调用方式

### 作为独立脚本运行

#### 1. 环境变量配置

首先需要设置 POE API 密钥：

**方式一：直接设置环境变量**

```bash
# Windows (CMD)
set POE_API_KEY=your_api_key_here

# Windows (PowerShell)
$env:POE_API_KEY="your_api_key_here"

# Linux/Mac
export POE_API_KEY="your_api_key_here"
```

**方式二：创建 .env 文件（推荐）**

在技能目录创建 `.env` 文件：

```
POE_API_KEY=your_api_key_here
# 可选: POE_API_BASE=https://api.poe.com/chat/completions
```

脚本会自动检测并加载 `.env` 文件中的环境变量（需要安装 python-dotenv）：
```bash
pip install python-dotenv
```

#### 2. 指定模型运行

```bash
# 进入技能目录
cd .agents/skills/play-math-problem

# 激活虚拟环境
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate    # Windows

# 查看支持的模型列表
python generate_answer.py --list-models

# 使用默认模型 (kimi-k2.5-fw) - 所有输出实时流式显示
python generate_answer.py --problem "当 $x > 0$ 时，证明 $e^x > 1 + x + \frac{x^2}{2}$"

# 指定其他模型
python generate_answer.py -p "求函数极值" -m gemma-4-31b
python generate_answer.py -p "不等式证明" -m glm-5.1-t -t 0.5
python generate_answer.py -p "数列求和" -m glm-5-t
python generate_answer.py -p "几何问题" -m claude-sonnet-4-20250514

# 保存到文件（同时仍会实时显示输出）
python generate_answer.py -p "复杂导数题" -o output.md
```

#### 支持的模型（成本控制：仅允许便宜模型）

| 模型 | 描述 |
|------|------|
| `kimi-k2.5-fw` | 默认模型，Kimi K2.5 版本，数学推理强 |
| `gemma-4-31b` | Google Gemma 4 31B，轻量级/免费模型 |

### 作为技能被 AI 调用

当用户提出数学问题时，Claude 应该：

**Step 1: 查看构建好的 Prompt**

```bash
python generate_answer.py -p "问题内容" --print-prompt
```

这会输出完整的系统提示词（包括 exploration 模板内容），帮助 AI 理解整个解题框架。

**Step 2: 使用所有模型同时解答**

```bash
python generate_answer.py -p "问题内容" --all-models
```

这会调用所有三个模型（kimi-k2.5-fw, gemma-4-31b）同时解答问题，并实时流式输出每个模型的结果。

**Step 3: AI 整合所有模型结果**

AI 需要综合三个模型的输出：

1. **对比不同解法**：各模型可能有不同的解题角度
2. **筛选最优解**：选择最清晰、最严谨的步骤
3. **补充进阶技巧**：主动补充模型可能遗漏的高级技巧
4. **统一格式**：按照【常规解法】【进阶解法/技巧】【总结与反思】结构输出

**Step 4: 将最终结果呈现给用户**

结合三个模型的优势，输出一个完整、深度的解答。

## 输出格式

模型输出包含三个明确部分：

1. **【常规解法】** - 基于标准考纲的严谨推导
2. **【进阶解法/技巧】** - 利用二级结论、同构变换等的高效思路
3. **【总结与反思】** - 思想模型提炼和迁移应用

## 技术规范

- 所有数学公式使用 LaTeX 格式（`$...$` 或 `$$...$$`）
- 严格遵循中英文排版空格规约
- 关键步骤编号，重要结论加粗强调
- 保持非 AI 化的专家口吻

## 依赖项

- Python >= 3.13
- jinja2 >= 3.1.6
- openai >= 2.36.0

## 配置说明

### 环境变量配置

API 调用配置通过环境变量：

| 变量 | 说明 | 必填 |
|------|------|------|
| `POE_API_KEY` | POE 平台 API 密钥 | ✓ 必须 |
| `POE_API_BASE` | POE API 基础 URL | ✗ 可选（默认: `https://api.poe.com/v1`） |

### 如何获取 POE API Key

1. 访问 [POE 开发者平台](https://poe.com/developers)
2. 登录并创建新的 API Token
3. 复制 API Key 并保存到环境变量

### 模型参数配置

```bash
# 温度参数（创造性）
-t 0.0   # 最确定，适合严谨证明
-t 0.7   # 默认，平衡性与创造性
-t 1.0   # 最创造，适合探索多种解法
```

### 编码处理说明

本脚本已内置 UTF-8 编码处理，支持中文和数学符号正确显示。如遇到编码问题：

**Windows PowerShell/CMD:**
- 脚本已自动尝试设置 UTF-8 模式
- 如仍有问题，请设置环境变量 `PYTHONIOENCODING=utf-8`

**Linux/Mac:**
- 通常默认支持 UTF-8，无需额外配置

**AI 使用时的编码处理:**
- 如果在调用脚本时遇到乱码，请检查调用环境的编码设置
- 建议在 UTF-8 编码的环境中运行脚本

### 流式输出说明

本脚本**强制使用流式输出**，所有内容（包括思考过程和正式答案）都会实时显示在终端。

- **模型信息**: 开始时显示使用的模型和温度参数
- **思考过程**: 如果模型支持 reasoning_content，会先显示思考过程
- **正式解答**: 思考完成后显示正式解题内容
- **保存文件**: 使用 `-o` 参数可同时保存完整内容到文件

### 常见配置问题

**错误**: `POE_API_KEY 环境变量未设置`  
**解决**:
```bash
# Windows PowerShell
$env:POE_API_KEY="poe-api-key-here"

# Windows CMD
set POE_API_KEY=poe-api-key-here

# Linux/Mac
export POE_API_KEY="poe-api-key-here"
```

**错误**: `API 认证失败`  
**解决**: 检查 API Key 是否正确，或者在 POE 平台确认 Token 状态。
