import os
import re
import glob
import json

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

print("=== STARTING AUDIT RUNNER ===")
for fname in FILES:
    fpath = os.path.join(TARGET_DIR, fname)
    if not os.path.exists(fpath):
        print(f"MISSING FILE: {fname}")
    else:
        with open(fpath, "r", encoding="utf-8") as f:
            lines = f.readlines()
            size = os.path.getsize(fpath)
            print(f"File: {fname:30} | Lines: {len(lines):5} | Size: {size:7} bytes")
