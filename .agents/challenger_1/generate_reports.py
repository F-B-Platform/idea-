import os, sys, re, json, datetime

sys.stdout.reconfigure(encoding='utf-8')
repo_root = r'd:\Idea_DoAn'

canonical_files = [
    r'01_Tai_Lieu_Dac_Ta_Goc\Actor_Phan_Quyen_Chuc_Nang.md',
    r'01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md',
    r'01_Tai_Lieu_Dac_Ta_Goc\Tom_Tat_1_Trang_Executive_Summary.md',
    r'01_Tai_Lieu_Dac_Ta_Goc\Tong_Quan_Kien_Truc_He_Thong.md',
    r'01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md',
    r'02_Bao_Gia_Chi_Phi\Bang_Bao_Gia_Smart_FB_OS.md',
    r'02_Bao_Gia_Chi_Phi\Chi_Phi_Duy_Tri_Hang_Thang.md',
    r'03_Quy_Trinh_Trien_Khai\01_Phan_Tich_Yeu_Cau.md',
    r'03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md',
    r'03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md',
    r'03_Quy_Trinh_Trien_Khai\04_Thiet_Ke_UI_UX.md',
    r'03_Quy_Trinh_Trien_Khai\05_Quy_Trinh_Backend.md',
    r'03_Quy_Trinh_Trien_Khai\06_Quy_Trinh_Frontend.md',
    r'03_Quy_Trinh_Trien_Khai\07_Ke_Hoach_Kiem_Thu.md',
    r'03_Quy_Trinh_Trien_Khai\08_Trien_Khai_He_Thong.md',
    r'03_Quy_Trinh_Trien_Khai\README.md',
    r'04_Thiet_Ke_Kien_Truc_Diagrams\01_Kien_Truc_Tong_Quan.md',
    r'04_Thiet_Ke_Kien_Truc_Diagrams\02_Sequence_Diagrams.md',
    r'04_Thiet_Ke_Kien_Truc_Diagrams\03_ERD_Database_Diagram.md',
    r'04_Thiet_Ke_Kien_Truc_Diagrams\04_Deployment_Diagram.md',
    r'05_Quy_Chuan_&_Test_Cases\Git_Workflow_&_Branching_Strategy.md',
    r'05_Quy_Chuan_&_Test_Cases\Seed_Data_&_Database_Script.md',
    r'05_Quy_Chuan_&_Test_Cases\UAT_Test_Cases.md',
    r'06_Danh_Sach_Skills\README.md',
    r'ROADMAP.md',
    r'DOC_AUDIT_REPORT.md',
    r'PROJECT.md'
]

# 1. Existence and stats
file_stats = []
for rel in canonical_files:
    full = os.path.join(repo_root, rel)
    exists = os.path.isfile(full)
    sz = os.path.getsize(full) if exists else 0
    lines = len(open(full, 'r', encoding='utf-8', errors='ignore').readlines()) if exists else 0
    file_stats.append({
        'rel': rel,
        'exists': exists,
        'size': sz,
        'lines': lines
    })

# 2. Obsolete scan
obsolete_hits = []
for item in file_stats:
    rel = item['rel']
    full = os.path.join(repo_root, rel)
    with open(full, 'r', encoding='utf-8', errors='ignore') as fp:
        for idx, line in enumerate(fp, 1):
            ll = line.lower()
            # check yeu cau bill
            if 'yêu c?u bill' in ll or 'yeu cau bill' in ll:
                obsolete_hits.append({'file': rel, 'line': idx, 'term': 'yêu c?u bill', 'content': line.strip()})
            # check thanh toan sau
            elif 'thanh toán sau' in ll or 'thanh toan sau' in ll:
                obsolete_hits.append({'file': rel, 'line': idx, 'term': 'thanh toán sau', 'content': line.strip()})
            # check staff mobile app
            elif 'staff mobile app' in ll or 'staff app' in ll:
                obsolete_hits.append({'file': rel, 'line': idx, 'term': 'Staff Mobile App', 'content': line.strip()})
            # check gps
            elif 'gps' in ll:
                obsolete_hits.append({'file': rel, 'line': idx, 'term': 'GPS', 'content': line.strip()})
            # check qr 30s
            elif any(k in ll for k in ['30 giây', '30s', '30 giay']) and any(k in ll for k in ['ch?m công', 'cham cong', 'qr ð?ng']):
                obsolete_hits.append({'file': rel, 'line': idx, 'term': 'QR 30s', 'content': line.strip()})

