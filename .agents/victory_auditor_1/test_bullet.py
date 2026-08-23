import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

filepath = r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\UAT_Test_Cases.md"
with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

m = re.search(r"(#### `TC-AUTH-01`:.*?)(?=####|\Z)", text, re.DOTALL)
if m:
    lines = m.group(1).splitlines()
    for l in lines:
        if l.strip().startswith("- **"):
            print("BULLET:", l.strip()[:60])
