import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

docs_dir = r'd:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc'
files = [
    'Smart_FB_Operating_System.md',
    'Actor_Phan_Quyen_Chuc_Nang.md',
    'Workflow_Quy_Trinh_Nghiep_Vu.md',
    'Tong_Quan_Kien_Truc_He_Thong.md',
    'Tom_Tat_1_Trang_Executive_Summary.md'
]

for f in files:
    path = os.path.join(docs_dir, f)
    with open(path, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    print(f"\n==================================================")
    print(f"FILE: {f} ({len(lines)} lines)")
    print(f"==================================================")
    headings = [l.strip() for l in lines if l.startswith('#')]
    for h in headings[:25]:
        print(f"  {h}")
    if len(headings) > 25:
        print(f"  ... ({len(headings)-25} more headings)")
