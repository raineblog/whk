const fs = require('fs').promises;
const fsSync = require('fs');
const path = require('path');
const crypto = require('crypto');

/**
 * 计算文件内容的 SHA-256，返回后 7 位十六进制字符串。
 * 与 RainPPR/action-image-resize 的 getFileSha7 保持一致。
 */
async function getFileSha7(filePath) {
  const buf = await fs.readFile(filePath);
  const hash = crypto.createHash('sha256').update(buf).digest('hex');
  return hash.slice(-7);
}

/**
 * 仅匹配需要重命名的文件：
 *   image.avif            -> image-{sha7}.avif
 *   image-N.avif          -> image-N-{sha7}.avif   (N 为数字)
 * 排除已经带 hash 后缀的文件以及 image.spec.avif 这类非标准命名。
 */
function isTargetName(name) {
  return /^image(?:-\d+)?\.avif$/.test(name);
}

function buildNewName(oldName, sha7) {
  const base = oldName.slice(0, oldName.length - '.avif'.length);
  return `${base}-${sha7}.avif`;
}

const logger = {
  _ts: () => {
    const d = new Date();
    const pad = (n) => n.toString().padStart(2, '0');
    return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())} ${pad(d.getHours())}:${pad(d.getMinutes())}:${pad(d.getSeconds())}`;
  },
  info: (m) => console.log(`[${logger._ts()}] [INFO] ${m}`),
  item: (m) => console.log(`[${logger._ts()}] [ITEM] ${m}`),
  done: (m) => console.log(`[${logger._ts()}] [DONE] ${m || 'Completed'}`),
  warn: (m) => console.log(`[${logger._ts()}] [WARN] ${m}`),
  error: (m, e) => console.error(`[${logger._ts()}] [ERR]  ${m}${e ? `: ${e.message}` : ''}`),
};

async function walk(dir, acc) {
  const entries = await fs.readdir(dir, { withFileTypes: true });
  for (const e of entries) {
    const full = path.join(dir, e.name);
    if (e.isDirectory()) {
      if (e.name === 'node_modules' || e.name === '.git') continue;
      await walk(full, acc);
    } else if (e.isFile()) {
      acc.push(full);
    }
  }
}

async function run() {
  const root = path.resolve(process.cwd(), process.argv[2] || 'docs');
  logger.info(`Root: ${root}`);

  const allFiles = [];
  await walk(root, allFiles);

  const renameMap = new Map(); // 旧绝对路径 -> 新绝对路径

  // 1. 重命名 image.avif / image-N.avif
  const targets = allFiles.filter((f) => isTargetName(path.basename(f)));
  logger.info(`Found ${targets.length} target image(s) to rename`);

  for (const file of targets) {
    const dir = path.dirname(file);
    const sha7 = await getFileSha7(file);
    const newName = buildNewName(path.basename(file), sha7);
    const newPath = path.join(dir, newName);
    if (fsSync.existsSync(newPath)) {
      logger.warn(`Target ${newName} already exists, skipping ${file}`);
      continue;
    }
    await fs.rename(file, newPath);
    renameMap.set(path.resolve(file), path.resolve(newPath));
    logger.done(`${path.relative(root, file)} -> ${newName} [sha:${sha7}]`);
  }

  if (renameMap.size === 0) {
    logger.info('Nothing renamed. Done.');
    return;
  }

  // 2. 更新 Markdown 中的引用
  const mdFiles = allFiles.filter((f) => f.endsWith('.md'));
  const markdownImgRegex = /(!\[.*?\]\((?!https?:\/\/)(.*?\.avif)\))|(<img\b[^>]*?\bsrc=["'](?!https?:\/\/)(.*?\.avif)["'][^>]*?>)/gi;

  let updatedCount = 0;
  for (const mdFile of mdFiles) {
    try {
      const content = await fs.readFile(mdFile, 'utf8');
      const mdDir = path.dirname(mdFile);
      let changed = false;

      const updated = content.replace(markdownImgRegex, (match, mdFull, mdPath, htmlFull, htmlPath) => {
        const rawPath = mdPath || htmlPath;
        if (!rawPath) return match;
        const fullOriginal = path.resolve(mdDir, rawPath);
        if (renameMap.has(fullOriginal)) {
          const newAbs = renameMap.get(fullOriginal);
          const newRel = path.relative(mdDir, newAbs).replace(/\\/g, '/');
          changed = true;
          return (mdPath ? mdFull : htmlFull).replace(rawPath, newRel);
        }
        return match;
      });

      if (changed) {
        await fs.writeFile(mdFile, updated, 'utf8');
        updatedCount++;
        logger.done(`Updated links in ${path.relative(root, mdFile)}`);
      }
    } catch (err) {
      logger.error(`Error updating ${mdFile}`, err);
    }
  }

  logger.info(`Renamed ${renameMap.size} image(s), updated ${updatedCount} markdown file(s).`);
}

run().catch((err) => {
  console.error('\n[FATAL]', err);
  process.exit(1);
});
