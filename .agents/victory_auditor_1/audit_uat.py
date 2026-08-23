import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

filepath = r"d:\Idea_DoAn\05_Quy_Chuan_&_Test_Cases\UAT_Test_Cases.md"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

print("=== AUDIT UAT_Test_Cases.md ===")
print(f"Total characters: {len(content):,}")
print(f"Total lines: {len(content.splitlines()):,}")

# 1. Check Demo Scenario
print("\n--- 1. 5-Minute Demo Scenario Check ---")
demo_keywords = [
    ("Dine-In Nhánh A", r"Nhánh A.*Trả trước.*VietQR|Dine-In.*Nhánh A|TC-DINE-01A"),
    ("Dine-In Nhánh B", r"Nhánh B.*Trả sau.*Tiền mặt|Dine-In.*Nhánh B|TC-DINE-01B"),
    ("Delivery Phí Ship 20k", r"20\.000|20k.*ship|phí giao hàng.*20"),
    ("Takeaway Tích 10 ly", r"10 ly|tích điểm|tặng 1 ly|Takeaway"),
    ("Chấm công WiFi BSSID/IP", r"WiFi|BSSID|IP|Chấm công"),
    ("KDS Barista BOM & 86-Toggle", r"BOM|86-Toggle|Undo 10s|định lượng"),
    ("Quản lý Z-Report chênh lệch 50k", r"Z-Report|50\.000|chênh lệch"),
    ("Admin AI-2 Combo Apriori", r"AI-2|Combo|Apriori|menu theo mùa|giá theo vùng"),
]

for name, pat in demo_keywords:
    m = re.search(pat, content, re.IGNORECASE)
    print(f"  [{'PASS' if m else 'FAIL'}] {name}: {'Found match' if m else 'Not found'}")

# 2. Extract Test Cases
print("\n--- 2. Test Case Extraction & Counting ---")
tc_pattern = r"(TC-[A-Z0-9_\-]+)"
found_tcs = list(dict.fromkeys(re.findall(tc_pattern, content)))
print(f"Total Unique TC Codes found: {len(found_tcs)}")
print("Test Case Codes:")
for i in range(0, len(found_tcs), 6):
    print("  " + ", ".join(found_tcs[i:i+6]))

required_tcs = [
    "TC-DINE-01A", "TC-DINE-01B", "TC-DEL-01", "TC-TAKE-01",
    "TC-ATT-01", "TC-KDS-01", "TC-MGR-01", "TC-ADM-01",
    "TC-EDGE-01", "TC-EDGE-02", "TC-EDGE-03", "TC-EDGE-04", "TC-EDGE-05",
    "TC-EDGE-06", "TC-EDGE-07", "TC-EDGE-08", "TC-EDGE-09", "TC-EDGE-10"
]

print("\n--- 3. Required Test Cases Verification ---")
missing_req = []
for req in required_tcs:
    if req in found_tcs:
        print(f"  [PASS] {req} present")
    else:
        print(f"  [FAIL] {req} MISSING")
        missing_req.append(req)

# 4. Check Test Case Structure (Headers / Columns)
print("\n--- 4. Test Case Table Structure Check ---")
tables = re.findall(r"(\|.+?\|\n\|[\s\-:|]+\|\n(?:\|.+?\|\n?)+)", content)
print(f"Total Markdown tables found: {len(tables)}")

# Check required fields in TC tables
tc_sections = re.findall(r"(###\s+(?:TC-[A-Z0-9_\-]+|Mã\s+Test:?\s*(?:TC-[A-Z0-9_\-]+)).*?)(?=(?:###\s+(?:TC-|Mã\s+Test)|\Z))", content, re.DOTALL)
print(f"Detailed TC blocks parsed: {len(tc_sections)}")

fields_to_check = ["Mục đích", "Tiền điều kiện", "Các bước", "Dữ liệu", "Kết quả kỳ vọng", "Trạng thái"]
print("Field completeness scan in TC sections:")
incomplete_blocks = 0
for idx, sec in enumerate(tc_sections):
    missing_fields = [f for f in fields_to_check if f.lower() not in sec.lower()]
    if missing_fields:
        header = sec.splitlines()[0]
        print(f"  [WARN] {header} missing: {missing_fields}")
        incomplete_blocks += 1

if incomplete_blocks == 0:
    print("  [PASS] All parsed TC blocks contain standard required metadata fields!")
