"""
katex_ssr.py - Pandoc JSON AST Filter for Server-Side KaTeX Rendering

This filter processes Pandoc JSON AST, finds Math elements, and replaces them
with pre-rendered HTML using KaTeX via bunx/bun runtime.

Configuration is read from katex_config.yml (same directory as this script).

Usage in mkpandocs.yml:
    pandoc:
      json_filters:
        - filters/katex_ssr.py
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

# ─── Embedded KaTeX renderer for bun ───────────────────────────────────────
KATEX_RENDERER_JS = """\
import katex from "katex";
import { readFileSync } from "fs";

const inputFile = process.argv[2];
const input = JSON.parse(readFileSync(inputFile, "utf-8"));
const { formulas, options } = input;

const renderOptions = {
    displayMode: false,
    throwOnError: false,
    output: "html",
    ...options,
    macros: { ...(options.macros || {}) },
};

const results = [];
for (const item of formulas) {
    try {
        const { content, displayMode, index } = item;
        const opts = { ...renderOptions, displayMode };
        const html = katex.renderToString(content, opts);
        results.push({ index, status: "success", html });
    } catch (err) {
        results.push({ index: item.index, status: "error", message: err.message });
    }
}

console.log(JSON.stringify({ results }));
"""


def _load_katex_config():
    """Load KaTeX configuration from katex_config.yml."""
    config_path = Path(__file__).parent / "katex_config.yml"
    if not config_path.exists():
        return {}

    if yaml is None:
        print("Warning: pyyaml not installed, using default katex config.", file=sys.stderr)
        return {}

    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def _find_bun():
    """Find an available bun/bunx executable using shutil.which."""
    for cmd in ["bun", "bunx"]:
        path = shutil.which(cmd)
        if path:
            return path
    return None


def _render_formulas_with_bun(formulas, options):
    """Render all formulas at once using bunx/bun."""
    if not formulas:
        return {}

    bun_cmd = _find_bun()
    if bun_cmd is None:
        print("Warning: bun/bunx not found. KaTeX formulas will not be rendered.", file=sys.stderr)
        return {}

    input_data = json.dumps({"formulas": formulas, "options": options}, ensure_ascii=False)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
        f.write(input_data)
        input_path = f.name

    with tempfile.NamedTemporaryFile(mode="w", suffix=".mjs", delete=False, encoding="utf-8") as f:
        f.write(KATEX_RENDERER_JS)
        renderer_path = f.name

    try:
        result = subprocess.run(
            [bun_cmd, "--bun", "run", renderer_path, input_path],
            capture_output=True,
            timeout=60,
            check=False,
        )

        if result.returncode != 0:
            stderr_text = result.stderr.decode("utf-8", errors="replace")
            print(f"katex-ssr: bun renderer error: {stderr_text}", file=sys.stderr)
            return {}

        output = json.loads(result.stdout.decode("utf-8"))
        results = output.get("results", [])

        mapping = {}
        for r in results:
            if r["status"] == "success":
                mapping[r["index"]] = r["html"]
            else:
                mapping[r["index"]] = None

        return mapping

    except subprocess.TimeoutExpired:
        print("katex-ssr: bun rendering timed out after 60s", file=sys.stderr)
        return {}
    except json.JSONDecodeError as e:
        print(f"katex-ssr: failed to parse bun output: {e}", file=sys.stderr)
        return {}
    finally:
        try:
            os.unlink(input_path)
            os.unlink(renderer_path)
        except OSError:
            pass


def walk_ast(obj, math_items):
    """Walk Pandoc JSON AST and collect all Math element references."""
    if isinstance(obj, dict):
        if obj.get("t") == "Math":
            c = obj.get("c", [])
            if len(c) == 2:
                math_type = c[0].get("t", "InlineMath") if isinstance(c[0], dict) else str(c[0])
                content = c[1]
                math_items.append({
                    "type": math_type,
                    "content": content,
                    "ref": obj,
                })
        else:
            for value in obj.values():
                walk_ast(value, math_items)
    elif isinstance(obj, list):
        for item in obj:
            walk_ast(item, math_items)


def _make_inline_html(html):
    """Create RawInline element with KaTeX HTML."""
    return {
        "t": "RawInline",
        "c": ["html", f'<span class="math math-inline">{html}</span>'],
    }


def transform_inlines(inlines, content_to_html):
    """Transform inline elements only, using RawInline for all math."""
    new_list = []
    for item in inlines:
        if isinstance(item, dict) and item.get("t") == "Math":
            c = item.get("c", [])
            if len(c) == 2:
                math_type = c[0].get("t", "InlineMath") if isinstance(c[0], dict) else str(c[0])
                content = c[1]
                is_display = math_type == "DisplayMath"
                html = content_to_html.get((content, is_display))

                if html is not None:
                    new_list.append(_make_inline_html(html))
                else:
                    new_list.append(item)
            else:
                new_list.append(item)
        elif isinstance(item, dict):
            for key in list(item.keys()):
                item[key] = transform_ast(item[key], content_to_html)
            new_list.append(item)
        else:
            new_list.append(item)
    return new_list


def transform_ast(obj, content_to_html):
    """Transform Pandoc AST: replace Math elements with RawInline HTML."""
    if isinstance(obj, dict):
        if obj.get("t") in ("Para", "Plain"):
            if "c" in obj and isinstance(obj["c"], list):
                obj["c"] = transform_inlines(obj["c"], content_to_html)
            return obj
        for key in list(obj.keys()):
            obj[key] = transform_ast(obj[key], content_to_html)
        return obj
    elif isinstance(obj, list):
        return [transform_ast(item, content_to_html) for item in obj]
    else:
        return obj


def main():
    # Read Pandoc JSON AST from stdin
    try:
        raw_bytes = sys.stdin.buffer.read()
        input_data = raw_bytes.decode("utf-8", errors="surrogateescape")
        ast = json.loads(input_data)
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        print(f"katex-ssr: failed to parse input JSON: {e}", file=sys.stderr)
        sys.exit(1)

    # Collect all Math elements
    math_items = []
    walk_ast(ast, math_items)

    if not math_items:
        sys.stdout.buffer.write(json.dumps(ast, ensure_ascii=False).encode("utf-8"))
        return

    # Build formulas list
    formulas = []
    content_index_map = {}

    for i, item in enumerate(math_items):
        content = item["content"]
        is_display = item["type"] == "DisplayMath"
        formulas.append({
            "index": i,
            "content": content,
            "displayMode": is_display,
        })
        content_index_map[(content, is_display)] = i

    # Load KaTeX configuration from katex_config.yml
    config = _load_katex_config()

    katex_options = {}
    macros = config.get("macros", {})
    if macros:
        katex_options["macros"] = macros
    katex_options["throwOnError"] = False

    verbose = os.environ.get("KATEX_VERBOSE") == "1"
    if verbose:
        print(f"katex-ssr: rendering {len(formulas)} formulas...", file=sys.stderr)

    render_results = _render_formulas_with_bun(formulas, katex_options)

    # Build content-based lookup
    content_to_html = {}
    for item in math_items:
        content = item["content"]
        is_display = item["type"] == "DisplayMath"
        idx = content_index_map.get((content, is_display))
        if idx is not None and idx in render_results:
            html = render_results[idx]
            if html is not None:
                content_to_html[(content, is_display)] = html

    # Transform AST
    ast = transform_ast(ast, content_to_html)

    if verbose:
        success_count = sum(1 for v in render_results.values() if v is not None)
        print(
            f"katex-ssr: {success_count}/{len(render_results)} formulas rendered successfully",
            file=sys.stderr,
        )

    # Write modified AST to stdout
    output = json.dumps(ast, ensure_ascii=False)
    output = output.encode("utf-8", errors="surrogateescape").decode("utf-8", errors="replace").encode("utf-8")
    sys.stdout.buffer.write(output)


if __name__ == "__main__":
    main()