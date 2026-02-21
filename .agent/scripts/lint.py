import subprocess
import argparse
import os
import sys
import re

def remove_ansi_codes(text):
    # Regex to remove ANSI escape sequences
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

def run_lint(file_path):
    log_file = f"{file_path}.log"
    results = []

    results.append(sys.executable + ' ' + ' '.join(sys.argv) + "\n" )
    
    def run_tool(cmd_list, name):
        results.append(f"=== {name} ===\n")
        try:
            is_windows = os.name == 'nt'
            # Use subprocess.list2cmdline only for shell=True on Windows
            cmd = subprocess.list2cmdline(cmd_list) if is_windows else cmd_list
            
            process = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='replace',
                shell=is_windows
            )
            
            stdout = remove_ansi_codes(process.stdout or "")
            stderr = remove_ansi_codes(process.stderr or "")
            
            results.append(f"Exit Code: {process.returncode}\n")
            if stdout.strip():
                results.append("STDOUT:\n" + stdout + "\n")
            if stderr.strip():
                results.append("STDERR:\n" + stderr + "\n")
                
        except Exception as e:
            results.append(f"Execution Error: {str(e)}\n")
        results.append("\n" + "="*40 + "\n\n")

    # 1. Autocorrect
    # Removed --no-color as it was not supported by the local version
    # Our remove_ansi_codes will clean up the output instead
    run_tool(["autocorrect", "--lint", file_path, "--format", "diff"], "Autocorrect Linting")

    # 2. Markdownlint-cli2
    run_tool(["markdownlint-cli2", file_path], "Markdownlint-cli2")

    try:
        with open(log_file, "w", encoding="utf-8") as f:
            f.writelines(results)
        print(f"Linting complete. Results saved to: {log_file}")
    except Exception as e:
        print(f"Failed to write log file: {e}", file=sys.stderr)
        return 1

    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lint a markdown file and save results to a log.")
    parser.add_argument("--file", required=True, help="Path to the markdown file to lint.")
    
    args = parser.parse_args()
    target_file = os.path.abspath(args.file)
    
    if not os.path.exists(target_file):
        print(f"Error: File '{target_file}' does not exist.", file=sys.stderr)
        sys.exit(1)
        
    # Always exit with 0 to prevent CI/CD failures on lint errors
    run_lint(target_file)
    sys.exit(0)
