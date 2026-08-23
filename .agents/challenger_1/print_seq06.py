import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\02_Sequence_Diagrams.md", "r", encoding="utf-8") as f:
    text = f.read()

m6 = re.search(r'(# 6\. SEQ-06:.*?)(?=# 7\. SEQ-07:)', text, re.DOTALL)
if m6:
    print(m6.group(1))