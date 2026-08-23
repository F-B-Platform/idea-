import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
DOCS_DIR = r"d:\Idea_DoAn"

# Check canonical files content details
files_to_check = [
    ("01_Tai_Lieu_Dac_Ta_Goc/Smart_FB_Operating_System.md", [
        "Dine-in", "PendingPayment", "VietQR", "QR Delivery", "20.000", "Takeaway", "10 ly", "WiFi", "BSSID", "Scale Up"
    ]),
    ("01_Tai_Lieu_Dac_Ta_Goc/Actor_Phan_Quyen_Chuc_Nang.md", [
        "Customer", "Staff / Barista", "Manager", "Admin", "Takeaway", "WiFi", "KDS"
    ]),
    ("01_Tai_Lieu_Dac_Ta_Goc/Tom_Tat_1_Trang_Executive_Summary.md", [
        "VietQR", "20.000", "Takeaway", "WiFi", "Scale-Up"
    ]),
    ("01_Tai_Lieu_Dac_Ta_Goc/Tong_Quan_Kien_Truc_He_Thong.md", [
        "Clean Architecture", "Next.js", "PostgreSQL", "Redis", "SignalR"
    ]),
    ("01_Tai_Lieu_Dac_Ta_Goc/Workflow_Quy_Trinh_Nghiep_Vu.md", [
        "WF-01", "WF-02", "WF-03", "WF-04", "WF-05", "WF-06", "WF-07", "WF-08",
        "WF-09", "WF-10", "WF-11", "WF-12", "WF-13", "WF-14", "WF-15", "WF-16"
    ]),
    ("02_Bao_Gia_Chi_Phi/Bang_Bao_Gia_Smart_FB_OS.md", [
        "Dine-in", "Delivery", "Takeaway", "WiFi", "Chi phí"
    ]),
    ("02_Bao_Gia_Chi_Phi/Chi_Phi_Duy_Tri_Hang_Thang.md", [
        "Cloud Run", "PostgreSQL", "Redis", "Cloudinary", "Chi phí duy trì"
    ]),
    ("03_Quy_Trinh_Trien_Khai/01_Phan_Tich_Yeu_Cau.md", [
        "FR-", "NFR-", "MVP", "Scale Up"
    ]),
    ("03_Quy_Trinh_Trien_Khai/02_Thiet_Ke_Database.md", [
        "OrderType", "delivery_address", "delivery_fee", "wifi_bssid", "allowed_ip_subnet"
    ]),
    ("03_Quy_Trinh_Trien_Khai/03_Thiet_Ke_API_Contract.md", [
        "/api/v1/orders/dine-in", "/api/v1/orders/delivery", "/api/v1/orders/takeaway", "/api/v1/attendance"
    ]),
    ("03_Quy_Trinh_Trien_Khai/04_Thiet_Ke_UI_UX.md", [
        "Dine-in", "Delivery", "Counter POS", "KDS", "Attendance"
    ]),
    ("03_Quy_Trinh_Trien_Khai/05_Quy_Trinh_Backend.md", [
        "Clean Architecture", ".NET 8", "CQRS", "SignalR", "VietQR"
    ]),
    ("03_Quy_Trinh_Trien_Khai/06_Quy_Trinh_Frontend.md", [
        "Next.js 14", "App Router", "PWA", "Zustand", "Tailwind"
    ]),
    ("03_Quy_Trinh_Trien_Khai/07_Ke_Hoach_Kiem_Thu.md", [
        "Unit Test", "Integration Test", "UAT", "Performance Test"
    ]),
    ("03_Quy_Trinh_Trien_Khai/08_Trien_Khai_He_Thong.md", [
        "Docker", "Cloud Run", "CI/CD", "GitHub Actions"
    ]),
    ("03_Quy_Trinh_Trien_Khai/README.md", [
        "5 Thay đổi cốt lõi", "8 quy trình"
    ]),
    ("04_Thiet_Ke_Kien_Truc_Diagrams/01_Kien_Truc_Tong_Quan.md", [
        "```mermaid", "graph", "C4"
    ]),
    ("04_Thiet_Ke_Kien_Truc_Diagrams/02_Sequence_Diagrams.md", [
        "```mermaid", "sequenceDiagram", "Dine-in", "Delivery", "Takeaway", "Attendance"
    ]),
    ("04_Thiet_Ke_Kien_Truc_Diagrams/03_ERD_Database_Diagram.md", [
        "```mermaid", "erDiagram", "OrderType", "delivery_address", "delivery_fee"
    ]),
    ("04_Thiet_Ke_Kien_Truc_Diagrams/04_Deployment_Diagram.md", [
        "```mermaid", "Cloud Run", "PostgreSQL", "Redis"
    ]),
    ("05_Quy_Chuan_&_Test_Cases/Git_Workflow_&_Branching_Strategy.md", [
        "git flow", "Conventional Commits", "PR Checklist"
    ]),
    ("05_Quy_Chuan_&_Test_Cases/Seed_Data_&_Database_Script.md", [
        "DineIn", "TakeAway", "Delivery", "WiFi", "BSSID"
    ]),
    ("05_Quy_Chuan_&_Test_Cases/UAT_Test_Cases.md", [
        "TC-DINEIN", "TC-DELIVERY", "TC-TAKEAWAY", "TC-ATTENDANCE"
    ]),
    ("06_Danh_Sach_Skills/README.md", [
        "backend-architect", "frontend-developer", "database-design"
    ]),
    ("ROADMAP.md", [
        "16 tuần", "M1", "M2", "M3", "M4", "M5", "M6"
    ]),
    ("DOC_AUDIT_REPORT.md", [
        "Kiểm toán", "5 Thay đổi", "Zero Placeholders"
    ])
]

print("=== VERIFYING CANONICAL FILES CONTENT INTEGRITY ===")
for rel_path, required_terms in files_to_check:
    full_path = os.path.join(DOCS_DIR, rel_path.replace("/", os.sep))
    if not os.path.exists(full_path):
        print(f"❌ {rel_path} MISSING!")
        continue
    with open(full_path, "r", encoding="utf-8", errors="ignore") as fp:
        content = fp.read()
    missing_terms = [t for t in required_terms if not re.search(re.escape(t), content, re.IGNORECASE)]
    if missing_terms:
        print(f"⚠️ {rel_path} missing terms: {missing_terms}")
    else:
        print(f"✅ {rel_path} ({len(content.splitlines())} lines) - All {len(required_terms)} required terms present.")
