const { spawnSync } = require('child_process');
const fs = require('fs');
const path = require('path');

function removeAnsiCodes(text) {
    // Regex to remove ANSI escape sequences
    const ansiEscape = /[\u001b\u009b][[()#;?]*(?:[0-9]{1,4}(?:;[0-9]{0,4})*)?[0-9A-ORZcf-nqry=><]/g;
    return text.replace(ansiEscape, '');
}

function runLint(filePath) {
    const rootProcess = spawnSync('git', ['rev-parse', '--show-toplevel'], { 
        encoding: 'utf8',
        shell: process.platform === 'win32'
    });
    const rootDir = rootProcess.stdout.trim();
    if (!rootDir) {
        console.error("无法找到 Git 根目录。");
        return 1;
    }

    const logFile = `${filePath}.log`;
    let results = [];

    results.push(`node ${process.argv.join(' ')}\n`);

    function runTool(cmd, args, name) {
        results.push(`=== ${name} ===\n`);
        try {
            const processRes = spawnSync(cmd, args, {
                encoding: 'utf8',
                cwd: rootDir,
                shell: process.platform === 'win32'
            });

            const stdout = removeAnsiCodes(processRes.stdout || "");
            const stderr = removeAnsiCodes(processRes.stderr || "");

            results.push(`Exit Code: ${processRes.status}\n`);
            if (stdout.trim()) {
                results.push("STDOUT:\n" + stdout + "\n");
            }
            if (stderr.trim()) {
                results.push("STDERR:\n" + stderr + "\n");
            }

        } catch (e) {
            results.push(`Execution Error: ${e.message}\n`);
        }
        results.push("\n" + "=".repeat(40) + "\n\n");
    }

    // 1. Autocorrect
    runTool("autocorrect", ["--lint", filePath, "--format", "diff"], "Autocorrect Linting");

    // 2. Markdownlint-cli2
    runTool("markdownlint-cli2", [filePath], "Markdownlint-cli2");

    try {
        fs.writeFileSync(logFile, results.join(''), 'utf8');
        console.log(`Linting complete. Results saved to: ${logFile}`);
    } catch (e) {
        console.error(`Failed to write log file: ${e.message}`);
        return 1;
    }

    return 0;
}

const args = process.argv.slice(2);
const fileArgIndex = args.indexOf('--file');
if (fileArgIndex === -1 || fileArgIndex + 1 >= args.length) {
    console.error("Usage: node lint.js --file <path-to-markdown-file>");
    process.exit(1);
}

const targetFile = path.resolve(args[fileArgIndex + 1]);

if (!fs.existsSync(targetFile)) {
    console.error(`Error: File '${targetFile}' does not exist.`);
    process.exit(1);
}

// Always exit with 0 to prevent CI/CD failures on lint errors
runLint(targetFile);
process.exit(0);
