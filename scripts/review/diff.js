const { spawnSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const TARGET_PATTERN = /[,'"\(\)]/;

// 检测错误字符的函数
function detectErrorCharacters(text) {
    const errors = [];
    
    for (let i = 0; i < text.length; i++) {
        const char = text[i];
        const code = char.charCodeAt(0);
        
        // 1. 检测 Unicode 替换字符（方块问号）
        if (code === 0xFFFD) {
            errors.push({
                position: i,
                char: char,
                code: code,
                type: 'replacement_character',
                description: 'Unicode 替换字符（通常显示为方块或问号）'
            });
        }
        
        // 2. 检测控制字符（除了常见的换行、制表符、回车符）
        else if (code >= 0x0000 && code <= 0x001F) {
            // 允许的控制字符：制表符(0x0009)、换行符(0x000A)、回车符(0x000D)
            if (code !== 0x0009 && code !== 0x000A && code !== 0x000D) {
                errors.push({
                    position: i,
                    char: char,
                    code: code,
                    type: 'control_character',
                    description: `控制字符 (U+${code.toString(16).toUpperCase().padStart(4, '0')})`
                });
            }
        }
        
        // 3. 检测 C1 控制字符 (U+0080-U+009F)
        else if (code >= 0x0080 && code <= 0x009F) {
            errors.push({
                position: i,
                char: char,
                code: code,
                type: 'c1_control_character',
                description: `C1 控制字符 (U+${code.toString(16).toUpperCase().padStart(4, '0')})`
            });
        }
        
        // 4. 检测零宽字符
        else if (code === 0x200B || // 零宽空格
                 code === 0x200C || // 零宽非连接符
                 code === 0x200D || // 零宽连接符
                 code === 0xFEFF) { // 零宽无断空格（字节顺序标记）
            errors.push({
                position: i,
                char: char,
                code: code,
                type: 'zero_width_character',
                description: `零宽字符 (U+${code.toString(16).toUpperCase().padStart(4, '0')})`
            });
        }
        
        // 5. 检测其他可能的乱码字符
        // 这里我们检测一些常见的乱码模式
        else if (code >= 0x007F && code <= 0x00FF) {
            // 扩展 ASCII 范围，但排除常见的标点符号和字母
            // 允许：À-ÿ（拉丁字母补充）
            if (!((code >= 0x00C0 && code <= 0x00FF) || // 拉丁字母补充
                  (code >= 0x00A0 && code <= 0x00BF))) { // 拉丁字母补充-1
                errors.push({
                    position: i,
                    char: char,
                    code: code,
                    type: 'extended_ascii',
                    description: `扩展 ASCII 字符 (U+${code.toString(16).toUpperCase().padStart(4, '0')})，可能是乱码`
                });
            }
        }
    }
    
    return errors;
}

// 检测字符串是否包含错误字符
function hasErrorCharacters(text) {
    return detectErrorCharacters(text).length > 0;
}

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
                const content = line.slice(1);
                const hasTarget = TARGET_PATTERN.test(content);
                const errorChars = detectErrorCharacters(content);
                currentHunk.push({
                    raw: line,
                    isAdded: true,
                    lineNum: currentLineNum,
                    hasTarget: hasTarget,
                    errorChars: errorChars,
                    hasErrors: errorChars.length > 0
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
    let errorCount = 0;
    
    for (const { file, hunk } of hunks) {
        for (let i = 0; i < hunk.length; i++) {
            const item = hunk[i];
            
            // 输出包含目标字符的行
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
            
            // 输出包含错误字符的行
            if (item.isAdded && item.hasErrors) {
                errorCount++;
                const prevLine = i > 0 ? hunk[i - 1].raw : "<位于 Diff 块顶部，无上一行上下文>";
                const nextLine = i < hunk.length - 1 ? hunk[i + 1].raw : "<位于 Diff 块底部，无下一行上下文>";
                const currLine = item.raw;
                const lineNum = item.lineNum;

                console.log(`⚠️ 错误字符 - 文件: ${file} (第 ${lineNum} 行)`);
                console.log(`  上一行: ${prevLine}`);
                console.log(`  当前行: ${currLine}`);
                console.log(`  下一行: ${nextLine}`);
                
                // 显示详细的错误字符信息
                console.log(`  错误字符详情:`);
                for (const error of item.errorChars) {
                    console.log(`    - 位置 ${error.position}: ${error.description}`);
                    console.log(`      字符: '${error.char}' (U+${error.code.toString(16).toUpperCase().padStart(4, '0')})`);
                }
                console.log("-".repeat(60));
            }
        }
    }

    console.log("\n" + "=".repeat(60));
    console.log("检测结果汇总:");
    console.log("=".repeat(60));
    
    if (matchCount === 0) {
        console.log("✓ 没有在 .md 文件中找到包含 , ' \" ( ) 的新增或修改行。");
    } else {
        console.log(`⚠️ 共找到 ${matchCount} 处包含目标字符的行。`);
    }
    
    if (errorCount === 0) {
        console.log("✓ 没有在 .md 文件中找到包含错误字符的新增行。");
    } else {
        console.log(`⚠️ 共找到 ${errorCount} 处包含错误字符的行。`);
        console.log("  错误字符类型包括:");
        console.log("  - Unicode 替换字符（通常显示为方块或问号）");
        console.log("  - 控制字符（不可见字符）");
        console.log("  - C1 控制字符");
        console.log("  - 零宽字符");
        console.log("  - 扩展 ASCII 字符（可能是乱码）");
    }
    
    console.log("=".repeat(60));
}

main();
