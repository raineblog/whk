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

// 传入一个文件名（相对路径），输出它的 frontmatter 和所有标题（带行号）
function extractHeadings(filePath) {
    try {
        const content = fs.readFileSync(filePath, 'utf-8');
        const lines = content.split('\n');

        // 获取 frontmatter
        const frontmatter = parseFrontmatter(content);

        // 获取标题
        const headings = [];
        for (let i = 0; i < lines.length; i++) {
            const line = lines[i];
            // 匹配以 # 开头，后面跟着空格的行
            if (line.match(/^#+\s/)) {
                const lineNumber = i + 1;
                headings.push(`[${lineNumber}] ${line}`);
            }
        }

        return { frontmatter, headings };
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
        console.error('用法：node file_headings.js <file_path>');
        process.exit(1);
    }

    const filePath = args[0];

    // 检查文件是否存在
    if (!fs.existsSync(filePath)) {
        console.error(`错误：文件不存在 ${filePath}`);
        process.exit(1);
    }

    const { frontmatter, headings } = extractHeadings(filePath);

    // 输出 frontmatter
    if (frontmatter) {
        console.log('---frontmatter---');
        console.log(frontmatter);
        console.log('---end frontmatter---');
    }

    // 输出标题
    for (const heading of headings) {
        console.log(heading);
    }
}

main();
