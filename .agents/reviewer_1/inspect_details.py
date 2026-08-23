import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
DOCS_DIR = r"d:\Idea_DoAn"

def inspect_details():
    print("=== INSPECTING DETAILED SECTIONS ===")
    
    # 1. 03_Thiet_Ke_API_Contract.md - Takeaway endpoints
    p_api = os.path.join(DOCS_DIR, "03_Quy_Trinh_Trien_Khai", "03_Thiet_Ke_API_Contract.md")
    with open(p_api, "r", encoding="utf-8", errors="ignore") as fp:
        c_api = fp.read()
    print("--- API Contract: Takeaway endpoints ---")
    matches = re.findall(r"(?:###.*?takeaway|POST /api/v1/orders/take-away|POST /api/v1/orders/takeaway|POST /api/v1/orders/pos).*?(?=\n###|\Z)", c_api, re.IGNORECASE | re.DOTALL)
    for m in matches:
        print(m[:400])
        print("...")

    # 2. 05_Quy_Chuan_&_Test_Cases/Seed_Data_&_Database_Script.md - Employee & Attendance Seed
    p_seed = os.path.join(DOCS_DIR, "05_Quy_Chuan_&_Test_Cases", "Seed_Data_&_Database_Script.md")
    with open(p_seed, "r", encoding="utf-8", errors="ignore") as fp:
        c_seed = fp.read()
    print("\n--- Seed Data: Attendance & Branch & Orders ---")
    matches = re.findall(r"INSERT INTO (?:branches|attendances|orders|users).*?;", c_seed, re.IGNORECASE | re.DOTALL)
    for m in matches[:6]:
        print(m[:300])
        print("...")

inspect_details()
