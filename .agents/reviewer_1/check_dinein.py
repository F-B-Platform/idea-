import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
DOCS_DIR = r"d:\Idea_DoAn"

def check_dine_in_details():
    print("=== DINE-IN FLOW DETAILED VERIFICATION ===")
    files = [
        "01_Tai_Lieu_Dac_Ta_Goc/Smart_FB_Operating_System.md",
        "01_Tai_Lieu_Dac_Ta_Goc/Workflow_Quy_Trinh_Nghiep_Vu.md",
        "03_Quy_Trinh_Trien_Khai/01_Phan_Tich_Yeu_Cau.md",
        "03_Quy_Trinh_Trien_Khai/03_Thiet_Ke_API_Contract.md",
        "04_Thiet_Ke_Kien_Truc_Diagrams/02_Sequence_Diagrams.md",
        "05_Quy_Chuan_&_Test_Cases/UAT_Test_Cases.md"
    ]
    for rel in files:
        full = os.path.join(DOCS_DIR, rel.replace("/", os.sep))
        with open(full, "r", encoding="utf-8", errors="ignore") as fp:
            content = fp.read()
        print(f"\n--- File: {rel} ---")
        # Find lines mentioning PendingPayment, VietQR, Kitchen KDS
        matches = re.findall(r".*(?:PendingPayment|VietQR|thanh toán trước|KDS|bếp nhận đơn).*", content, re.IGNORECASE)
        print(f"Found {len(matches)} matching lines. Samples:")
        for m in matches[:5]:
            print("  *", m.strip()[:110])

check_dine_in_details()
