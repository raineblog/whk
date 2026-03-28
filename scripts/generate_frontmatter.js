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
    apiKey: process.env.NVIDIA_NIM_API_KEY,
    baseURL: 'https://integrate.api.nvidia.com/v1',
});

const DOCS_DIR = path.resolve(__dirname, '../docs');
const TARGET_SUBDIRS = ['science'];
const EXCLUDE_DIRS = ['blog', 'home', 'cultural'];
const EXCLUDE_FILES = [path.join(DOCS_DIR, 'index.md')];
const CONCURRENT = 5;
const RPM_LIMIT = 30; // 每分钟请求数限制
const MIN_TIME_MS = Math.ceil(60000 / RPM_LIMIT); // 2000ms per request

const limiter = new Bottleneck({
    minTime: MIN_TIME_MS,
    maxConcurrent: CONCURRENT
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
        console.log(chalk.cyan(`\n⚡ 以 ${CONCURRENT} 并发启动处理...\n`));
    }

    const total = targetFiles.length;
    let completed = 0;
    const MAX_RETRIES = 10;
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

                
                console.log(`${chalk.green('✔')} ${logPrefix()} ${chalk.white(relPath)} 任务开始 ${filePath}`);
                
                const fmMatch = content.match(/^---\s*[\s\S]*?---\s*/);
                const pureContent = fmMatch ? content.slice(fmMatch[0].length).trimStart() : content;

                const completion = await client.chat.completions.create({
                    model: 'nvidia/nemotron-3-nano-30b-a3b',
                    messages: [
                        {
                            role: 'system', 
                            content: `## Role: 高级文档架构师与 SEO 策略专家 (Expert Mode v7.0)
## Context: 为专业科学/技术知识库构建元数据。当前处理的是"science"学科下的核心笔记。

## Task: 深度解析文章正文，产出具有强吸引力且 SEO 优化的 Frontmatter元数据。

## Output Specifications (STRICT CONSTRAINT):
1. **title**: SEO 创意标题。22±3 汉字。风格应为："[核心词]详解：[机制/原理]与[应用场景]"。
2. **description**: 内容价值描述。100-200 汉字。必须揭示文章的技术路线或物理/化学机理。
3. **summary**: 极简摘要。50-100 汉字。用于卡片展示。
4. **tags**: 极致密集标签 (15-25 个)。必须覆盖五个维度：
    - [维度 1: 学科] 如：高中物理、生物化学
    - [维度 2: 核心母词] 如：细胞工程、直流电路
    - [维度 3: 细节子词] 如：脱分化、楞次定律、安培力
    - [维度 4: 应用场景] 如：实验设计、工业制备、高考复习
    - [维度 5: 目标群体] 如：理综学习、竞赛备考

## Instruction for Thinking Model:
- 在输出 JSON 之前，请深入思考与字符计数。
- 严禁出现空标签或空格连接的标签。
- 严禁输出任何 JSON 以外的解释性文字。

## High Quality Example:
{
  "title": "深度解析酶抑制剂：生物化学酶动力学与特殊碱基机制详解",
  "title_count": 25,
  "description": "本文深入探讨细胞代谢中的酶抑制剂原理，涵盖可逆与不可逆抑制剂的分类、动力学参数变化及作用机制。同时解析特殊碱基与碱基配对计算，适用于生物化学学习与竞赛备考。",
  "description_count": 124,
  "summary": "全面覆盖酶抑制剂分类与动力学。详细对比竞争性、非竞争性抑制区别，并延伸至特殊碱基配对法则。",
  "summary_count": 52,
  "tags": ["生物化学", "酶抑制剂", "酶动力学", "竞争性抑制", "非竞争性抑制", "反竞争性抑制", "不可逆抑制剂", "活性中心", "米氏常数", "最大反应速率", "构象改变", "专一性", "5-BrdU", "次黄嘌呤", "Z 碱基", "分子生物学", "细胞代谢", "高中生物", "大学生物"]
}` 
                        },
                        { role: 'user', content: `[ARTICLE CONTENT]
${pureContent}

[HEADINGS]
${headings}

---
[TASK REPEAT & STICKY INSTRUCTIONS]:
基于上方正文生成 JSON 元数据。你现在的角色是"顶级 SEO 策略师"。

1. 标题必须有 20-25 个中文字符，不得过短！
2. 标签要给够 (至少 15 个)，覆盖学科、母词、子词、应用。
3. 在 JSON 中额外增加 'title_count' 和 'description_count' 字段，用于你自己确认字数是否达标。
4. 请不要让输出显得像个小模型，要体现出"深度解析"的专业感。

仅输出标准 JSON 格式。开始：` }
                    ],
                    temperature: 0.6,
                    top_p: 1,
                    // max_tokens: 262144,
                    reasoning_budget: -1,
                    chat_template_kwargs: {"enable_thinking":true},
                    stream: false
                });

                const fullRes = completion.choices[0]?.message?.content || '';
                const meta = JSON.parse(fullRes.replace(/^```json\s*|```$/g, '').trim());

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

                console.log(`${chalk.green('✔')} ${completed} ${chalk.white(relPath)} | Time: ${dur.toFixed(1)}s`);
                break;
            } catch (e) {
                if (attempt === MAX_RETRIES) {
                    console.log(`${chalk.red('✘')} ${completed} ${chalk.red(relPath)} - 彻底失败: ${e.message}`);
                } else {
                    console.log(`${chalk.red('？')} ${completed} ${chalk.red(relPath)} - 失败 ${e.message} - 重试第 ${attempt} 次`);
                    await new Promise(r => setTimeout(r, 10000));
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
