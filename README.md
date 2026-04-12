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

**RainPPR 的高中文化课（WHK）学习笔记** —— 以理科为核心，涵盖数学、物理、化学、生物等学科的系统性知识总结与深度解析。

本项目受 [CTF Wiki](https://ctf-wiki.org/) 和 [OI Wiki](https://oi-wiki.org/) 启发，在高中课程标准基础上，融入竞赛内容与自然科学逻辑。我们不仅记录知识点，更试图通过定理推演，理解世界的运行逻辑。

> 「人们习惯于赞美大地的厚重，却往往对破土而出的新芽感到不安，只因它打破了泥土固守的沉寂。生命最深沉的悲剧，莫过于被困在一种“不属于自己的真实”中，在嘈杂的反对声里日渐枯萎。然而，主观意志的意义，恰在于即便身处深渊，亦敢于否定造物者的疏忽。」

## 🌐 访问地址

- **在线阅读**：[raineblog.github.io/whk/](https://raineblog.github.io/whk/) (推荐)
- **镜像地址**：[raineblog.dpdns.org/whk/](https://raineblog.dpdns.org/whk/)
- **PDF 下载**：[GitHub Releases](https://github.com/raineblog/whk/releases) (由 GitHub Actions 自动构建)

## 📚 知识体系

项目采用结构化目录组织，涵盖理、文两门：

- **高中理科 (`docs/science/`)**
    - **数学**：数论、函数引论、导数微积分、解析几何、概率统计、组合数学等。
    - **物理**：运动学、牛顿力学、电磁场、波动光学、热力学、近代物理等。
    - **化学**：物质结构、元素性质、反应动力学、平衡移动、有机化学合成等。
    - **生物**：细胞工程、遗传演化、人体调节、生态系统、物种概述等。

- **中学文科 (`docs/cultural/`)**
    - **语言与阅读**：汉语/英语语法、阅读理解方法论、议论文写作等。
    - **人文与技术**：哲学艺术简介、计算机科学、工程设计与结构优化等。

## 🛠️ 技术实现

### 核心架构

- **构建引擎**：[mkpandocs](https://github.com/RainPPR/mkpandocs) —— 基于 Pandoc 的增强型静态站点生成器。
- **UI 主题**：[MkDocs Material](https://squidfunk.github.io/mkdocs-material/) 的深度定制版本。
- **公式渲染**：KaTeX 客户端渲染，确保极速构建与公式显示的绝对准确。

### 特色功能

- **自动化流水线**：使用 GitHub Actions 实现 CI/CD，自动部署并生成 PDF 离线文档。
- **现代化文档流**：支持 Admonition 提示框、图片灯箱 (glightbox)、RSS 订阅、高级 SEO 优化。
- **LLM 友好**：内置 `.txt` 文档导出，方便大型语言模型 (LLM) 进行检索与分析。

## 🚀 快速启动

### 开发环境

1. **Python**：3.14+ (推荐使用 [uv](https://github.com/astral-sh/uv) 管理依赖)
2. **Node.js**：20+

### 本地运行

```bash
# 克隆仓库
git clone --recursive https://github.com/raineblog/whk.git
cd whk

# 安装依赖
uv sync

# 启动本地预览 (默认端口 8000)
uv run scripts/generate.py --serve

# 执行生产环境构建
uv run scripts/generate.py --build --site_url=https://your-site-url/
```

### 使用 Taskfile (可选)

项目支持 `go-task`：

- `task build`：执行站点构建。
- `task sub-update`：同步并更新子模块。

## 🤝 贡献与反馈

- **纠错反馈**：如发现错别字、公式误或逻辑漏洞，请提交 [Issue](https://github.com/raineblog/whk/issues)。
- **排版指南**：创作请参考 [格式手册](https://raineblog.github.io/whk/home/format/)。
- **项目定位**：本项目由 RainPPR 个人维护，旨在打造“像读物一样可阅读”的文化课知识库。

## 📄 许可证

- **内容**：[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- **代码**：[MIT License](LICENSE)

---

<p align="center">
  <b>RainPPR's WHK Blog</b> | 在破碎中寻回自我，在火焰中实现永恒
  <br>
  <a href="https://github.com/raineblog/whk">GitHub</a> · <a href="https://x.com/rainppr2008">Twitter/X</a> · <a href="https://mastodon.social/@rainppr">Mastodon</a>
</p>
