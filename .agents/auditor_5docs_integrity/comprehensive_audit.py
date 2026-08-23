import os
import sys
import re
import json

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

results = {}

# 1. Check C-23 & C-24
results['C23_C24_Absence'] = {}
for k, c in file_contents.items():
    found_c23 = bool(re.search(r'\bC-?23\b', c, re.I))
    found_c24 = bool(re.search(r'\bC-?24\b', c, re.I))
    results['C23_C24_Absence'][files[k]] = {
        'C23_found': found_c23,
        'C24_found': found_c24,
        'status': 'PASS' if not (found_c23 or found_c24) else 'FAIL'
    }

# 2. Check Staff Mobile App mentions
results['Staff_Mobile_App'] = {}
for k, c in file_contents.items():
    matches = list(re.finditer(r'staff\s*(mobile\s*)?app|app\s*nhân\s*viên|ứng\s*dụng\s*di\s*động\s*nhân\s*viên', c, re.I))
    suspicious = []
    for m in matches:
        line_no = c[:m.start()].count('\n') + 1
        line_str = c.splitlines()[line_no-1].strip()
        # if not in removal context
        if not any(w in line_str.lower() for w in ['loại bỏ', 'bỏ', 'xóa', 'thay vì', 'không', '100% web', 'web-first']):
            suspicious.append((line_no, line_str))
    results['Staff_Mobile_App'][files[k]] = {
        'total_mentions': len(matches),
        'suspicious_mentions': suspicious,
        'status': 'PASS' if len(suspicious) == 0 else 'FAIL'
    }

# 3. Check Dine-in 2 payment paths
results['DineIn_DualPath'] = {}
for k, c in file_contents.items():
    has_a = 'vietqr' in c.lower() and ('trước' in c.lower() or 'pending' in c.lower() or 'pre-pay' in c.lower())
    has_b = 'tiền mặt' in c.lower() and ('sau' in c.lower() or 'hóa đơn' in c.lower() or 'bill' in c.lower())
    results['DineIn_DualPath'][files[k]] = {
        'VietQR_Prepay_Found': has_a,
        'Cash_Postpay_Found': has_b,
        'status': 'PASS' if (has_a and has_b) else 'FAIL'
    }

# 4. Check Delivery: 20k, address, only VietQR
results['Delivery_20k'] = {}
for k, c in file_contents.items():
    has_fee = '20.000' in c or '20k' in c.lower() or '20,000' in c
    has_addr = 'địa chỉ' in c.lower() or 'delivery_address' in c.lower()
    has_vietqr_only = 'vietqr' in c.lower() and ('không' in c.lower() or 'chỉ' in c.lower())
    results['Delivery_20k'][files[k]] = {
        'Fee_20k': has_fee,
        'Address': has_addr,
        'VietQR_Only': has_vietqr_only,
        'status': 'PASS' if (has_fee and has_addr) else 'PARTIAL'
    }

# 5. Check Takeaway: NV UI, no customer QR, 10=1 only takeaway
results['Takeaway_Loyalty'] = {}
for k, c in file_contents.items():
    has_nv_ui = 'takeaway' in c.lower() and ('nhân viên' in c.lower() or 'nv' in c.lower() or 'pos' in c.lower() or 'quầy' in c.lower())
    has_10_1 = bool(re.search(r'10\s*ly.*1\s*ly|mua\s*10.*1|10.*tặng.*1', c, re.I))
    results['Takeaway_Loyalty'][files[k]] = {
        'NV_UI': has_nv_ui,
        'Loyalty_10_1': has_10_1,
        'status': 'PASS' if (has_nv_ui and has_10_1) else 'FAIL'
    }

# 6. Check Attendance: WiFi locked, no GPS
results['WiFi_Attendance'] = {}
for k, c in file_contents.items():
    has_wifi = 'wifi' in c.lower() and ('quán' in c.lower() or 'ssid' in c.lower() or 'bssid' in c.lower() or 'locked' in c.lower())
    has_empid = 'mã' in c.lower() and ('nv' in c.lower() or 'nhân viên' in c.lower() or 'employee' in c.lower())
    results['WiFi_Attendance'][files[k]] = {
        'WiFi_Check': has_wifi,
        'EmpId_Check': has_empid,
        'status': 'PASS' if (has_wifi and has_empid) else 'FAIL'
    }

# 7. Check Admin CRUD: Full CRUD, Combo, Upload, 86 Toggle
results['Admin_CRUD'] = {}
for k, c in file_contents.items():
    has_crud = 'crud' in c.lower() or ('tạo' in c.lower() and 'sửa' in c.lower() and 'xóa' in c.lower())
    has_combo = 'combo' in c.lower()
    has_86 = '86' in c or 'bật/tắt' in c.lower() or 'toggle' in c.lower()
    results['Admin_CRUD'][files[k]] = {
        'CRUD': has_crud,
        'Combo': has_combo,
        'Toggle_86': has_86,
        'status': 'PASS' if (has_crud and has_combo and has_86) else 'FAIL'
    }

# 8. Check Zero-Placeholder
results['Zero_Placeholder'] = {}
for k, c in file_contents.items():
    # Ignore legitimate markdown citations or quotes
    # Look for literal placeholder comments
    bad_tokens = []
    for line_no, line in enumerate(c.splitlines(), 1):
        if re.search(r'//\s*TODO|/\*\s*TODO|//\s*rest of|/\*\s*rest of|\bFIXME\b|\bXXX\b|tương tự như trên|giữ nguyên logic cũ|\[chèn |\[bổ sung ', line, re.I):
            bad_tokens.append((line_no, line.strip()))
    results['Zero_Placeholder'][files[k]] = {
        'bad_tokens_count': len(bad_tokens),
        'bad_tokens': bad_tokens,
        'status': 'PASS' if len(bad_tokens) == 0 else 'FAIL'
    }

print(json.dumps(results, indent=2, ensure_ascii=False))
