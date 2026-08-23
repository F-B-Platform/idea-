import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\05_Quy_Trinh_Backend.md", "r", encoding="utf-8") as f:
    content = f.read()

m7 = re.search(r"# 7\.\s+BACKGROUND WORKERS", content)
m8 = re.search(r"# 8\.\s+PHÂN BỔ TRÁCH NHIỆM", content)
if m7 and m8:
    print(content[m7.start():m8.start()])
