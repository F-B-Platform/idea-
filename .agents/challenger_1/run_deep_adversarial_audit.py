import os
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

DIAG_DIR = r"d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams"
SRC_DB = r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md"
SRC_API = r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md"
SRC_SPEC = r"d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md"
SRC_WF = r"d:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md"

print("=================================================================")
print("  STEP 2: ERD 25 TABLES INTEGRITY & SCHEMA ALIGNMENT AUDIT       ")
print("=================================================================")

with open(os.path.join(DIAG_DIR, "03_ERD_Database_Diagram.md"), "r", encoding="utf-8") as f:
    erd_text = f.read()

with open(SRC_DB, "r", encoding="utf-8") as f:
    db_text = f.read()

# 1. Extract tables from 02_Thiet_Ke_Database.md
# Headers like: ### 1.1. Bảng users or ### 2.1. Bảng orders
db_tables_raw = re.findall(r'Bảng\s+?([a-zA-Z0-9_]+)?', db_text)
db_tables = sorted(list(set([t.lower() for t in db_tables_raw if not t in ['PostgreSQL', 'UUID', 'JSONB', 'INDEX', 'TRIGGER']])))

# 2. Extract tables from 03_ERD_Database_Diagram.md
# In mermaid erDiagram:
# TABLE_NAME {
# or in markdown descriptions
erd_entities_raw = re.findall(r'([A-Z0-9_]+)\s*\{', erd_text)
# Filter out non-table keywords
filter_out = {'SUBGRAPH', 'GRAPH', 'STYLE', 'CLASSDEF', 'CLASS', 'ENUM', 'ATTENDANCESTATUS', 'ORDERSTATUS', 'ORDERTYPE', 'PAYMENTMETHOD', 'PAYMENTSTATUS', 'TABLESTATUS', 'DISCREPANCYACTIONPLAN', 'LOYALTYTRANSACTIONTYPE', 'MODIFIERTYPE', 'SHIFTSTATUS', 'O'}
erd_entities = sorted(list(set([e.lower() for e in erd_entities_raw if e.upper() not in filter_out and not e.startswith('PK_')])))

# Also check markdown tables in 03_ERD_Database_Diagram.md
erd_md_tables = sorted(list(set([t.lower() for t in re.findall(r'###\s+\d+\.\d+\.\s+Bảng\s+?([a-zA-Z0-9_]+)?', erd_text)])))

print(f"Total tables documented in DB Design (02_Thiet_Ke_Database.md): {len(db_tables)}")
print(f"List in DB Design: {db_tables}")
print(f"\nTotal entities in ERD Mermaid diagram: {len(erd_entities)}")
print(f"List in ERD Mermaid: {erd_entities}")
print(f"\nTotal tables in ERD Markdown sections: {len(erd_md_tables)}")
print(f"List in ERD Markdown: {erd_md_tables}")

# Compare ERD vs DB Design
missing_in_erd = set(db_tables) - set(erd_entities)
extra_in_erd = set(erd_entities) - set(db_tables)
print(f"\nDiscrepancies:")
print(f"  Missing in ERD Diagram vs DB Design: {missing_in_erd}")
print(f"  Extra in ERD Diagram vs DB Design: {extra_in_erd}")

# 3. Check for specific 25 tables mapping
expected_25_tables = [
    "branches", "branch_wifi_configs", "tables", "table_qr_codes",
    "users", "roles", "permissions", "user_roles", "role_permissions", "refresh_tokens",
    "categories", "products", "product_sizes", "toppings", "product_toppings",
    "ingredients", "product_recipes", "inventory_stocks", "inventory_logs",
    "orders", "order_items", "order_item_toppings", "delivery_orders", "payments", "transactions",
    "work_shifts", "staff_attendances", "shift_handover_discrepancies",
    "customer_feedbacks", "customers", "loyalty_cup_transactions"
]
print(f"\nExpected core tables check (against system specs):")
for t in expected_25_tables:
    in_erd = t in erd_entities or t in erd_md_tables
    in_db = t in db_tables
    print(f"  - {t:32} | in ERD: {'YES' if in_erd else 'NO ':3} | in DB doc: {'YES' if in_db else 'NO ':3}")

print("\n=================================================================")
print("  STEP 3: CONCURRENCY & RACE CONDITIONS DEEP-DIVE                ")
print("=================================================================")

with open(os.path.join(DIAG_DIR, "02_Sequence_Diagrams.md"), "r", encoding="utf-8") as f:
    seq_text = f.read()

# Check Seq-01 to Seq-10 in 02_Sequence_Diagrams.md
seq_blocks = re.findall(r'##\s+(Seq-\d+[^#\n]+)', seq_text)
print(f"Found {len(seq_blocks)} Sequence Diagram Sections:")
for s in seq_blocks:
    print(f"  - {s}")

