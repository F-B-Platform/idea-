import os, sys, re, json

TARGET_DIR = r'd:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc'
FILES = [
    'Smart_FB_Operating_System.md',
    'Actor_Phan_Quyen_Chuc_Nang.md',
    'Workflow_Quy_Trinh_Nghiep_Vu.md',
    'Tong_Quan_Kien_Truc_He_Thong.md',
    'Tom_Tat_1_Trang_Executive_Summary.md'
]

results = {}

for filename in FILES:
    filepath = os.path.join(TARGET_DIR, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    file_res = {
        'filename': filename,
        'line_count': len(lines),
        'check1_c23_c24': [],
        'check2_placeholders': {},
        'check3_staff_app': [],
        'check4_dinein_payment': {},
        'check5_delivery': {},
        'check6_takeaway_loyalty': {},
        'check7_wifi_attendance': {}
    }
    
    # 1. Check C-23 & C-24
    for idx, line in enumerate(lines, 1):
        if re.search(r'\bC-?23\b', line, re.IGNORECASE):
            file_res['check1_c23_c24'].append({'line': idx, 'match': 'C-23', 'content': line.strip()})
        if re.search(r'\bC-?24\b', line, re.IGNORECASE):
            file_res['check1_c23_c24'].append({'line': idx, 'match': 'C-24', 'content': line.strip()})
            
    # 2. Check Placeholders
    placeholder_patterns = {
        'TODO': r'\bTODO\b',
        'TBD': r'\bTBD\b',
        'rest_of_code': r'/\*\s*rest of code\s*\*/|rest of code',
        'tuong_tu': r'//\s*tương tự|tương tự như trên',
        'placeholder_tag': r'\[placeholder\]|\[TBD\]|\[chưa xác định\]',
        'ellipsis': r'(?<!\.)\.\.\.(?!\.)'
    }
    for p_name, p_regex in placeholder_patterns.items():
        matches = []
        for idx, line in enumerate(lines, 1):
            if re.search(p_regex, line, re.IGNORECASE):
                matches.append({'line': idx, 'content': line.strip()})
        file_res['check2_placeholders'][p_name] = matches

    # 3. Check Staff Mobile App
    staff_app_patterns = r'(?i)Staff\s+Mobile\s+App|Staff\s+App|App\s+nhân\s+viên|mobile\s+app\s+nhân\s+viên|Staff\s+Mobile'
    for idx, line in enumerate(lines, 1):
        if re.search(staff_app_patterns, line):
            file_res['check3_staff_app'].append({'line': idx, 'content': line.strip()})

    # 4. Check Dine-In 2 payment paths
    check4_patterns = {
        'tien_mat': r'(?i)tiền mặt',
        'vietqr': r'(?i)VietQR',
        'tra_truoc': r'(?i)trả trước',
        'tra_sau': r'(?i)trả sau',
        'kem_hoa_don': r'(?i)kèm hóa đơn|hóa đơn tạm tính|phiếu tạm tính|in hóa đơn',
        'in_ma_qr': r'(?i)in mã QR|mã QR thanh toán|QR động'
    }
    for p_name, p_regex in check4_patterns.items():
        matches = []
        for idx, line in enumerate(lines, 1):
            if re.search(p_regex, line):
                matches.append({'line': idx, 'content': line.strip()})
        file_res['check4_dinein_payment'][p_name] = matches

    # 5. Check Delivery
    check5_patterns = {
        'fee_20k': r'20\.?000|20,000',
        'dia_chi_giao_hang': r'(?i)địa chỉ giao hàng|địa chỉ nhận hàng',
        'delivery_fee': r'(?i)delivery_fee|deliveryFee|phí giao hàng|phí vận chuyển',
        'order_type_delivery': r'(?i)DELIVERY|order_type|đơn giao hàng'
    }
    for p_name, p_regex in check5_patterns.items():
        matches = []
        for idx, line in enumerate(lines, 1):
            if re.search(p_regex, line):
                matches.append({'line': idx, 'content': line.strip()})
        file_res['check5_delivery'][p_name] = matches

    # 6. Check Takeaway loyalty
    check6_patterns = {
        '10_ly': r'(?i)10\s*ly|10_ly',
        'tang_1_ly': r'(?i)tặng\s*1\s*ly|tặng\s*1|miễn\s*phí\s*1\s*ly',
        'takeaway_only': r'(?i)Takeaway|Mang về|chỉ áp dụng.*takeaway|không áp dụng.*dine-in'
    }
    for p_name, p_regex in check6_patterns.items():
        matches = []
        for idx, line in enumerate(lines, 1):
            if re.search(p_regex, line):
                matches.append({'line': idx, 'content': line.strip()})
        file_res['check6_takeaway_loyalty'][p_name] = matches

    # 7. Check WiFi Attendance
    check7_patterns = {
        'wifi_locked': r'(?i)WiFi[-_]?Locked|wifi locked',
        'bssid': r'(?i)\bBSSID\b',
        'ip_subnet': r'(?i)IP\s*Subnet|Subnet|dải IP|IP nội bộ'
    }
    for p_name, p_regex in check7_patterns.items():
        matches = []
        for idx, line in enumerate(lines, 1):
            if re.search(p_regex, line):
                matches.append({'line': idx, 'content': line.strip()})
        file_res['check7_wifi_attendance'][p_name] = matches

    results[filename] = file_res

out_path = r'd:\Idea_DoAn\.agents\challenger_5docs_keywords\empirical_raw.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print('Saved empirical raw results to', out_path)
