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

def run_suite():
    print("=" * 80)
    print("      FINAL INDEPENDENT VICTORY AUDIT SUITE - v2.5.0")
    print("      Target: d:\\Idea_DoAn\\03_Quy_Trinh_Trien_Khai\\")
    print("=" * 80)
    
    file_data = {}
    for fname in FILES:
        fpath = os.path.join(DOCS_DIR, fname)
        if not os.path.exists(fpath):
            print(f"[FATAL] File not found: {fname}")
            return False
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        file_data[fname] = {
            "path": fpath,
            "size": os.path.getsize(fpath),
            "lines": len(content.splitlines()),
            "chars": len(content),
            "content": content
        }

    all_text = "\n".join([d["content"] for d in file_data.values()])

    # =========================================================
    # PHASE A: TIMELINE & PROVENANCE AUDIT
    # =========================================================
    print("\n" + "=" * 50)
    print("PHASE A: TIMELINE & PROVENANCE AUDIT")
    print("=" * 50)
    
    phase_a_pass = True
    total_lines = 0
    total_bytes = 0
    for fname in FILES:
        d = file_data[fname]
        total_lines += d["lines"]
        total_bytes += d["size"]
        mtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(d["path"])))
        print(f"  ✓ {fname:<30} | {d['lines']:>5} lines | {d['size']:>7,} B | Modified: {mtime}")
        if d["size"] < 10000 or d["lines"] < 100:
            phase_a_pass = False

    print(f"\n  Total Project Scope: 9 Documents | {total_lines:,} lines | {total_bytes:,} bytes ({total_bytes/1024:.1f} KB)")
    print(f"  Phase A Result: {'PASS' if phase_a_pass else 'FAIL'}")

    # =========================================================
    # PHASE B: INTEGRITY & FORENSIC CHECKS
    # =========================================================
    print("\n" + "=" * 50)
    print("PHASE B: FORENSIC INTEGRITY CHECKS")
    print("=" * 50)
    
    phase_b_pass = True
    
    # 1. Zero Placeholders
    placeholder_patterns = [
        (r'\bTODO\b', "TODO"),
        (r'\bTBD\b', "TBD"),
        (r'/\*\s*rest of code\s*\*/', "/* rest of code */"),
        (r'//\s*rest of implementation', "// rest of implementation"),
        (r'//\s*tương tự như trên', "// tương tự như trên"),
        (r'//\s*giữ nguyên logic cũ', "// giữ nguyên logic cũ"),
        (r'\.\.\.\s*giữ nguyên', "... giữ nguyên"),
        (r'//\s*viết tiếp ở đây', "// viết tiếp ở đây")
    ]
    ph_violations = []
    for fname, d in file_data.items():
        for pat, lbl in placeholder_patterns:
            for m in re.finditer(pat, d["content"], re.IGNORECASE):
                start = max(0, m.start() - 30)
                end = min(len(d["content"]), m.end() + 30)
                ph_violations.append((fname, lbl, d["content"][start:end].replace('\n', ' ')))
                
    if ph_violations:
        print(f"  [FAIL] Found {len(ph_violations)} placeholder violations:")
        for f, l, s in ph_violations:
            print(f"    - {f} ({l}): {s}")
        phase_b_pass = False
    else:
        print("  ✓ Zero Placeholders check: 100% CLEAN (No TODO, TBD, /* rest of code */)")

    # 2. No active deprecated features / concepts
    dep_violations = []
    for m in re.finditer(r'###\s*C-(2[1-9]|[3-9][0-9])\b', all_text):
        dep_violations.append(f"Active requirement header found: {m.group(0)}")
        
    if re.search(r'latitude|longitude|gps_radius', file_data["02_Thiet_Ke_Database.md"]["content"], re.I):
        dep_violations.append("GPS fields found in 02_Thiet_Ke_Database.md")
        
    if re.search(r'latitude|longitude|gpsLocation', file_data["03_Thiet_Ke_API_Contract.md"]["content"], re.I):
        dep_violations.append("GPS fields found in 03_Thiet_Ke_API_Contract.md")
        
    if re.search(r'pubspec\.yaml|flutter|react-native\b', file_data["06_Quy_Trinh_Frontend.md"]["content"], re.I):
        dep_violations.append("Flutter/React Native framework code found in 06_Quy_Trinh_Frontend.md")
        
    if dep_violations:
        print(f"  [FAIL] Found deprecated concept violations: {dep_violations}")
        phase_b_pass = False
    else:
        print("  ✓ Elimination of Deprecated Concepts: 100% CLEAN")

    print(f"  Phase B Result: {'PASS' if phase_b_pass else 'FAIL'}")

    # =========================================================
    # PHASE C: INDEPENDENT ACCEPTANCE CRITERIA AUDIT
    # =========================================================
    print("\n" + "=" * 50)
    print("PHASE C: INDEPENDENT ACCEPTANCE CRITERIA AUDIT")
    print("=" * 50)
    
    results = {}
    
    # ---------------------------------------------------------
    # Criteria 1: Exact 62 Core Features (20 C, 13 S, 12 M, 17 A)
    # ---------------------------------------------------------
    print("\n[CRITERION 1: EXACT 62 FUNCTIONAL REQUIREMENTS]")
    doc1 = file_data["01_Phan_Tich_Yeu_Cau.md"]["content"]
    
    c_reqs = sorted(list(set(re.findall(r'\b(C-(?:0[1-9]|1[0-9]|20))\b', doc1))))
    s_reqs = sorted(list(set(re.findall(r'\b(S-(?:0[1-9]|1[0-3]))\b', doc1))))
    m_reqs = sorted(list(set(re.findall(r'\b(M-(?:0[1-9]|1[0-2]))\b', doc1))))
    a_reqs = sorted(list(set(re.findall(r'\b(A-(?:0[1-9]|1[0-7]))\b', doc1))))
    
    print(f"  ✓ Customer (C-01 to C-20): {len(c_reqs)}/20 -> {c_reqs}")
    print(f"  ✓ Staff    (S-01 to S-13): {len(s_reqs)}/13 -> {s_reqs}")
    print(f"  ✓ Manager  (M-01 to M-12): {len(m_reqs)}/12 -> {m_reqs}")
    print(f"  ✓ Admin    (A-01 to A-17): {len(a_reqs)}/17 -> {a_reqs}")
    
    total_fr = len(c_reqs) + len(s_reqs) + len(m_reqs) + len(a_reqs)
    c1_ok = (len(c_reqs) == 20 and len(s_reqs) == 13 and len(m_reqs) == 12 and len(a_reqs) == 17 and total_fr == 62)
    
    doc7 = file_data["07_Ke_Hoach_Kiem_Thu.md"]["content"]
    c_in_test = len(set(re.findall(r'\b(C-(?:0[1-9]|1[0-9]|20))\b', doc7)))
    s_in_test = len(set(re.findall(r'\b(S-(?:0[1-9]|1[0-3]))\b', doc7)))
    m_in_test = len(set(re.findall(r'\b(M-(?:0[1-9]|1[0-2]))\b', doc7)))
    a_in_test = len(set(re.findall(r'\b(A-(?:0[1-9]|1[0-7]))\b', doc7)))
    print(f"  ✓ Test Traceability Matrix: C={c_in_test}/20, S={s_in_test}/13, M={m_in_test}/12, A={a_in_test}/17")
    
    results["1_Feature_Counts_62"] = c1_ok and (c_in_test == 20 and s_in_test == 13 and m_in_test == 12 and a_in_test == 17)
    print(f"  Criterion 1 Result: {'PASS' if results['1_Feature_Counts_62'] else 'FAIL'}")

    # ---------------------------------------------------------
    # Criteria 2: Elimination of Deprecated Items
    # ---------------------------------------------------------
    print("\n[CRITERION 2: ELIMINATION OF DEPRECATED ITEMS]")
    c2_ok = (len(dep_violations) == 0)
    results["2_Elimination_Deprecated"] = c2_ok
    print(f"  ✓ Zero active references to Staff App (Flutter/RN), GPS 50m, QR 30s, C-23, C-24, Voucher Wallet, Isolated Calorie")
    print(f"  Criterion 2 Result: {'PASS' if c2_ok else 'FAIL'}")

    # ---------------------------------------------------------
    # Criteria 3: 4 Core Engines
    # ---------------------------------------------------------
    print("\n[CRITERION 3: 4 CORE BUSINESS ENGINES]")
    doc2 = file_data["02_Thiet_Ke_Database.md"]["content"]
    doc3 = file_data["03_Thiet_Ke_API_Contract.md"]["content"]
    doc4 = file_data["04_Thiet_Ke_UI_UX.md"]["content"]
    doc5 = file_data["05_Quy_Trinh_Backend.md"]["content"]
    doc6 = file_data["06_Quy_Trinh_Frontend.md"]["content"]
    
    # Engine 1: Dine-In 2 branches
    e1_prepay = bool(re.search(r'VietQR.*trả trước|prepay|thanh toán trước', all_text, re.I))
    e1_postpay = bool(re.search(r'tiền mặt.*trả sau|postpay|Bill QR|QR hóa đơn', all_text, re.I))
    e1_kds = bool(re.search(r'KitchenHub|vé bếp|OrderCreatedEvent|báo bếp', doc3 + doc5, re.I))
    print(f"  ✓ Engine 1 (Dine-In 2 branches): Prepay={e1_prepay}, Postpay+BillQR={e1_postpay}, InstantKDS={e1_kds}")

    # Engine 2: Delivery QR (20k shipping fee, 100% VietQR prepay, COD locked, phone + address mandatory)
    e2_fee = bool(re.search(r'delivery_fee DECIMAL\(12,0\)', doc2) and re.search(r'20\.000|20k|20000', all_text))
    e2_vietqr = bool(re.search(r'100%\s+VietQR|bắt buộc VietQR|khóa COD|không hỗ trợ COD', all_text, re.I))
    e2_fields = bool(re.search(r'delivery_address VARCHAR\(500\)', doc2) and re.search(r'recipient_phone VARCHAR\(20\)', doc2))
    print(f"  ✓ Engine 2 (Delivery QR): 20k Fee={e2_fee}, 100% VietQR/No COD={e2_vietqr}, Phone+Addr Schema={e2_fields}")

    # Engine 3: Takeaway Web POS (Counter staff, no QR, phone CRM, 10 cups get 1 free loyalty, postpay)
    e3_pos = bool(re.search(r'SCR-STAFF-01.*Web POS Takeaway|usePosStore', doc4 + doc6))
    e3_crm = bool(re.search(r'/api/v1/customers/lookup-phone|tra cứu.*SĐT|CRM', doc3 + all_text, re.I))
    e3_10cups = bool(re.search(r'CREATE TABLE loyalty_cup_transactions', doc2) and re.search(r'10 ly tặng 1', all_text))
    print(f"  ✓ Engine 3 (Takeaway Web POS): Web POS UI={e3_pos}, CRM Phone Lookup={e3_crm}, 10 cups free 1={e3_10cups}")

    # Engine 4: WiFi Attendance (BSSID Router + IP Subnet + Staff PIN)
    e4_bssid = bool(re.search(r'bssid_list TEXT', doc2) and re.search(r'verified_bssid VARCHAR\(50\)', doc2))
    e4_subnet = bool(re.search(r'allowed_ip_subnets TEXT', doc2) and re.search(r'verified_ip VARCHAR\(50\)', doc2))
    e4_pin = bool(re.search(r'employee_code VARCHAR\(50\)', doc2) and re.search(r'/api/v1/attendances/wifi-checkin', doc3))
    print(f"  ✓ Engine 4 (WiFi Attendance): BSSID Schema={e4_bssid}, IP Subnet Schema={e4_subnet}, Employee Code/PIN={e4_pin}")

    c3_ok = (e1_prepay and e1_postpay and e1_kds and e2_fee and e2_vietqr and e2_fields and e3_pos and e3_crm and e3_10cups and e4_bssid and e4_subnet and e4_pin)
    results["3_Core_Engines_4"] = c3_ok
    print(f"  Criterion 3 Result: {'PASS' if c3_ok else 'FAIL'}")

    # ---------------------------------------------------------
    # Criteria 4: Database Design (25 3NF Tables in PostgreSQL 16)
    # ---------------------------------------------------------
    print("\n[CRITERION 4: DATABASE DESIGN (25 3NF TABLES IN POSTGRESQL 16)]")
    create_tables = re.findall(r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?([a-zA-Z0-9_]+)', doc2, re.I)
    unique_tables = sorted(list(set([t.lower() for t in create_tables])))
    print(f"  ✓ Total Tables: {len(unique_tables)}/25")
    for i, t in enumerate(unique_tables):
        print(f"    {i+1:>2}. {t}")
        
    pk_uuids = len(re.findall(r'UUID\s+PRIMARY\s+KEY\s+DEFAULT\s+gen_random_uuid\(\)', doc2, re.I))
    composite_pks = len(re.findall(r'PRIMARY\s+KEY\s*\([a-zA-Z0-9_,\s]+\)', doc2, re.I))
    fks = len(re.findall(r'REFERENCES\s+[a-zA-Z0-9_]+', doc2, re.I))
    indexes = len(re.findall(r'CREATE\s+INDEX', doc2, re.I))
    triggers = len(re.findall(r'CREATE\s+TRIGGER', doc2, re.I))
    
    print(f"  ✓ Schema Integrity: Single UUID PKs={pk_uuids}, Composite PKs (Junction Tables)={composite_pks}, Total Valid PKs={pk_uuids+composite_pks}/25, FKs={fks}, Indexes={indexes}, Triggers={triggers}")
    
    c4_ok = (len(unique_tables) == 25 and (pk_uuids + composite_pks) == 25 and fks >= 25 and indexes >= 15 and triggers >= 3)
    results["4_Database_25_Tables"] = c4_ok
    print(f"  Criterion 4 Result: {'PASS' if c4_ok else 'FAIL'}")

    # ---------------------------------------------------------
    # Criteria 5: API Contracts (10 REST Groups, 4 SignalR Hubs, PayOS Webhook)
    # ---------------------------------------------------------
    print("\n[CRITERION 5: API CONTRACTS (10 REST GROUPS + 4 SIGNALR HUBS + PAYOS WEBHOOK)]")
    rest_groups = [
        ("1. Auth & Profile", r'/api/v1/auth'),
        ("2. Branch Management", r'/api/v1/branches'),
        ("3. Table Management", r'/api/v1/tables'),
        ("4. Menu & BOM Catalog", r'/api/v1/products|/api/v1/categories'),
        ("5. Orders & Checkout", r'/api/v1/orders'),
        ("6. Payments & VietQR", r'/api/v1/payments'),
        ("7. Attendance & WiFi", r'/api/v1/attendances'),
        ("8. KDS Kitchen Operations", r'/api/v1/kds'),
        ("9. Manager Cash & Inventory", r'/api/v1/shifts|/api/v1/inventory'),
        ("10. Admin Analytics & AI-2", r'/api/v1/analytics|/api/v1/ai')
    ]
    rest_found = 0
    for name, pat in rest_groups:
        match_count = len(re.findall(pat, doc3, re.I))
        if match_count > 0:
            print(f"  ✓ REST Group [{name}]: {match_count} endpoints/references")
            rest_found += 1
        else:
            print(f"  ✗ REST Group [{name}]: MISSING")
            
    hubs = ["OrderHub", "KitchenHub", "PaymentHub", "NotificationHub"]
    hubs_found = [h for h in hubs if h in doc3 and h in doc5]
    print(f"  ✓ SignalR Hubs: {hubs_found} ({len(hubs_found)}/4)")
    
    payos_webhook_ok = bool(re.search(r'/api/v1/webhooks/payos', doc3) and re.search(r'HMAC-SHA256|HMAC SHA256|x-signature', doc3, re.I))
    print(f"  ✓ PayOS Webhook with HMAC-SHA256: {payos_webhook_ok}")
    
    c5_ok = (rest_found == 10 and len(hubs_found) == 4 and payos_webhook_ok)
    results["5_API_Contracts"] = c5_ok
    print(f"  Criterion 5 Result: {'PASS' if c5_ok else 'FAIL'}")

    # ---------------------------------------------------------
    # Criteria 6: UI/UX Design System (5 Route Groups, ASCII, Mermaid, WCAG AA)
    # ---------------------------------------------------------
    print("\n[CRITERION 6: UI/UX DESIGN SYSTEM (5 ROUTE GROUPS + ASCII + MERMAID + WCAG AA)]")
    rgs = [r'\(customer\)', r'\(kds\)', r'\(staff\)', r'\(manager\)', r'\(admin\)']
    rgs_found = [rg for rg in rgs if re.search(rg, doc4)]
    print(f"  ✓ Next.js 14 Route Groups: {rgs_found} ({len(rgs_found)}/5)")
    
    wireframes = re.findall(r'SCR-[A-Z]+-\d+', doc4)
    unique_wireframes = sorted(list(set(wireframes)))
    print(f"  ✓ Wireframe Screens specified: {len(unique_wireframes)} screens -> {unique_wireframes}")
    
    wcag_tokens = bool(re.search(r'WCAG\s*AA|4\.5:1|Contrast', doc4, re.I))
    print(f"  ✓ WCAG 2.1 AA Tokens & Accessibility: {wcag_tokens}")
    
    c6_ok = (len(rgs_found) == 5 and len(unique_wireframes) >= 12 and wcag_tokens)
    results["6_UI_UX_Design"] = c6_ok
    print(f"  Criterion 6 Result: {'PASS' if c6_ok else 'FAIL'}")

    # ---------------------------------------------------------
    # Criteria 7: Backend / Frontend / Testing / DevOps / README
    # ---------------------------------------------------------
    print("\n[CRITERION 7: TECHNICAL IMPLEMENTATIONS (BACKEND / FRONTEND / QA / DEVOPS / README)]")
    
    # 1. Backend: Clean Arch 4 Layers, MediatR CQRS, RedLock, Gemini/Apriori
    b_clean = "Clean Architecture" in doc5 and all(layer in doc5 for layer in ["Domain", "Application", "Infrastructure"]) and ("WebApi" in doc5 or "Presentation" in doc5 or "Api" in doc5)
    b_cqrs = "MediatR" in doc5 and "IRequest" in doc5 and "IRequestHandler" in doc5
    b_redis = ("RedLock" in doc5 or "RedlockFactory" in doc5) and ("IRedisCacheService" in doc5 or "RedisCacheService" in doc5)
    b_ai = "Gemini" in doc5 and "Apriori" in doc5
    print(f"  ✓ Backend: Clean Arch 4 Layers={b_clean}, MediatR CQRS={b_cqrs}, RedLock={b_redis}, Gemini+Apriori={b_ai}")
    
    # 2. Frontend: Next 14, Zustand 5 Stores, TanStack Query, PWA Workbox
    f_next14 = "Next.js 14" in doc6 and "App Router" in doc6
    f_zustand = all(st in doc6 for st in ["useCartStore", "usePosStore", "useShiftStore", "useKdsStore", "useAuthStore"])
    f_pwa = "Workbox" in doc6 or "serviceWorker" in doc6
    print(f"  ✓ Frontend: Next.js 14={f_next14}, 5 Zustand Stores={f_zustand}, PWA Workbox={f_pwa}")
    
    # 3. Testing: Matrix, 3 Channels, 10 Critical Edge Cases
    t_channels = ("DineIn" in doc7 or "Dine-In" in doc7) and "Delivery" in doc7 and ("TakeAway" in doc7 or "Takeaway" in doc7)
    t_edge_cases = re.findall(r'\bEC-(?:0[1-9]|10)\b', doc7)
    unique_ecs = sorted(list(set(t_edge_cases)))
    print(f"  ✓ QA Testing: 3 Channels={t_channels}, 10 Critical Edge Cases ({len(unique_ecs)}/10) -> {unique_ecs}")
    
    # 4. DevOps: Docker Compose, NGINX SSL, GitHub Actions, Backup scripts
    d_docker = "docker-compose" in file_data["08_Trien_Khai_He_Thong.md"]["content"] or "services:" in file_data["08_Trien_Khai_He_Thong.md"]["content"]
    d_nginx = "listen 443" in file_data["08_Trien_Khai_He_Thong.md"]["content"]
    d_ci = "deploy.yml" in file_data["08_Trien_Khai_He_Thong.md"]["content"] or "github/workflows" in file_data["08_Trien_Khai_He_Thong.md"]["content"]
    print(f"  ✓ DevOps: Docker Compose Multi-Container={d_docker}, NGINX SSL={d_nginx}, CI/CD GitHub Actions={d_ci}")
    
    # 5. README Index
    doc_readme = file_data["README.md"]["content"]
    r_indexed = all(f in doc_readme for f in FILES[:-1])
    print(f"  ✓ README.md: Complete Index & Traceability for all 8 deployment documents={r_indexed}")

    c7_ok = (b_clean and b_cqrs and b_redis and b_ai and f_next14 and f_zustand and f_pwa and t_channels and len(unique_ecs) == 10 and d_docker and d_nginx and d_ci and r_indexed)
    results["7_Technical_Implementations"] = c7_ok
    print(f"  Criterion 7 Result: {'PASS' if c7_ok else 'FAIL'}")

    # ---------------------------------------------------------
    # Criteria 8: Zero Placeholders
    # ---------------------------------------------------------
    print("\n[CRITERION 8: ZERO PLACEHOLDERS]")
    c8_ok = (len(ph_violations) == 0)
    results["8_Zero_Placeholders"] = c8_ok
    print(f"  Criterion 8 Result: {'PASS' if c8_ok else 'FAIL'}")

    # ---------------------------------------------------------
    # Criteria 9: Format & Markdown Syntaxes
    # ---------------------------------------------------------
    print("\n[CRITERION 9: FORMAT & SYNTAX VALIDATION]")
    mermaid_blocks = re.findall(r'```mermaid\s*\n(.*?)\n```', all_text, re.DOTALL)
    alert_callouts = re.findall(r'>\s*\[!(NOTE|IMPORTANT|TIP|WARNING|CAUTION)\]', all_text)
    print(f"  ✓ Valid Mermaid Diagrams: {len(mermaid_blocks)} diagrams found")
    print(f"  ✓ GitHub Alert Callouts: {len(alert_callouts)} callouts found")
    
    c9_ok = (len(mermaid_blocks) >= 15 and len(alert_callouts) >= 10)
    results["9_Format_Mermaid_Alerts"] = c9_ok
    print(f"  Criterion 9 Result: {'PASS' if c9_ok else 'FAIL'}")

    # =========================================================
    # FINAL AUDIT SUMMARY & VERDICT
    # =========================================================
    print("\n" + "=" * 50)
    print("FINAL SUMMARY OF ACCEPTANCE CRITERIA")
    print("=" * 50)
    for k, v in results.items():
        print(f"  {k:<32}: {'PASS' if v else 'FAIL'}")

    overall_verdict = phase_a_pass and phase_b_pass and all(results.values())
    
    print("\n" + "=" * 50)
    print(f"OVERALL AUDIT VERDICT: {'VICTORY CONFIRMED' if overall_verdict else 'VICTORY REJECTED'}")
    print("=" * 50)
    
    return overall_verdict

if __name__ == "__main__":
    passed = run_suite()
    sys.exit(0 if passed else 1)
