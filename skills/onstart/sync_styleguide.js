const fs = require('fs');
const path = require('path');

const sourceFile = path.resolve(__dirname, '../../AGENTS.md');
const skillsDir = path.resolve(__dirname, '..');

const styleguideTargets = [
    path.resolve(__dirname, '../../.agent/rules/styleguide.md'),
    path.resolve(__dirname, '../../.clinerules/styleguide.md'),
    path.resolve(__dirname, '../../.gemini/styleguide.md'),
    path.resolve(__dirname, '../../.kilocode/rules/styleguide.md')
];

const skillsTargets = [
    path.resolve(__dirname, '../../.agent/skills'),
    path.resolve(__dirname, '../../.clinerules/skills'),
    path.resolve(__dirname, '../../.gemini/skills'),
    path.resolve(__dirname, '../../.kilocode/skills')
];

function copyRecursiveSync(src, dest) {
    const exists = fs.existsSync(src);
    const stats = exists && fs.statSync(src);
    const isDirectory = exists && stats.isDirectory();
    if (isDirectory) {
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

// 1. Sync AGENTS.md
if (fs.existsSync(sourceFile)) {
    styleguideTargets.forEach(target => {
        const targetDir = path.dirname(target);
        if (!fs.existsSync(targetDir)) {
            fs.mkdirSync(targetDir, { recursive: true });
        }
        try {
            fs.copyFileSync(sourceFile, target);
            console.log(`Successfully sync AGENTS.md to ${target}`);
        } catch (err) {
            console.error(`Failed to sync AGENTS.md to ${target}: ${err.message}`);
        }
    });
}

// 2. Sync skills folders
if (fs.existsSync(skillsDir)) {
    const subdirs = fs.readdirSync(skillsDir).filter(file => {
        const fullPath = path.join(skillsDir, file);
        return fs.statSync(fullPath).isDirectory() && file !== 'onstart';
    });

    skillsTargets.forEach(targetBase => {
        subdirs.forEach(subdir => {
            const srcPath = path.join(skillsDir, subdir);
            const destPath = path.join(targetBase, subdir);
            try {
                copyRecursiveSync(srcPath, destPath);
                console.log(`Successfully sync skills/${subdir} to ${destPath}`);
            } catch (err) {
                console.error(`Failed to sync skills/${subdir} to ${destPath}: ${err.message}`);
            }
        });
    });
}
