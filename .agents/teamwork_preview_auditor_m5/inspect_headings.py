import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

TARGET_DIR = r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai"
FILES = [
    "01_Phan_Tich_Yeu_Cau.md",
    "02_Thiet_Ke_Database.md",
    "03_Thiet_Ke_API_Contract.md",
    "04_Thiet_Ke_UI_UX.md",
    "05_Quy_Trinh_Backend.md",
    "06_Quy_Trinh_Frontend.md",
    "07_Ke_Hoach_Kiem_Thu.md",
    "08_Trien_Khai_He_Thong.md",
    "README.md"
]

for fname in FILES:
    fpath = os.path.join(TARGET_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    print(f"\n=======================================================")
    print(f"FILE: {fname}")
    print(f"=======================================================")
    h1_h2 = [line.strip() for line in lines if line.startswith("# ") or line.startswith("## ")]
    for h in h1_h2[:15]:
        print(f"  {h}")
    if len(h1_h2) > 15:
        print(f"  ... and {len(h1_h2) - 15} more major headings")
