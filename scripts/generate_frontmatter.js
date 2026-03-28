require('dotenv').config();
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const OpenAI = require('openai');
const minimist = require('minimist');
const Bottleneck = require('bottleneck');
const chalk = require('chalk');
const ora = require('ora');
const { performance } = require('perf_hooks');

/**
 * 自动生成 Frontmatter 脚本 (CI/CD 运维适配版)
 * 核心升级: 
 *   1. 移除多行进度条，改为流式日志输出 (Tty-Independent)
 *   2. 增加每秒吞吐量 (TPS) 及 Token 维度统计
 *   3. 固化 262144 Token 硬限制与 Temperature 0.7
 *   4. 原子化高精度 Tag 提示词
 */

const argv = minimist(process.argv.slice(2), {
    string: ['file', 'days'],
    boolean: ['new', 'help'],
    alias: { n: 'new', d: 'days', f: 'file', h: 'help' }
});

if (argv.help) {
    console.log(chalk.cyan(`
用法: node scripts/generate_frontmatter.js [选项]
选项:
  --new, -n        仅为缺失 Frontmatter 的文件生成数据
  --days, -d <n>   处理 Git 最近 n 天内修改的文件 (扫描全量目录)
  --file, -f <路径> 直接处理特定文件 (跳过筛选)
`));
    process.exit(0);
}

const client = new OpenAI({
    apiKey: process.env.SILICONFLOW_API,
    baseURL: 'https://api.siliconflow.cn/v1',
});

const DOCS_DIR = path.resolve(__dirname, '../docs');
const TARGET_SUBDIRS = ['science'];
const EXCLUDE_DIRS = ['blog', 'home', 'cultural']; // 排除 cultural
const EXCLUDE_FILES = [path.join(DOCS_DIR, 'index.md')];

const limiter = new Bottleneck({
    minTime: 1000,
    maxConcurrent: 32
});

