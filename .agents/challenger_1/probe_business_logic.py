import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

DIAG_DIR = r"d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams"

def read_file(name):
    with open(os.path.join(DIAG_DIR, name), "r", encoding="utf-8") as f:
        return f.read()

f01 = read_file("01_Kien_Truc_Tong_Quan.md")
f02 = read_file("02_Sequence_Diagrams.md")
f03 = read_file("03_ERD_Database_Diagram.md")
f04 = read_file("04_Deployment_Diagram.md")

print("=================================================================")
print("  PROBING 1: RACE CONDITIONS & CONCURRENCY DEEP DIVE             ")
print("=================================================================")

# Extract Seq-01 to Seq-03 details
def print_section_concurrency(seq_title, text):
    print(f"\n--- {seq_title} ---")
    lines = text.split('\n')
    for l in lines:
        if any(k in l.lower() for k in ['redlock', 'lock', 'mutex', 'setnx', 'idempotent', 'idempotency', '409', 'rollback', 'release', 'lua', 'atomicity', 'transaction', 'pendingpayment']):
            print(f"  {l.strip()}")

# Seq-01
m1 = re.search(r'# 1\. SEQ-01:.*?(?=# 2\. SEQ-02:)', f02, re.DOTALL)
if m1:
    print_section_concurrency("SEQ-01 Dine-In VietQR", m1.group(0))

# Seq-02
m2 = re.search(r'# 2\. SEQ-02:.*?(?=# 3\. SEQ-03:)', f02, re.DOTALL)
if m2:
    print_section_concurrency("SEQ-02 Dine-In Cash", m2.group(0))

# Seq-03
m3 = re.search(r'# 3\. SEQ-03:.*?(?=# 4\. SEQ-04:)', f02, re.DOTALL)
if m3:
    print_section_concurrency("SEQ-03 QR Delivery", m3.group(0))

# Seq-06
m6 = re.search(r'# 6\. SEQ-06:.*?(?=# 7\. SEQ-07:)', f02, re.DOTALL)
if m6:
    print_section_concurrency("SEQ-06 KDS 86-Toggle & BOM", m6.group(0))

print("\n=================================================================")
print("  PROBING 2: SPECIFIC BUSINESS RULES V2.5.0 CHECK                ")
print("=================================================================")

# Seq-05 Attendance
m5 = re.search(r'# 5\. SEQ-05:.*?(?=# 6\. SEQ-06:)', f02, re.DOTALL)
if m5:
    print("\n--- SEQ-05 WiFi Attendance ---")
    for l in m5.group(0).split('\n'):
        if any(k in l.lower() for k in ['bssid', 'ssid', 'subnet', 'ip', 'wifi', 'gps']):
            print(f"  {l.strip()}")

# Seq-08 Rating
m8 = re.search(r'# 8\. SEQ-08:.*?(?=# 9\. SEQ-09:)', f02, re.DOTALL)
if m8:
    print("\n--- SEQ-08 Rating & Red Alert ---")
    for l in m8.group(0).split('\n'):
        if any(k in l.lower() for k in ['red alert', 'urgent', 'rating', 'star', 'sao', '<= 2', 'sentiment']):
            print(f"  {l.strip()}")

# Seq-09 Z-Report
m9 = re.search(r'# 9\. SEQ-09:.*?(?=# 10\. SEQ-10:)', f02, re.DOTALL)
if m9:
    print("\n--- SEQ-09 Z-Report & 50k Discrepancy ---")
    for l in m9.group(0).split('\n'):
        if any(k in l.lower() for k in ['50.000', '50k', '50000', 'z-report', 'discrepancy', 'giải trình', 'chênh lệch']):
            print(f"  {l.strip()}")

# Seq-04 Loyalty
m4 = re.search(r'# 4\. SEQ-04:.*?(?=# 5\. SEQ-05:)', f02, re.DOTALL)
if m4:
    print("\n--- SEQ-04 Takeaway & Loyalty 10 cups ---")
    for l in m4.group(0).split('\n'):
        if any(k in l.lower() for k in ['10 ly', '10 cups', 'loyalty', 'tích điểm', 'stamp', 'voucher', 'thưởng']):
            print(f"  {l.strip()}")
