import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

DOCS_DIR = r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai"
with open(os.path.join(DOCS_DIR, "05_Quy_Trinh_Backend.md"), "r", encoding="utf-8") as f:
    doc5 = f.read()

print("--- REDIS / CACHING IN 05_Quy_Trinh_Backend.md ---")
for line in doc5.splitlines():
    if "cache" in line.lower() or "redis" in line.lower() or "redlock" in line.lower():
        print(line[:100])
