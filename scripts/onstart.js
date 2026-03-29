const fs = require('fs');
const path = require('path');

/**
 * onstart.js
 * 
 * 项目启动和 Git 提交时的自动化同步脚本。
 * 负责同步 AGENTS.md、skills、review、rules、workflows 到各个 agent 配置目录。
 */

const sourceFile = path.resolve(__dirname, '../AGENTS.md');
const reviewSourceFile = path.resolve(__dirname, '../REVIEW.md');
const skillsDir = path.resolve(__dirname, 'skills');
const reviewDir = path.resolve(__dirname, 'review');
const rulesDir = path.resolve(__dirname, 'rules');
const workflowsDir = path.resolve(__dirname, 'workflows');

// 目标目录常量
const styleguideTargets = [
    path.resolve(__dirname, '../.agents/rules/styleguide.md'),
    path.resolve(__dirname, '../.clinerules/styleguide.md'),
    path.resolve(__dirname, '../.gemini/styleguide.md'),
    path.resolve(__dirname, '../.kilocode/rules/styleguide.md'),
    path.resolve(__dirname, '../.kilo/rules/styleguide.md'),
];

const skillsTargets = [
    path.resolve(__dirname, '../.agents/skills'),
    path.resolve(__dirname, '../.clinerules/skills'),
    path.resolve(__dirname, '../.gemini/skills'),
    path.resolve(__dirname, '../.kilocode/skills'),
    path.resolve(__dirname, '../.kilo/skills'),
];

const reviewTargets = [
    path.resolve(__dirname, '../.agents/review'),
    path.resolve(__dirname, '../.clinerules/review'),
    path.resolve(__dirname, '../.gemini/review'),
    path.resolve(__dirname, '../.kilocode/review'),
    path.resolve(__dirname, '../.kilo/review'),
];

const rulesTargets = [
    path.resolve(__dirname, '../.agents/rules'),
    path.resolve(__dirname, '../.clinerules'),
    path.resolve(__dirname, '../.gemini'),
    path.resolve(__dirname, '../.kilocode/rules'),
    path.resolve(__dirname, '../.kilo/rules'),
];

const workflowsTargets = [
    path.resolve(__dirname, '../.agents/workflows'),
    path.resolve(__dirname, '../.clinerules/workflows'),
    path.resolve(__dirname, '../.gemini/workflows'),
    path.resolve(__dirname, '../.kilocode/workflows'),
    path.resolve(__dirname, '../.kilo/workflows'),
];

/**
 * 递归同步目录
 */
function copyRecursiveSync(src, dest) {
    if (!fs.existsSync(src)) {
        throw new Error(`Source path does not exist: ${src}`);
    }
    const stats = fs.statSync(src);
    if (stats.isDirectory()) {
        if (!fs.existsSync(dest)) {
            fs.mkdirSync(dest, { recursive: true });
        }
        fs.readdirSync(src).forEach(childItemName => {
            copyRecursiveSync(path.join(src, childItemName), path.join(dest, childItemName));
        });
    } else {
        fs.copyFileSync(src, dest);
    }
}

/**
 * 递归删除目录
 */
function removeRecursiveSync(dir) {
    if (fs.existsSync(dir)) {
        fs.readdirSync(dir).forEach(file => {
            const curPath = path.join(dir, file);
            if (fs.lstatSync(curPath).isDirectory()) {
                removeRecursiveSync(curPath);
            } else {
                fs.unlinkSync(curPath);
            }
        });
        fs.rmdirSync(dir);
    }
}

// 1. 同步 AGENTS.md 到各个规则目录
if (fs.existsSync(sourceFile)) {
    styleguideTargets.forEach(target => {
        const targetDir = path.dirname(target);
        if (!fs.existsSync(targetDir)) {
            fs.mkdirSync(targetDir, { recursive: true });
        }
        try {
            fs.copyFileSync(sourceFile, target);
            console.log(`[onstart] Successfully sync AGENTS.md to ${target}`);
        } catch (err) {
            console.error(`[onstart] Failed to sync AGENTS.md to ${target}: ${err.message}`);
        }
    });
} else {
    console.warn(`[onstart] Source file not found: ${sourceFile}`);
}

