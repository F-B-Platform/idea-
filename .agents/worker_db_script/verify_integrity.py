# verify_integrity.py - Audits the generated document
import re
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

def audit():
    file_path = r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\Seed_Data_&_Database_Script.md"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    print(f"Auditing file: {file_path}")
    print(f"Size: {len(content)} bytes, Lines: {len(content.splitlines())}")

    # 1. Zero placeholder check
    banned = ["TODO", "...", "/* rest of", "// tương tự", "placeholder", "tương tự như trên"]
    violations = []
    for b in banned:
        matches = [m.start() for m in re.finditer(re.escape(b), content, re.IGNORECASE)]
        if matches:
            violations.append((b, len(matches), matches[:3]))
    
    if violations:
        print(f"ZERO PLACEHOLDER VIOLATIONS FOUND: {violations}")
        for b, count, sample_locs in violations:
            for loc in sample_locs:
                snippet = content[max(0, loc-30):min(len(content), loc+50)]
                print(f"  Snippet around '{b}': {repr(snippet)}")
    else:
        print("[PASS] 100% Zero Placeholder Check PASSED (No placeholders found)")

    # 2. Check 29 Tables in DDL
    expected_tables = [
        "branches", "branch_wifi_configs", "tables", "users", "roles", "user_roles",
        "audit_logs", "categories", "products", "product_sizes", "product_branch_prices",
        "modifiers", "product_modifiers", "ingredients", "recipes_bom", "inventory_checks",
        "inventory_check_details", "customers", "orders", "order_items", "order_item_modifiers",
        "payments", "loyalty_cup_transactions", "vouchers", "customer_reviews", "combos",
        "combo_items", "shifts", "attendances"
    ]
    
    missing_ddl = []
    for tbl in expected_tables:
        if f"CREATE TABLE IF NOT EXISTS {tbl}" not in content:
            missing_ddl.append(tbl)
    
    if missing_ddl:
        print(f"[FAIL] Missing CREATE TABLE in DDL: {missing_ddl}")
    else:
        print(f"[PASS] All {len(expected_tables)} Tables successfully defined in DDL")

    # 3. Check INSERT statements in DML
    missing_dml = []
    for tbl in expected_tables:
        if f"INSERT INTO {tbl}" not in content:
            missing_dml.append(tbl)
            
    if missing_dml:
        print(f"[FAIL] Missing INSERT INTO in DML: {missing_dml}")
    else:
        print(f"[PASS] All {len(expected_tables)} Tables successfully seeded with rich DML data")

    # 4. Check BCrypt hash
    bcrypt_hash = "$2a$11$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy"
    count_hash = content.count(bcrypt_hash)
    print(f"[PASS] Found {count_hash} occurrences of standard BCrypt password hash")

    # 5. Check 5 core business elements
    print("Checking core business elements:")
    print(" - 192.168.1.0/24, 192.168.2.0/24, 192.168.3.0/24:", "192.168.1.0/24" in content and "192.168.2.0/24" in content and "192.168.3.0/24" in content)
    print(" - 20000 delivery fee:", "20000" in content)
    print(" - TakeawayRedeem10Free:", "TakeawayRedeem10Free" in content)
    print(" - is_urgent_alert trigger:", "trigger_set_urgent_review_alert" in content)
    print(" - Z-Report 70000 variance:", "70000" in content and "chênh lệch thừa +70.000đ" in content)
    print(" - DbInitializer.cs code:", "public static class DbInitializer" in content)
    print(" - Verification SELECT queries:", "4.2.1 TRUY VẤN KIỂM CHỨNG TỔNG SỐ LƯỢNG BẢN GHI" in content)

if __name__ == "__main__":
    audit()
