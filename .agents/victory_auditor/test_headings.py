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
    fpath = os.path.join(DOCS_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Strip fenced code blocks
    content_no_code = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
    
    # Check for empty headings in markdown (headings with no content before next heading)
    empty_headings = re.findall(r'(^#{1,4}\s+[^\n]+)\n+(?=#{1,4}\s+)', content_no_code, re.MULTILINE)
    if empty_headings:
        print(f"[{fname}] Found genuine empty headings: {empty_headings}")
    else:
        print(f"[{fname}] All markdown headings have non-empty content! PASS")
