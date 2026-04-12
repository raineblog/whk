const fs = require('fs');
const path = require('path');

// 解析 frontmatter 中的 title 字段
function parseFrontmatterTitle(content) {
    const lines = content.split('\n');

    // 检查是否以 --- 开头（yaml frontmatter）
    if (lines[0] && lines[0].trim() === '---') {
        // 查找第二个 ---
        for (let i = 1; i < lines.length; i++) {
            if (lines[i].trim() === '---') {
                // 在 frontmatter 中查找 title 字段
                for (let j = 1; j < i; j++) {
                    const match = lines[j].match(/^title:\s*(.+)$/);
                    if (match) {
                        let title = match[1].trim();
                        // 去掉引号
                        if ((title.startsWith('"') && title.endsWith('"')) ||
                            (title.startsWith("'") && title.endsWith("'"))) {
                            title = title.slice(1, -1);
                        }
                        return title;
                    }
                }
                break;
            }
        }
    }
    return null;
}

// 遍历 docs 文件夹下的所有 .md 文件，输出每个文件的第一个 H1 标题和 frontmatter title
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
                    let h1Title = null;
                    for (const line of lines) {
                        if (line.startsWith('# ')) {
                            h1Title = line.substring(2).trim();
                            break;
                        }
                    }

                    // 解析 frontmatter title
                    const frontmatterTitle = parseFrontmatterTitle(content);

                    // 使用相对路径，统一使用正斜杠
                    const relativePath = path.relative(process.cwd(), filePath).replace(/\\/g, '/');

                    // 根据 h1Title 和 frontmatterTitle 的存在情况生成输出
                    if (h1Title && frontmatterTitle) {
                        results.push(`${relativePath} ${h1Title} | ${frontmatterTitle}`);
                    } else if (h1Title) {
                        results.push(`${relativePath} ${h1Title}`);
                    } else if (frontmatterTitle) {
                        results.push(`${relativePath} ${frontmatterTitle}`);
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
    const args = process.argv.slice(2);
    const docsDir = args.length > 0
        ? path.resolve(process.cwd(), args[0])
        : path.join(process.cwd(), 'docs');

    if (!fs.existsSync(docsDir)) {
        console.error(`错误：文件夹不存在 ${docsDir}`);
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
