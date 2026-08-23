import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

DOCS_DIR = r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai"

with open(os.path.join(DOCS_DIR, "06_Quy_Trinh_Frontend.md"), "r", encoding="utf-8") as f:
    doc6 = f.read()

print("--- SECTION 2 OF 06_Quy_Trinh_Frontend.md ---")
m = re.search(r'# 2\..*?(?=# 3\.)', doc6, re.DOTALL)
if m:
    sec2 = m.group(0)
    for line in sec2.splitlines():
        if "create<" in line or "store" in line.lower() or "export const" in line:
            print(line[:100])
