const fs = require('fs');
const path = require('path');

// 传入一个文件名（相对路径），输出它的所有标题（带行号）
function extractHeadings(filePath) {
    try {
        const content = fs.readFileSync(filePath, 'utf-8');
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
    
    const headings = extractHeadings(filePath);
    
    // 输出结果
    for (const heading of headings) {
        console.log(heading);
    }
}

main();
