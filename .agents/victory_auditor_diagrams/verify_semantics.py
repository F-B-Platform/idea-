import os
import re
import sys

# Ensure UTF-8 output encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

sources_of_truth = {
    'master_spec': r'd:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md',
    'rbac_spec': r'd:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Actor_Phan_Quyen_Chuc_Nang.md',
    'workflow_spec': r'd:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md',
    'arch_spec': r'd:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Tong_Quan_Kien_Truc_He_Thong.md',
    'db_spec': r'd:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md',
    'api_spec': r'd:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md'
}

target_files = {
    '01_arch': r'd:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\01_Kien_Truc_Tong_Quan.md',
    '02_seq': r'd:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\02_Sequence_Diagrams.md',
    '03_erd': r'd:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\03_ERD_Database_Diagram.md',
    '04_deploy': r'd:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\04_Deployment_Diagram.md'
}

print("=== CHECKING FILES EXISTENCE ===")
for k, v in {**sources_of_truth, **target_files}.items():
    exists = os.path.exists(v)
    size = os.path.getsize(v) if exists else 0
    print(f"[{'OK' if exists else 'MISSING'}] {k}: {v} ({size} bytes)")

print("\n=== SCANNING FOR FORBIDDEN PATTERNS IN TARGET FILES ===")
forbidden_regexes = [
    (r'\b(TODO|TBD)\b', 'Placeholder TODO/TBD'),
    (r'/\*\s*rest of code\s*\*/', 'Placeholder rest of code'),
    (r'//\s*tương tự như trên', 'Placeholder tuong tu nhu tren'),
    (r'Staff Mobile App\s+(?:được phát triển|chạy trên|sử dụng|cài đặt)', 'Active Staff Mobile App implementation'),
    (r'Flutter|React Native', 'Flutter/React Native framework'),
    (r'GPS\s+50m|bán kính\s+50m', 'GPS 50m constraint'),
    (r'QR\s+động\s+30s|mã\s+QR\s+30s|hết\s+hạn\s+sau\s+30\s*giây', 'QR 30s expiration'),
    (r'\bC-23\b|\bC-24\b', 'Deprecated C-23/C-24 functional codes'),
    (r'ví\s+voucher', 'Vi voucher legacy')
]

for name, path in target_files.items():
    content = open(path, encoding='utf-8').read()
    print(f"\nScanning {name} ({os.path.basename(path)}):")
    for regex, desc in forbidden_regexes:
        matches = list(re.finditer(regex, content, re.IGNORECASE))
        if matches:
            print(f"  [FOUND] {desc} (count: {len(matches)})")
            for m in matches[:3]:
                line_no = content[:m.start()].count('\n') + 1
                line_text = content.splitlines()[line_no - 1].strip()
                print(f"    Line {line_no}: {line_text[:100]}")
        else:
            print(f"  [CLEAN] {desc}")