race_checks = {
    "RedLock Table Reservation (Seq-01 / Seq-02)": {
        "pattern": r"(redlock|lock:table|setnx|lock\s+acquired|distributed\s+lock)",
        "found": bool(re.search(r"(redlock|lock:table|setnx|lock\s+acquired|distributed\s+lock)", seq_text, re.I))
    },
    "Inventory Reservation / Deduction (Seq-01 / Seq-03 / Seq-04)": {
        "pattern": r"(lock:inventory|inventory_stocks|deduct|reserve|tồn kho)",
        "found": bool(re.search(r"(lock:inventory|inventory_stocks|deduct|reserve|tồn kho)", seq_text, re.I))
    },
    "Double Payment / Webhook Idempotency (Seq-01 / Seq-03 / Seq-05)": {
        "pattern": r"(idempotent|idempotency|x-idempotency-key|webhook\s+signature|transaction_id)",
        "found": bool(re.search(r"(idempotent|idempotency|x-idempotency-key|webhook\s+signature|transaction_id)", seq_text, re.I))
    },
    "Lock Release on Failure / Timeout (Finally block / Unlock)": {
        "pattern": r"(unlock|release\s+lock|del\s+lock|finally)",
        "found": bool(re.search(r"(unlock|release\s+lock|del\s+lock|finally)", seq_text, re.I))
    }
}
print("\nRace Condition & Concurrency Features in Sequence Diagrams:")
for k, v in race_checks.items():
    print(f"  [{'PASS' if v['found'] else 'FAIL'}] {k}")

print("\n=================================================================")
print("  STEP 4: BUSINESS RULES V2.5.0 AUDIT                            ")
print("=================================================================")

rules_audit = [
    ("WiFi Attendance: BSSID + Subnet IP (No GPS)", r"(bssid|allowed_bssid|bssid_list).*?(subnet|allowed_ip_subnets|ip_subnet)", [seq_text, erd_text]),
    ("Z-Report Discrepancy > 50,000 VND / 50k", r"(50\.000|50k|50000).*?(discrepancy|giải trình|chênh lệch|shift_handover)", [seq_text, erd_text]),
    ("Red Alert on Reviews <= 2 Stars", r"(red\s*alert|urgent|khẩn cấp).*?(2\s*sao|2\s*star|<= 2|rating.*?[12])", [seq_text, erd_text]),
    ("86-Toggle on KDS (Out of stock broadcast)", r"(86-toggle|item86toggled|toggle86|báo hết món).*?(kds|signalr|websocket|orderhub)", [seq_text, erd_text]),
    ("Shipping Fee Flat 20,000 VND (<= 5km)", r"(20\.000|20k|20000).*?(phí ship|delivery_fee|shipping)", [seq_text, erd_text]),
    ("Loyalty: 10 Cups -> 1 Reward Cup", r"(10\s*ly|10\s*cups|10\s*stamps).*?(tặng 1|miễn phí|1\s*ly|loyalty_cup)", [seq_text, erd_text])
]

for name, pattern, doc_list in rules_audit:
    matched = False
    for doc in doc_list:
        if re.search(pattern, doc, re.I | re.DOTALL):
            matched = True
            break
    print(f"  [{'PASS' if matched else 'FAIL'}] {name}")

print("\n=================================================================")
print("  STEP 5: SCAN FOR PLACEHOLDERS AND OBSOLETE KEYWORDS            ")
print("=================================================================")

obsolete_keywords = [
    r"staff mobile app", r"staff app", r"gps 50m", r"gps lock", r"qr động 30 giây",
    r"yêu cầu bill", r"thanh toán sau"
]
placeholders = [r"\btodo\b", r"\btbd\b", r"\[tbd\]", r"/\* rest of code \*/", r"// tương tự"]

for fname in ["01_Kien_Truc_Tong_Quan.md", "02_Sequence_Diagrams.md", "03_ERD_Database_Diagram.md", "04_Deployment_Diagram.md"]:
    fpath = os.path.join(DIAG_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        c = f.read()
    
    obs_found = []
    for ob in obsolete_keywords:
        m = re.findall(ob, c, re.I)
        if m:
            obs_found.append(f"{ob} ({len(m)})")
            
    pl_found = []
    for pl in placeholders:
        m = re.findall(pl, c, re.I)
        if m:
            pl_found.append(f"{pl} ({len(m)})")
            
    print(f"File {fname}:")
    print(f"  Obsolete keywords: {', '.join(obs_found) if obs_found else 'NONE (Clean)'}")
    print(f"  Placeholders: {', '.join(pl_found) if pl_found else 'NONE (Clean)'}")
