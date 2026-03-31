#!/usr/bin/env bun
// bun 原生构建脚本 - 原地优化模式
// 直接在输入目录内修改文件，不创建输出目录
// 功能：JS/CSS 压缩 + SourceMap、HTML 深度优化（重排 head、合并内联样式/脚本、清理重复 SEO 标签、最大化网页性能）

import { $, Glob, file } from "bun";
import postcss from "postcss";
import posthtml from "posthtml";
import path from "path";

// PostHTML Plugins
import posthtmlPostcss from "posthtml-postcss";
import posthtmlAltAlways from "posthtml-alt-always";
import posthtmlLinkPreload from "posthtml-plugin-link-preload";
import { posthtmlExternalLink } from "posthtml-external-link";
import posthtmlRemoveDuplicates from "posthtml-remove-duplicates";
import mergeInlineLonghand from "posthtml-postcss-merge-longhand";

// PostCSS Plugins
import autoprefixer from "autoprefixer";
import postcssNested from "postcss-nested";
import cssnano from "cssnano";

// 解析命令行参数
function parseArgs() {
  const args = process.argv.slice(2);
  let dir = "site";

  for (let i = 0; i < args.length; i++) {
    if (args[i] === "--dir" || args[i] === "--input-dir" || args[i] === "--inputDir") {
      dir = args[i + 1];
      i++;
    }
  }
  return { dir };
}

// PostCSS 插件配置
const postcss_plugins = [
  postcssNested(),
  autoprefixer(),
  cssnano(),
];

// PostHTML 插件配置
const posthtml_plugins = [
  posthtmlPostcss(postcss_plugins, { from: undefined }),
  posthtmlAltAlways(),
  mergeInlineLonghand(),
  posthtmlLinkPreload(),
  posthtmlExternalLink(),
  posthtmlRemoveDuplicates("meta"),
];

// 自定义 img alt 插件
const posthtmlImgAlt = () => (tree) => {
  tree.walk((node) => {
    if (node.tag === "img" && node.attrs && node.attrs.src) {
      if (!node.attrs.alt || node.attrs.alt.trim() === "") {
        const src = node.attrs.src;
        const fileName = path.posix.basename(src, path.posix.extname(src));
        node.attrs.alt = decodeURIComponent(fileName) || "image";
      }
    }
    return node;
  });
};

posthtml_plugins.unshift(posthtmlImgAlt());

