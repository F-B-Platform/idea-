import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
p = r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md"
with open(p, "r", encoding="utf-8", errors="ignore") as fp:
    c = fp.read()
tables = re.findall(r'CREATE TABLE (?:IF NOT EXISTS )?"?([a-zA-Z0-9_]+)"?', c, re.IGNORECASE)
print(f"Total tables in 02_Thiet_Ke_Database.md: {len(tables)}")
for i, t in enumerate(tables, 1):
    print(f" {i:2}. {t}")