// 2. 同步 skills 文件夹到各个 agent 目录
if (fs.existsSync(skillsDir)) {
    const subdirs = fs.readdirSync(skillsDir).filter(file => {
        const fullPath = path.join(skillsDir, file);
        return fs.statSync(fullPath).isDirectory();
    });

    skillsTargets.forEach(targetBase => {
        if (!fs.existsSync(targetBase)) {
            fs.mkdirSync(targetBase, { recursive: true });
        }
        
        subdirs.forEach(subdir => {
            const srcPath = path.join(skillsDir, subdir);
            const destPath = path.join(targetBase, subdir);
            try {
                copyRecursiveSync(srcPath, destPath);
                console.log(`[onstart] Successfully sync skills/${subdir} to ${destPath}`);
            } catch (err) {
                console.error(`[onstart] Failed to sync skills/${subdir} to ${destPath}: ${err.message}`);
            }
        });
    });
} else {
    console.warn(`[onstart] Skills directory not found: ${skillsDir}`);
}

// 3. 同步 review 文件夹到各个 agent 目录
if (fs.existsSync(reviewDir)) {
    reviewTargets.forEach(targetBase => {
        if (!fs.existsSync(targetBase)) {
            fs.mkdirSync(targetBase, { recursive: true });
        }
        
        try {
            copyRecursiveSync(reviewDir, targetBase);
            console.log(`[onstart] Successfully sync review to ${targetBase}`);
        } catch (err) {
            console.error(`[onstart] Failed to sync review to ${targetBase}: ${err.message}`);
        }
    });
} else {
    console.warn(`[onstart] Review directory not found: ${reviewDir}`);
}

// 4. 同步 rules 文件夹到各个 agent 目录
if (fs.existsSync(rulesDir)) {
    const ruleFiles = fs.readdirSync(rulesDir).filter(file => {
        const fullPath = path.join(rulesDir, file);
        return fs.statSync(fullPath).isFile();
    });

    rulesTargets.forEach(targetBase => {
        if (!fs.existsSync(targetBase)) {
            fs.mkdirSync(targetBase, { recursive: true });
        }
        
        ruleFiles.forEach(ruleFile => {
            const srcPath = path.join(rulesDir, ruleFile);
            const destPath = path.join(targetBase, ruleFile);
            try {
                fs.copyFileSync(srcPath, destPath);
                console.log(`[onstart] Successfully sync rules/${ruleFile} to ${destPath}`);
            } catch (err) {
                console.error(`[onstart] Failed to sync rules/${ruleFile} to ${destPath}: ${err.message}`);
            }
        });
    });
} else {
    console.warn(`[onstart] Rules directory not found: ${rulesDir}`);
}

// 5. 同步 workflows 文件夹到各个 agent 目录
if (fs.existsSync(workflowsDir)) {
    const workflowFiles = fs.readdirSync(workflowsDir).filter(file => {
        const fullPath = path.join(workflowsDir, file);
        return fs.statSync(fullPath).isFile();
    });

    workflowsTargets.forEach(targetBase => {
        if (!fs.existsSync(targetBase)) {
            fs.mkdirSync(targetBase, { recursive: true });
        }
        
        workflowFiles.forEach(workflowFile => {
            const srcPath = path.join(workflowsDir, workflowFile);
            const destPath = path.join(targetBase, workflowFile);
            try {
                fs.copyFileSync(srcPath, destPath);
                console.log(`[onstart] Successfully sync workflows/${workflowFile} to ${destPath}`);
            } catch (err) {
                console.error(`[onstart] Failed to sync workflows/${workflowFile} to ${destPath}: ${err.message}`);
            }
        });
    });
} else {
    console.warn(`[onstart] Workflows directory not found: ${workflowsDir}`);
}

console.log('[onstart] Sync completed.');
