import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

filepath = r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\UAT_Test_Cases.md"
with open(filepath, "r", encoding="utf-8") as f:
    for idx, line in enumerate(f, 1):
        if line.startswith("#"):
            print(f"Line {idx:4d}: {line.strip()}")
