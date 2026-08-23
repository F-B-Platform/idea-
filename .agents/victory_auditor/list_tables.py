import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

DOCS_DIR = r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai"
with open(os.path.join(DOCS_DIR, "02_Thiet_Ke_Database.md"), "r", encoding="utf-8") as f:
    doc2 = f.read()

tables = re.findall(r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?([a-zA-Z0-9_]+)', doc2, re.I)
print(f"Total tables: {len(tables)}")
for i, t in enumerate(tables):
    print(f"{i+1}: {t}")
