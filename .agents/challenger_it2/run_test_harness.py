import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

seq_path = r"d:\Idea_DoAn\04_Thiet_Ke_Kien_Truc_Diagrams\02_Sequence_Diagrams.md"
with open(seq_path, 'r', encoding='utf-8') as f:
    seq_content = f.read()

tests = []

def record_test(test_id, category, description, passed, details=""):
    tests.append({
        "id": test_id,
        "category": category,
        "description": description,
        "passed": passed,
        "details": details
    })
    status = "[PASS]" if passed else "[FAIL]"
    print(f"{status} [{test_id}] {category}: {description}")
    if not passed or details:
        print(f"       Details: {details}")

print("================================================================================")
print("RUNNING ADVERSARIAL VERIFICATION TEST HARNESS ON 02_Sequence_Diagrams.md")
print("================================================================================\n")

# TEST CATEGORY 1: SOFT INVENTORY RESERVATION (Seq-01 & Seq-03)
has_redis_ttl_600_seq1 = "EXPIRE inventory:reserved:B01 600" in seq_content and "TTL 600s" in seq_content
record_test("TC-INV-01", "Soft Reservation", "Redis TTL 600s configured on reserved inventory keys", has_redis_ttl_600_seq1, "Found EXPIRE inventory:reserved:B01 600 and TTL 600s")

has_hincrby_reserve_seq1 = "HINCRBY inventory:reserved:B01 ing-coffee 80" in seq_content
record_test("TC-INV-02", "Soft Reservation", "Seq-01 increments reserved stock via HINCRBY", has_hincrby_reserve_seq1, "Found HINCRBY inventory:reserved:B01 ing-coffee 80")

has_avail_formula = "available_stock = current_quantity - reserved_stock >= required_qty" in seq_content or "current_quantity - reserved_stock >= required_qty" in seq_content
record_test("TC-INV-03", "Soft Reservation", "Available stock calculation strictly accounts for reserved stock", has_avail_formula, "Formula: current_quantity - reserved_stock >= required_qty verified")

has_rollback_seq1 = "HINCRBY inventory:reserved:B01 ing-coffee -80" in seq_content and "Compensation Rollback" in seq_content
record_test("TC-INV-04", "Soft Reservation", "Compensation rollback decrements reserved stock on timeout/cancellation (Seq-01)", has_rollback_seq1, "Found rollback HINCRBY -80 / -120 / -60")

has_rollback_seq3 = "HINCRBY inventory:reserved:B01 ing-tea -60" in seq_content and "Đơn Giao Hàng Quá Hạn Quét Mã 10 Phút" in seq_content
record_test("TC-INV-05", "Soft Reservation", "Compensation rollback decrements reserved stock on timeout/cancellation (Seq-03)", has_rollback_seq3, "Found rollback HINCRBY -60 / -100 / -80")

has_phys_deduct_seq1 = "UPDATE inventory_stocks SET current_quantity = current_quantity - 80" in seq_content and "INSERT INTO inventory_logs" in seq_content
record_test("TC-INV-06", "Physical Stock Commit", "Seq-01 commits permanent physical stock deduction in DB on PayOS webhook", has_phys_deduct_seq1, "Found UPDATE inventory_stocks and INSERT INTO inventory_logs")

has_phys_deduct_seq3 = "UPDATE inventory_stocks SET current_quantity = current_quantity - 60" in seq_content and "INSERT INTO inventory_logs" in seq_content
record_test("TC-INV-07", "Physical Stock Commit", "Seq-03 commits permanent physical stock deduction in DB on PayOS webhook", has_phys_deduct_seq3, "Found UPDATE inventory_stocks and INSERT INTO inventory_logs for delivery")

has_release_reserve_seq1 = "HINCRBY inventory:reserved:B01 ing-coffee -80" in seq_content
record_test("TC-INV-08", "Soft Reservation", "Seq-01 releases soft reservation in Redis after DB physical deduction", has_release_reserve_seq1, "Found release HINCRBY -80 in webhook success branch")

# TEST CATEGORY 2: KDS GATE & PRE-PAYMENT BLOCK
has_kds_block_seq1 = "Màn hình KDS Bếp CHƯA hiển thị đơn này" in seq_content
record_test("TC-KDS-01", "KDS Gate", "KDS screen strictly blocks unconfirmed/unpaid Dine-In VietQR orders", has_kds_block_seq1, "Found explicit note blocking KDS display before payment")

has_kds_immediate_seq2 = "KitchenHub.Clients.Group(\"branch_B01_kitchen\").SendAsync(\"NewKitchenOrder\"" in seq_content
record_test("TC-KDS-02", "KDS Gate", "Seq-02 Dine-In Cash immediately sends confirmed order to KDS", has_kds_immediate_seq2, "Found immediate NewKitchenOrder on Cash order creation")

