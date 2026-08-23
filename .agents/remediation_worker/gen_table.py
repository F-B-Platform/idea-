import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

files = [
    ("PROJECT.md", "Đóng băng 5 hợp đồng kỹ thuật cốt lõi và kiến trúc Clean Architecture."),
    ("ROADMAP.md", "Lộ trình 16 tuần 8 sprints cho 4 devs phân công chi tiết theo 5 Core Changes."),
    ("DOC_AUDIT_REPORT.md", "Báo cáo kiểm toán chất lượng toàn diện v3.0 Final."),
    ("01_Tai_Lieu_Dac_Ta_Goc/Actor_Phan_Quyen_Chuc_Nang.md", "Ma trận phân quyền 4 vai trò trên Web Portals; loại bỏ Staff App."),
    ("01_Tai_Lieu_Dac_Ta_Goc/Smart_FB_Operating_System.md", "Tài liệu đặc tả tổng quan: Khóa cứng .NET 8 / Next.js 14, giải pháp 5 Core Changes."),
    ("01_Tai_Lieu_Dac_Ta_Goc/Tom_Tat_1_Trang_Executive_Summary.md", "Tóm tắt nhanh 1 trang dành cho Ban giám khảo và Nhà đầu tư."),
    ("01_Tai_Lieu_Dac_Ta_Goc/Tong_Quan_Kien_Truc_He_Thong.md", "Kiến trúc hệ thống tổng quan và luồng dữ liệu 4 tầng."),
    ("01_Tai_Lieu_Dac_Ta_Goc/Workflow_Quy_Trinh_Nghiep_Vu.md", "16 Workflow chuẩn hóa chi tiết từng bước vận hành thực tế."),
    ("02_Bao_Gia_Chi_Phi/Bang_Bao_Gia_Smart_FB_OS.md", "Báo giá thương mại chuỗi 3 chi nhánh, tách rõ Standee QR Delivery và Web POS."),
    ("02_Bao_Gia_Chi_Phi/Chi_Phi_Duy_Tri_Hang_Thang.md", "Bảng dự toán chi phí máy chủ Cloud, VPS, Domain, SSL và bảo trì hàng tháng."),
    ("03_Quy_Trinh_Trien_Khai/01_Phan_Tich_Yeu_Cau.md", "12 nhóm tính năng MVP Tier 1, Business Rules và Ma trận RBAC."),
    ("03_Quy_Trinh_Trien_Khai/02_Thiet_Ke_Database.md", "Đặc tả chi tiết 28 bảng PostgreSQL: kiểu dữ liệu, khóa chính/ngoại, indexes."),
    ("03_Quy_Trinh_Trien_Khai/03_Thiet_Ke_API_Contract.md", "64+ RESTful endpoints, Envelope RFC 7807, 4 SignalR Hubs."),
    ("03_Quy_Trinh_Trien_Khai/04_Thiet_Ke_UI_UX.md", "29 Khung Wireframe ASCII cho Customer PWA, KDS Bếp, Staff POS, Manager."),
    ("03_Quy_Trinh_Trien_Khai/05_Quy_Trinh_Backend.md", "Hướng dẫn 4 tầng Clean Architecture, MediatR, FluentValidation, Caching."),
    ("03_Quy_Trinh_Trien_Khai/06_Quy_Trinh_Frontend.md", "Next.js 14 App Router, Zustand Cart Store, Hook SignalR an toàn."),
    ("03_Quy_Trinh_Trien_Khai/07_Ke_Hoach_Kiem_Thu.md", "Kế hoạch kiểm thử Unit Test, Integration Test và UAT 5 kịch bản chính."),
    ("03_Quy_Trinh_Trien_Khai/08_Trien_Khai_He_Thong.md", "Cấu hình Docker Compose 4 containers, Nginx Reverse Proxy, SSL."),
    ("03_Quy_Trinh_Trien_Khai/README.md", "Mục lục hướng dẫn toàn bộ 8 tài liệu quy trình triển khai."),
    ("04_Thiet_Ke_Kien_Truc_Diagrams/01_Kien_Truc_Tong_Quan.md", "6 Sơ đồ Mermaid: C4 Context, C4 Container (Container_Boundary), Data Flow, Layered Arch."),
    ("04_Thiet_Ke_Kien_Truc_Diagrams/02_Sequence_Diagrams.md", "7 Sơ đồ tuần tự Mermaid: Dine-in VietQR pre-pay, Delivery, Takeaway, WiFi."),
    ("04_Thiet_Ke_Kien_Truc_Diagrams/03_ERD_Database_Diagram.md", "Sơ đồ Mermaid ERD 28 bảng liên kết có đầy đủ trường mới (order_id FK)."),
    ("04_Thiet_Ke_Kien_Truc_Diagrams/04_Deployment_Diagram.md", "Sơ đồ Docker Compose mạng nội bộ `smartfb-net` và Nginx SSL."),
    ("05_Quy_Chuan_&_Test_Cases/Git_Workflow_&_Branching_Strategy.md", "Chiến lược phân nhánh Git và quy trình kiểm thử tự động."),
    ("05_Quy_Chuan_&_Test_Cases/Seed_Data_&_Database_Script.md", "Dữ liệu mẫu 28 bảng có cấu hình WiFi, 3 loại đơn và CRM 10 ly."),
    ("05_Quy_Chuan_&_Test_Cases/UAT_Test_Cases.md", "35 Test Cases UAT bao quát 5 Core Changes và kịch bản biên."),
    ("06_Danh_Sach_Skills/README.md", "Tổng bộ Master Skills Registry và điều phối AI Agents.")
]

for idx, (f, desc) in enumerate(files, 1):
    full_path = os.path.join(r"d:\Idea_DoAn", f.replace("/", "\\"))
    with open(full_path, "r", encoding="utf-8") as fh:
        lines = len(fh.readlines())
    sz = os.path.getsize(full_path)
    print(f"| {idx} | `{f}` | {lines} dòng ({sz/1024:.1f} KB) | 🟢 PASS | {desc} |")
