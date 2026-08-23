import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
DOCS_DIR = r"d:\Idea_DoAn"

patterns = [
    (r'\bStaff Mobile App\b', "Staff Mobile App"),
    (r'\bStaff App\b', "Staff App"),
    (r'\bGPS 50m\b', "GPS 50m"),
    (r'\bGPS lock\b', "GPS lock"),
    (r'QR động 30', "QR dong 30s"),
    (r'30s rotating QR', "30s rotating QR"),
    (r'thanh toán sau khi dùng', "thanh toan sau khi dung"),
    (r'khách yêu cầu bill', "khach yeu cau bill")
]

findings = []
for root, dirs, files in os.walk(DOCS_DIR):
    if ".agents" in root or ".git" in root:
        continue
    for f in files:
        if not f.endswith(".md"):
            continue
        path = os.path.join(root, f)
        rel = os.path.relpath(path, DOCS_DIR)
        with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
            lines = fp.readlines()
        for idx, line in enumerate(lines, 1):
            for pat, label in patterns:
                if re.search(pat, line, re.IGNORECASE):
                    clean = line.strip()
                    findings.append((rel, idx, label, clean))

print(f"Total occurrences of checked phrases: {len(findings)}")
for rel, idx, label, clean in findings:
    print(f"[{label:25}] {rel:50} : {idx:4} -> {clean}")
