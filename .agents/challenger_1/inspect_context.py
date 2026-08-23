import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

DIAG_DIR = r"d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams"
SRC_DB = r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md"

print("=== 1. CHECKING OBSOLETE KEYWORD CONTEXT ===")
for fname in ["01_Kien_Truc_Tong_Quan.md", "02_Sequence_Diagrams.md"]:
    fpath = os.path.join(DIAG_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for idx, l in enumerate(lines):
        for kw in ["staff mobile app", "staff app", "gps 50m", "gps lock", "qr động 30 giây", "yêu cầu bill", "thanh toán sau"]:
            if re.search(kw, l, re.I):
                print(f"[{fname}:{idx+1}] Keyword '{kw}':\n  {l.strip()}\n")

print("=== 2. PARSING TABLES IN 02_Thiet_Ke_Database.md ===")
with open(SRC_DB, "r", encoding="utf-8") as f:
    db_lines = f.readlines()

for idx, l in enumerate(db_lines):
    if l.startswith("### ") or l.startswith("## "):
        if any(w in l.lower() for w in ["bảng", "table", "schema"]):
            print(f"L{idx+1}: {l.strip()}")

print("\n=== 3. PARSING HEADINGS IN 02_Sequence_Diagrams.md ===")
with open(os.path.join(DIAG_DIR, "02_Sequence_Diagrams.md"), "r", encoding="utf-8") as f:
    seq_lines = f.readlines()

for idx, l in enumerate(seq_lines):
    if l.startswith("#"):
        print(f"L{idx+1}: {l.strip()}")