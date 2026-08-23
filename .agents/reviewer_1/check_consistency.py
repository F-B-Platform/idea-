import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

files = {
    '01_Arch': r'd:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\01_Kien_Truc_Tong_Quan.md',
    '02_Seq': r'd:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\02_Sequence_Diagrams.md',
    '03_ERD': r'd:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\03_ERD_Database_Diagram.md',
    '04_Deploy': r'd:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\04_Deployment_Diagram.md',
    'SoT_Master': r'd:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Smart_FB_Operating_System.md',
    'SoT_Workflows': r'd:\Idea_DoAn\01_Tai_Lieu_Dac_Ta_Goc\Workflow_Quy_Trinh_Nghiep_Vu.md',
    'SoT_DB': r'd:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md',
    'SoT_API': r'd:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md',
}

contents = {}
for k, v in files.items():
    if os.path.exists(v):
        with open(v, 'r', encoding='utf-8') as f:
            contents[k] = f.read()
    else:
        print(f"File not found: {v}")

# 1. Check Zero Placeholders
print("=== 1. CHECK ZERO PLACEHOLDERS ===")
placeholder_patterns = [r'\bTODO\b', r'\bTBD\b', r'\bFIXME\b', r'\bXXX\b', r'/\*\s*rest of', r'//\s*tương tự', r'/\*\s*code\s*\*/']
for name, text in contents.items():
    if not name.startswith('0'):
        continue
    for p in placeholder_patterns:
        matches = re.findall(p, text, re.IGNORECASE)
        if matches:
            print(f"[{name}] Found potential placeholder '{p}': {len(matches)} occurrences")
print("Zero placeholder check completed.")

# 2. Check Banned terms (Staff App, GPS 50m, QR 30s, C-23, C-24)
print("\n=== 2. CHECK BANNED / OUT-OF-SCOPE TERMS ===")
banned_patterns = [
    (r'flutter', 'Flutter'),
    (r'react\s*native', 'React Native'),
    (r'gps\s*50m', 'GPS 50m'),
    (r'qr\s*động\s*30s', 'QR động 30s'),
    (r'30\s*giây', '30 giây (QR)'),
    (r'c-23', 'C-23'),
    (r'c-24', 'C-24')
]

for name, text in contents.items():
    if not name.startswith('0'):
        continue
    for p, label in banned_patterns:
        lines = text.split('\n')
        for lno, l in enumerate(lines, 1):
            if re.search(p, l, re.IGNORECASE):
                is_negation = any(neg in l.lower() for neg in ['loại bỏ', 'xóa', 'không còn', 'triệt tiêu', 'bỏ', 'loại trừ', 'thay vì', 'không dùng', 'xóa bỏ', 'loại bỏ triệt để'])
                status = "EXPLICIT NEGATION / REMOVAL (Expected)" if is_negation else "WARNING: Check context!"
                print(f"[{name}:{lno}] {label} -> {status}: {l.strip()[:100]}")

# 3. Check Route Groups naming across 01, 02, 03, 04
print("\n=== 3. CHECK ROUTE GROUPS CONSISTENCY ===")
route_group_regex = r'\((customer|pos|kds|kitchen|staff|manager|admin|auth)\)'
for name, text in contents.items():
    if not name.startswith('0'):
        continue
    matches = set(re.findall(route_group_regex, text))
    print(f"[{name}] Route groups mentioned: {sorted(list(matches))}")

# 4. Check Hubs naming across 01, 02, 03, 04
print("\n=== 4. CHECK SIGNALR HUBS CONSISTENCY ===")
hub_regex = r'(OrderHub|KitchenHub|PaymentHub|NotificationHub|StaffHub)'
for name, text in contents.items():
    if not name.startswith('0'):
        continue
    matches = set(re.findall(hub_regex, text))
    print(f"[{name}] Hubs mentioned: {sorted(list(matches))}")

# 5. Check Tables consistency
print("\n=== 5. CHECK TABLES IN 03 vs SoT DB ===")
tables_in_03 = set(re.findall(r'### Bảng \d+:\s*`([^`]+)`', contents.get('03_ERD', '')))
print(f"03_ERD has {len(tables_in_03)} documented tables: {sorted(list(tables_in_03))}")

# Extract tables in SoT_DB
tables_in_sot = set(re.findall(r'### Bảng \d+:\s*`([^`]+)`', contents.get('SoT_DB', '')))
print(f"SoT_DB has {len(tables_in_sot)} documented tables: {sorted(list(tables_in_sot))}")

print(f"Tables in 03_ERD but not SoT_DB (extensions): {tables_in_03 - tables_in_sot}")
print(f"Tables in SoT_DB but not 03_ERD: {tables_in_sot - tables_in_03}")
