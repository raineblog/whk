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
    const rulesDest = mode === 2 ? path.join(targetDir, 'rules') : targetDir;
    
    console.log(`[onstart] Syncing to ${targetName} (Mode ${mode})...`);

    // 清理旧内容（如果存在），确保同步后目录干净
    if (fs.existsSync(targetDir)) {
        fs.rmSync(targetDir, { recursive: true, force: true });
    }
    
    fs.mkdirSync(targetDir, { recursive: true });
    if (mode === 2) fs.mkdirSync(rulesDest, { recursive: true });

    // 同步 AGENTS.md (更名为该目录所需的规则文件名，或对模式 1 直接复制)
    // 模式 1 复制为目标对应的专有名称（如 .clinerules），模式 2 复制到 rules 文件夹
    if (fs.existsSync(agentsMd)) {
        const destFile = mode === 1 ? path.join(targetDir, 'AGENT_GUIDE.md') : path.join(rulesDest, 'AGENTS.md');
        fs.copyFileSync(agentsMd, destFile);
    }

    // 同步 .agents 目录下的所有内容 (skills, workflows, rules)
    if (fs.existsSync(agentsDir)) {
        fs.readdirSync(agentsDir).forEach(item => {
            const srcPath = path.join(agentsDir, item);
            const destPath = path.join(rulesDest, item);
            copyRecursiveSync(srcPath, destPath);
        });
    }

    // 写入 .gitignore
    const gitignorePath = path.join(targetDir, '.gitignore');
    let gitignoreContent = '';
    if (mode === 1) {
        // 模式 1：忽略复制进去的文件夹
        gitignoreContent = 'skills/\nworkflows/\nrules/\nAGENT_GUIDE.md\n';
    } else {
        // 模式 2：忽略核心文件夹
        gitignoreContent = 'skills/\nworkflows/\nrules/\n';
    }
    fs.writeFileSync(gitignorePath, gitignoreContent);
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
