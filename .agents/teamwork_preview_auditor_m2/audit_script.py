# -*- coding: utf-8 -*-
import sys
import os
import io
import re
from collections import Counter

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

api_file = r'd:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md'
ui_file = r'd:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\04_Thiet_Ke_UI_UX.md'

print("=" * 80)
print("FORENSIC INTEGRITY AUDIT - MILESTONE M2")
print("=" * 80)

# Check existence
for f in [api_file, ui_file]:
    if not os.path.exists(f):
        print(f"ERROR: File not found: {f}")
        sys.exit(1)

with open(api_file, 'r', encoding='utf-8') as f:
    api_text = f.read()

with open(ui_file, 'r', encoding='utf-8') as f:
    ui_text = f.read()

print(f"03_Thiet_Ke_API_Contract.md: {len(api_text)} chars, {len(api_text.splitlines())} lines")
print(f"04_Thiet_Ke_UI_UX.md:        {len(ui_text)} chars, {len(ui_text.splitlines())} lines")

# 1. PLACEHOLDER & TRUNCATION DETECTION
print("\n--- [CHECK 1] ZERO PLACEHOLDER & TRUNCATION DETECTION ---")
placeholders = ['TODO', 'TBD', 'FIXME', 'WIP', 'coming soon', 'tương tự như trên', 'giữ nguyên logic cũ']
found_placeholders = []
for fname, content in [("03_API", api_text), ("04_UIUX", ui_text)]:
    for idx, line in enumerate(content.splitlines(), 1):
        for ph in placeholders:
            if re.search(r'\b' + re.escape(ph) + r'\b', line, re.IGNORECASE):
                found_placeholders.append((fname, idx, ph, line.strip()))

if found_placeholders:
    print(f"FAILED: Found {len(found_placeholders)} placeholders:")
    for fp in found_placeholders:
        print(f"  {fp[0]}:{fp[1]} -> [{fp[2]}] {fp[3][:100]}")
else:
    print("PASSED: Zero placeholders found across both files.")

# Check for lazy ellipsis in code blocks
lazy_ellipsis = []
for fname, content in [("03_API", api_text), ("04_UIUX", ui_text)]:
    blocks = re.findall(r'```(?:json|csharp|typescript|sql|http|markdown)?\n([\s\S]*?)```', content)
    for b_idx, block in enumerate(blocks):
        lines_b = block.split('\n')
        for l_idx, l in enumerate(lines_b):
            if re.search(r'/\*.*\.\.\..*\*/|//.*\.\.\.|\.\.\.$|^\s*\.\.\.\s*$', l):
                lazy_ellipsis.append((fname, b_idx, l_idx, l.strip()))

if lazy_ellipsis:
    print(f"WARNING/FAIL: Found {len(lazy_ellipsis)} potential lazy ellipses:")
    for le in lazy_ellipsis:
        print(f"  {le[0]} block {le[1]} line {le[2]}: {le[3]}")
else:
    print("PASSED: Zero lazy ellipses in code blocks.")

# 2. PROHIBITED LEGACY ITEMS SCAN
print("\n--- [CHECK 2] ELIMINATION OF PROHIBITED LEGACY ITEMS ---")
legacy_prohibited = [
    (r'Flutter|React Native', "Staff Mobile App Frameworks"),
    (r'Staff App.*(?:iOS|Android|store|Store|APK|apk)', "Staff Native Mobile App"),
    (r'GPS.*50m|50m.*GPS|bán kính.*50m', "GPS 50m attendance"),
    (r'QR.*30s|30s.*QR|hết hạn sau 30', "Dynamic QR 30s expiration"),
    (r'\bC-23\b|\bC-24\b', "Legacy removed features C-23/C-24"),
    (r'chia sẻ MXH|chia sẻ lên mạng xã hội', "Social share C-23"),
    (r'Push Notification.*PWA|Web Push PWA', "Push notification C-24"),
    (r'tra cứu calo riêng|màn hình calo riêng|màn hình ví voucher', "Separate voucher/calorie standalone screens")
]

prohibited_found = []
for fname, content in [("03_API", api_text), ("04_UIUX", ui_text)]:
    for idx, line in enumerate(content.splitlines(), 1):
        for pat, desc in legacy_prohibited:
            if re.search(pat, line, re.IGNORECASE):
                prohibited_found.append((fname, idx, desc, line.strip()))

if prohibited_found:
    print(f"FAILED: Found {len(prohibited_found)} prohibited legacy mentions:")
    for pf in prohibited_found:
        print(f"  {pf[0]}:{pf[1]} [{pf[2]}] -> {pf[3]}")
else:
    print("PASSED: Complete elimination of all prohibited legacy items confirmed.")

# 3. API CONTRACT VERIFICATION (03_Thiet_Ke_API_Contract.md)
print("\n--- [CHECK 3] API CONTRACTS VERIFICATION (03_Thiet_Ke_API_Contract.md) ---")
# 10 API Groups
expected_groups = [
    "Nhóm 1", "Nhóm 2", "Nhóm 3", "Nhóm 4", "Nhóm 5",
    "Nhóm 6", "Nhóm 7", "Nhóm 8", "Nhóm 9", "Nhóm 10"
]
for g in expected_groups:
    m = re.search(rf'##\s+2\.\d+\s+{g}.*', api_text)
    if m:
        print(f"  Found Group {g}: {m.group(0)}")
    else:
        print(f"  FAILED: Missing Group {g}")

