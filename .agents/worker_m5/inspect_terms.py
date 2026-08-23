import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT = r"d:\Idea_DoAn"
EXCLUDES = [".agents", ".git"]

patterns = {
    "Staff Mobile App": re.compile(r'(.{0,40}(?:Staff\s+Mobile\s+App|Staff\s+App\s*\(Mobile\)|app\s+nhân\s+viên\s+phục\s+vụ).{0,40})', re.IGNORECASE),
    "GPS 50m": re.compile(r'(.{0,40}(?:GPS\s+50m|bán\s+kính\s+50m|QR\s+động\s+30\s*s|QR\s+đổi\s+30\s*giây).{0,40})', re.IGNORECASE),
    "Dine-in Postpay": re.compile(r'(.{0,40}(?:yêu\s+cầu\s+bill\s+.*mang\s+ra\s+bàn|ăn\s+xong\s+mới\s+thanh\s+toán).{0,40})', re.IGNORECASE),
}

for dirpath, dirnames, filenames in os.walk(ROOT):
    parts = dirpath.split(os.sep)
    if any(ex in parts for ex in EXCLUDES):
        continue
    for f in filenames:
        if f.endswith(".md") and f not in ["DOC_AUDIT_REPORT.md"]:
            p = os.path.join(dirpath, f)
            with open(p, "r", encoding="utf-8", errors="ignore") as fp:
                txt = fp.read()
            rel = os.path.relpath(p, ROOT)
            for name, pat in patterns.items():
                matches = pat.findall(txt)
                if matches:
                    print(f"[{rel}] Matches for '{name}': ({len(matches)} occurrences)")
                    for m in matches[:2]:
                        print(f"   ... {m.strip()} ...")