# 3. Mandatory keywords
kw_dict = {
    'Delivery': re.compile(r'\bDelivery\b', re.IGNORECASE),
    'delivery_address': re.compile(r'\bdelivery_address\b', re.IGNORECASE),
    'phí ship': re.compile(r'phí\s*ship', re.IGNORECASE),
    '20.000': re.compile(r'20\.000', re.IGNORECASE),
    'WiFi': re.compile(r'\bWiFi\b', re.IGNORECASE),
    'SSID': re.compile(r'\bSSID\b', re.IGNORECASE),
    'BSSID': re.compile(r'\bBSSID\b', re.IGNORECASE),
    'ch?m công': re.compile(r'ch?m\s*công', re.IGNORECASE),
    'PendingPayment': re.compile(r'PendingPayment', re.IGNORECASE),
    '10 ly': re.compile(r'10\s*ly', re.IGNORECASE),
    'loyalty': re.compile(r'loyalty', re.IGNORECASE),
}

kw_results = {}
for kw, pat in kw_dict.items():
    matched_files = []
    tot = 0
    for item in file_stats:
        rel = item['rel']
        full = os.path.join(repo_root, rel)
        cnt = open(full, 'r', encoding='utf-8', errors='ignore').read()
        m = pat.findall(cnt)
        if len(m) > 0:
            matched_files.append(rel)
            tot += len(m)
    kw_results[kw] = {
        'files_count': len(matched_files),
        'total_count': tot,
        'files': matched_files
    }

# 4. Placeholders
placeholder_dict = {
    'TODO': re.compile(r'\bTODO\b'),
    'TBD': re.compile(r'\bTBD\b'),
    '[TBD]': re.compile(r'\[TBD\]'),
    '/* rest of code */': re.compile(r'/\*\s*rest of code\s*\*/', re.IGNORECASE),
    '// týõng t?': re.compile(r'//\s*týõng\s*t?', re.IGNORECASE),
    'Chýa xác ð?nh': re.compile(r'chýa\s*xác\s*ð?nh', re.IGNORECASE),
    's? b? sung sau': re.compile(r's?\s*b?\s*sung\s*sau', re.IGNORECASE),
}

placeholder_hits = []
for item in file_stats:
    rel = item['rel']
    full = os.path.join(repo_root, rel)
    with open(full, 'r', encoding='utf-8', errors='ignore') as fp:
        for idx, line in enumerate(fp, 1):
            for pname, ppat in placeholder_dict.items():
                if ppat.search(line):
                    ll = line.lower()
                    if 'zero todo' in ll or 'c?m comment' in ll or 'không phát hi?n b?t k? placeholder' in ll:
                        continue
                    placeholder_hits.append({'file': rel, 'line': idx, 'name': pname, 'content': line.strip()})

# 5. Mermaid syntax
mermaid_results = []
for item in file_stats:
    rel = item['rel']
    full = os.path.join(repo_root, rel)
    cnt = open(full, 'r', encoding='utf-8', errors='ignore').read()
    blocks = re.findall(r'`mermaid(.*?)`', cnt, re.DOTALL)
    for b_idx, block in enumerate(blocks, 1):
        lines = [l.strip() for l in block.strip().split('\n') if l.strip()]
        if not lines:
            mermaid_results.append({'file': rel, 'block': b_idx, 'valid': False, 'type': 'EMPTY'})
        else:
            first_l = lines[0]
            valid_types = ['sequenceDiagram', 'classDiagram', 'erDiagram', 'graph', 'flowchart', 'stateDiagram', 'stateDiagram-v2', 'gantt', 'pie', 'C4Context', 'C4Container', 'architecture-beta']
            valid = any(first_l.startswith(t) for t in valid_types)
            mermaid_results.append({'file': rel, 'block': b_idx, 'valid': valid, 'type': first_l, 'lines': len(lines)})

# 6. Legacy files
all_md = []
for dirpath, dirnames, filenames in os.walk(repo_root):
    if '.agents' in dirpath or '.git' in dirpath:
        continue
    for f in filenames:
        if f.endswith('.md'):
            all_md.append(os.path.relpath(os.path.join(dirpath, f), repo_root))
legacy_files = sorted(list(set(all_md) - set(canonical_files)))

print(f'Canonical: {len(canonical_files)}')
print(f'Obsolete hits: {len(obsolete_hits)}')
print(f'Placeholder hits: {len(placeholder_hits)}')
print(f'Mermaid blocks: {len(mermaid_results)} (all valid: {all(m[" valid\] for m in mermaid_results)})')
print(f'Legacy files: {len(legacy_files)}')
