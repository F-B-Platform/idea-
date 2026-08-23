import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\04_Thiet_Ke_UI_UX.md", "r", encoding="utf-8") as f:
    content = f.read()

m = re.search(r"# 4\.\s+BỘ 20 KHUNG GIAO DIỆN", content)
m5 = re.search(r"# 5\.\s+TIÊU CHUẨN TIẾP CẬN", content)
if m and m5:
    section_text = content[m.start():m5.start()]
    headings = [line for line in section_text.split("\n") if line.startswith("#")]
    print("Headings in Section 4:")
    for h in headings:
        print("  ", h)
