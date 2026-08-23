import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT = r"d:\Idea_DoAn"
EXCLUDES = [".agents", ".git"]

files_with_delivery = []
files_with_wifi = []
files_with_prepay = []
files_with_takeaway_pos = []

for dirpath, dirnames, filenames in os.walk(ROOT):
    parts = dirpath.split(os.sep)
    if any(ex in parts for ex in EXCLUDES):
        continue
    for f in filenames:
        if f.endswith(".md"):
            p = os.path.join(dirpath, f)
            with open(p, "r", encoding="utf-8", errors="ignore") as fp:
                txt = fp.read()
            rel = os.path.relpath(p, ROOT)
            
            if re.search(r'delivery_address|20\.000|20000|phí ship|QR Delivery', txt, re.IGNORECASE):
                files_with_delivery.append(rel)
            if re.search(r'WiFi|SSID|BSSID|chấm công.*WiFi|WiFi-locked', txt, re.IGNORECASE):
                files_with_wifi.append(rel)
            if re.search(r'PendingPayment|trả trước|thanh toán trước|VietQR.*trước', txt, re.IGNORECASE):
                files_with_prepay.append(rel)
            if re.search(r'10 ly.*(?:tặng|miễn phí)|CupBalance|Takeaway.*POS|tra cứu SĐT', txt, re.IGNORECASE):
                files_with_takeaway_pos.append(rel)

print(f"Delivery files count: {len(files_with_delivery)}")
print(f"WiFi attendance files count: {len(files_with_wifi)}")
print(f"Pre-payment files count: {len(files_with_prepay)}")
print(f"Takeaway POS / 10-cup Loyalty files count: {len(files_with_takeaway_pos)}")
