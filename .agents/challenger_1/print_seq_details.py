import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\02_Sequence_Diagrams.md", "r", encoding="utf-8") as f:
    text = f.read()

def get_sec(title_pat):
    m = re.search(rf"(# \d+\.\s+{title_pat}.*?)(?=# \d+\.|\Z)", text, re.DOTALL)
    return m.group(1) if m else ""

print("=== SEQ-01 FULL TEXT ===")
print(get_sec("SEQ-01"))

print("\n=== SEQ-02 FULL TEXT ===")
print(get_sec("SEQ-02"))

print("\n=== SEQ-03 FULL TEXT ===")
print(get_sec("SEQ-03"))