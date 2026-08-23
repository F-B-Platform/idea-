import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
DOCS_DIR = r"d:\Idea_DoAn"

def validate_all():
    print("================================================================================")
    print("         SMART F&B OS DOCUMENTATION OVERHAUL — RIGOROUS VALIDATION SUITE        ")
    print("================================================================================")
    
    sections = [
        ("01_Tai_Lieu_Dac_Ta_Goc", [
            "Smart_FB_Operating_System.md",
            "Actor_Phan_Quyen_Chuc_Nang.md",
            "Tom_Tat_1_Trang_Executive_Summary.md",
            "Tong_Quan_Kien_Truc_He_Thong.md",
            "Workflow_Quy_Trinh_Nghiep_Vu.md"
        ]),
        ("02_Bao_Gia_Chi_Phi", [
            "Bang_Bao_Gia_Smart_FB_OS.md",
            "Chi_Phi_Duy_Tri_Hang_Thang.md"
        ]),
        ("03_Quy_Trinh_Trien_Khai", [
            "01_Phan_Tich_Yeu_Cau.md",
            "02_Thiet_Ke_Database.md",
            "03_Thiet_Ke_API_Contract.md",
            "04_Thiet_Ke_UI_UX.md",
            "05_Quy_Trinh_Backend.md",
            "06_Quy_Trinh_Frontend.md",
            "07_Ke_Hoach_Kiem_Thu.md",
            "08_Trien_Khai_He_Thong.md",
            "README.md"
        ]),
        ("04_Thiet_Ke_Kien_Truc_Diagrams", [
            "01_Kien_Truc_Tong_Quan.md",
            "02_Sequence_Diagrams.md",
            "03_ERD_Database_Diagram.md",
            "04_Deployment_Diagram.md"
        ]),
        ("05_Quy_Chuan_&_Test_Cases", [
            "Git_Workflow_&_Branching_Strategy.md",
            "Seed_Data_&_Database_Script.md",
            "UAT_Test_Cases.md"
        ]),
        ("06_Danh_Sach_Skills", [
            "README.md"
        ]),
        ("", [
            "ROADMAP.md",
            "DOC_AUDIT_REPORT.md",
            "PROJECT.md"
        ])
    ]
    
    audit_results = []
    
    for folder, files in sections:
        print(f"\n--- Checking Folder: {folder or 'Root'} ---")
        for f in files:
            rel = os.path.join(folder, f) if folder else f
            full = os.path.join(DOCS_DIR, rel.replace("/", os.sep))
            if not os.path.exists(full):
                print(f"❌ [MISSING] {rel}")
                audit_results.append((rel, "MISSING", 0, []))
                continue
            
            with open(full, "r", encoding="utf-8", errors="ignore") as fp:
                lines = fp.readlines()
                content = "".join(lines)
                
            line_count = len(lines)
            byte_count = len(content.encode('utf-8'))
            
            # Checks
            checks = {
                "DineIn_Prepay": bool(re.search(r"PendingPayment|VietQR.*(trước|bếp)|thanh toán.*trước", content, re.IGNORECASE)),
                "Delivery_20k": bool(re.search(r"Delivery.*20\.000|20,000.*ship|delivery_fee|delivery_address", content, re.IGNORECASE)),
                "Takeaway_POS": bool(re.search(r"TakeAway|Takeaway.*(quầy|POS|10 ly|CRM)", content, re.IGNORECASE)),
                "WiFi_Attendance": bool(re.search(r"WiFi.*(BSSID|Subnet|chấm công)|chấm công.*WiFi", content, re.IGNORECASE)),
                "Web_Portals": bool(re.search(r"Web Portals|Next\.js 14|PWA|KDS|Counter POS", content, re.IGNORECASE)),
                "Scale_Up": bool(re.search(r"Scale[\s\-]Up|Future Work|Tương lai|Mở rộng", content, re.IGNORECASE))
            }
            
            print(f"  📄 {rel:50} | {line_count:4} lines | {byte_count:6} bytes | Checks: {sum(checks.values())}/6")
            audit_results.append((rel, "OK", line_count, checks))

    print("\n================================================================================")
    print("                         DETAILED SECTION-BY-SECTION REVIEW                     ")
    print("================================================================================")

if __name__ == "__main__":
    validate_all()
