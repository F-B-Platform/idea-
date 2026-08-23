import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

DOCS_DIR = r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai"
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
    path = os.path.join(DOCS_DIR, fname)
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    for idx, line in enumerate(lines):
        # check C-23, C-24
        if re.search(r'\bC-(2[1-9]|[3-9][0-9])\b', line):
            print(f"[{fname}:{idx+1}] C-2x match: {line.strip()}")
            
        # check GPS 50m
        if re.search(r'GPS.*50|50.*GPS', line, re.I):
            print(f"[{fname}:{idx+1}] GPS 50m match: {line.strip()}")
            
        # check QR 30s
        if re.search(r'(?:QR.*30\s*s|30\s*s.*QR|xoay.*30|30.*giây)', line, re.I):
            print(f"[{fname}:{idx+1}] QR 30s match: {line.strip()}")
            
        # check Flutter / React Native / Staff App
        if re.search(r'Flutter|React\s+Native', line, re.I):
            print(f"[{fname}:{idx+1}] Flutter/RN match: {line.strip()}")
