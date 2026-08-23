import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

f1_path = r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\01_Phan_Tich_Yeu_Cau.md"
f2_path = r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md"

with open(f1_path, "r", encoding="utf-8") as f:
    f1_text = f.read()

with open(f2_path, "r", encoding="utf-8") as f:
    f2_text = f.read()

print(f"File 1 length: {len(f1_text)} chars, {len(f1_text.splitlines())} lines")
print(f"File 2 length: {len(f2_text)} chars, {len(f2_text.splitlines())} lines")

# 1. Check Feature Coverage
expected_features = []
for i in range(1, 21):
    expected_features.append(f"C-{i:02d}")
for i in range(1, 14):
    expected_features.append(f"S-{i:02d}")
for i in range(1, 13):
    expected_features.append(f"M-{i:02d}")
for i in range(1, 18):
    expected_features.append(f"A-{i:02d}")

print(f"\nTotal expected features: {len(expected_features)} (should be 62)")

missing_features = []
feature_sections = {}
for feat in expected_features:
    # Pattern: ### C-01: or ### C-01 -
    pat = rf"###\s+{feat}[:\s\-]"
    m = re.search(pat, f1_text)
    if not m:
        missing_features.append(feat)
    else:
        feature_sections[feat] = m.start()

if missing_features:
    print(f"❌ MISSING FEATURES: {missing_features}")
else:
    print("✅ All 62 features found in 01_Phan_Tich_Yeu_Cau.md")

# 2. Check each feature structure (5 sub-sections)
subsections = [
    "Mô tả",
    "Quy tắc & Ràng buộc",
    "Hợp đồng dữ liệu",
    "Kịch bản biên & Xử lý ngoại lệ",
    "Tiêu chí nghiệm thu định lượng"
]

incomplete_features = []
# Sort features by position in file
sorted_feats = sorted(feature_sections.keys(), key=lambda k: feature_sections[k])
for i, feat in enumerate(sorted_feats):
    start = feature_sections[feat]
    end = feature_sections[sorted_feats[i+1]] if i+1 < len(sorted_feats) else start + 10000
    section_content = f1_text[start:end]
    
    missing_subs = []
    for sub in subsections:
        if sub.lower() not in section_content.lower():
            missing_subs.append(sub)
    if missing_subs:
        incomplete_features.append((feat, missing_subs))

if incomplete_features:
    print(f"❌ INCOMPLETE FEATURES: {incomplete_features}")
else:
    print("✅ All 62 features have all 5 standardized sub-sections!")

# 3. Check Banned Items
banned_patterns = [
    r"\bC-23\b",
    r"\bC-24\b",
    r"Flutter",
    r"React Native",
    r"\bGPS\b",
    r"50m",
    r"50 mét",
    r"QR 30s",
    r"30 giây",
    r"xoay vòng 30",
    r"ví voucher",
    r"tra cứu calo riêng",
]

print("\n--- Banned Items Scan ---")
for bp in banned_patterns:
    m1 = re.findall(bp, f1_text, re.IGNORECASE)
    m2 = re.findall(bp, f2_text, re.IGNORECASE)
    if m1 or m2:
        print(f"⚠️ Found match for banned pattern '{bp}': f1={len(m1)}, f2={len(m2)}")
        # Print context
        for match in re.finditer(bp, f1_text, re.IGNORECASE):
            s = max(0, match.start() - 50)
            e = min(len(f1_text), match.end() + 50)
            print(f"   In f1: ...{f1_text[s:e]}...")
        for match in re.finditer(bp, f2_text, re.IGNORECASE):
            s = max(0, match.start() - 50)
            e = min(len(f2_text), match.end() + 50)
            print(f"   In f2: ...{f2_text[s:e]}...")
    else:
        print(f"✅ Clean: No '{bp}' found")

# 4. Check Placeholders
placeholder_patterns = [
    r"\bTODO\b",
    r"\bTBD\b",
    r"/\*\s*rest of code\s*\*/",
    r"//\s*tương tự",
    r"//\s*giữ nguyên",
    r"\.\.\.\s*còn tiếp",
]
print("\n--- Placeholder Scan ---")
for pp in placeholder_patterns:
    m1 = re.findall(pp, f1_text, re.IGNORECASE)
    m2 = re.findall(pp, f2_text, re.IGNORECASE)
    if m1 or m2:
        print(f"❌ Found placeholder '{pp}': f1={len(m1)}, f2={len(m2)}")
    else:
        print(f"✅ Clean: No '{pp}' found")

# 5. Check Database Tables in 02_
create_table_matches = re.findall(r"CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?([a-zA-Z0-9_]+)", f2_text, re.IGNORECASE)
print(f"\n--- Database Tables ({len(create_table_matches)} found) ---")
for t in create_table_matches:
    print(f"  - {t}")

expected_25_tables = [
    "branches", "branch_wifi_configs", "users", "roles", "user_roles", "audit_logs",
    "categories", "products", "product_sizes", "product_branch_prices", "modifiers",
    "product_modifiers", "ingredients", "recipes_bom", "tables", "orders", "order_items",
    "order_item_modifiers", "payments", "customers", "loyalty_cup_transactions", "vouchers",
    "customer_reviews", "shifts", "attendances"
]

missing_tables = [t for t in expected_25_tables if t.lower() not in [x.lower() for x in create_table_matches]]
extra_tables = [t for t in create_table_matches if t.lower() not in [x.lower() for x in expected_25_tables]]

print(f"Expected: {len(expected_25_tables)} tables")
print(f"Missing tables: {missing_tables}")
print(f"Extra tables: {extra_tables}")

