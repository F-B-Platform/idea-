import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"d:\Idea_DoAn"
FILES = [
    os.path.join(BASE_DIR, "05_Quy_Chuan_&_Test_Cases", "UAT_Test_Cases.md"),
    os.path.join(BASE_DIR, "05_Quy_Chuan_&_Test_Cases", "Seed_Data_&_Database_Script.md"),
    os.path.join(BASE_DIR, "05_Quy_Chuan_&_Test_Cases", "Git_Workflow_&_Branching_Strategy.md")
]

for fpath in FILES:
    fname = os.path.basename(fpath)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    matches = re.findall(r">\s*\[!(NOTE|IMPORTANT|TIP|WARNING|CAUTION)\]", content, re.IGNORECASE)
    breakdown = {}
    for m in matches:
        k = m.upper()
        breakdown[k] = breakdown.get(k, 0) + 1
    print(f"File: {fname:<40} Total: {len(matches):<3} Breakdown: {breakdown}")
