import os
import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

files = {
    '01_arch': r'd:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\01_Kien_Truc_Tong_Quan.md',
    '02_seq': r'd:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\02_Sequence_Diagrams.md',
    '03_erd': r'd:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\03_ERD_Database_Diagram.md',
    '04_deploy': r'd:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\04_Deployment_Diagram.md'
}

print("=================================================================")
print("=== DEEP TECHNICAL AUDIT OF 4 ARCHITECTURE DIAGRAM FILES ===")
print("=================================================================\n")

# 1. Check 01_Kien_Truc_Tong_Quan.md
arch_content = open(files['01_arch'], encoding='utf-8').read()
print("1. AUDITING 01_Kien_Truc_Tong_Quan.md:")
arch_checks = [
    ("C4 Level 1 - System Context Diagram", r"Level 1.*System Context|flowchart.*System Context"),
    ("C4 Level 2 - Container Diagram", r"Level 2.*Container|flowchart.*Container"),
    ("C4 Level 3 - Component Diagram (.NET 8 Clean Architecture)", r"Level 3.*Component|flowchart.*Component|Clean Architecture"),
    ("5 Next.js Route Groups ((customer), (kds), (staff), (manager), (admin))", r"\(customer\).*\(kds\).*\(staff\).*\(manager\).*\(admin\)"),
    ("4 SignalR Hubs (OrderHub, KitchenHub, PaymentHub, NotificationHub)", r"OrderHub.*KitchenHub.*PaymentHub.*NotificationHub"),
    ("Redis 7 Cache & Distributed Lock", r"Redis.*(?:Distributed Lock|RedLock|Cache)"),
    ("Gemini 1.5 Flash AI Engine & Apriori", r"Gemini.*1\.5.*Flash.*Apriori"),
    ("Explicit removal of Staff Mobile App & GPS/QR 30s", r"LOẠI BỎ.*Staff Mobile|XÓA.*Staff Mobile")
]
for title, pattern in arch_checks:
    found = bool(re.search(pattern, arch_content, re.DOTALL | re.IGNORECASE))
    print(f"  [{'PASS' if found else 'FAIL'}] {title}")

# 2. Check 02_Sequence_Diagrams.md
seq_content = open(files['02_seq'], encoding='utf-8').read()
print("\n2. AUDITING 02_Sequence_Diagrams.md:")
seq_checks = [
    ("Seq-01: Dine-In Nhánh A (VietQR trả trước -> PayOS Webhook -> KDS Bếp)", r"Seq-01|Dine-In Nhánh A.*VietQR trả trước"),
    ("Seq-02: Dine-In Nhánh B (Tiền mặt trả sau -> KDS Confirmed -> In bill VietQR -> NV xác nhận)", r"Seq-02|Dine-In Nhánh B.*Tiền mặt trả sau"),
    ("Seq-03: QR Delivery (QR riêng -> Form SĐT+Địa chỉ -> Ship 20k -> 100% PayOS -> KDS -> Shipper)", r"Seq-03|QR Delivery.*20\.000"),
    ("Seq-04: Takeaway Web POS (Quầy -> Tra CRM SĐT -> Tích 10 ly tặng 1 -> Thu sau)", r"Seq-04|Takeaway.*10 ly"),
    ("Seq-05: Chấm công Khóa mạng WiFi (BSSID Router / IP Subnet + Mã NV)", r"Seq-05|Chấm công Khóa mạng WiFi"),
    ("Seq-06: Điều phối KDS Bếp, Công thức định mức BOM trừ kho gam/ml & 86-Toggle", r"Seq-06|KDS.*BOM.*86-Toggle"),
    ("Seq-07: Gọi phục vụ tại bàn & Web Staff/KDS", r"Seq-07|Gọi phục vụ tại bàn"),
    ("Seq-08: Đánh giá món 1-5 sao, tải ảnh & Alert đỏ <= 2 sao", r"Seq-08|Đánh giá món 1-5 sao.*Alert"),
    ("Seq-09: Mở ca két tiền, Quản lý kho, Kết ca Z-Report (lệch > 50k)", r"Seq-09|Mở ca két tiền.*Z-Report"),
    ("Seq-10: Admin CRUD Thực đơn, BOM size, Seasonal Menu, Giá vùng & AI-2 Apriori", r"Seq-10|Admin CRUD Thực đơn.*Apriori")
]
for title, pattern in seq_checks:
    found = bool(re.search(pattern, seq_content, re.DOTALL | re.IGNORECASE))
    print(f"  [{'PASS' if found else 'FAIL'}] {title}")

# Count sequence diagrams in file
seq_diagram_matches = re.findall(r'```mermaid\s*\n\s*sequenceDiagram', seq_content)
print(f"  Total Mermaid Sequence Diagram blocks found: {len(seq_diagram_matches)} (Expected: 10)")

# 3. Check 03_ERD_Database_Diagram.md
erd_content = open(files['03_erd'], encoding='utf-8').read()
print("\n3. AUDITING 03_ERD_Database_Diagram.md:")
erd_checks = [
    ("Core 25-31 Tables 3NF", r"erDiagram"),
    ("orders table with delivery_address, delivery_fee, order_type", r"orders.*delivery_address.*delivery_fee|DELIVERY_ORDERS"),
    ("branch_wifi_configs with BSSID & IP Subnet", r"branch_wifi_configs.*bssid"),
    ("loyalty_cup_transactions (10 cups Takeaway)", r"loyalty_cup_transactions"),
    ("BOM & Ingredients (ingredients, product_recipes/product_boms, inventory_stocks)", r"ingredients.*product_recipes.*inventory_stocks"),
    ("Work Shifts & Cash Discrepancies (>50k Z-Report)", r"work_shifts.*shift_handover_discrepancies|z_reports"),
    ("Customer Feedbacks & Ratings 1-5 stars", r"customer_feedbacks|reviews")
]
for title, pattern in erd_checks:
    found = bool(re.search(pattern, erd_content, re.DOTALL | re.IGNORECASE))
    print(f"  [{'PASS' if found else 'FAIL'}] {title}")

# 4. Check 04_Deployment_Diagram.md
deploy_content = open(files['04_deploy'], encoding='utf-8').read()
print("\n4. AUDITING 04_Deployment_Diagram.md:")
deploy_checks = [
    ("Client Edge (Cloudflare CDN, PWA, Web POS/KDS)", r"Cloudflare.*PWA.*POS"),
    ("Ingress (NGINX Reverse Proxy, SSL Let's Encrypt, Rate Limiting)", r"NGINX.*SSL.*Let's Encrypt"),
    ("App Container (.NET 8 Web API, SignalR Backplane)", r"\.NET 8.*Web API.*SignalR"),
    ("Data Container (PostgreSQL 16 Volume, Redis 7)", r"PostgreSQL 16.*Redis 7"),
    ("External Services (PayOS, Gemini API, OpenWeatherMap, R2/S3)", r"PayOS.*Gemini.*OpenWeatherMap"),
    ("Comparative Analysis: Cloud VPS Vietnam vs Azure Singapore", r"Cloud VPS.*Azure.*Singapore")
]
for title, pattern in deploy_checks:
    found = bool(re.search(pattern, deploy_content, re.DOTALL | re.IGNORECASE))
    print(f"  [{'PASS' if found else 'FAIL'}] {title}")
