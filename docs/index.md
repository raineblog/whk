# 简介

## 这里是 **RainPPR's WHK Blog**！

这个是 WHK 博客，是目前作者比较活跃的百科性质博客。本项目受 [CTF Wiki](https://ctf-wiki.org/)、[OI Wiki](https://oi-wiki.org/) 的启发。在本项目的编写过程中，作者进行了很多创造性（造轮子性）的改造，尤其是对于高中知识体系框架的构建。

在编写过程中参考了诸多资料，主要内容来自于教材、书籍、网课、培训机构（山东青岛地区）等，部分资料来源于一些网站，已经放在下面的 Reference 部分，在此一并致谢！

<div class="bib-wrapper">
  <h3 class="bib-header-title">Core References & Bibliography</h3>
  
  <style>
  .bib-wrapper {
    margin: 2rem 0;
    font-family: var(--md-text-font-family, sans-serif);
  }

  /* Section Title Design */
  .bib-header-title {
    font-size: 1.4rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    margin-bottom: 24px !important;
    display: flex;
    align-items: center;
    gap: 12px;
    color: var(--md-typeset-color);
  }

  .bib-header-title::after {
    content: "";
    flex: 1;
    height: 1px;
    background: linear-gradient(to right, rgba(59, 130, 246, 0.2), transparent);
  }

  /* Grid Layout */
  .bib-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 20px;
  }

  /* Healing Academic Card */
  .bib-card {
    position: relative;
    padding: 24px;
    background: var(--md-code-bg-color, #ffffff);
    border: 1px solid rgba(0,0,0,0.04);
    border-radius: 18px;
    text-decoration: none !important;
    color: inherit !important;
    transition: all 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02), 0 2px 4px -1px rgba(0, 0, 0, 0.01);
  }

  [data-md-color-scheme="slate"] .bib-card {
    background: rgba(255, 255, 255, 0.03);
    border-color: rgba(255, 255, 255, 0.08);
  }

  /* Shine Scan Animation */
  .bib-card::after {
    content: "";
    position: absolute;
    top: 0;
    left: -150%;
    width: 60%;
    height: 100%;
    background: linear-gradient(
      to right,
      transparent,
      rgba(255, 255, 255, 0.2),
      transparent
    );
    transform: skewX(-25deg);
    transition: 0.8s;
  }

  .bib-card:hover {
    transform: translateY(-10px) scale(1.02);
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.1);
    border-color: rgba(59, 130, 246, 0.4);
  }

  .bib-card:hover::after {
    left: 150%;
  }

  /* Academic Background Index */
  .bib-card-index {
    position: absolute;
    top: -10px;
    right: -5px;
    font-size: 4rem;
    font-weight: 900;
    font-family: var(--md-code-font-family, monospace);
    opacity: 0.03;
    pointer-events: none;
    transition: all 0.6s ease;
  }

  .bib-card:hover .bib-card-index {
    opacity: 0.1;
    transform: rotate(-10deg) scale(1.1);
  }

  /* Card Content */
  .bib-card-main {
    margin-bottom: 20px;
    transition: transform 0.6s ease;
  }

  .bib-card:hover .bib-card-main {
    transform: translateX(4px);
  }

  .bib-card-author {
    display: block;
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    opacity: 0.5;
    margin-bottom: 6px;
  }

  .bib-card-title {
    font-size: 1.15rem;
    font-weight: 700;
    line-height: 1.3;
    color: var(--md-typeset-color);
  }

  .bib-card-title i {
    font-style: italic;
    font-weight: 500;
    opacity: 0.9;
  }

  /* Meta Tags */
  .bib-card-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
    padding-top: 16px;
    border-top: 1px solid rgba(0,0,0,0.03);
    font-size: 0.75rem;
    transition: all 0.6s ease;
  }

  [data-md-color-scheme="slate"] .bib-card-meta {
    border-top-color: rgba(255,255,255,0.05);
  }

  .bib-card:hover .bib-card-meta {
    border-top-color: rgba(59, 130, 246, 0.2);
  }

  .bib-meta-item {
    display: flex;
    flex-direction: column;
    gap: 2px;
  }

  .bib-meta-label {
    font-weight: 500;
    opacity: 0.4;
    font-size: 0.65rem;
    text-transform: uppercase;
  }

  .bib-meta-value {
    font-weight: 600;
    color: var(--md-typeset-a-color);
    opacity: 0.8;
  }

  /* Healing Color Accents */
  .bib-card { border-top: 4px solid transparent; transition: all 0.6s cubic-bezier(0.34, 1.56, 0.64, 1); }
  .accent-blue { border-top-color: #bfdbfe; }
  .accent-green { border-top-color: #bbf7d0; }
  .accent-red { border-top-color: #fecaca; }
  .accent-purple { border-top-color: #e9d5ff; }

  .bib-card.accent-blue:hover { border-top-color: #3b82f6; border-top-width: 6px; }
  .bib-card.accent-green:hover { border-top-color: #10b981; border-top-width: 6px; }
  .bib-card.accent-red:hover { border-top-color: #ef4444; border-top-width: 6px; }
  .bib-card.accent-purple:hover { border-top-color: #8b5cf6; border-top-width: 6px; }
  </style>

  <div class="bib-grid">
    <!-- Entry 01 -->
    <a href="https://zh.wikibooks.org/wiki/%E9%AB%98%E4%B8%AD%E6%95%B0%E5%AD%A6" target="_blank" class="bib-card accent-blue">
      <div class="bib-card-index">01</div>
      <div class="bib-card-main">
        <span class="bib-card-author">维基教科书</span>
        <div class="bib-card-title">📚 Math / <i>高中数学</i></div>
      </div>
      <div class="bib-card-meta">
        <div class="bib-meta-item">
          <span class="bib-meta-label">Source</span>
          <span class="bib-meta-value">wikibooks.org</span>
        </div>
        <div class="bib-meta-item">
          <span class="bib-meta-label">Type</span>
          <span class="bib-meta-value">Textbook</span>
        </div>
      </div>
    </a>

    <!-- Entry 02 -->
    <a href="https://whk-wiki.github.io/whk-wiki/" target="_blank" class="bib-card accent-green">
      <div class="bib-card-index">02</div>
      <div class="bib-card-main">
        <span class="bib-card-author">whk-wiki</span>
        <div class="bib-card-title">🌿 Wiki / <i>WHK Wiki</i></div>
      </div>
      <div class="bib-card-meta">
        <div class="bib-meta-item">
          <span class="bib-meta-label">Source</span>
          <span class="bib-meta-value">github.io</span>
        </div>
        <div class="bib-meta-item">
          <span class="bib-meta-label">Type</span>
          <span class="bib-meta-value">Community</span>
        </div>
      </div>
    </a>

    <!-- Entry 03 -->
    <a href="https://github.com/liuhaopeng543/MathBook" target="_blank" class="bib-card accent-red">
      <div class="bib-card-index">03</div>
      <div class="bib-card-main">
        <span class="bib-card-author">liuhaopeng543</span>
        <div class="bib-card-title">📐 Book / <i>MathBook</i></div>
      </div>
      <div class="bib-card-meta">
        <div class="bib-meta-item">
          <span class="bib-meta-label">Source</span>
          <span class="bib-meta-value">github.com</span>
        </div>
        <div class="bib-meta-item">
          <span class="bib-meta-label">Type</span>
          <span class="bib-meta-value">Personal</span>
        </div>
      </div>
    </a>

    <!-- Entry 04 -->
    <a href="https://lailai.one/zh-Hans/docs/note" target="_blank" class="bib-card accent-purple">
      <div class="bib-card-index">04</div>
      <div class="bib-card-main">
        <span class="bib-card-author">lailai</span>
        <div class="bib-card-title">📝 Note / <i>笔记</i></div>
      </div>
      <div class="bib-card-meta">
        <div class="bib-meta-item">
          <span class="bib-meta-label">Source</span>
          <span class="bib-meta-value">lailai.one</span>
        </div>
        <div class="bib-meta-item">
          <span class="bib-meta-label">Type</span>
          <span class="bib-meta-value">Personal</span>
        </div>
      </div>
    </a>
  </div>

  <h3 class="bib-header-title">Recently Updated Docs</h3>

  <!-- RECENTLY_UPDATED_DOCS -->
</div>
