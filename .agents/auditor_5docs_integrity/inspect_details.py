import os
import sys
import re

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
print("CHECKING GPS / GEOFENCING REFERENCES")
print("==================================================")
for key, content in file_contents.items():
    for m in re.finditer(r'gps|geofenc|bán kính 50m', content, re.IGNORECASE):
        line_no = content[:m.start()].count('\n') + 1
        line_str = content.splitlines()[line_no-1].strip()
        print(f"File {files[key]} (Line {line_no}): {line_str}")

print("\n==================================================")
print("CHECKING DINE-IN 2 PAYMENT PATHS IN ALL 5 FILES")
print("==================================================")
for key, content in file_contents.items():
    print(f"\n--- File: {files[key]} ---")
    has_vietqr_path = bool(re.search(r'vietqr', content, re.IGNORECASE) and re.search(r'trước|pending.*payment|pre-pay', content, re.IGNORECASE))
    has_cash_path = bool(re.search(r'tiền mặt|cash', content, re.IGNORECASE) and re.search(r'sau|bếp.*ngay|hóa đơn.*qr|bill', content, re.IGNORECASE))
    print(f"  VietQR Pre-pay described: {has_vietqr_path}")
    print(f"  Cash Post-pay described: {has_cash_path}")
    # Print sample snippets
    snippets = []
    for line in content.splitlines():
        if any(k in line.lower() for k in ['tiền mặt', 'vietqr', 'thanh toán trước', 'thanh toán sau', 'nhánh a', 'nhánh b', 'phương thức a', 'phương thức b', 'bếp mới nhận đơn', 'bếp nhận ngay']):
            snippets.append(line.strip())
    print(f"  Total relevant lines: {len(snippets)}")
    for s in snippets[:6]:
        print(f"    - {s[:120]}")

print("\n==================================================")
print("CHECKING SCOPE QUARANTINE: SCALE UP / FUTURE WORK")
print("==================================================")
for key, content in file_contents.items():
    print(f"\n--- File: {files[key]} ---")
    future_work_matches = list(re.finditer(r'scale\s*up|future\s*work|giai đoạn sau|tương lai|chưa triển khai', content, re.IGNORECASE))
    print(f"  Mentions of Future Work/Scale Up: {len(future_work_matches)}")
    for m in future_work_matches[:5]:
        line_no = content[:m.start()].count('\n') + 1
        print(f"    Line {line_no}: {content.splitlines()[line_no-1].strip()[:120]}")

print("\n==================================================")
print("CHECKING MERMAID DIAGRAMS & FORMAT INTEGRITY")
print("==================================================")
for key, content in file_contents.items():
    mermaid_blocks = re.findall(r'```mermaid([\s\S]*?)```', content)
    print(f"\nFile: {files[key]} - Total Mermaid blocks: {len(mermaid_blocks)}")
    for i, mb in enumerate(mermaid_blocks):
        first_line = mb.strip().splitlines()[0] if mb.strip().splitlines() else "EMPTY"
        print(f"  Diagram #{i+1}: {first_line} ({len(mb.strip().splitlines())} lines)")
