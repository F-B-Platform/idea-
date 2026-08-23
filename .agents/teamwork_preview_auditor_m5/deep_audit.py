import os
import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

TARGET_DIR = r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai"

def read_file(filename):
    path = os.path.join(TARGET_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def audit_features():
    print("=== CHECK 1: 62 FEATURES AUDIT ===")
    req_text = read_file("01_Phan_Tich_Yeu_Cau.md")
    readme_text = read_file("README.md")
    ui_text = read_file("04_Thiet_Ke_UI_UX.md")

    customer_feats = [f"C-{i:02d}" for i in range(1, 21)]
    staff_feats = [f"S-{i:02d}" for i in range(1, 14)]
    manager_feats = [f"M-{i:02d}" for i in range(1, 13)]
    admin_feats = [f"A-{i:02d}" for i in range(1, 18)]
    all_feats = customer_feats + staff_feats + manager_feats + admin_feats

    print(f"Total expected features: {len(all_feats)} (20 Customer + 13 Staff + 12 Manager + 17 Admin)")

    missing_in_req = []
    missing_in_readme = []
    missing_in_ui = []

    for f in all_feats:
        if f not in req_text:
            missing_in_req.append(f)
        if f not in readme_text:
            missing_in_readme.append(f)
        if f not in ui_text:
            missing_in_ui.append(f)

    print(f"Missing in 01_Phan_Tich_Yeu_Cau.md: {missing_in_req}")
    print(f"Missing in README.md (Traceability Matrix): {missing_in_readme}")
    print(f"Missing in 04_Thiet_Ke_UI_UX.md (Traceability Matrix): {missing_in_ui}")

    # Check for legacy features C-21, C-22, C-23, C-24, C-25 in active feature lists
    active_legacy = re.findall(r"###\s+(?:Tính năng\s+)?(C-2[1-9]|C-[3-9]\d)", req_text)
    print(f"Active legacy Customer features in 01_: {active_legacy}")

    return {
        "total": len(all_feats),
        "missing_req": missing_in_req,
        "missing_readme": missing_in_readme,
        "missing_ui": missing_in_ui,
        "active_legacy": active_legacy
    }

def audit_database():
    print("\n=== CHECK 2: DATABASE AUDIT (02_Thiet_Ke_Database.md) ===")
    db_text = read_file("02_Thiet_Ke_Database.md")

    # Find table definitions: CREATE TABLE or Markdown table sections
    table_matches = re.findall(r"CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?([a-zA-Z0-9_]+)", db_text, re.IGNORECASE)
    unique_tables = sorted(list(set(table_matches)))
    print(f"Identified {len(unique_tables)} tables in DDL:")
    for t in unique_tables:
        print(f"  - {t}")

    # Check key columns and business tables
    checks = {
        "Orders has delivery_fee": bool(re.search(r"delivery_fee", db_text, re.IGNORECASE)),
        "Orders has delivery_address": bool(re.search(r"delivery_address", db_text, re.IGNORECASE)),
        "Orders has order_type": bool(re.search(r"order_type", db_text, re.IGNORECASE)),
        "BranchWifiConfigs has bssid": bool(re.search(r"bssid", db_text, re.IGNORECASE)),
        "BranchWifiConfigs has ip_subnet / subnet": bool(re.search(r"subnet|ip_range", db_text, re.IGNORECASE)),
        "LoyaltyCupTransactions table": "LoyaltyCupTransactions".lower() in [t.lower() for t in unique_tables] or "loyalty_cup_transactions" in [t.lower() for t in unique_tables],
        "ProductBOMs table": "ProductBOMs".lower() in [t.lower() for t in unique_tables] or "product_boms" in [t.lower() for t in unique_tables],
        "Ingredients table": "Ingredients".lower() in [t.lower() for t in unique_tables] or "ingredients" in [t.lower() for t in unique_tables],
        "InventoryTransactions table": "InventoryTransactions".lower() in [t.lower() for t in unique_tables] or "inventory_transactions" in [t.lower() for t in unique_tables],
        "CashShifts table": "CashShifts".lower() in [t.lower() for t in unique_tables] or "cash_shifts" in [t.lower() for t in unique_tables],
        "ZReports table": "ZReports".lower() in [t.lower() for t in unique_tables] or "z_reports" in [t.lower() for t in unique_tables] or "zreports" in [t.lower() for t in unique_tables],
    }

    for k, v in checks.items():
        print(f"  {k}: {'PASS' if v else 'FAIL'}")

    return {
        "table_count": len(unique_tables),
        "tables": unique_tables,
        "checks": checks
    }

def audit_api():
    print("\n=== CHECK 3: API CONTRACT AUDIT (03_Thiet_Ke_API_Contract.md) ===")
    api_text = read_file("03_Thiet_Ke_API_Contract.md")

    # Check 10 API Groups
    api_groups = [
        "Auth", "Branch", "Product", "Order", "Payment",
        "Attendance", "KDS", "Inventory", "Shift", "Analytics"
    ]
    found_groups = {}
    for g in api_groups:
        match = re.search(rf"{g}", api_text, re.IGNORECASE)
        found_groups[g] = bool(match)
        print(f"  Group '{g}': {'PASS' if bool(match) else 'FAIL'}")

    # Check key endpoints
    key_endpoints = [
        r"/api/v1/auth",
        r"/api/v1/branches",
        r"/api/v1/tables",
        r"/api/v1/products",
        r"/api/v1/orders",
        r"/api/v1/payments",
        r"/api/v1/attendance",
        r"/api/v1/kds",
        r"/api/v1/inventory",
        r"/api/v1/shifts",
    ]
    print("Key Endpoints:")
    for ep in key_endpoints:
        has_ep = bool(re.search(ep, api_text))
        print(f"  {ep}: {'PASS' if has_ep else 'FAIL'}")

    return {"groups": found_groups}

def audit_ui_ux():
    print("\n=== CHECK 4: UI/UX DESIGN SYSTEM AUDIT (04_Thiet_Ke_UI_UX.md) ===")
    ui_text = read_file("04_Thiet_Ke_UI_UX.md")

    routes = ["(customer)", "(kds)", "(staff)", "(manager)", "(admin)"]
    for r in routes:
        found = r in ui_text
        print(f"  Route Group '{r}': {'PASS' if found else 'FAIL'}")

    # Check Design Tokens
    has_tokens = "Design Tokens" in ui_text or "design token" in ui_text.lower()
    print(f"  Design Tokens present: {'PASS' if has_tokens else 'FAIL'}")

    # Check Web POS and KDS
    has_pos = "POS" in ui_text
    has_kds = "KDS" in ui_text
    print(f"  Web POS present: {'PASS' if has_pos else 'FAIL'}")
    print(f"  Web KDS present: {'PASS' if has_kds else 'FAIL'}")

def audit_backend():
    print("\n=== CHECK 5: BACKEND PROCESS AUDIT (05_Quy_Trinh_Backend.md) ===")
    be_text = read_file("05_Quy_Trinh_Backend.md")

    arch_elements = [
        "Clean Architecture", "Domain", "Application", "Infrastructure", "WebApi",
        "MediatR", "FluentValidation", "Entity Framework", "Redis", "SignalR",
        "PayOS", "Gemini", "Apriori"
    ]
    for el in arch_elements:
        found = el.lower() in be_text.lower()
        print(f"  Architecture component '{el}': {'PASS' if found else 'FAIL'}")

    # Check Hubs
    hubs = ["OrderHub", "KitchenHub", "PaymentHub", "NotificationHub"]
    for h in hubs:
        found = h.lower() in be_text.lower()
        print(f"  SignalR Hub '{h}': {'PASS' if found else 'FAIL'}")

def audit_frontend():
    print("\n=== CHECK 6: FRONTEND PROCESS AUDIT (06_Quy_Trinh_Frontend.md) ===")
    fe_text = read_file("06_Quy_Trinh_Frontend.md")

    fe_elements = [
        "Next.js 14", "App Router", "TypeScript", "Tailwind", "Shadcn",
        "Zustand", "TanStack Query", "SignalR", "Service Worker"
    ]
    for el in fe_elements:
        found = el.lower() in fe_text.lower()
        print(f"  Frontend component '{el}': {'PASS' if found else 'FAIL'}")

    # Check Zustand stores
    stores = ["Cart", "POS", "KDS", "Shift", "Auth"]
    for s in stores:
        found = s.lower() in fe_text.lower()
        print(f"  Zustand Store '{s}': {'PASS' if found else 'FAIL'}")

def audit_testing():
    print("\n=== CHECK 7: TESTING PLAN AUDIT (07_Ke_Hoach_Kiem_Thu.md) ===")
    test_text = read_file("07_Ke_Hoach_Kiem_Thu.md")

    test_elements = [
        "Unit Test", "Integration Test", "UAT", "Dine-In", "Delivery", "Takeaway",
        "SignalR", "Edge Case"
    ]
    for el in test_elements:
        found = el.lower() in test_text.lower()
        print(f"  Testing area '{el}': {'PASS' if found else 'FAIL'}")

def audit_devops():
    print("\n=== CHECK 8: DEVOPS & DEPLOYMENT AUDIT (08_Trien_Khai_He_Thong.md) ===")
    ops_text = read_file("08_Trien_Khai_He_Thong.md")

    ops_elements = [
        "Docker Compose", "PostgreSQL", "Redis", "NGINX", "SSL", "Let's Encrypt",
        "GitHub Actions", "CI/CD"
    ]
    for el in ops_elements:
        found = el.lower() in ops_text.lower()
        print(f"  DevOps component '{el}': {'PASS' if found else 'FAIL'}")

def audit_core_business_engines():
    print("\n=== CHECK 9: 4 CORE BUSINESS ENGINES CONSISTENCY ACROSS ALL 9 FILES ===")
    files_to_check = [
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

    for fname in files_to_check:
        txt = read_file(fname)
        dinein = "Dine-In" in txt or "dine_in" in txt.lower() or "tại bàn" in txt.lower()
        delivery = "20" in txt and ("delivery" in txt.lower() or "giao hàng" in txt.lower())
        takeaway = "Takeaway" in txt or "mang về" in txt.lower()
        wifi = "WiFi" in txt or "BSSID" in txt or "bssid" in txt

        print(f"File {fname:30}: Dine-In={dinein} | Delivery(20k)={delivery} | Takeaway={takeaway} | WiFi Attendance={wifi}")

if __name__ == "__main__":
    audit_features()
    audit_database()
    audit_api()
    audit_ui_ux()
    audit_backend()
    audit_frontend()
    audit_testing()
    audit_devops()
    audit_core_business_engines()
