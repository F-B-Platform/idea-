import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

TARGET_DIR = r"d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams"

files = [
    "01_Kien_Truc_Tong_Quan.md",
    "02_Sequence_Diagrams.md",
    "03_ERD_Database_Diagram.md",
    "04_Deployment_Diagram.md"
]

forbidden_patterns = [
    (r"Flutter", "Flutter mobile app reference"),
    (r"React Native", "React Native mobile app reference"),
    (r"Staff Mobile App", "Staff Mobile App reference"),
    (r"Mobile App Nhân viên", "Mobile App Staff reference"),
    (r"App Nhân viên", "App Nhân viên reference"),
    (r"GPS\s*(?:50m|bán kính|định vị|toạ độ|vị trí)", "GPS location attendance"),
    (r"QR\s*(?:động\s*)?30s", "QR 30s dynamic attendance"),
    (r"30\s*(?:giây|s)\s*đổi", "QR 30s rotation"),
    (r"C-23\b", "C-23 (Social share) feature reference"),
    (r"C-24\b", "C-24 (PWA push notification) feature reference"),
    (r"Ví voucher", "Voucher wallet"),
    (r"tra cứu calo\s*riêng", "Separate calorie lookup feature"),
    (r"TODO\b", "TODO placeholder"),
    (r"TBD\b", "TBD placeholder"),
    (r"/\*\s*rest of", "Truncated code placeholder"),
    (r"//\s*tương tự", "Truncated code placeholder"),
    (r"//\s*giữ nguyên", "Truncated code placeholder"),
]

print("=== SCANNING FOR FORBIDDEN / LEGACY PATTERNS ===")
findings = []

for filename in files:
    filepath = os.path.join(TARGET_DIR, filename)
    if not os.path.exists(filepath):
        continue
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    for line_idx, line in enumerate(lines, 1):
        for pat, desc in forbidden_patterns:
            matches = re.finditer(pat, line, re.IGNORECASE)
            for m in matches:
                # Check if it's explicitly saying "ĐÃ LOẠI BỎ" or "KHÔNG SỬ DỤNG"
                # Let's inspect context
                context = line.strip()
                findings.append({
                    "file": filename,
                    "line": line_idx,
                    "pattern": pat,
                    "description": desc,
                    "matched": m.group(0),
                    "context": context
                })

print(f"Total potential occurrences found: {len(findings)}")
for f in findings:
    print(f"- [{f['file']}:{f['line']}] {f['description']} -> matched '{f['matched']}':\n    Context: {f['context']}")

with open(r"d:\Idea_DoAn\.agents\challenger_2\legacy_scan.json", "w", encoding="utf-8") as jf:
    import json
    json.dump(findings, jf, indent=2, ensure_ascii=False)
