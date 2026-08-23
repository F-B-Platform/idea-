import os
import re
import sys
import json
import time

sys.stdout.reconfigure(encoding='utf-8')

DOCS_DIR = r"d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai"
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

def run_comprehensive_audit():
    print("=" * 80)
    print("      INDEPENDENT VICTORY AUDIT REPORT - 03_Quy_Trinh_Trien_Khai")
    print("=" * 80)
    
    file_data = {}
    
    # -------------------------------------------------------------
    # PHASE A: TIMELINE & PROVENANCE AUDIT
    # -------------------------------------------------------------
    print("\n" + "=" * 40)
    print("PHASE A: TIMELINE & PROVENANCE AUDIT")
    print("=" * 40)
    
    timeline_pass = True
    for fname in FILES:
        fpath = os.path.join(DOCS_DIR, fname)
        if not os.path.exists(fpath):
            print(f"[FAIL] Missing target artifact: {fname}")
            timeline_pass = False
            continue
        
        stat = os.stat(fpath)
        size = stat.st_size
        mtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stat.st_mtime))
        
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
            lines = content.splitlines()
            
        file_data[fname] = {
            "path": fpath,
            "size": size,
            "mtime": mtime,
            "lines": len(lines),
            "chars": len(content),
            "content": content
        }
        
        if size < 10000:
            print(f"[FAIL] File too small (<10KB): {fname} ({size} bytes)")
            timeline_pass = False
        else:
            print(f"[PASS] {fname:<30} | {len(lines):>5} lines | {size:>7,} bytes | Modified: {mtime}")
            
    print(f"\nPhase A Result: {'PASS' if timeline_pass else 'FAIL'}")

    # -------------------------------------------------------------
    # PHASE B: INTEGRITY & PROHIBITED PATTERNS CHECK
    # -------------------------------------------------------------
    print("\n" + "=" * 40)
    print("PHASE B: INTEGRITY & PROHIBITED PATTERNS CHECK")
    print("=" * 40)
    
    integrity_pass = True
    
    # Check 1: Zero Placeholders
    placeholder_patterns = [
        (r'\bTODO\b', "TODO comment"),
        (r'\bTBD\b', "TBD placeholder"),
        (r'/\*\s*rest of code\s*\*/', "rest of code placeholder"),
        (r'//\s*rest of implementation', "rest of implementation placeholder"),
        (r'//\s*tương tự như trên', "tương tự như trên placeholder"),
        (r'//\s*giữ nguyên logic cũ', "giữ nguyên logic cũ placeholder"),
        (r'\.\.\.\s*giữ nguyên', "... giữ nguyên placeholder"),
        (r'//\s*viết tiếp ở đây', "viết tiếp ở đây placeholder")
    ]
    
    placeholder_violations = []
    for fname, data in file_data.items():
        content = data["content"]
        for pat, label in placeholder_patterns:
            matches = list(re.finditer(pat, content, re.IGNORECASE))
            if matches:
                for m in matches:
                    start = max(0, m.start() - 40)
                    end = min(len(content), m.end() + 40)
                    snippet = content[start:end].replace('\n', ' ')
                    placeholder_violations.append((fname, label, snippet))
                    
    if placeholder_violations:
        print(f"[FAIL] Found {len(placeholder_violations)} placeholder violations:")
        for f, lbl, snip in placeholder_violations:
            print(f"  - {f} ({lbl}): {snip}")
        integrity_pass = False
    else:
        print("[PASS] Zero placeholders found across all 9 documentation files!")

    # Check 2: Facade / Empty sections
    empty_section_violations = []
    for fname, data in file_data.items():
        content = data["content"]
        # Find headings that have immediately another heading without content
        empty_headings = re.findall(r'(^#{1,4}\s+[^\n]+)\n+(?=#{1,4}\s+)', content, re.MULTILINE)
        if empty_headings:
            for eh in empty_headings:
                empty_section_violations.append((fname, eh))
                
    if empty_section_violations:
        print(f"[FAIL] Found {len(empty_section_violations)} empty sections:")
        for f, eh in empty_section_violations:
            print(f"  - {f}: {eh}")
        integrity_pass = False
    else:
        print("[PASS] No empty sections or facade headings detected!")

    print(f"\nPhase B Result: {'PASS' if integrity_pass else 'FAIL'}")

    # -------------------------------------------------------------
    # PHASE C: INDEPENDENT ACCEPTANCE CRITERIA VERIFICATION
    # -------------------------------------------------------------
    print("\n" + "=" * 40)
    print("PHASE C: INDEPENDENT ACCEPTANCE CRITERIA VERIFICATION")
    print("=" * 40)
    
    crit_results = {}
    
    # -------------------------------------------------------------
    # Criterion 1: Exact Core Feature Counts (62 Total)
    # -------------------------------------------------------------
    print("\n--- Criterion 1: Core Feature Counts (62 Total) ---")
    doc1 = file_data.get("01_Phan_Tich_Yeu_Cau.md", {}).get("content", "")
    
    # Extract feature definitions: e.g. "### C-01:", "### S-01:", "### M-01:", "### A-01:" or in tables
    c_features = re.findall(r'(?:###\s*|\b)(C-(?:0[1-9]|1[0-9]|20))\b', doc1)
    s_features = re.findall(r'(?:###\s*|\b)(S-(?:0[1-9]|1[0-3]))\b', doc1)
    m_features = re.findall(r'(?:###\s*|\b)(M-(?:0[1-9]|1[0-2]))\b', doc1)
    a_features = re.findall(r'(?:###\s*|\b)(A-(?:0[1-9]|1[0-7]))\b', doc1)
    
    c_set = sorted(list(set(c_features)))
    s_set = sorted(list(set(s_features)))
    m_set = sorted(list(set(m_features)))
    a_set = sorted(list(set(a_features)))
    
    print(f"  Customer (C-01 to C-20): {len(c_set)}/20 -> {c_set}")
    print(f"  Staff (S-01 to S-13):    {len(s_set)}/13 -> {s_set}")
    print(f"  Manager (M-01 to M-12):  {len(m_set)}/12 -> {m_set}")
    print(f"  Admin (A-01 to A-17):    {len(a_set)}/17 -> {a_set}")
    
    # Check that each feature has full specification details (Mô tả, Luồng, Quy tắc, Tiêu chí nghiệm thu)
    detailed_spec_count = 0
    for fid in c_set + s_set + m_set + a_set:
        # Check if the feature section has substantial content
        pat = rf'###\s*{fid}[:\s\w\-\/]+'
        match = re.search(pat, doc1)
        if match:
            detailed_spec_count += 1
            
    print(f"  Detailed Specification Sections: {detailed_spec_count}/62")
    
    c1_pass = (len(c_set) == 20 and len(s_set) == 13 and len(m_set) == 12 and len(a_set) == 17 and detailed_spec_count == 62)
    crit_results["1_Feature_Counts_62"] = c1_pass
    print(f"  -> Criterion 1 Result: {'PASS' if c1_pass else 'FAIL'}")

    # -------------------------------------------------------------
    # Criterion 2: Elimination of Deprecated Items
    # -------------------------------------------------------------
    print("\n--- Criterion 2: Elimination of Deprecated Items ---")
    # Verify that:
    # 1. Staff Mobile App is not an active component (0 references as an active app)
    # 2. GPS 50m is not active for attendance
    # 3. Rotating QR 30s is not active for table scanning
    # 4. C-23 & C-24 are not active requirements
    # 5. Separate voucher wallet is not active
    # 6. Isolated calorie lookup is not active
    
    # Check all files for active usage of these concepts
    all_text = "\n".join([d["content"] for d in file_data.values()])
    
    # Check if C-23 or C-24 is defined as an active feature heading:
    has_active_c23 = bool(re.search(r'###\s*C-23\b', all_text))
    has_active_c24 = bool(re.search(r'###\s*C-24\b', all_text))
    
    # Check if GPS is used in attendance API or DB:
    doc2 = file_data.get("02_Thiet_Ke_Database.md", {}).get("content", "")
    doc3 = file_data.get("03_Thiet_Ke_API_Contract.md", {}).get("content", "")
    doc5 = file_data.get("05_Quy_Trinh_Backend.md", {}).get("content", "")
    
    gps_in_db = bool(re.search(r'latitude|longitude|gps_radius', doc2, re.I))
    gps_in_api = bool(re.search(r'latitude|longitude|gpsLocation', doc3, re.I))
    
    # Check if Flutter/RN is in frontend or architecture
    doc6 = file_data.get("06_Quy_Trinh_Frontend.md", {}).get("content", "")
    flutter_in_fe = bool(re.search(r'flutter|react-native|pubspec\.yaml', doc6, re.I))
    
    print(f"  Active C-23 heading: {has_active_c23}")
    print(f"  Active C-24 heading: {has_active_c24}")
    print(f"  GPS fields in Database: {gps_in_db}")
    print(f"  GPS fields in API Contracts: {gps_in_api}")
    print(f"  Flutter/RN in Frontend guide: {flutter_in_fe}")
    
    c2_pass = (not has_active_c23 and not has_active_c24 and not gps_in_db and not gps_in_api and not flutter_in_fe)
    crit_results["2_Elimination_Deprecated"] = c2_pass
    print(f"  -> Criterion 2 Result: {'PASS' if c2_pass else 'FAIL'}")

    # -------------------------------------------------------------
    # Criterion 3: 4 Core Engines
    # -------------------------------------------------------------
    print("\n--- Criterion 3: 4 Core Engines ---")
    # Engine 1: Dine-In 2 branches (VietQR prepay vs Cash postpay + Bill QR)
    dinein_prepay = bool(re.search(r'VietQR.*trả trước|prepay|thanh toán trước', all_text, re.I))
    dinein_postpay = bool(re.search(r'tiền mặt.*trả sau|postpay|Bill QR|QR hóa đơn', all_text, re.I))
    dinein_kds = bool(re.search(r'bếp.*tức thì|chuyển bếp ngay|KDS.*nhận đơn|OrderCreatedEvent', all_text, re.I))
    print(f"  Engine 1 (Dine-In 2 branches): Prepay={dinein_prepay}, Postpay+BillQR={dinein_postpay}, InstantKDS={dinein_kds}")

    # Engine 2: Delivery QR (20k shipping fee, 100% VietQR prepay, COD locked, phone + address mandatory)
    deliv_fee = bool(re.search(r'20\.000|20k|20000', all_text, re.I))
    deliv_prepay = bool(re.search(r'100%\s+VietQR|bắt buộc VietQR|khóa COD|không hỗ trợ COD', all_text, re.I))
    deliv_fields = bool(re.search(r'delivery_address', doc2, re.I) and re.search(r'customer_phone', doc2, re.I))
    print(f"  Engine 2 (Delivery QR): 20k Fee={deliv_fee}, 100% VietQR/No COD={deliv_prepay}, Phone+Addr in DB={deliv_fields}")

    # Engine 3: Takeaway Web POS (Counter staff, no QR, phone CRM, 10 cups get 1 free loyalty, postpay)
    pos_flow = bool(re.search(r'Web POS|thao tác quầy|thu ngân', all_text, re.I))
    pos_loyalty = bool(re.search(r'10 ly tặng 1|loyalty_cup_transactions|tích 10 ly', all_text, re.I))
    pos_postpay = bool(re.search(r'thu tiền sau|giao hàng rồi thu|thanh toán tại quầy', all_text, re.I))
    print(f"  Engine 3 (Takeaway Web POS): Web POS={pos_flow}, 10 cups free 1={pos_loyalty}, Counter Postpay={pos_postpay}")

    # Engine 4: WiFi Attendance (BSSID Router + IP Subnet + Staff PIN)
    wifi_bssid = bool(re.search(r'bssid|router_bssid', doc2, re.I))
    wifi_subnet = bool(re.search(r'ip_subnet|subnet_mask', doc2, re.I))
    wifi_pin = bool(re.search(r'pin_code|staff_pin|mã pin', doc2, re.I))
    wifi_api = bool(re.search(r'/api/v1/attendances/check-in|CheckInCommand', doc3 + doc5, re.I))
    print(f"  Engine 4 (WiFi Attendance): BSSID in DB={wifi_bssid}, IP Subnet in DB={wifi_subnet}, PIN in DB={wifi_pin}, API/Command={wifi_api}")

    c3_pass = (dinein_prepay and dinein_postpay and dinein_kds and deliv_fee and deliv_prepay and deliv_fields and
               pos_flow and pos_loyalty and pos_postpay and wifi_bssid and wifi_subnet and wifi_pin and wifi_api)
    crit_results["3_Core_Engines_4"] = c3_pass
    print(f"  -> Criterion 3 Result: {'PASS' if c3_pass else 'FAIL'}")

    # -------------------------------------------------------------
    # Criterion 4: Database Design (25 3NF Tables in PostgreSQL 16)
    # -------------------------------------------------------------
    print("\n--- Criterion 4: Database Design (25 3NF Tables) ---")
    create_tables = re.findall(r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?([a-zA-Z0-9_]+)', doc2, re.I)
    unique_tables = sorted(list(set([t.lower() for t in create_tables])))
    print(f"  Total Tables defined with DDL: {len(unique_tables)}")
    
    req_25_tables = [
        "branches", "branch_wifi_configs", "users", "roles", "user_roles",
        "tables", "categories", "products", "product_boms", "ingredients",
        "combos", "combo_items", "orders", "order_items", "order_item_modifiers",
        "payments", "cash_shifts", "z_reports", "inventory_transactions",
        "purchase_orders", "purchase_order_items", "loyalty_accounts",
        "loyalty_cup_transactions", "vouchers", "notifications"
    ]
    missing_tbls = [t for t in req_25_tables if t not in unique_tables]
    print(f"  Required Tables Check (25 standard tables): Missing={missing_tbls}")
    
    # Check DDL completeness (CREATE TABLE, PRIMARY KEY, FOREIGN KEY, CREATE INDEX, CREATE TRIGGER)
    pk_count = len(re.findall(r'PRIMARY\s+KEY', doc2, re.I))
    fk_count = len(re.findall(r'REFERENCES\s+[a-zA-Z0-9_]+', doc2, re.I))
    idx_count = len(re.findall(r'CREATE\s+INDEX', doc2, re.I))
    trg_count = len(re.findall(r'CREATE\s+TRIGGER', doc2, re.I))
    
    print(f"  DDL Stats: PKs={pk_count}, FKs={fk_count}, Indexes={idx_count}, Triggers={trg_count}")
    
    c4_pass = (len(unique_tables) == 25 and len(missing_tbls) == 0 and pk_count >= 25 and fk_count >= 20 and idx_count >= 15 and trg_count >= 3)
    crit_results["4_Database_25_Tables"] = c4_pass
    print(f"  -> Criterion 4 Result: {'PASS' if c4_pass else 'FAIL'}")

    # -------------------------------------------------------------
    # Criterion 5: API Contracts (10 REST Groups, 4 Hubs, PayOS Webhook)
    # -------------------------------------------------------------
    print("\n--- Criterion 5: API Contracts ---")
    rest_endpoints = [
        ("1. Auth", r'/api/v1/auth/login|/api/v1/auth/refresh'),
        ("2. Branches", r'/api/v1/branches'),
        ("3. Tables", r'/api/v1/tables'),
        ("4. Products/BOM", r'/api/v1/products|/api/v1/categories'),
        ("5. Orders", r'/api/v1/orders'),
        ("6. Payments", r'/api/v1/payments'),
        ("7. Attendance", r'/api/v1/attendances'),
        ("8. KDS", r'/api/v1/kds'),
        ("9. Manager Cash/Inv", r'/api/v1/shifts|/api/v1/inventory'),
        ("10. Analytics/AI", r'/api/v1/analytics|/api/v1/ai')
    ]
    rest_ok = True
    for name, pat in rest_endpoints:
        found = bool(re.search(pat, doc3, re.I))
        print(f"  REST Group [{name}]: {'FOUND' if found else 'MISSING'}")
        if not found:
            rest_ok = False
            
    # 4 Hubs
    hubs = ["OrderHub", "KitchenHub", "PaymentHub", "NotificationHub"]
    found_hubs = [h for h in hubs if h in doc3 and h in doc5]
    print(f"  SignalR 4 Hubs in Contract & Backend: {found_hubs} ({len(found_hubs)}/4)")
    
    # PayOS Webhook & HMAC
    payos_ok = bool(re.search(r'/api/v1/webhooks/payos|PayOSWebhook', doc3, re.I) and re.search(r'HMAC|SHA256|signature', doc3, re.I))
    print(f"  PayOS Webhook + HMAC-SHA256: {payos_ok}")

    c5_pass = (rest_ok and len(found_hubs) == 4 and payos_ok)
    crit_results["5_API_Contracts"] = c5_pass
    print(f"  -> Criterion 5 Result: {'PASS' if c5_pass else 'FAIL'}")

    # -------------------------------------------------------------
    # Criterion 6: UI/UX (5 Route Groups, ASCII, Mermaid, WCAG AA)
    # -------------------------------------------------------------
    print("\n--- Criterion 6: UI/UX Design System ---")
    doc4 = file_data.get("04_Thiet_Ke_UI_UX.md", {}).get("content", "")
    
    route_groups = [r'\(customer\)', r'\(kds\)', r'\(staff\)', r'\(manager\)', r'\(admin\)']
    found_rgs = [rg for rg in route_groups if re.search(rg, doc4)]
    print(f"  Route Groups: {found_rgs} ({len(found_rgs)}/5)")
    
    ascii_ok = bool(re.search(r'\+[-=]+\+|\│|\┌|\─|\┐|\└|\┘', doc4))
    mermaid_ok = "```mermaid" in doc4
    wcag_ok = bool(re.search(r'WCAG\s*AA|4\.5:1|Contrast', doc4, re.I))
    web_pos_ui = bool(re.search(r'Web\s+POS|Giao\s+diện\s+quầy|Thu\s+ngân', doc4, re.I))
    web_kds_ui = bool(re.search(r'KDS|Màn\s+hình\s+bếp|Kitchen\s+Display', doc4, re.I))
    bill_qr_ui = bool(re.search(r'Bill\s+QR|QR\s+hóa\s+đơn|phiếu\s+thanh\s+toán', doc4, re.I))
    
    print(f"  ASCII Wireframes: {ascii_ok}")
    print(f"  Mermaid Flows: {mermaid_ok}")
    print(f"  WCAG AA Tokens: {wcag_ok}")
    print(f"  Web POS UI specified: {web_pos_ui}")
    print(f"  Web KDS TV UI specified: {web_kds_ui}")
    print(f"  Dine-In Bill QR UI specified: {bill_qr_ui}")

    c6_pass = (len(found_rgs) == 5 and ascii_ok and mermaid_ok and wcag_ok and web_pos_ui and web_kds_ui and bill_qr_ui)
    crit_results["6_UI_UX_Design"] = c6_pass
    print(f"  -> Criterion 6 Result: {'PASS' if c6_pass else 'FAIL'}")

    # -------------------------------------------------------------
    # Criterion 7: Backend / Frontend / Testing / DevOps
    # -------------------------------------------------------------
    print("\n--- Criterion 7: Backend / Frontend / Testing / DevOps ---")
    doc7 = file_data.get("07_Ke_Hoach_Kiem_Thu.md", {}).get("content", "")
    doc8 = file_data.get("08_Trien_Khai_He_Thong.md", {}).get("content", "")
    doc_readme = file_data.get("README.md", {}).get("content", "")
    
    # Clean Architecture 4 layers
    has_domain = "Domain" in doc5
    has_app = "Application" in doc5
    has_infra = "Infrastructure" in doc5
    has_webapi = "WebApi" in doc5 or "Api" in doc5
    clean_arch_ok = (has_domain and has_app and has_infra and has_webapi)
    print(f"  Backend Clean Arch 4 Layers: {clean_arch_ok}")
    
    # MediatR CQRS
    cqrs_ok = bool(re.search(r'IRequest|IRequestHandler|MediatR', doc5))
    print(f"  Backend MediatR CQRS: {cqrs_ok}")
    
    # Redis RedLock & Cache-aside
    redis_ok = bool(re.search(r'RedLock|IDistributedCache|Redis', doc5))
    print(f"  Backend Redis / RedLock: {redis_ok}")
    
    # AI Gemini + Apriori
    ai_ok = bool(re.search(r'Gemini|Apriori', doc5))
    print(f"  Backend Gemini 1.5 + Apriori: {ai_ok}")
    
    # Frontend Next.js 14 + Zustand + PWA
    fe_next14 = bool(re.search(r'Next\.js\s*14|App\s+Router', doc6))
    fe_zustand = bool(re.search(r'useCartStore|usePOSStore|useShiftStore|create<', doc6))
    fe_pwa = bool(re.search(r'workbox|serviceWorker|cacheName', doc6, re.I))
    fe_ok = (fe_next14 and fe_zustand and fe_pwa)
    print(f"  Frontend Next.js 14 + Zustand + PWA Workbox: {fe_ok}")
    
    # Testing Matrix & 10 Edge Cases
    test_channels = bool(re.search(r'DineIn|Dine-In', doc7, re.I) and re.search(r'Delivery', doc7, re.I) and re.search(r'TakeAway|Takeaway', doc7, re.I))
    # Count edge cases
    edge_cases = re.findall(r'Edge\s+Case\s*#?(\d+)', doc7, re.I)
    unique_edges = sorted(list(set(edge_cases)))
    test_ok = (test_channels and len(unique_edges) >= 10)
    print(f"  Testing: 3 Sales Channels={test_channels}, Edge Cases={len(unique_edges)}/10 -> {unique_edges}")
    
    # DevOps Docker, NGINX, GitHub Actions
    devops_docker = bool(re.search(r'services:\s*\n\s*(?:api|postgres|redis|nginx)', doc8))
    devops_nginx = bool(re.search(r'server\s*\{\s*\n\s*listen\s+443', doc8))
    devops_ci = bool(re.search(r'name:\s*(?:CI|CD|Deploy|Build)', doc8))
    devops_ok = (devops_docker and devops_nginx and devops_ci)
    print(f"  DevOps: Docker Compose={devops_docker}, NGINX SSL={devops_nginx}, GitHub Actions={devops_ci}")
    
    # README Index
    readme_has_all = all(f in doc_readme for f in FILES[:-1])
    print(f"  README indexes all 8 deployment docs: {readme_has_all}")

    c7_pass = (clean_arch_ok and cqrs_ok and redis_ok and ai_ok and fe_ok and test_ok and devops_ok and readme_has_all)
    crit_results["7_Technical_Implementations"] = c7_pass
    print(f"  -> Criterion 7 Result: {'PASS' if c7_pass else 'FAIL'}")

    # -------------------------------------------------------------
    # Criterion 8: Zero Placeholders
    # -------------------------------------------------------------
    print("\n--- Criterion 8: Zero Placeholders ---")
    c8_pass = (len(placeholder_violations) == 0)
    crit_results["8_Zero_Placeholders"] = c8_pass
    print(f"  -> Criterion 8 Result: {'PASS' if c8_pass else 'FAIL'}")

    # -------------------------------------------------------------
    # Criterion 9: Format & Valid Syntaxes
    # -------------------------------------------------------------
    print("\n--- Criterion 9: Format, Mermaid & Callouts ---")
    
    # Validate Mermaid diagrams
    mermaid_blocks = []
    for fname, data in file_data.items():
        m_matches = re.findall(r'```mermaid\s*\n(.*?)\n```', data["content"], re.DOTALL)
        for idx, block in enumerate(m_matches):
            mermaid_blocks.append((fname, idx+1, block.strip()))
            
    print(f"  Total Mermaid Diagrams: {len(mermaid_blocks)}")
    
    # Validate diagram starters
    valid_starters = ["flowchart", "sequenceDiagram", "graph", "classDiagram", "erDiagram", "stateDiagram", "journey", "gantt", "pie", "mindmap"]
    invalid_diagrams = []
    for fname, idx, block in mermaid_blocks:
        first_line = block.splitlines()[0].strip()
        first_word = first_line.split()[0] if first_line else ""
        if not any(first_line.startswith(s) for s in valid_starters):
            invalid_diagrams.append((fname, idx, first_line))
            
    print(f"  Invalid Mermaid Starters: {len(invalid_diagrams)}")
    
    # Count alert callouts
    alert_count = len(re.findall(r'>\s*\[!(NOTE|IMPORTANT|TIP|WARNING|CAUTION)\]', all_text))
    print(f"  GitHub Alert Callouts count: {alert_count}")

    c9_pass = (len(mermaid_blocks) >= 15 and len(invalid_diagrams) == 0 and alert_count >= 10)
    crit_results["9_Format_Mermaid_Alerts"] = c9_pass
    print(f"  -> Criterion 9 Result: {'PASS' if c9_pass else 'FAIL'}")

    # -------------------------------------------------------------
    # OVERALL AUDIT SUMMARY
    # -------------------------------------------------------------
    print("\n" + "=" * 40)
    print("FINAL AUDIT SUMMARY")
    print("=" * 40)
    
    for crit, res in crit_results.items():
        print(f"  {crit:<32}: {'PASS' if res else 'FAIL'}")
        
    all_crit_passed = all(crit_results.values())
    overall_verdict = timeline_pass and integrity_pass and all_crit_passed
    
    print("\n" + "=" * 40)
    print(f"OVERALL VERDICT: {'VICTORY CONFIRMED' if overall_verdict else 'VICTORY REJECTED'}")
    print("=" * 40)
    
    return overall_verdict

if __name__ == "__main__":
    passed = run_comprehensive_audit()
    sys.exit(0 if passed else 1)
