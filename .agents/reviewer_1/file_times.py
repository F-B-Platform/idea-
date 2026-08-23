import os
import sys
import datetime

sys.stdout.reconfigure(encoding='utf-8')
DOCS_DIR = r"d:\Idea_DoAn"

def compare_files():
    for root, dirs, files in os.walk(DOCS_DIR):
        if ".agents" in root or ".git" in root:
            continue
        for f in files:
            p = os.path.join(root, f)
            rel = os.path.relpath(p, DOCS_DIR)
            mtime = os.path.getmtime(p)
            dt = datetime.datetime.fromtimestamp(mtime).isoformat()
            sz = os.path.getsize(p)
            print(f"{rel:65} | {sz:7} bytes | {dt}")

compare_files()
