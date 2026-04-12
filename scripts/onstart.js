const fs = require('fs');
const path = require('path');

/**
 * onstart.js
 * 
 * 项目自动化同步脚本：
 * 负责将 .agents 中的技能、工作流及规则同步到各个 Agent 配置目录。
 * 
 * 核心逻辑：
 * 1. 模式 1 (Mode 1): 根同步模式，AGENTS.md 更名为 AGENT_GUIDE.md 放在根目录。
 * 2. 模式 2 (Mode 2): 子目录同步模式，规则文件放入 rules/ 文件夹下。
 * 3. 定向同步：仅管理 skills/, workflows/, rules/ 和特定的 .md 文件，不破坏用户其它文件。
 */

const projectRoot = path.resolve(__dirname, '..');
const agentsMd = path.resolve(projectRoot, 'AGENTS.md');
const agentsBaseDir = path.resolve(projectRoot, '.agents');

// 模式定义：1 -> 根目录, 2 -> 子目录(rules/)
const agentsConfig = {
    '.clinerules': 1,
    '.gemini': 1,
    '.kilocode': 2,
    '.kilo': 2,
    '.qwen': 2
};

/**
 * 递归删除
 */
function removePathSync(targetPath) {
    if (!fs.existsSync(targetPath)) return;
    try {
        fs.rmSync(targetPath, { recursive: true, force: true });
    } catch (err) {
        console.warn(`[onstart] Warning: Could not remove ${targetPath}: ${err.message}`);
    }
}

/**
 * 递归复制
 */
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

/**
 * 同步单个 Agent 目录
 */
function syncAgent(agentName, mode) {
    const targetDir = path.resolve(projectRoot, agentName);
    const rulesDest = mode === 2 ? path.join(targetDir, 'rules') : targetDir;

    console.log(`[onstart] Syncing ${agentName} (Mode ${mode})...`);

    // 1. 定向清理：只删除受管文件夹，保留用户手动放置的文件
    const managedFolders = ['skills', 'workflows', 'rules'];
    managedFolders.forEach(folder => {
        removePathSync(path.join(targetDir, folder));
        // 模式 2 特有的子目录 rules 及其内部
        if (mode === 2) removePathSync(path.join(targetDir, 'rules', folder));
    });
    // 删除旧的记录文件
    removePathSync(path.join(targetDir, 'AGENT_GUIDE.md'));
    if (mode === 2) removePathSync(path.join(targetDir, 'rules', 'AGENTS.md'));

    // 2. 确保目标目录存在
    if (!fs.existsSync(targetDir)) fs.mkdirSync(targetDir, { recursive: true });
    if (mode === 2 && !fs.existsSync(rulesDest)) fs.mkdirSync(rulesDest, { recursive: true });

    // 3. 同步 AGENTS.md
    if (fs.existsSync(agentsMd)) {
        const destFileName = mode === 1 ? 'AGENT_GUIDE.md' : 'AGENTS.md';
        const destPath = path.join(rulesDest, destFileName);
        fs.copyFileSync(agentsMd, destPath);
    }

    // 4. 同步 .agents 目录内容
    if (fs.existsSync(agentsBaseDir)) {
        fs.readdirSync(agentsBaseDir).forEach(item => {
            const srcPath = path.join(agentsBaseDir, item);
            let finalDest;
            
            if (item === 'skills' || item === 'workflows') {
                // Skills 和 workflows 始终放置在代理目录根部
                finalDest = path.join(targetDir, item);
            } else if (item === 'rules') {
                // rules 内容根据模式放置
                // 如果是目录模式，复制为 rules/rules/ 子文件夹，或者如果 rules 下只是 md，直接平铺
                // 推荐逻辑：.agents/rules 下的内容全部放入 rules 目标子文件夹
                finalDest = path.join(rulesDest, 'rules');
            } else {
                // 其它文件直接跟随 rules 目标
                finalDest = path.join(rulesDest, item);
            }
            
            copyRecursiveSync(srcPath, finalDest);
        });
    }

    // 5. 更新 .gitignore
    const gitignorePath = path.join(targetDir, '.gitignore');
    const ignoreList = ['skills/', 'workflows/', 'rules/'];
    if (mode === 1) ignoreList.push('AGENT_GUIDE.md');
    fs.writeFileSync(gitignorePath, ignoreList.join('\n') + '\n');
}

// 主程序
console.log('[onstart] Starting synchronization tasks...');
Object.entries(agentsConfig).forEach(([name, mode]) => {
    try {
        syncAgent(name, mode);
    } catch (err) {
        console.error(`[onstart] Critical error syncing ${name}:`, err);
    }
});
console.log('[onstart] All synchronization tasks completed.');
