import os
import re
import json

DIAG_DIR = r"d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams"
SRC_DB = r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md"
SRC_API = r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md"
SRC_SPEC = r"d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md"
SRC_WF = r"d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md"

# 1. Inspect ERD Tables vs Database Design doc
print('=== 1. ANALYZING ERD TABLES ===')
with open(os.path.join(DIAG_DIR, "03_ERD_Database_Diagram.md"), "r", encoding="utf-8") as f:
    erd_content = f.read()

with open(SRC_DB, "r", encoding="utf-8") as f:
    db_content = f.read()

# Extract tables in 03_ERD_Database_Diagram.md
# Look for entity definitions in Mermaid erDiagram
# Format: TABLE_NAME { or entity TABLE_NAME {
erd_entities = re.findall(r'(\w+)\s*\{', erd_content)
# filter out non-table keywords if any
erd_tables = sorted(list(set([e for e in erd_entities if not e in ['subgraph', 'graph', 'style', 'classDef', 'class']])))

# Extract tables in 02_Thiet_Ke_Database.md
# Markdown headers like: ### 1.1. Bảng 	en_bang or ### Bảng 	en_bang or CREATE TABLE 	en_bang
db_tables = sorted(list(set(re.findall(r'Bảng\s+(\w+)', db_content))))
if not db_tables:
    db_tables = sorted(list(set(re.findall(r'###\s+\d+\.\d+\.\s+?(\w+)?', db_content))))

print(f"ERD Document found {len(erd_tables)} entities: {erd_tables}")
print(f"DB Design Document found {len(db_tables)} tables: {db_tables}")

# Check diffs
diff_erd_db = set(erd_tables) - set(db_tables)
diff_db_erd = set(db_tables) - set(erd_tables)
print(f"In ERD but not in DB doc: {diff_erd_db}")
print(f"In DB doc but not in ERD: {diff_db_erd}")

# 2. Check Business Rules in 01, 02, 03, 04
print('\n=== 2. ANALYZING BUSINESS RULES IN 4 DIAGRAM DOCS ===')
rules = {
    "WiFi Attendance (BSSID + IP Subnet)": {
        "keywords": [r"bssid", r"ssid", r"subnet", r"chấm công", r"attendance", r"wifi"],
        "files_checked": {}
    },
    "Z-Report Discrepancy (> 50,000 VND / 50k)": {
        "keywords": [r"z-report", r"z_report", r"50\.000", r"50k", r"discrepancy", r"giải trình", r"chênh lệch"],
        "files_checked": {}
    },
    "Red Alert (<= 2 stars)": {
        "keywords": [r"red alert", r"red_alert", r"2 sao", r"<= 2", r"đánh giá", r"review", r"rating"],
        "files_checked": {}
    },
    "86-Toggle KDS (Hết món / Sold Out)": {
        "keywords": [r"86-toggle", r"86 toggle", r"báo hết món", r"sold out", r"kds", r"item_86"],
        "files_checked": {}
    },
    "Shipping Fee (20,000 VND / 20k)": {
        "keywords": [r"20\.000", r"20k", r"phí ship", r"shipping_fee", r"delivery"],
        "files_checked": {}
    },
    "Loyalty Program (10 ly tặng 1)": {
        "keywords": [r"10 ly", r"tặng 1", r"loyalty", r"tích điểm", r"stamp", r"reward"],
        "files_checked": {}
    },
    "RedLock / Distributed Lock": {
        "keywords": [r"redlock", r"distributed lock", r"lock:table", r"lock:inventory", r"khóa phân tán", r"redis lock"],
        "files_checked": {}
    }
}

for rname, rinfo in rules.items():
    print(f"\nRule: {rname}")
    for fname in ["01_Kien_Truc_Tong_Quan.md", "02_Sequence_Diagrams.md", "03_ERD_Database_Diagram.md", "04_Deployment_Diagram.md"]:
        fpath = os.path.join(DIAG_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read().lower()
        matches = []
        for kw in rinfo["keywords"]:
            found = re.findall(kw, content)
            if found:
                matches.append(f"{kw}: {len(found)}")
        print(f"  {fname}: {', '.join(matches) if matches else 'NOT FOUND'}")
