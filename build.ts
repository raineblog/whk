#!/usr/bin/env bun
/**
 * bun 原生构建脚本 - 原地优化模式
 * 直接在输入目录内修改文件，不创建输出目录
 *
 * 功能:
 *   CSS: PostCSS + cssnano(default) + autoprefixer + sourcemap
 *   JS:  terser 深度压缩 + sourcemap
 *   HTML: PostHTML 深度优化 (去重、重排、合并、压缩) + html-minifier-terser
 *
 * 用法:
 *   bun run build.ts --dir site
 *   bun build --compile build.ts --outfile build-bin && ./build-bin --dir site
 */

import { Glob, file } from "bun";
import postcss from "postcss";
import posthtml from "posthtml";
import { minify as terserMinify } from "terser";
import { minify as htmlMinify } from "html-minifier-terser";
import path from "path";

// PostHTML Plugins
import posthtmlPostcss from "posthtml-postcss";
import posthtmlAltAlways from "posthtml-alt-always";
import { posthtmlExternalLink } from "posthtml-external-link";
import posthtmlRemoveDuplicates from "posthtml-remove-duplicates";
import mergeInlineLonghand from "posthtml-postcss-merge-longhand";

// PostCSS Plugins
import autoprefixer from "autoprefixer";
import postcssNested from "postcss-nested";
import cssnano from "cssnano";

// ============================================================
// Configuration
// ============================================================

const CONCURRENCY = 16;
const LOG_INTERVAL = 50;
const BROWSERSLIST = [
  "last 2 Chrome versions",
  "last 2 Firefox versions",
  "last 2 Safari versions",
  "last 2 Edge versions",
];

// ============================================================
// Shared Batch Processor
// ============================================================

/**
 * 带有并发控制的批处理函数
 */
async function processBatch<T>(
  items: T[],
  limit: number,
  processor: (item: T) => Promise<void>,
  onProgress?: (processed: number, total: number) => void
): Promise<{ count: number; errors: string[] }> {
  let count = 0;
  const errors: string[] = [];

  for (let i = 0; i < items.length; i += limit) {
    const batch = items.slice(i, i + limit);
    const results = await Promise.allSettled(batch.map(processor));

    for (let j = 0; j < results.length; j++) {
      if (results[j].status === "rejected") {
        errors.push(`${batch[j]}: ${(results[j] as PromiseRejectedResult).reason}`);
      } else {
        count++;
      }
    }

    if (onProgress) {
      const processed = Math.min(i + limit, items.length);
      onProgress(processed, items.length);
    }
  }

  return { count, errors };
}

// ============================================================
// Argument Parsing
// ============================================================

