# -*- coding: utf-8 -*-
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

folder = r'd:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc'
files = {
    'Smart_FB_Operating_System.md': os.path.join(folder, 'Smart_FB_Operating_System.md'),
    'Actor_Phan_Quyen_Chuc_Nang.md': os.path.join(folder, 'Actor_Phan_Quyen_Chuc_Nang.md'),
    'Workflow_Quy_Trinh_Nghiep_Vu.md': os.path.join(folder, 'Workflow_Quy_Trinh_Nghiep_Vu.md'),
    'Tong_Quan_Kien_Truc_He_Thong.md': os.path.join(folder, 'Tong_Quan_Kien_Truc_He_Thong.md'),
    'Tom_Tat_1_Trang_Executive_Summary.md': os.path.join(folder, 'Tom_Tat_1_Trang_Executive_Summary.md')
}

file_contents = {}
for name, path in files.items():
    with open(path, 'r', encoding='utf-8') as f:
        file_contents[name] = f.read()

print('=' * 80)
print('AUDIT REQUIREMENT 1.1: C-23 and C-24 Grep Check (Must be EXACTLY 0)')
print('=' * 80)
req1_1_pass = True
for name, content in file_contents.items():
    c23_matches = re.findall(r'\bC-23\b', content, re.IGNORECASE)
    c24_matches = re.findall(r'\bC-24\b', content, re.IGNORECASE)
    if c23_matches or c24_matches:
        req1_1_pass = False
        print(f'[FAIL] {name}: C-23 matches={len(c23_matches)}, C-24 matches={len(c24_matches)}')
    else:
        print(f'[PASS] {name}: C-23=0, C-24=0')
print('Req 1.1 Overall Status:', 'PASS' if req1_1_pass else 'FAIL')

print('\n' + '=' * 80)
print('AUDIT REQUIREMENT 1.2: Staff Mobile App (Must be 0 or only mentioned as removed/deprecated)')
print('=' * 80)
req1_2_pass = True
for name, content in file_contents.items():
    lines = content.splitlines()
    print(f'-- {name} --')
    app_lines = []
    for idx, line in enumerate(lines, 1):
        if 'staff mobile app' in line.lower() or 'staff app' in line.lower():
            app_lines.append((idx, line))
    for idx, line in app_lines:
        is_removal = any(w in line.lower() for w in ['loại bỏ', 'xóa', 'không có', 'bỏ', 'deprecated', 'thay bằng', '100% web'])
        print(f'   Line {idx} (Removed context: {is_removal}): {line.strip()[:100]}')
        if not is_removal:
            print(f'   [WARNING/FAIL] Potential active Staff App mention at line {idx}')
            req1_2_pass = False
    if not app_lines:
        print('   No mentions found.')
print('Req 1.2 Overall Status:', 'PASS' if req1_2_pass else 'FAIL')

print('\n' + '=' * 80)
print('AUDIT REQUIREMENT 1.3: Dine-In Cash Flow Verification')
print('=' * 80)
for name, content in file_contents.items():
    has_cash = 'tiền mặt' in content.lower()
    has_bep_ngay = any(k in content.lower() for k in ['bếp nhận ngay', 'vào bếp ngay', 'chuyển ngay xuống bếp', 'bếp kds nhận'])
    has_bill_qr = any(k in content.lower() for k in ['kèm hóa đơn', 'in mã qr', 'vietqr trên hóa đơn', 'qr trên hóa đơn', 'bill có in mã qr'])
    print(f'{name}:')
    print(f'   tiền mặt: {has_cash} | bếp nhận ngay: {has_bep_ngay} | bill có mã QR: {has_bill_qr}')

print('\n' + '=' * 80)
print('AUDIT REQUIREMENT 1.4: Loyalty 10 ly = 1 ly strictly Takeaway only')
print('=' * 80)
for name, content in file_contents.items():
    has_10ly = ('10 ly' in content.lower() or '10 cốc' in content.lower())
    has_takeaway_restriction = any(k in content.lower() for k in [
        'chỉ áp dụng cho đơn takeaway',
        'chỉ áp dụng duy nhất cho đơn takeaway',
        'chỉ áp dụng cho takeaway',
        'không áp dụng cho dine-in',
        'chỉ áp dụng mang về',
        'chỉ takeaway'
    ])
    print(f'{name}: 10 ly mentioned={has_10ly} | Takeaway only restriction={has_takeaway_restriction}')

print('\n' + '=' * 80)
print('AUDIT REQUIREMENT 1.5: Delivery + địa chỉ + 20.000 (at least 3/5 files)')
print('=' * 80)
deliv_files = 0
for name, content in file_contents.items():
    c_lower = content.lower()
    h_del = 'delivery' in c_lower
    h_addr = 'địa chỉ' in c_lower
    h_fee = ('20.000' in content or '20,000' in content or '20k' in c_lower)
    all_3 = h_del and h_addr and h_fee
    if all_3:
        deliv_files += 1
    print(f'{name}: Delivery={h_del} | Địa chỉ={h_addr} | Phí 20k={h_fee} -> All 3={all_3}')
print(f'Delivery Criteria matched in {deliv_files}/5 files (Target: >= 3)')

print('\n' + '=' * 80)
print('AUDIT REQUIREMENT 1.6: WiFi-locked Attendance Mechanism')
print('=' * 80)
for name, content in file_contents.items():
    c_lower = content.lower()
    h_wifi = 'wifi' in c_lower
    h_att = 'chấm công' in c_lower
    h_lock = any(k in c_lower for k in ['khóa wifi', 'wifi-locked', 'bssid', 'ssid', 'mạng wifi'])
    print(f'{name}: WiFi={h_wifi} | Chấm công={h_att} | WiFi-lock mechanism details={h_lock}')

print('\n' + '=' * 80)
print('AUDIT REQUIREMENT 2: Dine-In 2 distinct status flows')
print('=' * 80)
wf_doc = file_contents['Workflow_Quy_Trinh_Nghiep_Vu.md']
wf01a_pos = wf_doc.find('WF-01A')
wf01b_pos = wf_doc.find('WF-01B')
wf02_pos = wf_doc.find('WF-02')
print('[WF-01A Snippet]:')
print(wf_doc[wf01a_pos:wf01a_pos+400])
print('\n[WF-01B Snippet]:')
print(wf_doc[wf01b_pos:wf01b_pos+400])

print('\n' + '=' * 80)
print('AUDIT REQUIREMENT 3: Admin full CRUD capabilities')
print('=' * 80)
spec_doc = file_contents['Smart_FB_Operating_System.md']
actor_doc = file_contents['Actor_Phan_Quyen_Chuc_Nang.md']
admin_items = [
    ('Products CRUD', ['Tạo mới', 'Chỉnh sửa', 'Xóa mềm', 'Thay thế']),
    ('Combos', ['Combo', 'AI-2', 'Apriori']),
    ('Image Uploads', ['WebP', 'Upload', 'Tối ưu']),
    ('Branch Pricing', ['Bảng giá', 'Nhóm giá', 'Chi nhánh']),
    ('86 Toggle', ['86', 'Khóa món', 'Hết hàng']),
    ('Seasonal Menu', ['Mùa vụ', 'Lên lịch', 'Seasonal'])
]
for item_name, kw_list in admin_items:
    found_spec = [k for k in kw_list if k.lower() in spec_doc.lower()]
    found_actor = [k for k in kw_list if k.lower() in actor_doc.lower()]
    print(f'{item_name:18s} | Spec Doc keywords: {found_spec} | Actor Doc keywords: {found_actor}')
