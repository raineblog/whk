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
</p>

---

这里是 **RainPPR** 的高中文化课（WHK）学习笔记集合，主要涵盖理科学习内容。

本仓库不仅包含了基于高中课程标准的知识点总结，还融入了部分进阶竞赛内容以及个人对自然科学逻辑的理解。笔记旨在帮助学生更好地理解数学、物理、化学、生物等学科的底层原理，而非仅仅是死记硬背。

我们在这本笔记里寻找定理与法则，试图理解世界的运行逻辑。但不要忘记，人们习惯于赞美大地的厚重，却往往对破土而出的新芽感到不安，只因它打破了泥土固守的沉寂。生命最深沉的悲剧，莫过于被困在一种“不属于自己的真实”中，在嘈杂的反对声里日渐枯萎。然而，主观意志的意义，恰在于即便身处深渊，亦敢于否定造物者的疏忽。

## 🚀 快速访问

- [**在线阅读**](https://raineblog.dpdns.org/whk/)：通过 MkDocs Material 实时渲染，支持公式搜索、暗黑模式，提供最舒适的阅读体验。

- [**离线 PDF**](https://github.com/raineblog/whk/releases)：由 GitHub Actions 自动构建的最新版 PDF 文档，带目录索引，方便打印与离线查阅。

## 🛠️ 本地开发与构建

本项目基于 [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) 构建。

### 1. 克隆仓库

```bash
git clone --recursive https://github.com/raineblog/whk.git
cd whk
```

### 2. 环境准备

建议使用 Docker 以保证构建环境的一致性。

- **启动本地实时预览**：

    ```bash
    make serve
    ```

    服务启动后，可以通过浏览器访问 `http://localhost:8000`。

- **构建静态站点**：

    ```bash
    make build
    ```

## 🤝 贡献与反馈

本项目主要由 **RainPPR** 个人维护，目的是记录个人的学习历程与思考。

- **纠错与反馈**：非常欢迎通过 [Issues](https://github.com/raineblog/whk/issues) 提交纠错（如错别字、公式错误、逻辑漏洞等）。
- **功能请求**：由于个人维护精力有限，目前**不接受**大规模的功能性添加建议或内容扩充请求。
- **参与贡献**：如果您希望参与维护或修复项目 Bug，请务必先阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 以了解详细的格式规范。

---

> [!NOTE]
> 本文件由人工智能 **Antigravity** (基于 Google Gemini 系列模型) 自动生成，并由人工审核验收。