function parseArgs(): { dir: string } {
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

// ============================================================
// PostCSS Configuration
// ============================================================

const postcss_plugins = [
  postcssNested(),
  autoprefixer({ overrideBrowserslist: BROWSERSLIST }),
  cssnano({
    preset: [
      "default",
      {
        cssDeclarationSorter: true,
        mergeRules: true,
        mergeIdents: true,
        zindex: false,
      },
    ],
  }),
];

// ============================================================
// PostHTML Custom Plugins
// ============================================================

type PostHTMLNode = {
  tag?: string;
  attrs?: Record<string, string>;
  content?: any[];
};

type PostHTMLTree = {
  walk: (cb: (node: PostHTMLNode) => PostHTMLNode) => void;
  match: (matcher: any, cb: (node: PostHTMLNode) => PostHTMLNode) => void;
};

const posthtmlImgAlt = () => (tree: PostHTMLTree) => {
  tree.walk((node) => {
    if (node.tag === "img" && node.attrs?.src) {
      if (!node.attrs.alt || node.attrs.alt.trim() === "") {
        const src = node.attrs.src;
        const fileName = path.posix.basename(src, path.posix.extname(src));
        node.attrs.alt = decodeURIComponent(fileName) || "image";
      }
    }
    return node;
  });
};

const deduplicateMeta = () => (tree: PostHTMLTree) => {
  tree.walk((node) => {
    if (node.tag !== "head") return node;

    const children = node.content || [];
    const seenKeys = new Map<string, number>();

    for (let i = children.length - 1; i >= 0; i--) {
      const child = children[i];
      if (typeof child !== "object" || !child.tag) continue;

      if (child.tag === "meta") {
        const name = child.attrs?.name || child.attrs?.property || child.attrs?.["http-equiv"] || "";
        if (!name) continue;

        const key = name.toLowerCase();

        if (key === "description" || key === "author" || key === "keywords") {
          if (seenKeys.has(key)) {
            children.splice(seenKeys.get(key)!, 1);
          }
          seenKeys.set(key, i);
        }
      }

      if (child.tag === "link" && child.attrs?.rel === "canonical") {
        const key = "canonical";
        if (seenKeys.has(key)) {
          children.splice(seenKeys.get(key)!, 1);
        }
        seenKeys.set(key, i);
      }
    }

    node.content = children;
    return node;
  });
};

const deduplicateLinks = () => (tree: PostHTMLTree) => {
  tree.walk((node) => {
    if (node.tag !== "head") return node;

    const children = node.content || [];
    const seenLinks = new Set<string>();

    for (let i = children.length - 1; i >= 0; i--) {
      const child = children[i];
      if (typeof child !== "object" || !child.tag || child.tag !== "link") continue;

      const rel = child.attrs?.rel || "";
      const href = child.attrs?.href || "";

      if (rel === "alternate" && href) {
        const type = child.attrs?.type || "";
        const key = `alternate:${type}:${href}`;
        if (seenLinks.has(key)) {
          children.splice(i, 1);
        } else {
          seenLinks.add(key);
        }
      }
    }

    node.content = children;
    return node;
  });
};

const deduplicateStructuredData = () => (tree: PostHTMLTree) => {
  tree.walk((node) => {
    if (node.tag !== "head") return node;

    const children = node.content || [];
    const seenTypes = new Map<string, number>();

    for (let i = children.length - 1; i >= 0; i--) {
      const child = children[i];
      if (typeof child !== "object" || !child.tag) continue;
      if (child.tag !== "script" || child.attrs?.type !== "application/ld+json") continue;

      const content = child.content?.[0] || "";
      try {
        const json = JSON.parse(content);
        // 支持 json 为数组的情况
        const items = Array.isArray(json) ? json : [json];
        let type = "";
        let id = "";
        if (items.length > 0) {
          type = items[0]["@type"] || "";
          id = items[0]["@id"] || "";
        }

        if (!type) continue;

        const key = id ? `${type}:${id}` : type;

        if (seenTypes.has(key)) {
          children.splice(seenTypes.get(key)!, 1);
        }
        seenTypes.set(key, i);
      } catch {
        // Invalid JSON, skip
      }
    }

    node.content = children;
    return node;
  });
};

const reorderHead = () => (tree: PostHTMLTree) => {
  tree.walk((node) => {
    if (node.tag !== "head") return node;

    const children = node.content || [];

    const CATEGORIES = {
      charset: 0,
      viewport: 1,
      title: 2,
      meta: 3,
      preconnect: 4,
      preload: 5,
      stylesheet: 6,
      style: 7,
      script_module: 8,
      script_defer: 9,
      script_async: 10,
      script_blocking: 11,
      other: 12,
    } as const;

    function categorize(child: any): number {
      if (typeof child !== "object" || !child.tag) return CATEGORIES.other;
      if (child.attrs?.["data-no-move"] !== undefined) return CATEGORIES.other;

      switch (child.tag) {
        case "meta": {
          if (child.attrs?.charset !== undefined) return CATEGORIES.charset;
          const httpEquiv = (child.attrs?.["http-equiv"] || "").toLowerCase();
          if (httpEquiv === "content-type") return CATEGORIES.charset;
          const name = (child.attrs?.name || "").toLowerCase();
          if (name === "viewport") return CATEGORIES.viewport;
          return CATEGORIES.meta;
        }
        case "title":
          return CATEGORIES.title;
        case "link": {
          const rel = child.attrs?.rel || "";
          const rels = rel.split(" ");
          if (rels.includes("preconnect") || rels.includes("dns-prefetch")) return CATEGORIES.preconnect;
          if (rels.includes("preload") || rels.includes("prefetch")) return CATEGORIES.preload;
          if (rels.includes("stylesheet")) return CATEGORIES.stylesheet;
          return CATEGORIES.other;
        }
        case "style":
          return CATEGORIES.style;
        case "script": {
          const type = child.attrs?.type;
          if (type === "module") return CATEGORIES.script_module;
          if (child.attrs?.defer !== undefined) return CATEGORIES.script_defer;
          if (child.attrs?.async !== undefined) return CATEGORIES.script_async;
          return CATEGORIES.script_blocking;
        }
        default:
          return CATEGORIES.other;
      }
    }

    const indexed = children.map((child, idx) => ({ child, idx }));
    indexed.sort((a, b) => {
      const catA = categorize(a.child);
      const catB = categorize(b.child);
      if (catA !== catB) return catA - catB;
      return a.idx - b.idx;
    });

    node.content = indexed.map((s) => s.child);
    return node;
  });
};

const mergeStyleTags = () => (tree: PostHTMLTree) => {
  tree.walk((node) => {
    if (node.tag !== "head") return node;

    const children = node.content || [];
    const merged: any[] = [];
    let currentStyle: any = null;

    for (const child of children) {
      if (typeof child !== "object" || !child.tag) {
        if (currentStyle) {
          merged.push(currentStyle);
          currentStyle = null;
        }
        merged.push(child);
        continue;
      }

      if (child.tag === "style" && !child.attrs?.media) {
        if (currentStyle) {
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

const removeRedundantAttrs = () => (tree: PostHTMLTree) => {
  tree.walk((node) => {
    if (!node.attrs) return node;

    if (node.tag === "style" && node.attrs.type === "text/css") {
      delete node.attrs.type;
    }

    // Keep script type attribute - removing it breaks some JS that depends on it
    for (const key of ["class", "id"]) {
      if (node.attrs[key] === "") {
        delete node.attrs[key];
      }
    }

    return node;
  });
};

const removeEmptyElements = () => (tree: PostHTMLTree) => {
  tree.walk((node) => {
    if (node.tag !== "head") return node;

    const children = node.content || [];
    node.content = children.filter((child) => {
      if (typeof child !== "object" || !child.tag) return true;

      if (child.tag === "style") {
        const content = (child.content || []).join("").trim();
        if (content === "") return false;
      }

      // Only remove inline scripts with no content - never remove external scripts with src
      if (child.tag === "script" && !child.attrs?.src) {
        const content = (child.content || []).join("").trim();
        if (content === "") return false;
      }

      if (child.tag === "meta") {
        const hasContent = child.attrs?.content?.trim();
        if (!hasContent && !child.attrs?.charset) return false;
      }

      return true;
    });

    return node;
  });
};

// ============================================================
// PostHTML Plugin Pipeline
// ============================================================

const posthtml_plugins: any[] = [
  posthtmlPostcss(postcss_plugins, { from: undefined }),
  posthtmlImgAlt(),
  posthtmlAltAlways(),
  mergeInlineLonghand(),
  posthtmlExternalLink(),
  deduplicateMeta(),
  deduplicateStructuredData(),
  deduplicateLinks(),
  posthtmlRemoveDuplicates("meta"),
  removeRedundantAttrs(),
  mergeStyleTags(),
  reorderHead(),
  removeEmptyElements(),
];

// ============================================================
// HTML minification (html-minifier-terser)
// ============================================================

const htmlMinOptions = {
  collapseWhitespace: true,
  conservativeCollapse: true,
  removeComments: true,
  removeEmptyAttributes: true,
  removeRedundantAttributes: true,
  removeScriptTypeAttributes: false, // Keep type attribute for rocket-loader compatibility
  removeStyleLinkTypeAttributes: true,
  useShortDoctype: true,
  minifyCSS: { level: 2 },
  minifyJS: true,
  continueOnParseError: true,
  keepClosingSlash: true,
  processConditionalComments: true,
  html5: true,
  includeAutoGeneratedTags: true,
  collapseBooleanAttributes: true,
};

// ============================================================
// Processing Functions
// ============================================================

async function processHtml(dir: string): Promise<{ count: number; errors: string[] }> {
  const htmlFiles = new Glob(`${dir}/**/*.html`);
  const files: string[] = [];
  for await (const f of htmlFiles.scan(".")) {
    files.push(f);
  }

  // 并发处理 HTML 文件
  return processBatch(
    files,
    CONCURRENCY,
    async (htmlFile) => {
      const content = await file(htmlFile).text();

      // PostHTML 处理
      // 开启 directives 解析来更好地处理原始的 <!DOCTYPE ...> 而不掉失
      const posthtmlResult = await posthtml(posthtml_plugins).process(content, {
        sync: false,
        directives: [
          { name: "?php", start: "<", end: ">" },
          { name: "!DOCTYPE", start: "<", end: ">" },
        ],
      });

      // html-minifier-terser 会进一步优化
      let minified = await htmlMinify(posthtmlResult.html, htmlMinOptions);

      // 处理 doctype 缺失的问题（安全补偿）
      // 由于历史代码或 SSG 引擎可能偶尔漏掉 doctype，或者 html-minifier 压缩时不规范丢失
      // 在此使用安全且稳健的方法确保 doctype 位于最顶端
      const trimmed = minified.trimStart();
      if (!trimmed.toLowerCase().startsWith("<!doctype")) {
        minified = "<!DOCTYPE html>\n" + trimmed;
      } else {
        // 如果已经有 doctype，确保上方没有多余空白
        minified = trimmed;
      }

      await Bun.write(htmlFile, minified);
    },
    (processed, total) => {
      if (processed % LOG_INTERVAL === 0 || processed === total) {
        console.log(`  HTML: ${processed}/${total}`);
      }
    }
  );
}

async function processCss(dir: string): Promise<{ count: number; errors: string[] }> {
  const cssFiles = new Glob(`${dir}/**/*.css`);
  const files: string[] = [];
  for await (const f of cssFiles.scan(".")) {
    files.push(f);
  }

  // 并发处理 CSS 文件
  return processBatch(
    files,
    CONCURRENCY,
    async (cssFile) => {
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
    },
    (processed, total) => {
      if (processed % LOG_INTERVAL === 0 || processed === total) {
        console.log(`  CSS:  ${processed}/${total}`);
      }
    }
  );
}

async function processJs(dir: string): Promise<{ count: number; errors: string[] }> {
  const jsFiles = new Glob(`${dir}/**/*.js`);
  const files: string[] = [];
  for await (const f of jsFiles.scan(".")) {
    if (!f.endsWith(".min.js")) {
      files.push(f);
    }
  }

  // 并发处理 JS 文件
  return processBatch(
    files,
    CONCURRENCY,
    async (jsFile) => {
      const content = await file(jsFile).text();
      const mapFile = jsFile + ".map";

      const result = await terserMinify(content, {
        compress: {
          passes: 2,
          ecma: 2020,
          pure_getters: true,
        },
        mangle: {
          keep_classnames: true,
          keep_fnames: true,
        },
        format: {
          ecma: 2020,
          comments: false,
        },
        sourceMap: {
          filename: path.basename(jsFile),
          url: path.basename(mapFile),
        },
      });

      if (result.code) {
        await Bun.write(jsFile, result.code);
      }
      if (result.map) {
        await Bun.write(
          mapFile,
          typeof result.map === "string" ? result.map : JSON.stringify(result.map)
        );
      }
    },
    (processed, total) => {
      if (processed % LOG_INTERVAL === 0 || processed === total) {
        console.log(`  JS:   ${processed}/${total}`);
      }
    }
  );
}

// ============================================================
// Main
// ============================================================

async function main() {
  const { dir } = parseArgs();

  console.log(`Build post-processing: ${dir}/`);
  const startTime = performance.now();

  const [htmlResult, cssResult, jsResult] = await Promise.all([
    processHtml(dir),
    processCss(dir),
    processJs(dir),
  ]);

  const endTime = performance.now();
  const elapsed = ((endTime - startTime) / 1000).toFixed(2);

  console.log("");
  console.log("--- Build Summary ---");
  console.log(`HTML: ${htmlResult.count} processed, ${htmlResult.errors.length} errors`);
  console.log(`CSS:  ${cssResult.count} processed, ${cssResult.errors.length} errors`);
  console.log(`JS:   ${jsResult.count} processed, ${jsResult.errors.length} errors`);
  console.log(`Time: ${elapsed}s`);

  const allErrors = [
    ...htmlResult.errors.map((e) => `  HTML: ${e}`),
    ...cssResult.errors.map((e) => `  CSS:  ${e}`),
    ...jsResult.errors.map((e) => `  JS:   ${e}`),
  ];

  if (allErrors.length > 0) {
    console.error(`\n${allErrors.length} files failed:`);
    for (const err of allErrors) {
      console.error(err);
    }
    process.exit(1);
  }

  console.log("Build complete!");
}

main().catch((err) => {
  console.error("Build failed:", err);
  process.exit(1);
});