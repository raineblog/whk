# RainPPR's WHK Blog

<p align="center">
  <a href="https://github.com/raineblog/whk/actions/workflows/ci.yml">
    <img src="https://github.com/raineblog/whk/actions/workflows/ci.yml/badge.svg" alt="Build and Deploy">
  </a>
  <a href="https://github.com/raineblog/whk/actions/workflows/export.yml">
    <img src="https://github.com/raineblog/whk/actions/workflows/export.yml/badge.svg" alt="Export to PDF">
  </a>
  <a href="https://github.com/raineblog/whk/releases">
    <img src="https://img.shields.io/github/v/release/raineblog/whk?color=blue&label=version" alt="Version">
  </a>
  <a href="https://github.com/raineblog/whk/graphs/contributors">
    <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat" alt="Contributions Welcome">
  </a>
  <a href="https://deepwiki.com/raineblog/whk">
    <img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki">
  </a>
</p>

---

**RainPPR 的高中文化课（WHK）学习笔记** —— 以理科为核心，涵盖数学、物理、化学、生物等学科的系统性知识总结。

本项目受 [CTF Wiki](https://ctf-wiki.org/) 和 [OI Wiki](https://oi-wiki.org/) 启发，在高中课程标准的基础上，融入了部分竞赛内容及个人对自然科学逻辑的深层理解。我们不仅记录知识点，更试图通过定理与法则的推演，理解世界的运行逻辑。

> 人们习惯于赞美大地的厚重，却往往对破土而出的新芽感到不安，只因它打破了泥土固守的沉寂。生命最深沉的悲剧，莫过于被困在一种"不属于自己的真实"中，在嘈杂的反对声里日渐枯萎。然而，主观意志的意义，恰在于即便身处深渊，亦敢于否定造物者的疏忽。

## 🌐 在线访问

| 类型 | 链接 | 说明 |
|------|------|------|
| **在线阅读** | [raineblog.dpdns.org/whk/](https://raineblog.dpdns.org/whk/) | 基于 MkDocs Material 实时渲染，支持公式搜索、暗黑模式 |
| **PDF 下载** | [GitHub Releases](https://github.com/raineblog/whk/releases) | GitHub Actions 自动构建，带目录索引，支持离线阅读 |

## 📚 内容结构

```
docs/
├── index.md              # 首页简介
├── home/                 # 使用说明、格式规范、路线图等
├── science/              # 高中理科（数学、物理、化学、生物）
│   ├── mathematics/      # 数学
│   ├── mechanics/        # 力学
│   ├── electromagnetism/ # 电磁学
│   ├── reaction/         # 化学反应
│   ├── cell/             # 细胞生物学
│   └── ...
├── cultural/             # 中学文科（语文、英语、历史等）
└── blog/                 # 博客文章（AI 辅助生成）
```

### 理科知识体系

| 学科 | 主要模块 |
|------|----------|
| **数学** | 数列、函数、圆锥曲线、概率统计、组合数学 |
| **物理** | 运动学、力学、电磁学、机械振动、近代物理 |
| **化学** | 元素性质、化学反应、化学平衡、有机化学、实验探究 |
| **生物** | 细胞结构、遗传学、人体生理、物种演化 |

## 🛠️ 技术栈

### 核心框架

- **静态站点生成器**: [MkDocs](https://www.mkdocs.org/) + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- **数学公式渲染**: [KaTeX SSR](https://github.com/raineblog/mkdocs-katex-ssr)（服务端渲染，支持 mhchem）
- **PDF 导出**: [mkdocs-exporter](https://github.com/raineblog/mkdocs-exporter) + Puppeteer + LaTeX

### 主要插件

| 插件 | 功能 |
|------|------|
| `mkdocs-katex-ssr` | KaTeX 服务端渲染，支持宏定义和化学式 |
| `mkdocs-document-dates` | 文档创建/更新时间显示 |
| `mkdocs-glightbox` | 图片灯箱效果 |
| `mkdocs-llmstxt` | 生成 LLM 友好的文本格式 |
| `mkdocs-rss-plugin` | RSS 订阅源 |
| `mkdocs-minify-html-plugin` | HTML 压缩优化 |
| `mkdocs-advanced-seo` | SEO 元数据优化 |
| `mkdocs-blog-plugin` | 博客功能支持 |

### 开发工具

- **包管理**: [uv](https://github.com/astral-sh/uv) (Python), [Bun](https://bun.sh/) (Node.js)
- **代码检查**: markdownlint, autocorrect
- **容器化**: Docker (使用自定义镜像 `ghcr.io/raineblog/mkdocs-docker`)

## 🚀 快速开始

### 前置要求

- [Docker](https://www.docker.com/)（推荐）或
- Python 3.14+ + uv + Node.js 20+

### 方式一：使用 Docker（推荐）

```bash
# 克隆仓库
git clone --recursive https://github.com/raineblog/whk.git
cd whk

# 启动本地预览服务器（访问 http://localhost:8000）
make serve

# 构建静态站点
make build
```

### 方式二：本地环境

```bash
# 克隆仓库
git clone --recursive https://github.com/raineblog/whk.git
cd whk

# 安装 Python 依赖
uv sync --locked

# 安装 Node.js 依赖
bun install --frozen-lockfile

# 启动预览
uv run scripts/generate.py --serve

# 构建站点
uv run scripts/generate.py --build --site_url=https://your-site-url/
```

### Make 命令速查

| 命令 | 说明 |
|------|------|
| `make serve` | 启动本地预览（Docker） |
| `make build` | 构建静态站点 |
| `make lint` | 运行 Markdown 检查 |
| `make pull` | 拉取最新 Docker 镜像 |
| `make sub-update` | 更新 Git 子模块 |
| `make autoblog` | 运行自动博客生成 |
| `make export` | 导出 PDF 文档 |

## 📝 内容创作指南

### 文档规范

本项目使用增强的 Markdown 语法，支持以下特性：

- **数学公式**: 行内 `$...$`，行间 `$$...$$`
- **化学方程式**: `$\ce{2H2 + O2 -> 2H2O}$`
- **物理单位**: `$\pu{1kg}$`, `$\pu{9.6E11}$`
- **提示框**: 使用 `/// note` 和 `/// details` 语法
- **网格布局**: 使用 `<div class="grid">` 实现多栏排版

### 排版规范

详细规范请参阅 [`scripts/rules/styleguide.md`](scripts/rules/styleguide.md)，主要要点：

- 中英文、中文与数字之间需添加空格
- 使用全角中文标点
- 列表项之间必须有空行
- 所有缩进使用 4 个空格（禁用 Tab）
- 一级标题仅能有一个
- 最多使用三级标题构建文档目录

### AI 辅助工具

项目内置了 AI 辅助写作工具：

```bash
# 文档排版检查
node scripts/skills/review/review.js lint -- --file docs/your-file.md

# 查看待提交文件的变更
node scripts/skills/review/review.js diff

# 快速预览文档结构
node scripts/skills/read/file_headings.js docs/your-file.md
```

## 🤖 CI/CD 流程

项目配置了两条主要的工作流：

### 1. CI/CD Pipeline (`.github/workflows/ci.yml`)

- **触发条件**: 推送到 main 分支、定时任务（每周一）、手动触发
- **功能**: 
  - 自动构建静态站点
  - 部署到 GitHub Pages 和 Cloudflare Pages
  - 支持多环境并行构建

### 2. Export to PDF (`.github/workflows/export.yml`)

- **触发条件**: 创建 `v*` 标签、手动触发
- **功能**:
  - 使用 Puppeteer 将网页转换为 PDF
  - 使用 LaTeX 生成带书签的精美文档
  - 自动发布到 GitHub Releases

## 🤝 贡献指南

### 项目定位

本项目由 **RainPPR** 主导维护，旨在记录个人学习历程与思考。

### 参与方式

- **纠错反馈**: 欢迎通过 [Issues](https://github.com/raineblog/whk/issues) 提交错别字、公式错误、逻辑漏洞等问题
- **功能建议**: 由于个人维护精力有限，暂不接受大规模功能扩展请求
- **代码贡献**: 请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解格式规范

### 开发流程

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交变更 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📊 项目统计

- **文档数量**: 100+ 篇知识点文档
- **技术特色**: 
  - 自定义 KaTeX SSR 插件，支持宏定义和化学式
  - 自动化 PDF 导出，支持书签和目录
  - AI 辅助写作与审查流程
- **部署平台**: GitHub Pages + Cloudflare Pages 双站部署

## 📄 许可证

本项目采用双重许可：

- **内容许可**: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
- **代码许可**: [MIT License](LICENSE)

## 🙏 致谢

本项目的编写参考了诸多资料，包括但不限于：

- 教材与课程标准
- 竞赛培训资料（山东青岛地区）
- 在线教育平台与网课资源
- 开源社区的技术支持

特别感谢 [CTF Wiki](https://ctf-wiki.org/) 和 [OI Wiki](https://oi-wiki.org/) 提供的灵感与参考。

---

<div align="center">

**RainPPR's WHK Blog** | 在破碎中寻回自我，在火焰中实现永恒

[GitHub](https://github.com/raineblog/whk) · [博客园](https://www.cnblogs.com/RainPPR) · [X/Twitter](https://x.com/rainppr2008)

</div>
