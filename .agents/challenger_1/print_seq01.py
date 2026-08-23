import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\02_Sequence_Diagrams.md", "r", encoding="utf-8") as f:
    text = f.read()

m1 = re.search(r'(# 1\. SEQ-01:.*?)(?=# 2\. SEQ-02:)', text, re.DOTALL)
if m1:
    print(m1.group(1))