# Endpoints check
endpoints = re.findall(r'`(GET|POST|PUT|PATCH|DELETE)\s+([^`\n]+)`', api_text)
print(f"  Total REST endpoints documented: {len(endpoints)}")
for m, p in endpoints:
    print(f"    - [{m}] {p}")

# SignalR Hubs check
expected_hubs = [
    "/hubs/order",
    "/hubs/kitchen",
    "/hubs/payment",
    "/hubs/notification"
]
for hub in expected_hubs:
    if hub in api_text:
        print(f"  Found SignalR Hub: {hub}")
    else:
        print(f"  FAILED: Missing SignalR Hub: {hub}")

# Check key business rules in API doc
api_biz_checks = [
    ("DineIn 2-branch", r'DineIn|dine-in|vietqr.*cash|tiền mặt|bill.*qr', True),
    ("Delivery 20k", r'20,?000|delivery_fee|fixed.*20k|20k', True),
    ("Takeaway 10 cups", r'10.*ly|loyalty.*cup|10.*cups|10_cups', True),
    ("WiFi BSSID & Subnet Attendance", r'bssid|ip_subnet|client_ip|wifi.*bssid', True),
    ("PayOS Webhook HMAC SHA256", r'payos|webhook|signature|hmac.*sha256', True),
    ("Cash shift & Z-Report", r'z_report|cash_shift|z-report|zreport|closing_cash', True),
    ("BOM & Ingredients", r'bom|recipe|ingredient|inventory', True),
    ("Gemini AI-2 & Apriori", r'gemini|apriori|ai.*recommend|cross_sell', True)
]

for name, pattern, expected in api_biz_checks:
    match = re.search(pattern, api_text, re.IGNORECASE)
    if match:
        print(f"  PASSED [API Contract]: {name} (sample: {match.group(0)[:60]})")
    else:
        print(f"  FAILED [API Contract]: {name}")

# 4. UI/UX DESIGN SYSTEM & ROUTE GROUPS (04_Thiet_Ke_UI_UX.md)
print("\n--- [CHECK 4] UI/UX SPECIFICATION VERIFICATION (04_Thiet_Ke_UI_UX.md) ---")
expected_route_groups = [
    (r'\(customer\)', "Customer Portal & PWA App Router"),
    (r'\(kds\)', "KDS Kitchen TV App Router"),
    (r'\(staff\)', "Staff Web POS App Router"),
    (r'\(manager\)', "Store Manager App Router"),
    (r'\(admin\)', "System Admin App Router")
]
for rg, desc in expected_route_groups:
    match = re.search(rg, ui_text)
    if match:
        print(f"  Found Route Group {rg}: {desc}")
    else:
        print(f"  FAILED: Missing Route Group {rg}")

# Check key UI/UX screens & wireframes
ui_screen_checks = [
    ("Design System Tokens (Colors, Typography, Spacing)", r'Design System|Design Tokens|Color Palette|Typography|Bảng màu', True),
    ("(customer) Dine-In 2-branch Checkout (VietQR vs Cash + Bill QR)", r'dine-in|bill.*qr|vietqr.*tiền mặt|trả trước.*trả sau', True),
    ("(customer) Delivery Order (20k ship fee, phone, address, 100% VietQR)", r'20,?000.*đ|phí.*giao hàng|khóa.*cod', True),
    ("(customer) Loyalty 10 Cups View & Stamp Card", r'10.*ly|thẻ tích điểm|loyalty|10 cup', True),
    ("(kds) Kitchen TV Display & Station Routing & Timer", r'kds|màn hình bếp|station|timer|báo trễ|pending.*cooking', True),
    ("(staff) Web POS Takeaway & Phone CRM & Cup Redemption", r'pos.*takeaway|sđt.*crm|10 ly.*tặng 1|quẹt mã', True),
    ("(staff) Dine-In Table Management & Bill QR Print", r'sơ đồ bàn|in bill qr|chuyển bàn|tách bàn|gộp bàn', True),
    ("(staff) WiFi One-Click Attendance", r'chấm công.*wifi|bssid|ip subnet', True),
    ("(manager) Cash Shift Audit & Z-Report", r'két tiền|z-report|bàn giao ca|chênh lệch tiền', True),
    ("(manager) Inventory Stock-in / BOM Consumption", r'nhập kho|kiểm kê|bom|nguyên vật liệu|cảnh báo tồn', True),
    ("(admin) Multi-Branch & Gemini AI-2 Analytics", r'chuỗi.*chi nhánh|ai.*phân tích|doanh thu.*dự báo|apriori', True)
]

for name, pattern, expected in ui_screen_checks:
    match = re.search(pattern, ui_text, re.IGNORECASE)
    if match:
        print(f"  PASSED [UI/UX Spec]: {name}")
    else:
        print(f"  FAILED [UI/UX Spec]: {name}")

print("\n" + "=" * 80)
print("AUDIT EXECUTION COMPLETE")
print("=" * 80)
