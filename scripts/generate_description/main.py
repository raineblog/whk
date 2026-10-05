import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

from nvidia_api import get_description

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DOCS_DIR = PROJECT_ROOT / "docs"
BLOG_DIR = DOCS_DIR / "blog"
BLOG_POSTS_DIR = BLOG_DIR / "posts"
CACHE_FILE = PROJECT_ROOT / "description_cache.json"
MAX_PER_RUN = 80
DELAY = 1


def load_cache():
    if CACHE_FILE.exists():
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def parse_frontmatter(content):
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if match:
        return match.group(1), content[match.end() :]
    return "", content


def build_frontmatter(fm_body, description):
    lines = fm_body.split("\n")
    desc_re = re.compile(r"^description\s*:.*$", re.MULTILINE)
    if desc_re.search(fm_body):
        cleaned = desc_re.sub(f"description: {description}", fm_body)
    else:
        after_title = None
        for i, line in enumerate(lines):
            if re.match(r"^title\s*:", line):
                after_title = i + 1
                break
        if after_title is not None:
            lines.insert(after_title, f"description: {description}")
        else:
            lines.insert(0, f"description: {description}")
        cleaned = "\n".join(lines)
    return cleaned


def body_md5(body):
    stripped = re.sub(r"\s+", "", body)
    return hashlib.md5(stripped.encode("utf-8")).hexdigest()


def needs_description(content):
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if match:
        fm_text = match.group(1)
        return not bool(re.search(r"^description\s*:", fm_text, re.MULTILINE))
    return True


def is_blog_post(md_file):
    """Check if the file is under docs/blog/posts."""
    try:
        md_file.relative_to(BLOG_POSTS_DIR)
        return True
    except ValueError:
        return False


def apply_more_excerpt(body, desc):
    """Insert description + <!-- more --> after the H1 heading in blog post body.

    If <!-- more --> already exists, clear the old excerpt between H1 and <!-- more -->,
    then insert the new description.

    Expected output format (body part, after frontmatter):

        # Title

        <description text>

        <!-- more -->

        <rest of content>
    """
    # Split into lines for processing
    lines = body.split("\n")

    # Find H1 heading line index
    h1_idx = None
    for i, line in enumerate(lines):
        if re.match(r"^#\s+", line):
            h1_idx = i
            break

    if h1_idx is None:
        # No H1 heading found, just prepend excerpt
        return f"{desc}\n\n<!-- more -->\n\n{body}"

    # Find existing <!-- more --> line index
    more_idx = None
    for i, line in enumerate(lines):
        if i > h1_idx and line.strip() == "<!-- more -->":
            more_idx = i
            break

    if more_idx is not None:
        # Remove old excerpt: everything between H1 and <!-- more --> (exclusive)
        # Keep H1, remove old excerpt lines, keep <!-- more --> and after
        before = lines[: h1_idx + 1]
        after = lines[more_idx + 1 :]  # lines after <!-- more -->
        # Rebuild: H1 + blank + desc + blank + <!-- more --> + rest
        new_lines = before + ["", desc, "", "<!-- more -->"] + after
    else:
        # No existing <!-- more -->, insert after H1
        before = lines[: h1_idx + 1]
        # Skip blank lines immediately after H1
        rest_start = h1_idx + 1
        while rest_start < len(lines) and lines[rest_start].strip() == "":
            rest_start += 1
        after = lines[rest_start:]
        new_lines = before + ["", desc, "", "<!-- more -->", ""] + after

    return "\n".join(new_lines)


def get_md_files():
    result = []
    for root, dirs, files in os.walk(DOCS_DIR):
        root_path = Path(root)
        if root_path == BLOG_DIR:
            dirs[:] = ["posts"]
            continue
        for f in files:
            if f.endswith(".md"):
                result.append(root_path / f)
    return sorted(result)


def main():
    cache = load_cache()
    md_files = get_md_files()
    now = time.time()

    needs_update = []
    for md_file in md_files:
        rel = str(md_file.relative_to(PROJECT_ROOT))
        content = read_file(md_file)
        fm_body, body = parse_frontmatter(content)
        md5 = body_md5(body)
        entry = cache.get(rel)
        old_md5 = entry.get("md5") if entry else None
        last_ts = entry.get("last_submitted", 0) if entry else 0
        if old_md5 != md5:
            needs_update.append((rel, md_file, last_ts, content, fm_body, body, md5))

    needs_update.sort(key=lambda x: x[2])
    to_process = needs_update[:MAX_PER_RUN]

    if not to_process:
        print("No files need description updates.")
        return

    print(f"Processing {len(to_process)} file(s)...")

    for i, (rel, md_file, last_ts, content, fm_body, body, md5) in enumerate(
        to_process
    ):
        print(f"[{i + 1}/{len(to_process)}] {rel}")

        try:
            description = get_description(body, {"路径": rel})

            if description and description.strip():
                desc = description.strip()

                # For blog posts, apply excerpt with <!-- more -->
                if is_blog_post(md_file):
                    body = apply_more_excerpt(body, desc)

                if fm_body:
                    new_fm = build_frontmatter(fm_body, desc)
                    new_content = f"---\n{new_fm}\n---\n\n{body}"
                else:
                    new_content = f"---\ndescription: {desc}\n---\n\n{body}"
                write_file(md_file, new_content)

                cache[rel] = {"md5": md5, "last_submitted": now}
                save_cache(cache)

                print(f"  <- {len(desc)} chars")
            else:
                print(f"  !! empty response, skipped")
        except Exception as e:
            print(f"  !! error: {e}")

        if i < len(to_process) - 1:
            time.sleep(DELAY)

    print("Done.")


if __name__ == "__main__":
    main()
