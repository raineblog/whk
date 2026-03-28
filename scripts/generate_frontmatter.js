require('dotenv').config();
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const readline = require('readline');
const OpenAI = require('openai');
const minimist = require('minimist');
const Bottleneck = require('bottleneck');
const chalk = require('chalk');
const ora = require('ora');
const { performance } = require('perf_hooks');

/**
 * 自动生成 Frontmatter 脚本 (v6.0 精简版)
 * 核心升级: 
 *   1. 移除 Stream 模式，使用标准 API 响应以获得 100% 准确的 Token 统计 (usage 字段)。
 *   2. 精确化 Title (20-25), Description (100-200), Summary (50-100) 维度输出。
 *   3. 强制原子化混合维度 Tag。
 *   4. 支持 --clean-new 全量重置模式。
 */

const argv = minimist(process.argv.slice(2), {
    string: ['file', 'days'],
    boolean: ['new', 'clean-new', 'help'],
    alias: { n: 'new', c: 'clean-new', d: 'days', f: 'file', h: 'help' }
});

if (argv.help) {
    console.log(chalk.cyan(`
用法: node scripts/generate_frontmatter.js [选项]
选项:
  --new, -n           仅为缺失 Frontmatter 的文件生成数据
  --clean-new, -c     删除所有已有的 Frontmatter 并全部重新生成
  --days, -d <n>      从 Git 日志处理最近 n 天内修改的文件
  --file, -f <路径>    直接处理特定文件
`));
    process.exit(0);
}

const client = new OpenAI({
    apiKey: process.env.SILICONFLOW_API,
    baseURL: 'https://api.siliconflow.cn/v1',
});

const DOCS_DIR = path.resolve(__dirname, '../docs');
const TARGET_SUBDIRS = ['science'];
const EXCLUDE_DIRS = ['blog', 'home', 'cultural'];
const EXCLUDE_FILES = [path.join(DOCS_DIR, 'index.md')];

