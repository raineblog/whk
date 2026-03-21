const fs = require('fs');
const path = require('path');

const sourceFile = path.resolve(__dirname, '../../AGENTS.md');
const targets = [
    path.resolve(__dirname, '../../.agent/rules/styleguide.md'),
    path.resolve(__dirname, '../../.clinerules/styleguide.md'),
    path.resolve(__dirname, '../../.gemini/styleguide.md'),
    path.resolve(__dirname, '../../.kilocode/rules/styleguide.md')
];

if (!fs.existsSync(sourceFile)) {
    console.error(`Source file not found: ${sourceFile}`);
    process.exit(1);
}

targets.forEach(target => {
    const targetDir = path.dirname(target);
    if (!fs.existsSync(targetDir)) {
        fs.mkdirSync(targetDir, { recursive: true });
    }
    try {
        fs.copyFileSync(sourceFile, target);
        console.log(`Successfully copied AGENTS.md to ${target}`);
    } catch (err) {
        console.error(`Failed to copy AGENTS.md to ${target}: ${err.message}`);
    }
});