// HTML 压缩函数
function minifyHtml(html) {
  let result = html;
  result = result.replace(/\n\s+/g, " ").replace(/\s{2,}/g, " ").replace(/>\s+</g, "><");
  result = result.replace(/<!--(?!\[)(?![\s\S]*?\[endif-->)[\s\S]*?-->/g, "");
  return result;
}

// ============================================
// HTML 深度优化 PostHTML 插件
// ============================================

/**
 * 重排 <head> 内元素顺序，优化渲染性能
 * 最佳顺序：meta → title → preload/prefetch → link(stylesheet) → style → script(defer) → script(async) → script
 */
const reorderHead = () => (tree) => {
  tree.walk((node) => {
    if (node.tag !== "head") return node;

    const order = {
      meta: 0,
      title: 1,
      link: 2,
      style: 3,
      script: 4,
    };

    const priority = {
      "preload": 0,
      "prefetch": 1,
      "preconnect": 2,
      "dns-prefetch": 3,
      "stylesheet": 4,
      "icon": 5,
      "canonical": 6,
      "other": 7,
    };

    const scriptPriority = {
      "module": 0,
      "defer": 1,
      "async": 2,
      "other": 3,
    };

    const children = node.content || [];
    const metas = [];
    const title = [];
    const links = [];
    const styles = [];
    const scripts = [];
    const others = [];

    for (const child of children) {
      if (typeof child !== "object" || !child.tag) {
        if (typeof child === "string" && child.trim()) {
          others.push(child);
        }
        continue;
      }

      switch (child.tag) {
        case "meta":
          metas.push(child);
          break;
        case "title":
          title.push(child);
          break;
        case "link": {
          const rel = child.attrs?.rel || "other";
          const relArr = rel.split(" ");
          const p = relArr.reduce((max, r) => Math.max(max, priority[r] ?? priority.other), priority.other);
          links.push({ node: child, priority: p });
          break;
        }
        case "style":
          styles.push(child);
          break;
        case "script": {
          const attrs = child.attrs || {};
          let sp = scriptPriority.other;
          if (attrs.type === "module") sp = scriptPriority.module;
          else if (attrs.defer) sp = scriptPriority.defer;
          else if (attrs.async) sp = scriptPriority.async;
          scripts.push({ node: child, priority: sp });
          break;
        }
        default:
          others.push(child);
      }
    }

    // 排序 links
    links.sort((a, b) => a.priority - b.priority);
    // 排序 scripts
    scripts.sort((a, b) => a.priority - b.priority);

    node.content = [
      ...metas,
      ...title,
      ...links.map((l) => l.node),
      ...styles,
      ...scripts.map((s) => s.node),
      ...others,
    ];

    return node;
  });
};

/**
 * 清理重复的 SEO 标签
 * 保留第一个 og:title, og:description, og:image, twitter:card 等
 * 清理重复的 charset, viewport
 */
const cleanDuplicateSeo = () => (tree) => {
  tree.walk((node) => {
    if (node.tag !== "head") return node;

    const seen = new Set();
    const duplicates = new Set();
    const children = node.content || [];

    const seoKeys = [
      "charset",
      "viewport",
      "og:title",
      "og:description",
      "og:image",
      "og:url",
      "og:type",
      "og:site_name",
      "og:locale",
      "twitter:card",
      "twitter:title",
      "twitter:description",
      "twitter:image",
      "description",
      "keywords",
      "author",
      "canonical",
    ];

    for (let i = 0; i < children.length; i++) {
      const child = children[i];
      if (typeof child !== "object" || !child.tag) continue;

      if (child.tag === "meta") {
        const name = child.attrs?.name || child.attrs?.property || child.attrs?.["http-equiv"] || "";
        const key = name.toLowerCase();

        if (seoKeys.some((s) => key === s || key.includes(s))) {
          if (seen.has(key)) {
            duplicates.add(i);
          } else {
            seen.add(key);
          }
        }
      }

      if (child.tag === "link" && child.attrs?.rel === "canonical") {
        if (seen.has("canonical")) {
          duplicates.add(i);
        } else {
          seen.add("canonical");
        }
      }
    }

    // 移除重复项（从后往前删）
    for (const idx of [...duplicates].sort((a, b) => b - a)) {
      children.splice(idx, 1);
    }

    return node;
  });
};

/**
 * 合并相邻的 <style> 标签
 */
const mergeStyleTags = () => (tree) => {
  tree.walk((node) => {
    if (node.tag !== "head") return node;

    const children = node.content || [];
    const merged = [];
    let currentStyle = null;

    for (const child of children) {
      if (typeof child !== "object" || !child.tag) {
        if (currentStyle) {
          merged.push(currentStyle);
          currentStyle = null;
        }
        merged.push(child);
        continue;
      }

      if (child.tag === "style") {
        if (currentStyle) {
          // 合并内容
          const existingContent = currentStyle.content?.[0] || "";
          const newContent = child.content?.[0] || "";
          currentStyle.content = [existingContent + "\n" + newContent];
        } else {
          currentStyle = { ...child, content: [...(child.content || [])] };
        }
      } else {
        if (currentStyle) {
          merged.push(currentStyle);
          currentStyle = null;
        }
        merged.push(child);
      }
    }

    if (currentStyle) {
      merged.push(currentStyle);
    }

    node.content = merged;
    return node;
  });
};

/**
 * 将 <script> 标签移至 </body> 前（非 defer/async/module 的阻塞脚本）
 * 保留 defer/async/module 脚本在 <head> 中
 */
const moveBlockingScripts = () => (tree) => {
  tree.walk((node) => {
    if (node.tag === "head") {
      const children = node.content || [];
      const blockingScripts = [];
      const keep = [];

      for (const child of children) {
        if (
          typeof child === "object" &&
          child.tag === "script" &&
          !child.attrs?.defer &&
          !child.attrs?.async &&
          child.attrs?.type !== "module"
        ) {
          blockingScripts.push(child);
        } else {
          keep.push(child);
        }
      }

      node.content = keep;
      node._blockingScripts = blockingScripts;
    }

    if (node.tag === "body") {
      const headNode = findHead(tree);
      const blockingScripts = headNode?._blockingScripts || [];

      const children = node.content || [];
      // 在 </body> 前插入阻塞脚本
      node.content = [...children, ...blockingScripts];
    }

    return node;
  });
};

function findHead(tree) {
  let result = null;
  tree.walk((node) => {
    if (node.tag === "head") {
      result = node;
    }
    return node;
  });
  return result;
}

/**
 * 移除空的 HTML 属性
 */
const removeEmptyAttrs = () => (tree) => {
  tree.walk((node) => {
    if (node.attrs) {
      for (const [key, value] of Object.entries(node.attrs)) {
        if (value === "" || value === null || value === undefined) {
          delete node.attrs[key];
        }
      }
    }
    return node;
  });
};

// 将新插件加入 posthtml_plugins
posthtml_plugins.push(reorderHead());
posthtml_plugins.push(cleanDuplicateSeo());
posthtml_plugins.push(mergeStyleTags());
posthtml_plugins.push(moveBlockingScripts());
posthtml_plugins.push(removeEmptyAttrs());

// ============================================
// 处理函数
// ============================================

// 处理 HTML 文件（原地修改）
async function processHtml(dir) {
  const htmlFiles = new Glob(`${dir}/**/*.html`);
  let count = 0;

  for await (const htmlFile of htmlFiles.scan(".")) {
    const content = await file(htmlFile).text();
    const result = await posthtml(posthtml_plugins).process(content, { sync: false });
    const minified = minifyHtml(result.html);
    await Bun.write(htmlFile, minified);
    count++;
  }

  return count;
}

// 处理 CSS 文件（原地压缩 + SourceMap）
async function processCss(dir) {
  const cssFiles = new Glob(`${dir}/**/*.css`);
  let count = 0;

  for await (const cssFile of cssFiles.scan(".")) {
    const content = await file(cssFile).text();
    const result = await postcss(postcss_plugins).process(content, {
      from: cssFile,
      to: cssFile,
      map: { inline: false },
    });

    await Bun.write(cssFile, result.css);
    if (result.map) {
      await Bun.write(cssFile + ".map", result.map.toString());
    }
    count++;
  }

  return count;
}

// 处理 JS 文件（原地压缩 + SourceMap）
async function processJs(dir) {
  let count = 0;
  const jsFiles = new Glob(`${dir}/**/*.js`);

  for await (const jsFile of jsFiles.scan(".")) {
    try {
      const result = await Bun.build({
        entrypoints: [jsFile],
        minify: true,
        packages: "external",
        format: "iife",
        target: "browser",
        sourcemap: "external",
        outdir: path.dirname(jsFile),
      });

      if (result.success && result.outputs.length > 0) {
        // 找到生成的 .js 和 .js.map
        for (const output of result.outputs) {
          const outPath = output.path;
          const outText = await output.text();
          await Bun.write(outPath, outText);
        }
        // 清理原文件（如果输出文件名不同）
        const baseName = path.basename(jsFile, ".js");
        const outJs = path.join(path.dirname(jsFile), `${baseName}.js`);
        if (outJs !== jsFile) {
          await $`mv ${outJs} ${jsFile}`.quiet();
          const outMap = outJs + ".map";
          if (await file(outMap).exists()) {
            await $`mv ${outMap} ${jsFile}.map`.quiet();
          }
        }
      } else {
        // 如果压缩失败，保留原文件
      }
    } catch {
      // 压缩失败，保留原文件
    }
    count++;
  }

  return count;
}

// 主函数
async function main() {
  const { dir } = parseArgs();
  
  const startTime = Date.now();

  const [htmlCount, jsCount, cssCount] = await Promise.all([
    processHtml(dir),
    processJs(dir),
    processCss(dir),
  ]);

  const endTime = Date.now();
  console.log(`HTML: ${htmlCount} 个文件`);
  console.log(`JS: ${jsCount} 个文件`);
  console.log(`CSS: ${cssCount} 个文件`);
  console.log(`构建完成！耗时: ${endTime - startTime}ms`);
}

main().catch((err) => {
  console.error("构建失败:", err);
  process.exit(1);
});