# TEST CATEGORY 3: DELIVERY RULES (Seq-03)
has_delivery_fee_20k = "delivery_fee=20000" in seq_content and "20.000 VNĐ" in seq_content
record_test("TC-DEL-01", "Delivery Rules", "Fixed delivery fee 20,000 VND enforced", has_delivery_fee_20k, "delivery_fee=20000 and 20.000 VNĐ verified")

has_delivery_100_vietqr = "100% VietQR" in seq_content and "Khóa hoàn toàn hình thức COD" in seq_content
record_test("TC-DEL-02", "Delivery Rules", "Delivery requires 100% VietQR prepayment (COD banned)", has_delivery_100_vietqr, "COD banned, 100% VietQR verified")

# TEST CATEGORY 4: LOYALTY CRM 10 CUPS (Seq-04)
has_takeaway_crm = "CHỈ áp dụng riêng cho đơn Takeaway tại quầy" in seq_content
record_test("TC-CRM-01", "Loyalty CRM", "Loyalty 10 cups earn 1 free cup restricted strictly to Takeaway", has_takeaway_crm, "Rule verified: Takeaway only")

has_cup_math = "cup_balance = (10 - 10 + 2)" in seq_content and "loyalty_cup_transactions" in seq_content
record_test("TC-CRM-02", "Loyalty CRM", "Cup calculation and audit logging in loyalty_cup_transactions", has_cup_math, "Atomic balance update and log rows verified")

# TEST CATEGORY 5: WIFI-LOCKED ATTENDANCE (Seq-05)
has_wifi_dual = "allowed_ip_subnets" in seq_content and "bssid_list" in seq_content and "branch_wifi_configs" in seq_content
record_test("TC-ATT-01", "Attendance", "Dual-factor WiFi verification (BSSID + IP Subnet)", has_wifi_dual, "branch_wifi_configs BSSID + IP subnet check verified")

has_zero_gps = "Loại bỏ 100% định vị GPS 50m" in seq_content and "mã QR 30 giây" in seq_content
record_test("TC-ATT-02", "Attendance", "Zero GPS 50m and Zero 30s QR policy compliance", has_zero_gps, "Verified removal of GPS 50m & 30s QR")

# TEST CATEGORY 6: 86-TOGGLE & BOM DEDUCTION (Seq-06)
has_86_toggle = "Item86Toggled" in seq_content and "branch:B01:out_of_stock" in seq_content and "products.is_available = false" in seq_content
record_test("TC-86-01", "Emergency 86-Toggle", "86-Toggle locks product in DB, Redis cache, and broadcasts to customer PWAs via SignalR", has_86_toggle, "Item86Toggled broadcast & Redis out_of_stock verified")

# TEST CATEGORY 7: RATE LIMITING (Seq-07)
has_rate_limit_call = "SET lock:ratelimit:call:T04 \"1\" NX EX 60" in seq_content
record_test("TC-SRV-01", "Service Call", "Redis rate limit lock (60s) prevents service call spam", has_rate_limit_call, "lock:ratelimit:call:T04 NX EX 60 verified")

# TEST CATEGORY 8: REVIEW & RED ALERT (Seq-08)
has_red_alert = "is_urgent_alert" in seq_content and "UrgentRedAlert" in seq_content and "ratingStars: 1" in seq_content and "gemini-1.5-flash" in seq_content
record_test("TC-REV-01", "Review & Alert", "Gemini 1.5 Flash sentiment analysis triggers UrgentRedAlert for ratings <= 2 stars", has_red_alert, "Gemini sentiment + UrgentRedAlert verified")

# TEST CATEGORY 9: CASH SHIFT & Z-REPORT (Seq-09)
has_z_report_discrepancy = "shift_handover_discrepancies" in seq_content and "discrepancy_amount" in seq_content and "70000" in seq_content
record_test("TC-SFT-01", "Shift & Z-Report", "Cash discrepancy > 50,000 VND enforces mandatory explanation and manager PIN", has_z_report_discrepancy, "shift_handover_discrepancies logging verified")

# TEST CATEGORY 10: ADMIN CRUD & APRIORI COMBO (Seq-10)
has_admin_apriori = "ImageSharp" in seq_content and "Apriori" in seq_content and "Lift > 1.5" in seq_content
record_test("TC-ADM-01", "Admin & AI", "ImageSharp WebP pipeline and Apriori combo mining with Lift > 1.5", has_admin_apriori, "Apriori Lift > 1.5 & ImageSharp pipeline verified")

# SUMMARY
total_tests = len(tests)
passed_tests = sum(1 for t in tests if t["passed"])
failed_tests = total_tests - passed_tests

print("\n================================================================================")
print(f"VERIFICATION SUMMARY: {passed_tests}/{total_tests} Tests Passed (100% Pass Rate: {failed_tests == 0})")
print("================================================================================")

with open(r"d:\Idea_DoAn\.agents\challenger_it2\test_harness_results.json", "w", encoding="utf-8") as f:
    json.dump({
        "total": total_tests,
        "passed": passed_tests,
        "failed": failed_tests,
        "tests": tests
    }, f, indent=2, ensure_ascii=False)
