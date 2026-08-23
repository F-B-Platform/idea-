import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
DOCS_DIR = r"d:\Idea_DoAn"

def verify_rules():
    print("================================================================================")
    print("                      CORE BUSINESS RULES DEEP DIVE AUDIT                       ")
    print("================================================================================")
    
    # 1. Delivery
    print("\n--- RULE 2: QR DELIVERY (Address + 20k flat fee + 100% VietQR upfront, No COD) ---")
    files_delivery = [
        "01_Tai_Lieu_Dac_Ta_Goc/Smart_FB_Operating_System.md",
        "01_Tai_Lieu_Dac_Ta_Goc/Workflow_Quy_Trinh_Nghiep_Vu.md",
        "03_Quy_Trinh_Trien_Khai/02_Thiet_Ke_Database.md",
        "03_Quy_Trinh_Trien_Khai/03_Thiet_Ke_API_Contract.md",
        "04_Thiet_Ke_Kien_Truc_Diagrams/02_Sequence_Diagrams.md",
        "04_Thiet_Ke_Kien_Truc_Diagrams/03_ERD_Database_Diagram.md",
        "05_Quy_Chuan_&_Test_Cases/Seed_Data_&_Database_Script.md",
        "05_Quy_Chuan_&_Test_Cases/UAT_Test_Cases.md"
    ]
    for rf in files_delivery:
        path = os.path.join(DOCS_DIR, rf.replace("/", os.sep))
        with open(path, "r", encoding="utf-8", errors="ignore") as fp:
            c = fp.read()
        has_fee = bool(re.search(r"20\.000|20,000|20000", c))
        has_addr = bool(re.search(r"delivery_address|địa chỉ giao|địa chỉ nhận", c, re.IGNORECASE))
        has_vietqr = bool(re.search(r"VietQR.*Delivery|Delivery.*VietQR|100%.*VietQR|không COD|No COD", c, re.IGNORECASE))
        print(f"  {rf:55} | Fee: {has_fee} | Addr: {has_addr} | VietQR: {has_vietqr}")

    # 2. Takeaway Staff POS
    print("\n--- RULE 3: TAKEAWAY STAFF POS (No QR + Phone CRM + 10 cups loyalty + Post-pay) ---")
    files_takeaway = [
        "01_Tai_Lieu_Dac_Ta_Goc/Smart_FB_Operating_System.md",
        "01_Tai_Lieu_Dac_Ta_Goc/Workflow_Quy_Trinh_Nghiep_Vu.md",
        "03_Quy_Trinh_Trien_Khai/02_Thiet_Ke_Database.md",
        "03_Quy_Trinh_Trien_Khai/03_Thiet_Ke_API_Contract.md",
        "04_Thiet_Ke_Kien_Truc_Diagrams/02_Sequence_Diagrams.md",
        "05_Quy_Chuan_&_Test_Cases/UAT_Test_Cases.md"
    ]
    for rf in files_takeaway:
        path = os.path.join(DOCS_DIR, rf.replace("/", os.sep))
        with open(path, "r", encoding="utf-8", errors="ignore") as fp:
            c = fp.read()
        has_no_qr = bool(re.search(r"không dùng QR|loại bỏ QR Takeaway|Giao diện NV|Web POS|Counter POS", c, re.IGNORECASE))
        has_crm = bool(re.search(r"CRM|SĐT|tra cứu SĐT", c, re.IGNORECASE))
        has_loyalty = bool(re.search(r"10 ly|10_cups|LoyaltyCup|tích ly", c, re.IGNORECASE))
        has_postpay = bool(re.search(r"thanh toán sau|tiền mặt|sau khi nhận món", c, re.IGNORECASE))
        print(f"  {rf:55} | NoQR: {has_no_qr} | CRM: {has_crm} | Loyalty: {has_loyalty} | PostPay: {has_postpay}")

    # 3. WiFi-locked Attendance
    print("\n--- RULE 4: WIFI-LOCKED ATTENDANCE (BSSID / Subnet + Employee Code, No GPS 50m / QR 30s) ---")
    files_wifi = [
        "01_Tai_Lieu_Dac_Ta_Goc/Smart_FB_Operating_System.md",
        "01_Tai_Lieu_Dac_Ta_Goc/Workflow_Quy_Trinh_Nghiep_Vu.md",
        "03_Quy_Trinh_Trien_Khai/02_Thiet_Ke_Database.md",
        "03_Quy_Trinh_Trien_Khai/03_Thiet_Ke_API_Contract.md",
        "04_Thiet_Ke_Kien_Truc_Diagrams/02_Sequence_Diagrams.md",
        "04_Thiet_Ke_Kien_Truc_Diagrams/03_ERD_Database_Diagram.md",
        "05_Quy_Chuan_&_Test_Cases/Seed_Data_&_Database_Script.md",
        "05_Quy_Chuan_&_Test_Cases/UAT_Test_Cases.md"
    ]
    for rf in files_wifi:
        path = os.path.join(DOCS_DIR, rf.replace("/", os.sep))
        with open(path, "r", encoding="utf-8", errors="ignore") as fp:
            c = fp.read()
        has_wifi = bool(re.search(r"wifi_bssid|allowed_ip_subnet|BSSID|Subnet", c, re.IGNORECASE))
        has_empid = bool(re.search(r"EmployeeCode|Mã NV|mã số nhân viên", c, re.IGNORECASE))
        has_check = bool(re.search(r"chấm công|attendance|WF-07", c, re.IGNORECASE))
        print(f"  {rf:55} | WiFi BSSID/IP: {has_wifi} | EmpCode: {has_empid} | Attendance: {has_check}")

    # 4. Staff Mobile App Deprecation
    print("\n--- RULE 5: STAFF MOBILE APP DEPRECATION & WEB PORTALS CONSOLIDATION ---")
    files_app = [
        "01_Tai_Lieu_Dac_Ta_Goc/Smart_FB_Operating_System.md",
        "01_Tai_Lieu_Dac_Ta_Goc/Tong_Quan_Kien_Truc_He_Thong.md",
        "03_Quy_Trinh_Trien_Khai/01_Phan_Tich_Yeu_Cau.md",
        "03_Quy_Trinh_Trien_Khai/04_Thiet_Ke_UI_UX.md",
        "03_Quy_Trinh_Trien_Khai/06_Quy_Trinh_Frontend.md",
        "04_Thiet_Ke_Kien_Truc_Diagrams/01_Kien_Truc_Tong_Quan.md",
        "04_Thiet_Ke_Kien_Truc_Diagrams/04_Deployment_Diagram.md",
        "ROADMAP.md"
    ]
    for rf in files_app:
        path = os.path.join(DOCS_DIR, rf.replace("/", os.sep))
        with open(path, "r", encoding="utf-8", errors="ignore") as fp:
            c = fp.read()
        has_web_kds = bool(re.search(r"Web KDS|kds", c, re.IGNORECASE))
        has_web_pos = bool(re.search(r"Web POS|Counter POS|staff", c, re.IGNORECASE))
        has_web_manager = bool(re.search(r"Web Quản trị|Manager Portal|manager|admin", c, re.IGNORECASE))
        print(f"  {rf:55} | KDS: {has_web_kds} | POS: {has_web_pos} | Manager: {has_web_manager}")

if __name__ == "__main__":
    verify_rules()
