import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

root = r'd:\Idea_DoAn'

# Terms that should NOT appear except when explicitly discussing deprecated/eliminated features or Future Work
deprecated_patterns = [
    (r'\bStaff\s+Mobile\s+App\b', "Staff Mobile App"),
    (r'\bGPS\s+lock\b', "GPS lock"),
    (r'GPS\s+50m', "GPS 50m"),
    (r'QR\s+động\s+30\s+giây', "QR động 30 giây"),
    (r'30s\s+QR', "30s QR"),
]

# Required terms that MUST appear in the revised documentation
required_terms = [
    'Delivery',
    'delivery_address',
    'phí ship',
    '20.000',
    'WiFi',
    'SSID',
    'chấm công'
]

print("=== 1. AUDIT DEPRECATED / FORBIDDEN PATTERNS ===")
findings = []

for dirpath, dirnames, filenames in os.walk(root):
    if '.git' in dirpath or '.agents' in dirpath:
        continue
    for f in filenames:
        if f.endswith('.md'):
            filepath = os.path.join(dirpath, f)
            rel_path = os.path.relpath(filepath, root)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as fp:
                lines = fp.readlines()
            
            for line_idx, line in enumerate(lines):
                # Check if this line is in a section explicitly talking about "Loại bỏ", "Thay thế", "Deprecate", "Khác biệt", or "Scale Up"
                is_contextual_explanation = any(k in line.lower() for k in [
                    'loại bỏ', 'bỏ hoàn toàn', 'thay thế', 'deprecated', 'không dùng', 
                    'thay vì', 'trước đây', 'phiên bản cũ', 'tiền thân', 'scale-up', 'future work', 'chuyển sang web'
                ])
                
                # Check dine-in "thanh toán sau" / "yêu cầu bill"
                if re.search(r'dine-in.*(thanh toán sau|yêu cầu bill)|(thanh toán sau|yêu cầu bill).*dine-in', line, re.IGNORECASE):
                    if not is_contextual_explanation:
                        findings.append({
                            'file': rel_path,
                            'line_num': line_idx + 1,
                            'pattern': 'Dine-in Post-payment / Yeu cau bill',
                            'content': line.strip()
                        })

                for pat, label in deprecated_patterns:
                    if re.search(pat, line, re.IGNORECASE):
                        if not is_contextual_explanation:
                            findings.append({
                                'file': rel_path,
                                'line_num': line_idx + 1,
                                'pattern': label,
                                'content': line.strip()
                            })

if findings:
    print(f"Found {len(findings)} potential deprecated term usages outside elimination context:")
    for f in findings:
        print(f"  - {f['file']}:{f['line_num']} [{f['pattern']}] -> {f['content']}")
else:
    print("[PASS] 0 unauthorized deprecated terms found across all markdown files!")

print("\n=== 2. AUDIT REQUIRED TERMS ACROSS REPOSITORY ===")
for term in required_terms:
    matching_files = set()
    total_count = 0
    for dirpath, dirnames, filenames in os.walk(root):
        if '.git' in dirpath or '.agents' in dirpath:
            continue
        for f in filenames:
            if f.endswith('.md'):
                filepath = os.path.join(dirpath, f)
                rel_path = os.path.relpath(filepath, root)
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as fp:
                    content = fp.read()
                matches = re.findall(re.escape(term), content, re.IGNORECASE)
                if matches:
                    matching_files.add(rel_path)
                    total_count += len(matches)
    
    print(f"Term '{term}': found {total_count} occurrences across {len(matching_files)} files.")
    if len(matching_files) >= 3:
        print(f"  -> [PASS] Meets distribution requirement (>= 3 files)")
    else:
        print(f"  -> [WARN] Found in only {len(matching_files)} files")
