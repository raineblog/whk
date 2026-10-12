#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

/**
 * file_split.js - 文件分割器
 * 
 * 将文件按照 20000 个字符分割成多个临时文件
 * 分割后的文件命名为：原文件名.001.tmp, 原文件名.002.tmp 等
 */

// 分割大小：20000 个字符
const SPLIT_SIZE = 20000;

/**
 * 格式化文件大小，按照英文习惯每3位用逗号分隔
 * @param {number} bytes - 字节数
 * @returns {string} 格式化后的字符串
 */
function formatFileSize(bytes) {
    return bytes.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}

/**
 * 分割文件
 * @param {string} filePath - 文件相对路径
 */
function splitFile(filePath) {
    try {
        // 检查文件是否存在
        if (!fs.existsSync(filePath)) {
            console.error(`Error: File not found: ${filePath}`);
            process.exit(1);
        }

        // 读取文件内容
        const content = fs.readFileSync(filePath, 'utf8');
        const totalLength = content.length;
        
        // 如果文件小于分割大小，不需要分割
        if (totalLength <= SPLIT_SIZE) {
            console.log(`File is smaller than ${SPLIT_SIZE} characters, no splitting needed.`);
            return;
        }

        // 计算需要分割成多少个文件
        const numParts = Math.ceil(totalLength / SPLIT_SIZE);
        const results = [];

        // 分割文件
        for (let i = 0; i < numParts; i++) {
            const start = i * SPLIT_SIZE;
            const end = Math.min(start + SPLIT_SIZE, totalLength);
            const partContent = content.substring(start, end);
            
            // 生成文件名：原文件名.001.tmp, 原文件名.002.tmp 等
            const partNumber = String(i + 1).padStart(3, '0');
            const partFileName = `${filePath}.${partNumber}.tmp`;
            
            // 写入文件
            fs.writeFileSync(partFileName, partContent, 'utf8');
            
            // 获取文件大小
            const stats = fs.statSync(partFileName);
            const fileSize = stats.size;
            
            results.push({
                filename: partFileName,
                size: formatFileSize(fileSize)
            });
        }

        // 输出结果
        console.log(`Split ${filePath} into ${numParts} parts:`);
        results.forEach(result => {
            console.log(`${result.filename} ${result.size} bytes`);
        });

    } catch (error) {
        console.error(`Error: ${error.message}`);
        process.exit(1);
    }
}

// 主程序
if (require.main === module) {
    const args = process.argv.slice(2);
    
    if (args.length !== 1) {
        console.error('Usage: node file_split.js <file_path>');
        process.exit(1);
    }
    
    const filePath = args[0];
    splitFile(filePath);
}

module.exports = { splitFile, formatFileSize };