function extractTitle(content) {
    const lines = content.split('\n');
    for (const line of lines) {
        const match = line.trim().match(/^#\s+(.+)$/);
        if (match) return match[1].trim();
    }
    return null;
}

function extractHeadings(content) {
    const lines = content.split('\n');
    const headings = [];
    for (let i = 0; i < Math.min(lines.length, 1000); i++) {
        const line = lines[i].trim();
        if (line.match(/^#+\s/)) headings.push(`[L${i + 1}] ${line}`);
    }
    return headings.join('\n');
}

function hasFrontmatter(content) {
    return content.trim().startsWith('---');
}

function getRelPath(absPath) {
    return path.relative(DOCS_DIR, absPath);
}

function scanAllMarkdown(dir, files = []) {
    if (!fs.existsSync(dir)) return files;
    const items = fs.readdirSync(dir);
    for (const item of items) {
        const fullPath = path.join(dir, item);
        const stat = fs.statSync(fullPath);
        if (stat.isDirectory()) {
            if (EXCLUDE_DIRS.includes(item)) continue;
            scanAllMarkdown(fullPath, files);
        } else if (item.endsWith('.md')) {
            if (!EXCLUDE_FILES.includes(fullPath)) files.push(fullPath);
        }
    }
    return files;
}

async function main() {
    process.stdout.write(chalk.bold.blue('\n🚀 Frontmatter Turbo [CI/CD Edition] v4.0\n'));
    const scanSpinner = ora('正在扫描文件任务...').start();

    let targetFiles = [];

    if (argv.file) {
        const filePath = path.resolve(process.cwd(), argv.file);
        if (fs.existsSync(filePath)) targetFiles.push(filePath);
        else { scanSpinner.fail(chalk.red(`文件不存在: ${argv.file}`)); process.exit(1); }
    } else if (argv.days) {
        try {
            const gitOutput = execSync(`git log --since="${argv.days} days ago" --name-only --pretty=format: -- "*.md"`, { encoding: 'utf-8' });
            const rawFiles = [...new Set(gitOutput.split('\n').map(f => f.trim()).filter(f => f))];
            targetFiles = rawFiles.map(f => path.resolve(process.cwd(), f)).filter(f => {
                const rel = getRelPath(f);
                return f.startsWith(DOCS_DIR) && TARGET_SUBDIRS.some(s => rel.startsWith(s)) && !EXCLUDE_FILES.includes(f);
            });
        } catch (e) { scanSpinner.fail(chalk.red(`Git 失败: ${e.message}`)); process.exit(1); }
    } else {
        for (const sub of TARGET_SUBDIRS) {
            scanAllMarkdown(path.join(DOCS_DIR, sub), targetFiles);
        }
        if (argv.new) targetFiles = targetFiles.filter(f => !hasFrontmatter(fs.readFileSync(f, 'utf-8')));
    }

    scanSpinner.succeed(`扫描完成。任务总计: ${chalk.bold.yellow(targetFiles.length)}\n`);
    if (targetFiles.length === 0) return;

    console.log(chalk.dim('任务概览 (显示前后共 10 项):'));
    const displayList = targetFiles.length > 10 ? [...targetFiles.slice(0, 5), '...', ...targetFiles.slice(-5)] : targetFiles;
    displayList.forEach((f, i) => f === '...' ? console.log('   ...') : console.log(chalk.gray(` [${i + 1}] ${getRelPath(f)}`)));
    console.log(chalk.cyan(`\n⚡ 正在以 32 并发直接启动处理...\n`));

    const total = targetFiles.length;
    let completed = 0;
    const MAX_RETRIES = 3;
    const globalStart = performance.now();

    const tasks = targetFiles.map((filePath, index) => limiter.schedule(async () => {
        const relPath = getRelPath(filePath);
        const logPrefix = () => chalk.dim(`[${String(++completed).padStart(String(total).length, '0')}/${total}]`);

        for (let attempt = 0; attempt <= MAX_RETRIES; attempt++) {
            const taskStart = performance.now();
            let outTok = 0, thinkTok = 0, inTok = 0;
            
            try {
                const content = fs.readFileSync(filePath, 'utf-8');
                const title = extractTitle(content) || path.basename(filePath, '.md');
                const headings = extractHeadings(content);
                inTok = Math.floor(content.length * 0.7);

                const stream = await client.chat.completions.create({
                    model: 'Qwen/Qwen3.5-4B',
                    temperature: 0.7,
                    messages: [
                        { 
                            role: 'system', 
                            content: `你是一个专业的内容分析专家和 SEO 优化师。请为文章生成 'title'、'description' 和 'tags'。
[Requirements]
1. **title**: SEO 友好，25 汉字以内，严禁直接使用原标题。
2. **description**: 50-100 字，中英文空格规范。
3. **tags**: 数量不限(建议 10-25 个)，**必须原子化** (禁止空格合并标签)，学科+内容+细节三维度混合。
4. **Output**: 仅输出纯 JSON。` 
                        },
                        { role: 'user', content: `[ARTICLE]\n${content.substring(0, 15000)}\n\n[INDEX]\n${headings}` }
                    ],
                    stream: true,
                });

                let fullRes = '';
                for await (const chunk of stream) {
                    const delta = chunk.choices[0]?.delta || {};
                    const text = delta.content || '';
                    const thinking = delta.reasoning_content || '';
                    if (thinking) thinkTok += thinking.length / 1.5;
                    if (text) { fullRes += text; outTok += text.length / 1.5; }
                }

                const meta = JSON.parse(fullRes.replace(/^```json\s*|```$/g, '').trim());
                const header = [
                    '---',
                    `title: "${(meta.title || title).replace(/"/g, '\\"')}"`,
                    `description: "${meta.description.replace(/"/g, '\\"')}"`,
                    `tags:`,
                    ...(meta.tags || []).map(t => `  - "${t.replace(/"/g, '\\"')}"`),
                    '---',
                    '', ''
                ].join('\n');

                const fmMatch = content.match(/^---\s*[\s\S]*?---\s*/);
                const body = fmMatch ? content.slice(fmMatch[0].length) : content;
                fs.writeFileSync(filePath, header + body.trimStart());

                const taskEnd = performance.now();
                const dur = (taskEnd - taskStart) / 1000;
                const totalTok = Math.floor(inTok + outTok + thinkTok);
                const tps = (totalTok / dur).toFixed(1);

                console.log(`${chalk.green('✔')} ${logPrefix()} ${chalk.white(relPath)}`);
                console.log(chalk.dim(`    Tokens: ${totalTok} (In: ${inTok}, Out: ${Math.floor(outTok)}, Think: ${Math.floor(thinkTok)}) | Time: ${dur.toFixed(1)}s | ${tps} Tok/s`));
                break;
            } catch (e) {
                if (attempt === MAX_RETRIES) {
                    console.log(`${chalk.red('✘')} ${logPrefix()} ${chalk.red(relPath)} - 彻底失败: ${e.message}`);
                } else {
                    const wait = 2000 * (attempt + 1);
                    await new Promise(r => setTimeout(r, wait));
                }
            }
        }
    }));

    await Promise.allSettled(tasks);
    const globalEnd = performance.now();
    const totalTime = ((globalEnd - globalStart) / 1000).toFixed(1);
    console.log(chalk.bold.green(`\n✨ 所有任务执行完毕! 总耗时: ${totalTime}s\n`));
}

main().catch(err => {
    console.error(chalk.red('\nFatal Error:'), err);
    process.exit(1);
});
