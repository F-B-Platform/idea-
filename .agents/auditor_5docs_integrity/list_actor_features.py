import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

path = r'd:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Actor_Phan_Quyen_Chuc_Nang.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

categories = {
    'Customer (C-)': r'####\s*(C-\d{2}):\s*([^\n]+)',
    'Staff (S-)': r'####\s*(S-\d{2}):\s*([^\n]+)',
    'Manager (M-)': r'####\s*(M-\d{2}):\s*([^\n]+)',
    'Admin (A-)': r'####\s*(A-\d{2}):\s*([^\n]+)'
}

for cat_name, pat in categories.items():
    feats = re.findall(pat, text)
    print(f"\n=== {cat_name} : {len(feats)} features ===")
    for code, name in feats:
        print(f"  {code}: {name.strip()}")
