import os
import re

ROOT = r"d:\Idea_DoAn"
EXCLUDES = [".agents", ".git"]

md_files = []
for dirpath, dirnames, filenames in os.walk(ROOT):
    # filter excludes
    parts = dirpath.split(os.sep)
    if any(ex in parts for ex in EXCLUDES):
        continue
    for f in filenames:
        if f.endswith(".md"):
            md_files.append(os.path.join(dirpath, f))

print(f"Total markdown files found: {len(md_files)}")

results = []
for p in sorted(md_files):
    rel = os.path.relpath(p, ROOT)
    with open(p, "r", encoding="utf-8", errors="ignore") as fp:
        content = fp.read()
    lines = content.splitlines()
    size = os.path.getsize(p)
    
    # checks
    has_todo = bool(re.search(r'\b(TODO|TBD|\/\* rest of code \*\/|\/\/ \.\.\.)\b', content, re.IGNORECASE))
    
    # check 5 core business terms
    has_prepay = bool(re.search(r'PendingPayment|trả trước|thanh toán trước|VietQR', content, re.IGNORECASE))
    has_delivery = bool(re.search(r'Delivery|giao hàng|20\.000|20000|phí ship', content, re.IGNORECASE))
    has_takeaway = bool(re.search(r'Takeaway|mang về|10 ly|CupBalance|quầy POS', content, re.IGNORECASE))
    has_wifi = bool(re.search(r'WiFi|BSSID|SSID|Subnet|chấm công', content, re.IGNORECASE))
    
    # check obsolete forbidden terms
    has_staff_app = bool(re.search(r'Staff\s+Mobile\s+App|Staff\s+App\s*\(Mobile\)|app\s+nhân\s+viên\s+phục\s+vụ', content, re.IGNORECASE))
    has_gps_attendance = bool(re.search(r'GPS\s+50m|bán\s+kính\s+50m|QR\s+động\s+30\s*s|QR\s+đổi\s+30\s*giây', content, re.IGNORECASE))
    has_dinein_postpay = bool(re.search(r'yêu\s+cầu\s+bill\s+.*mang\s+ra\s+bàn|ăn\s+xong\s+mới\s+thanh\s+toán', content, re.IGNORECASE))
    
    # mermaid blocks
    mermaid_blocks = re.findall(r'```mermaid\s+(.*?)\s+```', content, re.DOTALL)
    
    results.append({
        "rel": rel,
        "lines": len(lines),
        "size": size,
        "mermaid_count": len(mermaid_blocks),
        "has_todo": has_todo,
        "has_prepay": has_prepay,
        "has_delivery": has_delivery,
        "has_takeaway": has_takeaway,
        "has_wifi": has_wifi,
        "has_staff_app": has_staff_app,
        "has_gps_attendance": has_gps_attendance,
        "has_dinein_postpay": has_dinein_postpay
    })

print(f"{'File':<55} | {'Lines':<6} | {'Bytes':<7} | {'Mermaid':<7} | {'Forbidden':<9}")
print("-" * 95)
for r in results:
    forbidden = []
    if r['has_staff_app']: forbidden.append("StaffApp")
    if r['has_gps_attendance']: forbidden.append("GPS50m")
    if r['has_dinein_postpay']: forbidden.append("DineInPostpay")
    forb_str = ",".join(forbidden) if forbidden else "None (CLEAN)"
    print(f"{r['rel']:<55} | {r['lines']:<6} | {r['size']:<7} | {r['mermaid_count']:<7} | {forb_str:<9}")