const limiter = new Bottleneck({
    minTime: 1000,
    maxConcurrent: 20
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
    process.stdout.write(chalk.bold.blue('\n🚀 Frontmatter Turbo [Expert Mode] v6.0\n'));
    const scanSpinner = ora('正在扫描任务...').start();

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
        if (argv['clean-new']) {
            console.log(chalk.yellow('⚠️ 注意: 已开启 --clean-new 模式，全量覆盖已有元数据。'));
        } else if (argv.new) {
            targetFiles = targetFiles.filter(f => !fs.readFileSync(f, 'utf-8').trim().startsWith('---'));
        }
    }

    scanSpinner.succeed(`任务扫描完毕。总计: ${chalk.bold.yellow(targetFiles.length)}\n`);
    if (targetFiles.length === 0) return;

    if (!process.env.CI) {
        console.log(chalk.dim('任务列表概览:'));
        const displayList = targetFiles.length > 10 ? [...targetFiles.slice(0, 5), '...', ...targetFiles.slice(-5)] : targetFiles;
        displayList.forEach((f, i) => f === '...' ? console.log('   ...') : console.log(chalk.gray(` [${i + 1}] ${getRelPath(f)}`)));
        console.log(chalk.cyan(`\n⚡ 以 20 并发启动处理...\n`));
    }

    const total = targetFiles.length;
    let completed = 0;
    const MAX_RETRIES = 3;
    const globalStart = performance.now();

    const tasks = targetFiles.map((filePath) => limiter.schedule(async () => {
        const relPath = getRelPath(filePath);
        const logPrefix = () => chalk.dim(`[${String(++completed).padStart(String(total).length, '0')}/${total}]`);

        for (let attempt = 0; attempt <= MAX_RETRIES; attempt++) {
            const taskStart = performance.now();
            
            try {
                const content = fs.readFileSync(filePath, 'utf-8');
                const title = extractTitle(content) || path.basename(filePath, '.md');
                const headings = extractHeadings(content);
                
                const fmMatch = content.match(/^---\s*[\s\S]*?---\s*/);
                const pureContent = fmMatch ? content.slice(fmMatch[0].length).trimStart() : content;

                const completion = await client.chat.completions.create({
                    model: 'Qwen/Qwen3.5-4B',
                    temperature: 0.7,
                    messages: [
                        { 
                            role: 'system', 
                            content: `## Role: 高级文档架构师与 SEO 策略师
## Context: 为专业知识库、学术博客及技术教程构建元数据索引。
## Task: 基于文章正文及目录，完成内容提炼、语义索引与 SEO 元数据产出。

## Logic Chain (CoT):
1. **内容分解**: 识别核心学科、关键术语及技术深度。
2. **场景匹配**: 分析文章对读者的实际价值点（学习指导、竞赛提分、应用工程）。
3. **分维度创作**: 根据锁定字数约束，由简入深进行标题、摘要及描述的级联生成。
4. **语义标记**: 提取“学科-内容-细节”层级的原子标签。

## Output Specifications (STRICT):
1. **title**: SEO 创意标题。20-25 汉字。必须包含 2-3 个核心关键词，增强搜索引擎点击率。
2. **description**: 专业知识图谱。100-200 汉字。描述文章涉及的物理/数学原理、教学意义及跨学科关联。
3. **summary**: 核心摘要短语。50-100 汉字。用于文章索引页或检索结果页。
4. **tags**: 原子化标签阵列。严禁空格或多个术语合并为一个标签。例如：[高中物理, 电磁感应, 楞次定律]。
5. **Format**: 仅输出标准 JSON 格式。

## Few-Shot Example:
[Input]: 《电磁感应法拉第定律》
[Output]: 
{
  "title": "深度解析法拉第电磁感应定律：从物理模型推导到工业感应应用",
  "description": "本文系统性地梳理了电磁场动力学的核心规律，深入探讨了法拉第定律的数学表达及其背后的能量守恒本质。文章通过对动生与感生电动势的精细化建模，结合楞次定律判定电流方向，并延伸探讨了涡流、磁泄露等复杂工程场景下的物理表现，旨在为学习者构建完整的电磁物理认知体系。",
  "summary": "全面覆盖电磁感应核心规律。涵盖通量变化率计算、物理机制推导及能量转化平衡分析。适合作为学科进阶参考。",
  "tags": ["高中物理", "电磁学", "法拉第定律", "电磁感应", "楞次定律", "磁通量", "电动势", "能量守恒", "涡流"]
}` 
                        },
                        { role: 'user', content: `[ARTICLE CONTENT]\n${pureContent.substring(0, 15000)}\n\n[HEADINGS]\n${headings}` }
                    ],
                    stream: false,
                });

                const fullRes = completion.choices[0].message.content;
                const meta = JSON.parse(fullRes.replace(/^```json\s*|```$/g, '').trim());
                const usage = completion.usage;

                const header = [
                    '---',
                    `title: "${(meta.title || title).replace(/"/g, '\\"')}"`,
                    `description: "${(meta.description || '').replace(/"/g, '\\"')}"`,
                    `summary: "${(meta.summary || '').replace(/"/g, '\\"')}"`,
                    `tags:`,
                    ...(meta.tags || []).map(t => `  - "${t.replace(/"/g, '\\"')}"`),
                    '---',
                    '', ''
                ].join('\n');

                fs.writeFileSync(filePath, header + pureContent);

                const taskEnd = performance.now();
                const dur = (taskEnd - taskStart) / 1000;
                const inTok = usage.prompt_tokens;
                const thinkTok = usage.completion_tokens_details?.reasoning_tokens || 0;
                const outTok = usage.completion_tokens - thinkTok; 
                const totalTok = usage.total_tokens;
                const tps = (totalTok / dur).toFixed(1);

                console.log(`${chalk.green('✔')} ${logPrefix()} ${chalk.white(relPath)}`);
                console.log(chalk.dim(`    Usage: ${totalTok} Tok (In:${inTok} Out:${outTok} Think:${thinkTok}) | Time: ${dur.toFixed(1)}s | ${tps} Tok/s`));
                break;
            } catch (e) {
                if (attempt === MAX_RETRIES) {
                    console.log(`${chalk.red('✘')} ${logPrefix()} ${chalk.red(relPath)} - 彻底失败: ${e.message}`);
                } else {
                    await new Promise(r => setTimeout(r, 2000 * (attempt + 1)));
                }
            }
        }
    }));

    await Promise.allSettled(tasks);
    const globalEnd = performance.now();
    const totalTime = ((globalEnd - globalStart) / 1000).toFixed(1);
    process.stdout.write(chalk.bold.green(`\n✨ 任务全部结束！总耗时: ${totalTime}s\n`));
}

main().catch(err => {
    console.error(chalk.red('\nFatal:'), err);
    process.exit(1);
});
