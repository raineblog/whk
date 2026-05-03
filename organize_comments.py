import json
from collections import defaultdict

with open("pr_comments_latest.json", "r", encoding="utf-8") as f:
    comments = json.load(f)

organized = defaultdict(list)
for c in comments:
    file_path = c.get("path")
    line = c.get("line") or c.get("original_line")
    user = c.get("user", {}).get("login")
    body = c.get("body")
    organized[file_path].append({
        "line": line,
        "user": user,
        "body": body
    })

for file_path, cmts in organized.items():
    print(f"FILE: {file_path}")
    for c in sorted(cmts, key=lambda x: x["line"] if x["line"] is not None else 0):
        print(f"  LINE {c['line']} [{c['user']}]: {c['body']}\n")
    print("-" * 40)
