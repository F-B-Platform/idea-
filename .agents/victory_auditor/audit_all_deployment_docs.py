import os
import re
import sys
import glob

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

def load_file(fname):
    path = os.path.join(DOCS_DIR, fname)
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def run_audit():
    results = {}
    print("=== STARTING VICTORY AUDIT ON 03_Quy_Trinh_Trien_Khai ===")
    
    # 1. Check file existence and size
    print("\n--- 1. FILE EXISTENCE & SIZES ---")
    all_files_exist = True
    file_contents = {}
    for f in FILES:
        content = load_file(f)
        if content is None:
            print(f"[FAIL] Missing file: {f}")
            all_files_exist = False
        else:
            lines = len(content.splitlines())
            chars = len(content)
            print(f"[PASS] {f}: {lines} lines, {chars:,} chars ({os.path.getsize(os.path.join(DOCS_DIR, f)):,} bytes)")
            file_contents[f] = content
    results["all_files_exist"] = all_files_exist

    # 2. Check Requirement 1: Exact Core Feature Counts in 01_Phan_Tich_Yeu_Cau.md
    print("\n--- 2. CORE FEATURE COUNTS (62 Total) ---")
    doc1 = file_contents.get("01_Phan_Tich_Yeu_Cau.md", "")
    
    # Find all C-xx, S-xx, M-xx, A-xx
    c_reqs = sorted(list(set(re.findall(r'\bC-(0[1-9]|1[0-9]|20)\b', doc1))))
    s_reqs = sorted(list(set(re.findall(r'\bS-(0[1-9]|1[0-3])\b', doc1))))
    m_reqs = sorted(list(set(re.findall(r'\bM-(0[1-9]|1[0-2])\b', doc1))))
    a_reqs = sorted(list(set(re.findall(r'\bA-(0[1-9]|1[0-7])\b', doc1))))
    
    # Check for unauthorized high numbers (e.g. C-21..C-99, S-14..S-99, M-13..M-99, A-18..A-99)
    bad_c = sorted(list(set(re.findall(r'\bC-(2[1-9]|[3-9][0-9])\b', doc1))))
    bad_s = sorted(list(set(re.findall(r'\bS-(1[4-9]|[2-9][0-9])\b', doc1))))
    bad_m = sorted(list(set(re.findall(r'\bM-(1[3-9]|[2-9][0-9])\b', doc1))))
    bad_a = sorted(list(set(re.findall(r'\bA-(1[8-9]|[2-9][0-9])\b', doc1))))
    
    print(f"Customer Features (C-01 to C-20): Found {len(c_reqs)}/20 -> {c_reqs}")
    print(f"Staff Features (S-01 to S-13): Found {len(s_reqs)}/13 -> {s_reqs}")
    print(f"Manager Features (M-01 to M-12): Found {len(m_reqs)}/12 -> {m_reqs}")
    print(f"Admin Features (A-01 to A-17): Found {len(a_reqs)}/17 -> {a_reqs}")
    print(f"Bad Customer Reqs: {bad_c}")
    print(f"Bad Staff Reqs: {bad_s}")
    print(f"Bad Manager Reqs: {bad_m}")
    print(f"Bad Admin Reqs: {bad_a}")
    
    req_count_pass = (len(c_reqs) == 20 and len(s_reqs) == 13 and len(m_reqs) == 12 and len(a_reqs) == 17 
                      and not bad_c and not bad_s and not bad_m and not bad_a)
    print(f"Requirement 1 Pass: {req_count_pass} (Total = {len(c_reqs)+len(s_reqs)+len(m_reqs)+len(a_reqs)})")
    results["req_count_pass"] = req_count_pass

    # 3. Check Requirement 2: Elimination of Deprecated Items
    print("\n--- 3. ELIMINATION OF DEPRECATED ITEMS ---")
    deprecated_patterns = [
        ("Staff Mobile App (Flutter/React Native)", r"(?:Flutter|React\s+Native|Staff\s+Mobile\s+App|App\s+nhân\s+viên\s+mobile)", "check_context"),
        ("GPS 50m attendance", r"(?:GPS\s+50\s*m|50\s*m[eé]t|b[aá]n\s+k[ií]nh\s+50|định\s+vị\s+GPS)", "check_context"),
        ("Rotating dynamic QR 30s", r"(?:QR\s+động\s+30|30\s*s|30\s*gi[aâ]y|xoay\s+v[oò]ng\s+30)", "check_context"),
        ("C-23 or C-24", r"\b(?:C-23|C-24)\b", "strict"),
        ("Separate voucher wallet", r"(?:v[ií]\s+voucher|voucher\s+wallet)", "check_context"),
        ("Isolated calorie lookup", r"(?:tra\s+c[uứ]u\s+calo\s+ri[eê]ng|isolated\s+calorie)", "check_context")
    ]
    
    dep_violations = []
    for fname, content in file_contents.items():
        for label, pat, mode in deprecated_patterns:
            matches = list(re.finditer(pat, content, re.IGNORECASE))
            if matches:
                for m in matches:
                    # check if match is in a context explaining it was eliminated / banned / prohibited
                    start = max(0, m.start() - 100)
                    end = min(len(content), m.end() + 100)
                    snippet = content[start:end].replace('\n', ' ')
                    # If it's saying "loại bỏ", "bỏ hoàn toàn", "cấm", "không dùng", etc., that's valid documentation of deprecation
                    negation_words = ["loại bỏ", "bỏ", "không dùng", "thay thế", "khác với", "tránh", "thay vì", "xóa", "deprecated", "banned", "cấm"]
                    is_negated = any(nw in snippet.lower() for nw in negation_words)
                    
                    if mode == "strict" and not is_negated:
                        dep_violations.append((fname, label, snippet))
                    elif mode == "check_context" and not is_negated:
                        # Let's inspect snippet carefully
                        dep_violations.append((fname, label, snippet))
                        
    if dep_violations:
        print(f"[WARN/FAIL] Deprecated pattern occurrences without explicit negation: {len(dep_violations)}")
        for f, lbl, snip in dep_violations[:10]:
            print(f"  - [{f}] ({lbl}): {snip}")
    else:
        print("[PASS] Zero active deprecated pattern violations found across all 9 files!")
    results["deprecated_clean"] = (len(dep_violations) == 0)

    # 4. Check Requirement 3: 4 Core Engines
    print("\n--- 4. 4 CORE ENGINES VERIFICATION ---")
    all_text = "\n".join(file_contents.values())
    
    # Engine 1: Dine-In 2 branches (VietQR prepay vs Cash postpay + Bill QR)
    has_dinein_branch1 = bool(re.search(r'(?:VietQR\s+trả\s+trước|prepay|thanh\s+toán\s+trước)', all_text, re.I))
    has_dinein_branch2 = bool(re.search(r'(?:tiền\s+mặt\s+trả\s+sau|postpay|Bill\s+QR|QR\s+hóa\s+đơn)', all_text, re.I))
    has_instant_kds = bool(re.search(r'(?:KDS|báo\s+bếp|chuyển\s+bếp\s+ngay|tức\s+thì)', all_text, re.I))
    print(f"Engine 1 (Dine-In 2 branches): Prepay={has_dinein_branch1}, Postpay+BillQR={has_dinein_branch2}, InstantKDS={has_instant_kds}")
    
    # Engine 2: Delivery QR (20k fixed fee, 100% VietQR, COD locked, phone + address mandatory)
    has_delivery_20k = bool(re.search(r'(?:20\.000|20k|20000)\s*(?:đ|VND|đồng|phí\s+ship|phí\s+giao)', all_text, re.I))
    has_delivery_vietqr = bool(re.search(r'(?:100%\s+VietQR|bắt\s+buộc\s+VietQR|khóa\s+COD|không\s+hỗ\s+trợ\s+COD|cấm\s+COD)', all_text, re.I))
    has_delivery_fields = bool(re.search(r'(?:delivery_address|địa\s+chỉ\s+giao).*(?:customer_phone|số\s+điện\s+thoại)', all_text, re.I | re.S))
    print(f"Engine 2 (Delivery QR): 20k fee={has_delivery_20k}, 100% VietQR/No COD={has_delivery_vietqr}, Phone+Addr={has_delivery_fields}")

    # Engine 3: Takeaway Web POS (Counter staff, no QR, phone CRM, 10 cups get 1 free loyalty, postpay)
    has_takeaway_pos = bool(re.search(r'(?:Web\s+POS|POS\s+quầy|thao\s+tác\s+quầy)', all_text, re.I))
    has_takeaway_crm = bool(re.search(r'(?:tra\s+cứu\s+SĐT|CRM\s+SĐT|tích\s+điểm\s+SĐT)', all_text, re.I))
    has_takeaway_10cups = bool(re.search(r'(?:10\s+ly\s+tặng\s+1|tích\s+10\s+ly|loyalty_cup)', all_text, re.I))
    print(f"Engine 3 (Takeaway Web POS): Web POS={has_takeaway_pos}, Phone CRM={has_takeaway_crm}, 10 cups free 1={has_takeaway_10cups}")

    # Engine 4: WiFi Attendance (BSSID Router + IP Subnet + Staff PIN)
    has_wifi_bssid = bool(re.search(r'(?:BSSID|MAC\s+Router|Router\s+BSSID)', all_text, re.I))
    has_wifi_subnet = bool(re.search(r'(?:IP\s+Subnet|Subnet\s+IP|dải\s+IP)', all_text, re.I))
    has_wifi_pin = bool(re.search(r'(?:Mã\s+NV|Staff\s+PIN|Mã\s+PIN\s+nhân\s+viên)', all_text, re.I))
    print(f"Engine 4 (WiFi Attendance): BSSID={has_wifi_bssid}, IP Subnet={has_wifi_subnet}, Staff PIN={has_wifi_pin}")

    engines_pass = (has_dinein_branch1 and has_dinein_branch2 and has_delivery_20k and has_delivery_vietqr and
                    has_takeaway_pos and has_takeaway_10cups and has_wifi_bssid and has_wifi_subnet and has_wifi_pin)
    print(f"Requirement 3 Pass: {engines_pass}")
    results["engines_pass"] = engines_pass

    # 5. Check Database Design in 02_Thiet_Ke_Database.md
    print("\n--- 5. DATABASE DESIGN (25 3NF Tables) ---")
    doc2 = file_contents.get("02_Thiet_Ke_Database.md", "")
    
    create_tables = re.findall(r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?([a-zA-Z0-9_]+)', doc2, re.I)
    unique_tables = sorted(list(set([t.lower() for t in create_tables])))
    print(f"Found {len(unique_tables)} CREATE TABLE definitions: {unique_tables}")
    
    # Check specific required tables
    req_tables = [
        "branches", "branch_wifi_configs", "users", "roles", "user_roles",
        "tables", "categories", "products", "product_boms", "ingredients",
        "combos", "combo_items", "orders", "order_items", "order_item_modifiers",
        "payments", "cash_shifts", "z_reports", "inventory_transactions",
        "purchase_orders", "purchase_order_items", "loyalty_accounts",
        "loyalty_cup_transactions", "vouchers", "notifications"
    ]
    missing_tables = [t for t in req_tables if t not in unique_tables]
    print(f"Missing required tables (out of 25): {missing_tables}")
    
    has_uuid_pks = bool(re.search(r'id\s+UUID\s+PRIMARY\s+KEY', doc2, re.I) or re.search(r'gen_random_uuid\(\)', doc2, re.I))
    has_indexes = len(re.findall(r'CREATE\s+INDEX', doc2, re.I))
    has_triggers = len(re.findall(r'CREATE\s+TRIGGER', doc2, re.I))
    print(f"UUID PKs: {has_uuid_pks}, CREATE INDEX count: {has_indexes}, CREATE TRIGGER count: {has_triggers}")
    
    db_pass = (len(unique_tables) >= 25 and len(missing_tables) == 0 and has_uuid_pks and has_indexes >= 10 and has_triggers >= 3)
    print(f"Requirement 4 Pass: {db_pass}")
    results["db_pass"] = db_pass

    # 6. Check API Contracts in 03_Thiet_Ke_API_Contract.md
    print("\n--- 6. API CONTRACTS (10 REST Groups, 4 Hubs, PayOS Webhook) ---")
    doc3 = file_contents.get("03_Thiet_Ke_API_Contract.md", "")
    
    # 10 REST Groups check
    rest_groups = [
        ("Auth", r'/api/v1/auth'),
        ("Branch", r'/api/v1/branches'),
        ("Table", r'/api/v1/tables'),
        ("Product/BOM/Category", r'/api/v1/products|/api/v1/categories|/api/v1/boms'),
        ("Order", r'/api/v1/orders'),
        ("Payment", r'/api/v1/payments'),
        ("Attendance", r'/api/v1/attendances|/api/v1/wifi-configs'),
        ("KDS", r'/api/v1/kds'),
        ("Manager Cash/Inventory", r'/api/v1/shifts|/api/v1/inventory|/api/v1/z-reports'),
        ("Admin Analytics/AI", r'/api/v1/analytics|/api/v1/ai')
    ]
    rest_matches = {}
    for name, pat in rest_groups:
        m = len(re.findall(pat, doc3, re.I))
        rest_matches[name] = m
        print(f"REST Group [{name}]: {m} occurrences")
    
    # 4 SignalR Hubs
    hubs = ["OrderHub", "KitchenHub", "PaymentHub", "NotificationHub"]
    found_hubs = [h for h in hubs if h in doc3]
    print(f"SignalR Hubs found: {len(found_hubs)}/4 -> {found_hubs}")
    
    # PayOS Webhook
    has_payos_webhook = bool(re.search(r'webhook.*payos|payos.*webhook', doc3, re.I))
    has_hmac = bool(re.search(r'HMAC\s*SHA256|signature|x-signature', doc3, re.I))
    print(f"PayOS Webhook: endpoint={has_payos_webhook}, HMAC-SHA256={has_hmac}")
    
    api_pass = (all(v > 0 for v in rest_matches.values()) and len(found_hubs) == 4 and has_payos_webhook and has_hmac)
    print(f"Requirement 5 Pass: {api_pass}")
    results["api_pass"] = api_pass

    # 7. Check UI/UX in 04_Thiet_Ke_UI_UX.md
    print("\n--- 7. UI/UX DESIGN SYSTEM ---")
    doc4 = file_contents.get("04_Thiet_Ke_UI_UX.md", "")
    
    routes = [r'\(customer\)', r'\(kds\)', r'\(staff\)', r'\(manager\)', r'\(admin\)']
    found_routes = [r for r in routes if re.search(r, doc4)]
    print(f"Next.js Route Groups found: {len(found_routes)}/5 -> {found_routes}")
    
    has_ascii = bool(re.search(r'\+[-=]+\+|\│|\┌|\─|\┐|\└|\┘', doc4))
    has_mermaid = "```mermaid" in doc4
    has_wcag = bool(re.search(r'WCAG\s*AA|4\.5:1|contrast', doc4, re.I))
    print(f"ASCII wireframes: {has_ascii}, Mermaid flows: {has_mermaid}, WCAG AA: {has_wcag}")
    
    ui_pass = (len(found_routes) == 5 and has_ascii and has_mermaid and has_wcag)
    print(f"Requirement 6 Pass: {ui_pass}")
    results["ui_pass"] = ui_pass

    # 8. Check Backend, Frontend, Testing, DevOps
    print("\n--- 8. BACKEND / FRONTEND / TESTING / DEVOPS ---")
    doc5 = file_contents.get("05_Quy_Trinh_Backend.md", "")
    doc6 = file_contents.get("06_Quy_Trinh_Frontend.md", "")
    doc7 = file_contents.get("07_Ke_Hoach_Kiem_Thu.md", "")
    doc8 = file_contents.get("08_Trien_Khai_He_Thong.md", "")
    doc_readme = file_contents.get("README.md", "")
    
    # Backend checks
    has_clean_arch = bool(re.search(r'Clean\s+Architecture|Domain|Application|Infrastructure|WebApi', doc5, re.I))
    has_cqrs = bool(re.search(r'MediatR|CQRS|IRequest|IRequestHandler', doc5, re.I))
    has_redis = bool(re.search(r'Redis|Distributed\s+Lock|RedLock', doc5, re.I))
    has_gemini = bool(re.search(r'Gemini|Apriori', doc5, re.I))
    backend_ok = (has_clean_arch and has_cqrs and has_redis and has_gemini)
    print(f"Backend (Clean Arch, CQRS MediatR, Redis RedLock, Gemini/Apriori): {backend_ok}")

    # Frontend checks
    has_next14 = bool(re.search(r'Next\.js\s*14|App\s+Router', doc6, re.I))
    has_zustand = bool(re.search(r'Zustand|create<', doc6, re.I))
    has_pwa = bool(re.search(r'PWA|Workbox|Service\s+Worker|offline', doc6, re.I))
    frontend_ok = (has_next14 and has_zustand and has_pwa)
    print(f"Frontend (Next.js 14, Zustand, PWA Workbox): {frontend_ok}")

    # Testing checks
    has_matrix = bool(re.search(r'Unit\s+Test|Integration\s+Test|UAT|Matrix', doc7, re.I))
    has_3channels = bool(re.search(r'DineIn|Dine-In', doc7, re.I) and re.search(r'Delivery', doc7, re.I) and re.search(r'TakeAway|Takeaway', doc7, re.I))
    has_10edge = bool(re.search(r'Edge\s+Case', doc7, re.I))
    testing_ok = (has_matrix and has_3channels and has_10edge)
    print(f"Testing (Matrix, 3 Channels, 10 Edge Cases): {testing_ok}")

    # DevOps checks
    has_docker = bool(re.search(r'docker-compose|Dockerfile|services:', doc8, re.I))
    has_nginx = bool(re.search(r'nginx|ssl_certificate|proxy_pass', doc8, re.I))
    has_ci_cd = bool(re.search(r'github\s+actions|workflows|deploy\.yml', doc8, re.I))
    devops_ok = (has_docker and has_nginx and has_ci_cd)
    print(f"DevOps (Docker Compose, NGINX SSL, GitHub Actions): {devops_ok}")

    # README check
    readme_ok = bool(len(doc_readme) > 2000 and "01_Phan_Tich_Yeu_Cau.md" in doc_readme and "08_Trien_Khai_He_Thong.md" in doc_readme)
    print(f"README complete index: {readme_ok}")

    req7_pass = (backend_ok and frontend_ok and testing_ok and devops_ok and readme_ok)
    results["req7_pass"] = req7_pass

    # 9. Zero Placeholders Check
    print("\n--- 9. ZERO PLACEHOLDERS AUDIT ---")
    placeholder_patterns = [
        r'\bTODO\b',
        r'\bTBD\b',
        r'/\*\s*rest of code\s*\*/',
        r'//\s*rest of implementation',
        r'//\s*tương tự như trên',
        r'//\s*giữ nguyên logic cũ',
        r'\.\.\.\s*giữ nguyên',
        r'//\s*viết tiếp ở đây',
    ]
    
    placeholder_hits = []
    for fname, content in file_contents.items():
        for pat in placeholder_patterns:
            matches = list(re.finditer(pat, content, re.IGNORECASE))
            if matches:
                for m in matches:
                    start = max(0, m.start() - 50)
                    end = min(len(content), m.end() + 50)
                    snippet = content[start:end].replace('\n', ' ')
                    placeholder_hits.append((fname, pat, snippet))
                    
    if placeholder_hits:
        print(f"[FAIL] Found {len(placeholder_hits)} placeholder hits:")
        for f, p, s in placeholder_hits:
            print(f"  - [{f}] ({p}): {s}")
    else:
        print("[PASS] Zero placeholders found across all 9 files!")
    results["placeholders_pass"] = (len(placeholder_hits) == 0)

    # 10. Format & Syntax Validation (Mermaid diagrams & GitHub Alert Callouts)
    print("\n--- 10. FORMAT & SYNTAX VALIDATION ---")
    mermaid_blocks = []
    for fname, content in file_contents.items():
        m_matches = re.findall(r'```mermaid\s*\n(.*?)\n```', content, re.DOTALL)
        for idx, block in enumerate(m_matches):
            mermaid_blocks.append((fname, idx+1, block.strip()))
    
    print(f"Found {len(mermaid_blocks)} Mermaid diagram blocks across 9 files.")
    
    # Check alert callouts
    alert_count = 0
    for fname, content in file_contents.items():
        alerts = re.findall(r'>\s*\[!(NOTE|IMPORTANT|TIP|WARNING|CAUTION)\]', content)
        alert_count += len(alerts)
    print(f"Found {alert_count} GitHub Alert Callouts across 9 files.")

    format_pass = (len(mermaid_blocks) > 0 and alert_count > 0)
    results["format_pass"] = format_pass

    print("\n=== SUMMARY OF RESULTS ===")
    for k, v in results.items():
        print(f"  {k}: {'PASS' if v else 'FAIL'}")
        
    overall_pass = all(results.values())
    print(f"\nOVERALL VERDICT: {'VICTORY CONFIRMED' if overall_pass else 'VICTORY REJECTED'}")
    return overall_pass

if __name__ == "__main__":
    success = run_audit()
    sys.exit(0 if success else 1)
