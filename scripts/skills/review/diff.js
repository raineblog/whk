const { spawnSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const TARGET_PATTERN = /[,'"\(\)]/;

function main() {
    const rootDir = spawnSync('git', ['rev-parse', '--show-toplevel'], { encoding: 'utf8' }).stdout.trim();
    if (!rootDir) {
        console.error('无法找到 Git 根目录。');
        return;
    }

    console.log('正在执行 git diff (仅筛选 .md 文件)...');

    const diffProcess = spawnSync('git', ['diff', '--', '*.md'], { 
        encoding: 'utf8',
        cwd: rootDir
    });

    if (diffProcess.error) {
        console.error(`执行 git diff 失败: ${diffProcess.error.message}`);
        return;
    }

    const diffOutput = diffProcess.stdout;

    if (!diffOutput || diffOutput.trim().length === 0) {
        console.log('当前没有针对 .md 文件的未提交更改。');
        return;
    }

    console.log('正在解析 diff 数据...\n');

    const lines = diffOutput.split(/\r?\n/);
    const hunks = [];
    let currentFile = null;
    let currentHunk = null;
    let currentLineNum = 0;

    for (const line of lines) {
        if (line.startsWith('diff --git ')) {
            if (currentFile && currentHunk) {
                hunks.push({ file: currentFile, hunk: currentHunk });
            }
            currentFile = null;
            currentHunk = null;
            continue;
        }

        if (line.startsWith('+++ ')) {
            let filepath = line.slice(4).trim();
            if (filepath.startsWith('b/')) {
                filepath = filepath.slice(2);
            }
            if (!filepath.toLowerCase().endsWith('.md')) {
                currentFile = null;
                continue;
            }
            currentFile = filepath;
            continue;
        }

        if (line.startsWith('@@ ')) {
            if (currentFile && currentHunk) {
                hunks.push({ file: currentFile, hunk: currentHunk });
            }
            currentHunk = [];
            const match = line.match(/@@ -\d+(?:,\d+)? \+(\d+)(?:,\d+)? @@/);
            if (match) {
                currentLineNum = parseInt(match[1], 10);
            }
            continue;
        }

        if (currentFile !== null && currentHunk !== null) {
            if (line.startsWith('+') && !line.startsWith('+++')) {
                const hasTarget = TARGET_PATTERN.test(line.slice(1));
                currentHunk.push({
                    raw: line,
                    isAdded: true,
                    lineNum: currentLineNum,
                    hasTarget: hasTarget
                });
                currentLineNum++;
            } else if (line.startsWith('-') && !line.startsWith('---')) {
                currentHunk.push({
                    raw: line,
                    isAdded: false,
                    lineNum: null,
                    hasTarget: false
                });
            } else if (line.startsWith(' ')) {
                currentHunk.push({
                    raw: line,
                    isAdded: false,
                    lineNum: currentLineNum,
                    hasTarget: false
                });
                currentLineNum++;
            } else if (line.startsWith('\\')) {
                currentHunk.push({
                    raw: line,
                    isAdded: false,
                    lineNum: null,
                    hasTarget: false
                });
            } else {
                if (currentHunk) {
                    hunks.push({ file: currentFile, hunk: currentHunk });
                }
                currentHunk = null;
            }
        }
    }

    if (currentFile && currentHunk) {
        hunks.push({ file: currentFile, hunk: currentHunk });
    }

    let matchCount = 0;
    for (const { file, hunk } of hunks) {
        for (let i = 0; i < hunk.length; i++) {
            const item = hunk[i];
            if (item.isAdded && item.hasTarget) {
                matchCount++;
                const prevLine = i > 0 ? hunk[i - 1].raw : "<位于 Diff 块顶部，无上一行上下文>";
                const nextLine = i < hunk.length - 1 ? hunk[i + 1].raw : "<位于 Diff 块底部，无下一行上下文>";
                const currLine = item.raw;
                const lineNum = item.lineNum;

                console.log(`文件: ${file} (第 ${lineNum} 行)`);
                console.log(`  上一行: ${prevLine}`);
                console.log(`  当前行: ${currLine}`);
                console.log(`  下一行: ${nextLine}`);
                console.log("-".repeat(60));
            }
        }
    }

    if (matchCount === 0) {
        console.log("没有在 .md 文件中找到包含 , ' \" ( ) 的新增或修改行。");
    } else {
        console.log(`共找到 ${matchCount} 处匹配。`);
    }
}

main();
