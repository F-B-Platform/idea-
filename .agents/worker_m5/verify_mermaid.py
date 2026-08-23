import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT = r"d:\Idea_DoAn"
EXCLUDES = [".agents", ".git"]

mermaid_diagrams = []

for dirpath, dirnames, filenames in os.walk(ROOT):
    parts = dirpath.split(os.sep)
    if any(ex in parts for ex in EXCLUDES):
        continue
    for f in filenames:
        if f.endswith(".md"):
            p = os.path.join(dirpath, f)
            with open(p, "r", encoding="utf-8", errors="ignore") as fp:
                txt = fp.read()
            rel = os.path.relpath(p, ROOT)
            blocks = re.findall(r'```mermaid\s+(.*?)\s+```', txt, re.DOTALL)
            for i, b in enumerate(blocks):
                first_line = b.strip().splitlines()[0] if b.strip() else ""
                diag_type = first_line.split()[0] if first_line else "unknown"
                mermaid_diagrams.append({
                    "file": rel,
                    "index": i + 1,
                    "type": diag_type,
                    "first_line": first_line,
                    "lines": len(b.strip().splitlines())
                })

print(f"Total Mermaid diagrams found: {len(mermaid_diagrams)}")
for d in mermaid_diagrams:
    print(f"[{d['file']}] Diagram #{d['index']} - Type: {d['type']} ({d['lines']} lines) - '{d['first_line']}'")
