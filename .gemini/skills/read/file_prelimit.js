const fs = require('fs');
const path = require('path');

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
            result.push(`[${lineNumber}] ${line}`);
        }
        
        return result;
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
    
    const preview = previewFile(filePath);
    
    // 输出结果
    for (const line of preview) {
        console.log(line);
    }
}

main();
