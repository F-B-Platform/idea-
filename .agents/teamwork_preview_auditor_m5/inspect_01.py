import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\01_Phan_Tich_Yeu_Cau.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"01_Phan_Tich_Yeu_Cau.md has {len(lines)} lines")
h1_h2_h3 = [line.strip() for line in lines if line.startswith("# ") or line.startswith("## ") or line.startswith("### ")]
for h in h1_h2_h3[:30]:
    print(f"  {h}")
if len(h1_h2_h3) > 30:
    print(f"  ... and {len(h1_h2_h3) - 30} more headings")
