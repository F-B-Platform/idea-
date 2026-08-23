import os
import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"d:\Idea_DoAn"
UAT_PATH = os.path.join(BASE_DIR, "05_Quy_Chuan_&_Test_Cases", "UAT_Test_Cases.md")

with open(UAT_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Pattern for test cases: #### `TC-XXX-YY`: Title
tc_blocks = re.findall(r"(####\s+`?(TC-[A-Za-z0-9_\-]+)`?:\s*([^\n]+)\n(.*?))(?=(?:####\s+`?TC-|\Z|###\s+5\.))", content, re.DOTALL)

print(f"Total test case sections parsed: {len(tc_blocks)}")

expected_keys = [
    "TC-DINE-01A", "TC-DINE-01B", "TC-DEL-01", "TC-TAKE-01",
    "TC-ATT-01", "TC-KDS-01", "TC-MGR-01", "TC-ADM-01"
]
for i in range(1, 11):
    expected_keys.append(f"TC-EDGE-{i:02d}")

found_tc_ids = []
for full_block, tc_id, title, body in tc_blocks:
    found_tc_ids.append(tc_id)
    # Check fields
    has_muc_dich = "- **Mục đích:**" in body
    has_tien_dieu_kien = "- **Tiền điều kiện:**" in body
    has_cac_buoc = "- **Các bước thực hiện:**" in body
    has_du_lieu = "- **Dữ liệu đầu vào" in body
    has_ky_vong = "- **Kết quả kỳ vọng" in body
    has_tieu_chi = "- **Tiêu chí nghiệm thu" in body or "- **Trạng thái" in body
    
    missing = []
    if not has_muc_dich: missing.append("Mục đích")
    if not has_tien_dieu_kien: missing.append("Tiền điều kiện")
    if not has_cac_buoc: missing.append("Các bước")
    if not has_du_lieu: missing.append("Dữ liệu đầu vào")
    if not has_ky_vong: missing.append("Kết quả kỳ vọng")
    if not has_tieu_chi: missing.append("Tiêu chí nghiệm thu")
    
    if missing:
        print(f"TC {tc_id} missing: {missing}")

print("\nList of all found Test Cases:")
for idx, tc in enumerate(found_tc_ids, 1):
    print(f"{idx:02d}. {tc}")

print("\nChecking expected core test cases:")
for exp in expected_keys:
    status = "FOUND" if exp in found_tc_ids else "MISSING"
    print(f"  {exp}: {status}")

# Check 5-minute Demo continuous scenario
has_demo = "CHƯƠNG 2: KỊCH BẢN DEMO 5 PHÚT KẾT NỐI LIÊN HOÀN" in content
print(f"\n5-minute Continuous Demo Scenario Present: {has_demo}")
