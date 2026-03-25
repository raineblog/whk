const fs = require('fs');
const path = require('path');

// 遍历 docs 文件夹下的所有 .md 文件，输出每个文件的第一个 H1 标题
function findFirstH1(dir) {
    const results = [];
    
    function walkDir(currentPath) {
        const files = fs.readdirSync(currentPath);
        
        for (const file of files) {
            const filePath = path.join(currentPath, file);
            const stat = fs.statSync(filePath);
            
            if (stat.isDirectory()) {
                walkDir(filePath);
            } else if (file.endsWith('.md')) {
                try {
                    const content = fs.readFileSync(filePath, 'utf-8');
                    const lines = content.split('\n');
                    
                    // 查找第一个 H1（以 "# " 开头的行）
                    for (const line of lines) {
                        if (line.startsWith('# ')) {
                            const title = line.substring(2).trim();
                            // 使用相对路径，统一使用正斜杠
                            const relativePath = path.relative(process.cwd(), filePath).replace(/\\/g, '/');
                            results.push(`${relativePath} ${title}`);
                            break;
                        }
                    }
                } catch (err) {
                    // 忽略读取错误
                }
            }
        }
    }
    
    walkDir(dir);
    return results;
}

// 主函数
function main() {
    const docsDir = path.join(process.cwd(), 'docs');
    
    if (!fs.existsSync(docsDir)) {
        console.error('错误：docs 文件夹不存在');
        process.exit(1);
    }
    
    const results = findFirstH1(docsDir);
    
    // 按路径排序
    results.sort();
    
    // 输出结果
    for (const result of results) {
        console.log(result);
    }
}

main();
