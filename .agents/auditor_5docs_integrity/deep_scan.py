import os
import sys
import re
import json

# Ensure utf-8 output
sys.stdout.reconfigure(encoding='utf-8')

docs_dir = r'd:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc'
files = {
    'Smart_FB_OS': 'Smart_FB_Operating_System.md',
    'Actor': 'Actor_Phan_Quyen_Chuc_Nang.md',
    'Workflow': 'Workflow_Quy_Trinh_Nghiep_Vu.md',
    'Architecture': 'Tong_Quan_Kien_Truc_He_Thong.md',
    'Summary': 'Tom_Tat_1_Trang_Executive_Summary.md'
}

file_contents = {}
for key, fname in files.items():
    path = os.path.join(docs_dir, fname)
    with open(path, 'r', encoding='utf-8') as fp:
        file_contents[key] = fp.read()

print("==================================================")
print("PHASE 1: FORBIDDEN TERMS & REMOVALS AUDIT")
print("==================================================")

forbidden_patterns = [
    (r'\bC-23\b', 'C-23 identifier'),
    (r'\bC-24\b', 'C-24 identifier'),
    (r'\bC23\b', 'C23 identifier'),
    (r'\bC24\b', 'C24 identifier'),
    (r'chia sẻ món ăn (lên |qua )?mxh', 'Social share feature'),
    (r'push notification khuyến mãi', 'Promotional push notifications'),
    (r'gps[ -]?lock|bán kính 50m|geofenc', 'GPS attendance lock'),
    (r'qr động đổi mỗi 30', 'Dynamic 30s QR attendance')
]

for key, content in file_contents.items():
    print(f"\n--- Checking file: {files[key]} ---")
    for pattern, desc in forbidden_patterns:
        matches = list(re.finditer(pattern, content, re.IGNORECASE))
        if matches:
            print(f"  Matches for '{desc}' ({len(matches)} matches):")
            for m in matches:
                line_no = content[:m.start()].count('\n') + 1
                line_str = content.splitlines()[line_no-1].strip()
                print(f"    Line {line_no}: {line_str}")
        else:
            print(f"  [PASS] Clean of '{desc}'")

print("\n--- Staff Mobile App Context Check ---")
for key, content in file_contents.items():
    matches = list(re.finditer(r'staff\s*(mobile\s*)?app|ứng dụng di động nhân viên|app nhân viên', content, re.IGNORECASE))
    if matches:
        print(f"\nFile {files[key]}: {len(matches)} mentions found. Checking context:")
        for m in matches:
            line_no = content[:m.start()].count('\n') + 1
            line_str = content.splitlines()[line_no-1].strip()
            is_removal = any(kw in line_str.lower() for kw in ['loại bỏ', 'bỏ hoàn toàn', 'thay vì', 'không dùng', 'không cần', 'không có', 'bãi bỏ', 'chuyển sang web', 'hủy bỏ', 'đã xóa', 'loại trừ', 'đã bãi bỏ', 'bỏ hẳn'])
            status = "[PASS - Removal context]" if is_removal else "[FLAG - Potential violation]"
            print(f"    Line {line_no} {status}: {line_str}")
    else:
        print(f"File {files[key]}: 0 mentions of Staff Mobile App.")

print("\n==================================================")
print("PHASE 2: ZERO-PLACEHOLDER SCAN")
print("==================================================")

placeholder_patterns = [
    (r'\bTODO\b', 'TODO tag'),
    (r'\bTBD\b', 'TBD tag'),
    (r'\bFIXME\b', 'FIXME tag'),
    (r'\bXXX\b', 'XXX tag'),
    (r'//\s*rest of', '// rest of'),
    (r'/\*\s*rest of', '/* rest of'),
    (r'tương tự như trên', 'tuong tu nhu tren'),
    (r'giữ nguyên logic cũ', 'giu nguyen logic cu'),
    (r'\[chèn .*?\]', '[chèn ...]'),
    (r'\[bổ sung .*?\]', '[bổ sung ...]'),
    (r'\[placeholder.*?\]', '[placeholder...]')
]

for key, content in file_contents.items():
    print(f"\n--- Checking placeholders in: {files[key]} ---")
    found_any = False
    for pattern, desc in placeholder_patterns:
        matches = list(re.finditer(pattern, content, re.IGNORECASE))
        if matches:
            found_any = True
            print(f"  [FLAG] Found '{desc}' ({len(matches)} matches):")
            for m in matches:
                line_no = content[:m.start()].count('\n') + 1
                line_str = content.splitlines()[line_no-1].strip()
                print(f"    Line {line_no}: {line_str}")
    if not found_any:
        print(f"  [PASS] No standard placeholder patterns detected.")

print("\n==================================================")
print("PHASE 3: 6 CORE BUSINESS RULES AUDIT")
print("==================================================")

rules_to_check = {
    "Dine-in 2 payment paths": [
        (r'vietqr.*(thanh toán trước|trước khi bếp)|thanh toán trước.*vietqr', "VietQR Path: Pre-payment before kitchen"),
        (r'tiền mặt.*(thanh toán sau|bếp nhận ngay|hóa đơn.*qr)|hóa đơn.*(in mã|in qr)|sau khi nhận món.*tiền mặt', "Cash Path: Kitchen immediately + Bill with QR")
    ],
    "Delivery 20k fee & address": [
        (r'20\.000', "Fixed 20,000 VND fee"),
        (r'địa chỉ giao hàng|delivery_address', "Mandatory delivery address"),
        (r'chỉ.*vietqr|không.*(cod|tiền mặt)|không hỗ trợ cod', "Only VietQR (No COD/cash)")
    ],
    "Takeaway NV UI & 10=1 loyalty": [
        (r'takeaway|mang đi', "Takeaway presence"),
        (r'10\s*ly.*(1\s*ly|miễn phí)|mua\s*10.*tặng\s*1', "Loyalty 10 drinks = 1 free"),
        (r'chỉ.*(takeaway|mang đi)|áp dụng.*chỉ.*takeaway|không áp dụng.*dine-in', "Loyalty ONLY for Takeaway")
    ],
    "WiFi Attendance": [
        (r'wifi.*(bssid|ssid|quán|locked|mạng)', "WiFi verification (SSID/BSSID)"),
        (r'mã.*nhân viên|mã số nv|mã nv', "Employee code verification")
    ],
    "Admin Full CRUD": [
        (r'crud|tạo mới.*sửa.*xóa|quản lý.*món', "Menu Full CRUD"),
        (r'combo', "Combo management"),
        (r'upload.*ảnh|hình ảnh|tải lên hình ảnh', "Image upload"),
        (r'86|toggle.*món|bật/tắt|bật / tắt', "86 Toggle item status")
    ]
}

for rule_name, patterns in rules_to_check.items():
    print(f"\n--- Auditing Business Rule: {rule_name} ---")
    for key, content in file_contents.items():
        print(f"  File {files[key]}:")
        for pat, desc in patterns:
            matched = bool(re.search(pat, content, re.IGNORECASE))
            status = "[PASS]" if matched else "[FAIL/NOT FOUND]"
            print(f"    {status} {desc}")
