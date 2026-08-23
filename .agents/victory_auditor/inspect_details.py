import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

DOCS_DIR = r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai"

with open(os.path.join(DOCS_DIR, "02_Thiet_Ke_Database.md"), "r", encoding="utf-8") as f:
    doc2 = f.read()

with open(os.path.join(DOCS_DIR, "03_Thiet_Ke_API_Contract.md"), "r", encoding="utf-8") as f:
    doc3 = f.read()

with open(os.path.join(DOCS_DIR, "05_Quy_Trinh_Backend.md"), "r", encoding="utf-8") as f:
    doc5 = f.read()

with open(os.path.join(DOCS_DIR, "06_Quy_Trinh_Frontend.md"), "r", encoding="utf-8") as f:
    doc6 = f.read()

# 1. Inspect DB primary keys for all 25 tables
print("=== 1. PRIMARY KEYS OF ALL 25 TABLES IN 02_Thiet_Ke_Database.md ===")
for m in re.finditer(r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?([a-zA-Z0-9_]+)\s*\((.*?)\);', doc2, re.DOTALL | re.I):
    tbl_name = m.group(1)
    body = m.group(2)
    pk = re.search(r'PRIMARY\s+KEY[^\n,]*', body, re.I)
    pk_str = pk.group(0) if pk else "NO PK FOUND"
    print(f"Table [{tbl_name:<25}]: {pk_str}")

# 2. Inspect Attendance endpoint in 03_Thiet_Ke_API_Contract.md
print("\n=== 2. ATTENDANCE ENDPOINTS IN 03_Thiet_Ke_API_Contract.md ===")
for line in doc3.splitlines():
    if "/api/v1/attendances" in line or "/api/v1/attendance" in line or "check-in" in line.lower():
        print(line)

# 3. Inspect Backend Layers & RedLock in 05_Quy_Trinh_Backend.md
print("\n=== 3. BACKEND LAYERS & REDLOCK IN 05_Quy_Trinh_Backend.md ===")
for layer in ["Domain", "Application", "Infrastructure", "WebApi", "Presentation", "Api"]:
    print(f"Layer [{layer}]: {layer in doc5}")
print("RedLock occurrences:", len(re.findall(r'RedLock|distributed.*lock', doc5, re.I)))
for line in doc5.splitlines():
    if "redlock" in line.lower() or "distributed lock" in line.lower() or "khóa phân tán" in line.lower():
        print("  Line:", line.strip())

# 4. Inspect Zustand Stores in 06_Quy_Trinh_Frontend.md
print("\n=== 4. ZUSTAND STORES IN 06_Quy_Trinh_Frontend.md ===")
stores = re.findall(r'use[A-Z0-9_]+Store', doc6)
print("Found stores:", set(stores))
