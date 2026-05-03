import json
with open("pr_comments_final.json", "r", encoding="utf-8") as f:
    data = json.load(f)

bodies = set()
for item in data:
    body = item.get("body", "")
    # Clean up
    lines = body.splitlines()
    clean_lines = []
    for line in lines:
        if any(x in line for x in ["metadata", "devin-review-badge", "Was this helpful", "details", "summary", "```", "suggestion"]):
            continue
        if line.strip():
            clean_lines.append(line.strip())
    if clean_lines:
        bodies.add("\n".join(clean_lines))

for b in sorted(list(bodies)):
    print(b)
    print("-" * 20)
