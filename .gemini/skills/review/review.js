const { spawnSync } = require('child_process');
const path = require('path');
const fs = require('fs');

function main() {
    const args = process.argv.slice(2);
    if (args.length === 0) {
        console.log('Usage: npm run review <command> [args]');
        console.log('Available commands:');
        const files = fs.readdirSync(__dirname);
        files.forEach(file => {
            if (file.endsWith('.js') && file !== 'review.js') {
                console.log(`  - ${path.basename(file, '.js')}`);
            }
        });
        return;
    }

    const command = args[0];
    const scriptPath = path.resolve(__dirname, `${command}.js`);

    if (!fs.existsSync(scriptPath)) {
        console.error(`Error: Command '${command}' not found in ${__dirname}`);
        process.exit(1);
    }

    const remainingArgs = args.slice(1);
    
    // Find project root to ensure scripts run correctly
    const rootProcess = spawnSync('git', ['rev-parse', '--show-toplevel'], { 
        encoding: 'utf8',
        shell: process.platform === 'win32'
    });
    const rootDir = rootProcess.stdout.trim() || path.resolve(__dirname, '../../');

    const result = spawnSync('node', [scriptPath, ...remainingArgs], {
        stdio: 'inherit',
        shell: process.platform === 'win32',
        cwd: rootDir
    });

    process.exit(result.status);
}

main();
