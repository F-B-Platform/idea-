import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Seed_Data_&_Database_Script.md", "r", encoding="utf-8") as f:
    content = f.read()

# Let's find lines around order_items and comments in INSERT statements
lines = content.splitlines()
for idx, line in enumerate(lines):
    if "INSERT INTO" in line.upper():
        print(f"Line {idx+1}: {line}")
    if "order_items" in line.lower():
        print(f"  [order_items line {idx+1}]: {line[:100]}")
