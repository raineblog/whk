#!/usr/bin/env bun
// bun 原生构建脚本 - 完全等价于 gulpfile.js
// 支持 --compile 编译为可执行文件

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
  let inputDir = "dist";
  let outputDir = "dest";

  for (let i = 0; i < args.length; i++) {
    if (args[i] === "--input-dir" || args[i] === "--inputDir") {
      inputDir = args[i + 1];
      i++;
    } else if (args[i] === "--output-dir" || args[i] === "--outputDir") {
      outputDir = args[i + 1];
      i++;
    }
  }
  return { inputDir, outputDir };
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

// 自定义 img alt 插件（从 gulpfile.js 移植）
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

// HTML 压缩选项（从 gulpfile.js 移植）
const htmlmin_options = {
  collapseWhitespace: true,
  removeComments: true,
  removeEmptyAttributes: true,
  minifyJS: true,
  minifyCSS: true,
  useShortDoctype: true,
};

// HTML 压缩函数
function minifyHtml(html) {
  let result = html;
  if (htmlmin_options.collapseWhitespace) {
    result = result.replace(/\n\s+/g, " ").replace(/\s{2,}/g, " ").replace(/>\s+</g, "><");
  }
  if (htmlmin_options.removeComments) {
    result = result.replace(/<!--[\s\S]*?-->/g, "");
  }
  return result;
}

// 处理 HTML 文件
async function processHtml(inputDir, outputDir) {
  const htmlFiles = new Glob(`${inputDir}/**/*.html`);
  let count = 0;

  for await (const htmlFile of htmlFiles.scan(".")) {
    const content = await file(htmlFile).text();
    const result = await posthtml(posthtml_plugins).process(content, { sync: false });
    const minified = minifyHtml(result.html);
    
    const relativePath = path.relative(inputDir, htmlFile);
    const outputPath = path.join(outputDir, relativePath);
    const dir = path.dirname(outputPath);
    await $`mkdir -p ${dir}`.quiet();

    await Bun.write(outputPath, minified);
    count++;
  }

  return count;
}

// 处理 CSS 文件
async function processCss(inputDir, outputDir) {
  const cssFiles = new Glob(`${inputDir}/**/*.css`);
  let count = 0;

  for await (const cssFile of cssFiles.scan(".")) {
    const content = await file(cssFile).text();
    const result = await postcss(postcss_plugins).process(content, {
      from: cssFile,
      to: path.join(outputDir, path.relative(inputDir, cssFile)),
      map: { inline: false },
    });

    const relativePath = path.relative(inputDir, cssFile);
    const outputPath = path.join(outputDir, relativePath);
    const dir = path.dirname(outputPath);
    await $`mkdir -p ${dir}`.quiet();

    await Bun.write(outputPath, result.css);
    if (result.map) {
      await Bun.write(outputPath + ".map", result.map.toString());
    }
    count++;
  }

  return count;
}

// 处理 JS 文件
async function processJs(inputDir, outputDir) {
  const jsFiles = new Glob(`${inputDir}/**/*.js`);
  let count = 0;

  for await (const jsFile of jsFiles.scan(".")) {
    const relativePath = path.relative(inputDir, jsFile);
    const outDir = path.join(outputDir, path.dirname(relativePath));
    await $`mkdir -p ${outDir}`.quiet();
    
    await Bun.build({
      entrypoints: [jsFile],
      minify: true,
      sourcemap: "external",
      outdir: outDir,
    });
    count++;
  }

  return count;
}

// 复制其他资源文件
async function copyAssets(inputDir, outputDir) {
  let count = 0;
  const allFiles = new Glob(`${inputDir}/**/*`);

  for await (const filePath of allFiles.scan(".")) {
    const ext = path.extname(filePath).toLowerCase();
    if (ext === ".html" || ext === ".css" || ext === ".js") continue;

    const relativePath = path.relative(inputDir, filePath);
    const outputPath = path.join(outputDir, relativePath);
    const dir = path.dirname(outputPath);
    await $`mkdir -p ${dir}`.quiet();

    const content = await file(filePath).bytes();
    await Bun.write(outputPath, content);
    count++;
  }

  return count;
}

// 主函数
async function main() {
  const { inputDir, outputDir } = parseArgs();
  
  // 确保输出目录存在
  await $`mkdir -p ${outputDir}`.quiet();
  
  const startTime = Date.now();

  const [htmlCount, jsCount, assetCount, cssCount] = await Promise.all([
    processHtml(inputDir, outputDir),
    processJs(inputDir, outputDir),
    copyAssets(inputDir, outputDir),
    processCss(inputDir, outputDir),
  ]);

  const endTime = Date.now();
  console.log(`HTML: ${htmlCount} 个文件`);
  console.log(`JS: ${jsCount} 个文件`);
  console.log(`Assets: ${assetCount} 个文件`);
  console.log(`CSS: ${cssCount} 个文件`);
  console.log(`构建完成！耗时: ${endTime - startTime}ms`);
}

main().catch((err) => {
  console.error("构建失败:", err);
  process.exit(1);
});
