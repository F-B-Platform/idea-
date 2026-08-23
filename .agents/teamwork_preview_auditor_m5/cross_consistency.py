import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

TARGET_DIR = r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai"
FILES = [
    "01_Phan_Tich_Yeu_Cau.md",
    "02_Thiet_Ke_Database.md",
    "03_Thiet_Ke_API_Contract.md",
    "04_Thiet_Ke_UI_UX.md",
    "05_Quy_Trinh_Backend.md",
    "06_Quy_Trinh_Frontend.md",
    "07_Ke_Hoach_Kiem_Thu.md",
    "08_Trien_Khai_He_Thong.md",
    "README.md"
]

def cross_file_consistency():
    print("=== CROSS-FILE CONSISTENCY FORENSIC CHECK ===")
    
    # 1. Check Delivery fee consistency: 20k / 20000 across files
    print("\n--- 1. Delivery Fee (20k VND) ---")
    for fname in FILES:
        fpath = os.path.join(TARGET_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        has_20k = bool(re.search(r"20\.?000|20k", content, re.IGNORECASE))
        has_delivery = bool(re.search(r"delivery|giao\s+hàng", content, re.IGNORECASE))
        print(f"  {fname:30}: has_delivery={has_delivery} | has_20k={has_20k}")

    # 2. Check 10 cups loyalty consistency across files
    print("\n--- 2. Loyalty (10 cups = 1 free) ---")
    for fname in FILES:
        fpath = os.path.join(TARGET_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        has_10_cups = bool(re.search(r"10\s*ly|10\s*cốc|10_cups", content, re.IGNORECASE))
        has_takeaway = bool(re.search(r"takeaway|mang\s+về", content, re.IGNORECASE))
        print(f"  {fname:30}: has_takeaway={has_takeaway} | has_10_cups={has_10_cups}")

    # 3. Check WiFi-locked attendance (BSSID + IP Subnet)
    print("\n--- 3. WiFi Attendance (BSSID + Subnet) ---")
    for fname in FILES:
        fpath = os.path.join(TARGET_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        has_bssid = bool(re.search(r"bssid", content, re.IGNORECASE))
        has_subnet = bool(re.search(r"subnet|ip_subnet|dải\s+ip", content, re.IGNORECASE))
        print(f"  {fname:30}: has_bssid={has_bssid} | has_subnet={has_subnet}")

    # 4. Check Dine-In 2 branches (Branch 1 vs Branch 2 / VietQR vs Cash)
    print("\n--- 4. Dine-In 2 Branches (VietQR vs Cash Postpay) ---")
    for fname in FILES:
        fpath = os.path.join(TARGET_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        has_dinein_branches = bool(re.search(r"2\s+nhánh|nhánh\s+A|nhánh\s+1|trả\s+trước.*trả\s+sau", content, re.IGNORECASE))
        print(f"  {fname:30}: has_dinein_branches={has_dinein_branches}")

cross_file_consistency()
