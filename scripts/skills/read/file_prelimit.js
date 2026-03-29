const fs = require('fs');
const path = require('path');

// 解析 frontmatter 原文
function parseFrontmatter(content) {
    const lines = content.split('\n');

    // 检查是否以 --- 开头（yaml frontmatter）
    if (lines[0] && lines[0].trim() === '---') {
        // 查找第二个 ---
        for (let i = 1; i < lines.length; i++) {
            if (lines[i].trim() === '---') {
                // 返回 frontmatter 内容（包含两端的 ---）
                return lines.slice(0, i + 1).join('\n');
            }
        }
    }
    return null;
}

// 提取所有标题（带行号）
function extractHeadings(content) {
    const lines = content.split('\n');
    const headings = [];

    for (let i = 0; i < lines.length; i++) {
        const line = lines[i];
        // 匹配以 # 开头，后面跟着空格的行
        if (line.match(/^#+\s/)) {
            const lineNumber = i + 1;
            headings.push(`[${lineNumber}] ${line}`);
        }
    }

    return headings;
}

// 传入文件的相对路径，输出文件内容的前 1000 个字符
// 如果文件以 --- 开头（yaml frontmatter），跳过到第二个 --- 之后开始
function previewFile(filePath) {
    try {
        const content = fs.readFileSync(filePath, 'utf-8');
        const lines = content.split('\n');

        let startIndex = 0;

        // 检查是否以 --- 开头（yaml frontmatter）
        if (lines[0] && lines[0].trim() === '---') {
            // 查找第二个 ---
            for (let i = 1; i < lines.length; i++) {
                if (lines[i].trim() === '---') {
                    startIndex = i + 1;
                    break;
                }
            }
        }

        // 收集内容，直到达到 1000 个字符（不包含空行和空格）
        let charCount = 0;
        const result = [];

        for (let i = startIndex; i < lines.length; i++) {
            const line = lines[i];
            const lineNumber = i + 1;

            // 计算非空格字符数
            const nonSpaceChars = line.replace(/\s/g, '').length;

            // 如果已经达到 1000 字符限制，停止
            if (charCount + nonSpaceChars > 1000) {
                // 输出当前行（截断到限制）
                const remainingChars = 1000 - charCount;
                if (remainingChars > 0) {
                    let truncatedLine = '';
                    let count = 0;
                    for (const char of line) {
                        if (char !== ' ' && char !== '\t' && char !== '\n') {
                            count++;
                        }
                        truncatedLine += char;
                        if (count >= remainingChars) {
                            break;
                        }
                    }
                    result.push(`[${lineNumber}] ${truncatedLine}`);
                }
                break;
            }

            charCount += nonSpaceChars;
            }

            charCount += nonSpaceChars;
            result.push(`[${lineNumber}] ${line}`);
        }

        // 获取 frontmatter 和标题
        const frontmatter = parseFrontmatter(content);
        const headings = extractHeadings(content);

        return { preview: result, charCount, frontmatter, headings };
    } catch (err) {
        console.error(`错误：无法读取文件 ${filePath}`);
        console.error(err.message);
        process.exit(1);
    }
}

// 主函数
function main() {
    const args = process.argv.slice(2);

    if (args.length === 0) {
        console.error('错误：请提供文件路径');
        console.error('用法：node file_prelimit.js <file_path>');
        process.exit(1);
    }

    const filePath = args[0];

    // 检查文件是否存在
    if (!fs.existsSync(filePath)) {
        console.error(`错误：文件不存在 ${filePath}`);
        process.exit(1);
    }

    const { preview, charCount, frontmatter, headings } = previewFile(filePath);

    // 输出预览内容
    for (const line of preview) {
        console.log(line);
    }

    // 输出分隔线
    console.log('');
    console.log('---以下为辅助信息---');

    // 输出 frontmatter
    if (frontmatter) {
        console.log('');
        console.log('---frontmatter---');
        console.log(frontmatter);
        console.log('---end frontmatter---');
    }

    // 输出标题
    if (headings.length > 0) {
        console.log('');
        for (const heading of headings) {
            console.log(heading);
        }
    }

    // 输出 AI 提示
    console.log('');
    console.log(`提示：内容可能不完整，前 ${charCount} 个字符可能不能反应全文结构和主题，如果需要，请阅读全文或使用 file_headings.js 查看完整标题结构。`);
}

main();
