const fs = require('fs');
const path = require('path');

/**
 * onstart.js
 * 
 * 项目启动和代理规则同步脚本。
 * 支持两种同步模式：
 * 模式 1: 复制到目标目录根文件夹 (例如 .clinerules, .gemini)
 * 模式 2: 复制到目标目录的 rules 文件夹 (例如 .kilo, .kilocode, .qwen)
 */

const projectRoot = path.resolve(__dirname, '..');
const agentsMd = path.resolve(projectRoot, 'AGENTS.md');
const agentsDir = path.resolve(projectRoot, '.agents');

// 模式定义：1 -> 根目录, 2 -> rules 文件夹
const modeConfig = {
    '.clinerules': 1,
    '.gemini': 1,
    '.kilocode': 2,
    '.kilo': 2,
    '.qwen': 2
};

function copyRecursiveSync(src, dest) {
    if (!fs.existsSync(src)) return;
    const stats = fs.statSync(src);
    if (stats.isDirectory()) {
        if (!fs.existsSync(dest)) fs.mkdirSync(dest, { recursive: true });
        fs.readdirSync(src).forEach(child => {
            copyRecursiveSync(path.join(src, child), path.join(dest, child));
        });
    } else {
        fs.copyFileSync(src, dest);
    }
}

function syncToTarget(targetName, mode) {
    const targetDir = path.resolve(projectRoot, targetName);
    
    console.log(`[onstart] Syncing to ${targetName} (Mode ${mode})...`);

    // 清理旧内容
    if (fs.existsSync(targetDir)) {
        fs.rmSync(targetDir, { recursive: true, force: true });
    }
    
    fs.mkdirSync(targetDir, { recursive: true });

    // 1. 同步 AGENTS.md
    if (fs.existsSync(agentsMd)) {
        const destFile = mode === 1 ? path.join(targetDir, 'AGENT_GUIDE.md') : path.join(targetDir, 'rules', 'AGENTS.md');
        if (mode === 2) fs.mkdirSync(path.join(targetDir, 'rules'), { recursive: true });
        fs.copyFileSync(agentsMd, destFile);
    }

    // 2. 同步 .agents 目录下的内容
    if (fs.existsSync(agentsDir)) {
        fs.readdirSync(agentsDir).forEach(item => {
            const srcPath = path.join(agentsDir, item);
            let destPath;
            
            if (item === 'skills' || item === 'workflows') {
                // skills 和 workflows 始终在根目录
                destPath = path.join(targetDir, item);
            } else if (item === 'rules') {
                // rules 文件夹根据模式放置
                destPath = mode === 2 ? path.join(targetDir, 'rules', 'rules') : path.join(targetDir, 'rules');
                if (mode === 2) fs.mkdirSync(path.join(targetDir, 'rules'), { recursive: true });
            } else {
                // 其它文件（如可能存在的 README）
                destPath = mode === 2 ? path.join(targetDir, 'rules', item) : path.join(targetDir, item);
            }
            
            copyRecursiveSync(srcPath, destPath);
        });
    }

    // 3. 写入 .gitignore
    const gitignorePath = path.join(targetDir, '.gitignore');
    let ignoreItems = ['skills/', 'workflows/'];
    if (mode === 1) {
        ignoreItems.push('rules/', 'AGENT_GUIDE.md');
    } else {
        ignoreItems.push('rules/');
    }
    fs.writeFileSync(gitignorePath, ignoreItems.join('\n') + '\n');
}

// 执行同步
Object.entries(modeConfig).forEach(([target, mode]) => {
    try {
        syncToTarget(target, mode);
    } catch (err) {
        console.error(`[onstart] Failed to sync ${target}: ${err.message}`);
    }
});

console.log('[onstart] Rules synchronization completed.');
