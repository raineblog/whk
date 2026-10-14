import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

from kilo_api import get_description

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DOCS_DIR = PROJECT_ROOT / "docs"
BLOG_DIR = DOCS_DIR / "blog"
BLOG_POSTS_DIR = BLOG_DIR / "posts"
CACHE_FILE = PROJECT_ROOT / "description_cache.json"
MAX_PER_RUN = 80
DELAY = 1
MAX_RETRIES = 5
RETRY_DELAY = 1


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


def strip_more_excerpt(body):
    """Remove the excerpt between H1 and <!-- more --> for stable hashing.

    Returns the body with the inserted excerpt stripped out,
    so the MD5 only reflects the actual content.
    """
    lines = body.split("\n")
    h1_idx = None
    for i, line in enumerate(lines):
        if re.match(r"^#\s+", line):
            h1_idx = i
            break
    if h1_idx is None:
        # No H1: treat everything before the first <!-- more --> as excerpt
        for i, line in enumerate(lines):
            if line.strip() == "<!-- more -->":
                return "\n".join(lines[i + 1 :])
        return body
    more_idx = None
    for i, line in enumerate(lines):
        if i > h1_idx and line.strip() == "<!-- more -->":
            more_idx = i
            break
    if more_idx is None:
        return body
    # Remove everything between H1 (exclusive) and <!-- more --> (inclusive)
    return "\n".join(lines[: h1_idx + 1] + lines[more_idx + 1 :])


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
        # No H1: if <!-- more --> exists, replace the excerpt before it
        more_idx = None
        for i, line in enumerate(lines):
            if line.strip() == "<!-- more -->":
                more_idx = i
                break
        if more_idx is not None:
            after = lines[more_idx + 1 :]
            return "\n".join([desc, "", "<!-- more -->"] + after)
        # No existing <!-- more -->, just prepend excerpt
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


def get_description_with_retry(body, rel):
    """Call get_description, retrying up to MAX_RETRIES times on failure."""
    for attempt in range(MAX_RETRIES + 1):
        try:
            return get_description(body, {"路径": rel})
        except Exception as e:
            if attempt >= MAX_RETRIES:
                raise
            print(f"  !! retry {attempt + 1}/{MAX_RETRIES} after error: {e}")
            time.sleep(RETRY_DELAY)


def main():
    cache = load_cache()
    md_files = get_md_files()
    now = time.time()

    current_rels = {f.relative_to(PROJECT_ROOT).as_posix() for f in md_files}

    # 收集在当前磁盘上已不存在的旧缓存项索引（按 md5 归类），用于识别文件移动/重命名
    missing_by_md5 = {}
    for k, v in cache.items():
        if k not in current_rels:
            m = v.get("md5")
            if m:
                missing_by_md5.setdefault(m, []).append(k)

    needs_update = []
    cache_modified = False
    migrated_count = 0
    reused_count = 0

    for md_file in md_files:
        rel = md_file.relative_to(PROJECT_ROOT).as_posix()
        content = read_file(md_file)
        fm_body, body = parse_frontmatter(content)
        # For blog posts, strip the inserted excerpt before hashing
        # so the MD5 stays stable after description insertion
        hash_body = strip_more_excerpt(body) if is_blog_post(md_file) else body
        md5 = body_md5(hash_body)
        entry = cache.get(rel)

        # 1. 当前路径已有缓存且 MD5 一致，无需更新
        if entry and entry.get("md5") == md5:
            continue

        # 2. 从已移动/删除的旧文件中匹配相同 MD5，重命名缓存键
        if md5 in missing_by_md5 and missing_by_md5[md5]:
            # 若有多个相同 md5 候选，优先匹配文件名相同的项
            matching_idx = 0
            for idx, cand in enumerate(missing_by_md5[md5]):
                if Path(cand).name == md_file.name:
                    matching_idx = idx
                    break
            old_rel = missing_by_md5[md5].pop(matching_idx)
            cache[rel] = cache.pop(old_rel)
            cache_modified = True
            migrated_count += 1
            print(f"  [cache migrated] {old_rel} -> {rel}")
            continue

        # 3. 若有磁盘上其他文件具有相同 MD5（如文件复制），复用缓存
        matching_k = next((k for k, v in cache.items() if v.get("md5") == md5 and k != rel), None)
        if matching_k:
            cache[rel] = {
                "md5": md5,
                "last_submitted": cache[matching_k].get("last_submitted", now),
            }
            cache_modified = True
            reused_count += 1
            print(f"  [cache reused] {matching_k} -> {rel}")
            continue

        # 4. 全新文件或内容发生实质变动，加入待更新队列
        last_ts = entry.get("last_submitted", 0) if entry else 0
        needs_update.append((rel, md_file, last_ts, content, fm_body, body, md5))

    # 若发生了缓存迁移或复用，先持久化保存
    if cache_modified:
        save_cache(cache)
        print(f"Updated cache: {migrated_count} migrated, {reused_count} reused.")

    if "--migrate-only" in sys.argv:
        print("Migrate-only mode requested. Exiting.")
        return

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
            description = get_description_with_retry(body, rel)

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
