import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

DOCS_DIR = r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai"

# Inspect Database tables
with open(os.path.join(DOCS_DIR, "02_Thiet_Ke_Database.md"), "r", encoding="utf-8") as f:
    doc2 = f.read()

print("--- TABLES IN 02_Thiet_Ke_Database.md ---")
tables = re.findall(r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?([a-zA-Z0-9_]+)', doc2, re.I)
for idx, t in enumerate(tables):
    print(f"{idx+1}. {t}")

print("\n--- ORDERS TABLE COLUMNS ---")
orders_match = re.search(r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?orders\s*\((.*?)\);', doc2, re.DOTALL | re.I)
if orders_match:
    print(orders_match.group(1))

print("\n--- ATTENDANCE / USERS / WIFI COLUMNS ---")
att_match = re.search(r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?(?:attendances|branch_wifi_configs|users)\s*\((.*?)\);', doc2, re.DOTALL | re.I)
for m in re.finditer(r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?([a-zA-Z0-9_]+)\s*\((.*?)\);', doc2, re.DOTALL | re.I):
    tbl_name = m.group(1)
    if tbl_name in ["attendances", "branch_wifi_configs", "users", "shifts", "work_shifts"]:
        print(f"Table {tbl_name}:\n{m.group(2)}\n")

# Inspect Edge Cases in 07_Ke_Hoach_Kiem_Thu.md
with open(os.path.join(DOCS_DIR, "07_Ke_Hoach_Kiem_Thu.md"), "r", encoding="utf-8") as f:
    doc7 = f.read()

print("--- EDGE CASES IN 07_Ke_Hoach_Kiem_Thu.md ---")
for line in doc7.splitlines():
    if "edge" in line.lower() or "kịch bản" in line.lower() or "biên" in line.lower() or "ec-" in line.lower():
        print(line)
