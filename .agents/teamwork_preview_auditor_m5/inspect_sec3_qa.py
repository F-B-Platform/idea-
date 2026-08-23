import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\07_Ke_Hoach_Kiem_Thu.md", "r", encoding="utf-8") as f:
    content = f.read()

m3 = re.search(r"# 3\.\s+MA TRẬN 10 KỊCH BẢN BIÊN", content)
m4 = re.search(r"# 4\.\s+KIỂM THỬ HIỆU NĂNG", content)
if m3 and m4:
    sec3 = content[m3.start():m4.start()]
    print("Headings in Section 3:")
    for l in sec3.split("\n"):
        if l.startswith("#"):
            print("  ", l)
