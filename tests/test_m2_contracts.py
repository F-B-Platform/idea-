"""
Empirical Verification Test Suite for Milestone M2 (API Contracts & UI/UX Design System)
Challenger 2 Empirical Harness
"""

import hmac
import hashlib
import ipaddress
import re
import json
import time
from typing import Dict, Any, Tuple, Optional

# ==============================================================================
# SCENARIO 1: PayOS Webhook HMAC SHA256 & Redis Lock Idempotency Verification
# ==============================================================================

class PayOSWebhookValidator:
    def __init__(self, checksum_key: str):
        self.checksum_key = checksum_key

    def verify_raw_body_signature(self, raw_body: str, received_signature: str) -> bool:
        """Verifies signature by hashing raw body directly (as written in C# snippet)."""
        mac = hmac.new(self.checksum_key.encode('utf-8'), raw_body.encode('utf-8'), hashlib.sha256)
        computed_signature = mac.hexdigest().lower()
        return hmac.compare_digest(computed_signature, received_signature.lower())

    def verify_payos_standard_signature(self, data_dict: dict, received_signature: str) -> bool:
        """Verifies signature by sorting data keys alphabetically per official PayOS specification."""
        sorted_keys = sorted(data_dict.keys())
        sign_string = "&".join(f"{k}={data_dict[k]}" for k in sorted_keys if data_dict[k] is not None)
        mac = hmac.new(self.checksum_key.encode('utf-8'), sign_string.encode('utf-8'), hashlib.sha256)
        computed_signature = mac.hexdigest().lower()
        return hmac.compare_digest(computed_signature, received_signature.lower())


class MockRedisLockIdempotency:
    def __init__(self):
        self.store = {}

    def acquire_lock(self, key: str, ttl_seconds: int = 60) -> bool:
        now = time.time()
        if key in self.store:
            val, expiry = self.store[key]
            if now < expiry:
                return False  # Already locked / processed
        self.store[key] = ("processing", now + ttl_seconds)
        return True

    def release_lock_flawed(self, key: str):
        """Flawed release pattern in finally block: deletes key immediately upon completion."""
        if key in self.store:
            del self.store[key]

    def mark_completed_correct(self, key: str, ttl_seconds: int = 86400):
        """Proper idempotency pattern: retains 'completed' flag for TTL duration."""
        self.store[key] = ("completed", time.time() + ttl_seconds)


def test_payos_webhook_and_idempotency() -> Dict[str, Any]:
    checksum_key = "a1b2c3d4e5f67890123456789abcdef0123456789abcdef0123456789abcdef0"
    validator = PayOSWebhookValidator(checksum_key)

    webhook_data = {
        "orderCode": 10042,
        "amount": 104000,
        "description": "ORD0042",
        "accountNumber": "0001882199201",
        "reference": "FT262359918239",
        "transactionDateTime": "2026-08-23T14:32:15Z",
        "currency": "VND",
        "paymentLinkId": "pay-9918239-0042"
    }
    
    # 1. Test HMAC computation with standard PayOS sorted query string
    sorted_keys = sorted(webhook_data.keys())
    sign_str = "&".join(f"{k}={webhook_data[k]}" for k in sorted_keys)
    mac = hmac.new(checksum_key.encode('utf-8'), sign_str.encode('utf-8'), hashlib.sha256)
    expected_payos_sig = mac.hexdigest()

    # Verify matching
    valid_payos = validator.verify_payos_standard_signature(webhook_data, expected_payos_sig)
    
    # Test Raw Body Hashing (what C# snippet line 1417 shows)
    raw_payload_json = json.dumps({"code": "00", "desc": "success", "data": webhook_data, "signature": expected_payos_sig})
    raw_body_mac = hmac.new(checksum_key.encode('utf-8'), raw_payload_json.encode('utf-8'), hashlib.sha256).hexdigest()
    valid_raw = validator.verify_raw_body_signature(raw_payload_json, raw_body_mac)

    # 2. Test Idempotency with flawed delete-in-finally
    redis = MockRedisLockIdempotency()
    lock_key = f"lock:webhook:payos:{webhook_data['paymentLinkId']}"

    # First delivery
    first_acquired = redis.acquire_lock(lock_key, 60)
    # Simulate flawed controller: deletes lock key in finally block
    redis.release_lock_flawed(lock_key)

    # Immediate duplicate delivery from PayOS retry
    second_acquired_flawed = redis.acquire_lock(lock_key, 60)

    # Now test correct pattern
    redis_correct = MockRedisLockIdempotency()
    first_acquired_correct = redis_correct.acquire_lock(lock_key, 60)
    redis_correct.mark_completed_correct(lock_key, 86400)
    second_acquired_correct = redis_correct.acquire_lock(lock_key, 60)

    return {
        "payos_standard_signature_valid": valid_payos,
        "raw_body_signature_valid": valid_raw,
        "flawed_finally_allows_duplicate_replay": second_acquired_flawed, # True indicates vulnerability!
        "correct_idempotency_blocks_duplicate": not second_acquired_correct
    }


# ==============================================================================
# SCENARIO 2: WiFi Attendance (BSSID + IP Subnet check + Staff payload)
# ==============================================================================

class WifiAttendanceChecker:
    BSSID_REGEX = re.compile(r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$")

    @staticmethod
    def validate_bssid_format(bssid: str) -> bool:
        return bool(WifiAttendanceChecker.BSSID_REGEX.match(bssid))

    @staticmethod
    def is_ip_in_subnet(client_ip: str, gateway_ip: str, subnet_mask: str) -> bool:
        try:
            net = ipaddress.IPv4Network(f"{gateway_ip}/{subnet_mask}", strict=False)
            ip = ipaddress.IPv4Address(client_ip)
            return ip in net
        except ValueError:
            return False

    @staticmethod
    def checkin(payload: dict, branch_wifi_configs: list) -> Tuple[bool, str, int]:
        # Validate DTO
        if not payload.get("branchId"):
            return False, "Chi nhánh không được để trống.", 400
        if not payload.get("employeeCode"):
            return False, "Mã nhân viên không được để trống.", 400
        
        bssid = payload.get("clientBssid", "")
        if not WifiAttendanceChecker.validate_bssid_format(bssid):
            return False, "Định dạng địa chỉ MAC BSSID không hợp lệ.", 400

        client_ip = payload.get("clientIp", "")
        if not client_ip:
            return False, "Địa chỉ IP client không được để trống.", 400

        # Match against branch wifi configs
        normalized_bssid = bssid.replace("-", ":").upper()
        matched = False
        matched_ssid = ""

        for config in branch_wifi_configs:
            if not config.get("isActive", True):
                continue
            cfg_bssid = config.get("bssid", "").replace("-", ":").upper()
            if cfg_bssid == normalized_bssid:
                if WifiAttendanceChecker.is_ip_in_subnet(client_ip, config.get("ipGateway"), config.get("subnetMask")):
                    matched = True
                    matched_ssid = config.get("ssid")
                    break

        if not matched:
            return False, "Bạn đang dùng 4G hoặc mạng ngoài quán. Vui lòng kết nối WiFi nội bộ chi nhánh.", 400

        return True, f"Chấm công vào ca thành công trên WiFi {matched_ssid}", 200


def test_wifi_attendance() -> Dict[str, Any]:
    branch_configs = [
        {
            "ssid": "SmartCoffee_Quan1_Staff",
            "bssid": "00:14:22:01:23:45",
            "ipGateway": "192.168.1.1",
            "subnetMask": "255.255.255.0",
            "isActive": True
        },
        {
            "ssid": "SmartCoffee_Quan1_F2",
            "bssid": "00:14:22:01:23:46",
            "ipGateway": "192.168.1.2",
            "subnetMask": "255.255.255.0",
            "isActive": True
        }
    ]

    # Test Cases
    cases = [
        # 1. Valid Checkin
        {"payload": {"branchId": "b1", "employeeCode": "NV-001", "clientBssid": "00:14:22:01:23:45", "clientIp": "192.168.1.45"}, "expected": (True, 200)},
        # 2. Valid with hyphen MAC
        {"payload": {"branchId": "b1", "employeeCode": "NV-001", "clientBssid": "00-14-22-01-23-45", "clientIp": "192.168.1.100"}, "expected": (True, 200)},
        # 3. Invalid MAC format
        {"payload": {"branchId": "b1", "employeeCode": "NV-001", "clientBssid": "00:14:22:01:23", "clientIp": "192.168.1.45"}, "expected": (False, 400)},
        # 4. Unknown BSSID (home wifi)
        {"payload": {"branchId": "b1", "employeeCode": "NV-001", "clientBssid": "AA:BB:CC:DD:EE:FF", "clientIp": "192.168.1.45"}, "expected": (False, 400)},
        # 5. Correct BSSID but wrong IP (outside 192.168.1.0/24, e.g. 10.0.0.5 or 4G IP)
        {"payload": {"branchId": "b1", "employeeCode": "NV-001", "clientBssid": "00:14:22:01:23:45", "clientIp": "14.241.12.8"}, "expected": (False, 400)},
        # 6. Missing Employee Code
        {"payload": {"branchId": "b1", "employeeCode": "", "clientBssid": "00:14:22:01:23:45", "clientIp": "192.168.1.45"}, "expected": (False, 400)},
    ]

    results = []
    for i, c in enumerate(cases):
        success, msg, code = WifiAttendanceChecker.checkin(c["payload"], branch_configs)
        exp_success, exp_code = c["expected"]
        passed = (success == exp_success and code == exp_code)
        results.append({"case": i + 1, "passed": passed, "got_code": code, "msg": msg})

    all_passed = all(r["passed"] for r in results)
    return {"all_cases_passed": all_passed, "details": results}


# ==============================================================================
# SCENARIO 3: Takeaway POS Order Creation & 10 Cups Loyalty Logic
# ==============================================================================

class TakeawayPosEngine:
    @staticmethod
    def process_order(payload: dict, customer_crm: Optional[dict], product_catalog: dict) -> Tuple[bool, dict, int]:
        # Validate branch
        if not payload.get("branchId"):
            return False, {"error": "Chi nhánh bắt buộc"}, 400
        
        items = payload.get("items", [])
        if not items:
            return False, {"error": "Đơn hàng phải có ít nhất 1 món"}, 400

        # Calculate subtotal
        subtotal = 0
        ordered_cups_count = 0
        for item in items:
            p_id = item.get("productId")
            if p_id not in product_catalog:
                return False, {"error": f"Món {p_id} không tồn tại"}, 404
            prod = product_catalog[p_id]
            qty = item.get("quantity", 1)
            size = item.get("size", "M")
            price_adj = prod.get("sizes", {}).get(size, 0)
            item_price = prod["basePrice"] + price_adj
            subtotal += item_price * qty
            ordered_cups_count += qty

        # Loyalty calculation
        redeem_free_cup = payload.get("redeemFreeCup", False)
        loyalty_discount = 0
        current_cups = customer_crm.get("accumulatedCups", 0) if customer_crm else 0

        if redeem_free_cup:
            if not customer_crm:
                return False, {"error": "Cần tra cứu SĐT CRM để đổi ly miễn phí"}, 422
            if current_cups < 10:
                return False, {"error": f"Quỹ ly không đủ để đổi ly free (Hiện có: {current_cups}/10 ly)"}, 422
            
            free_p_id = payload.get("freeProductId")
            if not free_p_id or free_p_id not in product_catalog:
                return False, {"error": "Chưa chọn món đổi miễn phí hợp lệ"}, 400
            
            free_prod = product_catalog[free_p_id]
            loyalty_discount = free_prod["basePrice"] # Base price of free cup

        final_amount = max(0, subtotal - loyalty_discount)

        # Cash handling
        payment_method = payload.get("paymentMethod", "Cash")
        cash_given = payload.get("cashGiven", 0)
        cash_change = 0
        if payment_method == "Cash":
            if cash_given < final_amount:
                return False, {"error": f"Tiền khách đưa ({cash_given:,}đ) nhỏ hơn tổng tiền phải trả ({final_amount:,}đ)"}, 400
            cash_change = cash_given - final_amount

        # Update remaining cups in CRM
        new_cups = current_cups
        if redeem_free_cup:
            new_cups -= 10
        # For Takeaway, purchased paid cups are added to loyalty
        # Note: 1 free cup redeemed doesn't count towards new accumulation
        paid_cups = ordered_cups_count - (1 if redeem_free_cup else 0)
        new_cups += max(0, paid_cups)

        return True, {
            "orderId": "o-tk-001",
            "orderNumber": "TK-20260823-0089",
            "subtotalAmount": subtotal,
            "loyaltyDiscount": loyalty_discount,
            "finalAmount": final_amount,
            "cashGiven": cash_given,
            "cashChange": cash_change,
            "remainingLoyaltyCups": new_cups,
            "status": "Confirmed"
        }, 201


def test_takeaway_pos_and_loyalty() -> Dict[str, Any]:
    catalog = {
        "p1": {"name": "Cà Phê Muối", "basePrice": 35000, "sizes": {"M": 0, "L": 7000}},
        "p2": {"name": "Bạc Xỉu 3 Tầng", "basePrice": 39000, "sizes": {"S": -4000, "M": 0, "L": 8000}},
    }

    # Case 1: Customer with 10 cups redeems 1 free cup (orders 2x p2 Size M = 78,000đ, discount 39,000đ -> final 39,000đ, cash 100k -> change 61k)
    crm_10 = {"customerId": "c1", "phone": "0909123456", "accumulatedCups": 10}
    payload_1 = {
        "branchId": "b1",
        "customerPhone": "0909123456",
        "redeemFreeCup": True,
        "freeProductId": "p2",
        "paymentMethod": "Cash",
        "cashGiven": 100000,
        "items": [{"productId": "p2", "size": "M", "quantity": 2}]
    }
    s1, r1, c1 = TakeawayPosEngine.process_order(payload_1, crm_10, catalog)

    # Case 2: Customer with 7 cups tries to redeem free cup -> Should return 422
    crm_7 = {"customerId": "c2", "phone": "0912345678", "accumulatedCups": 7}
    payload_2 = {
        "branchId": "b1",
        "customerPhone": "0912345678",
        "redeemFreeCup": True,
        "freeProductId": "p2",
        "paymentMethod": "Cash",
        "cashGiven": 100000,
        "items": [{"productId": "p2", "size": "M", "quantity": 2}]
    }
    s2, r2, c2 = TakeawayPosEngine.process_order(payload_2, crm_7, catalog)

    # Case 3: Cash given less than final amount -> Should return 400
    payload_3 = {
        "branchId": "b1",
        "customerPhone": "0909123456",
        "redeemFreeCup": False,
        "paymentMethod": "Cash",
        "cashGiven": 50000,
        "items": [{"productId": "p2", "size": "M", "quantity": 2}] # Total 78,000đ > 50,000đ
    }
    s3, r3, c3 = TakeawayPosEngine.process_order(payload_3, crm_10, catalog)

    return {
        "case1_redemption_success": (s1 and c1 == 201 and r1["loyaltyDiscount"] == 39000 and r1["cashChange"] == 61000 and r1["remainingLoyaltyCups"] == 1),
        "case2_insufficient_cups_rejected_422": (not s2 and c2 == 422),
        "case3_insufficient_cash_rejected_400": (not s3 and c3 == 400)
    }


# ==============================================================================
# SCENARIO 4: Delivery Order Creation API (20,000 VND fee, phone, address)
# ==============================================================================

class DeliveryOrderEngine:
    PHONE_REGEX = re.compile(r"^(03|05|07|08|09)\d{8}$")
    MANDATORY_DELIVERY_FEE = 20000

    @staticmethod
    def create_delivery_order(payload: dict, product_catalog: dict) -> Tuple[bool, dict, int]:
        # Branch validation
        if not payload.get("branchId"):
            return False, {"error": "Chi nhánh bắt buộc"}, 400

        # Phone validation (10 digits starting with 03, 05, 07, 08, 09)
        phone = payload.get("recipientPhone", "")
        if not DeliveryOrderEngine.PHONE_REGEX.match(phone):
            return False, {
                "error": "Số điện thoại người nhận bắt buộc và phải có định dạng 10 chữ số bắt đầu bằng 03, 05, 07, 08, 09."
            }, 400

        # Delivery Address validation (min 10 chars)
        address = payload.get("deliveryAddress", "")
        if not address or len(address.strip()) < 10:
            return False, {
                "error": "Địa chỉ giao hàng không được để trống và phải có độ dài tối thiểu 10 ký tự."
            }, 400

        # Items
        items = payload.get("items", [])
        if not items:
            return False, {"error": "Đơn hàng phải có ít nhất 1 món"}, 400

        subtotal = 0
        for item in items:
            p_id = item.get("productId")
            if p_id not in product_catalog:
                return False, {"error": f"Món {p_id} không tồn tại"}, 404
            prod = product_catalog[p_id]
            qty = item.get("quantity", 1)
            size = item.get("size", "M")
            price_adj = prod.get("sizes", {}).get(size, 0)
            subtotal += (prod["basePrice"] + price_adj) * qty

        # Enforce server-side 20,000 VND fee (ignore client override)
        delivery_fee = DeliveryOrderEngine.MANDATORY_DELIVERY_FEE
        final_amount = subtotal + delivery_fee

        # Generates VietQR dynamic link with 10-minute expiry
        viet_qr_data = {
            "qrCodeUrl": f"https://img.vietqr.io/image/ICB-0001882199201-compact2.png?amount={final_amount}&addInfo=DEL0015",
            "accountNumber": "0001882199201",
            "transferContent": "DEL0015",
            "amount": final_amount,
            "expiresAtUtc": "2026-08-23T14:40:00Z"
        }

        return True, {
            "orderId": "o-del-001",
            "orderNumber": "DEL-20260823-0015",
            "subtotalAmount": subtotal,
            "deliveryFee": delivery_fee,
            "finalAmount": final_amount,
            "status": "PendingPayment",
            "vietQr": viet_qr_data
        }, 201


def test_delivery_order_api() -> Dict[str, Any]:
    catalog = {
        "p1": {"name": "Trà Đào Cam Sả", "basePrice": 35000, "sizes": {"M": 0, "L": 4000}},
    }

    # Case 1: Valid Delivery Order
    payload_valid = {
        "branchId": "b1",
        "recipientName": "Nguyễn Hoàng Nam",
        "recipientPhone": "0987654321",
        "deliveryAddress": "Tầng 12, Tòa nhà Bitexco, 2 Hải Triều, Q.1, TP.HCM",
        "items": [{"productId": "p1", "size": "L", "quantity": 2}] # 39,000 x 2 = 78,000 + 20,000 = 98,000
    }
    s1, r1, c1 = DeliveryOrderEngine.create_delivery_order(payload_valid, catalog)

    # Case 2: Invalid Phone (starts with 01, 11 digits)
    payload_invalid_phone = {
        "branchId": "b1",
        "recipientPhone": "01234567890",
        "deliveryAddress": "Tầng 12, Tòa nhà Bitexco, 2 Hải Triều, Q.1, TP.HCM",
        "items": [{"productId": "p1", "size": "M", "quantity": 1}]
    }
    s2, r2, c2 = DeliveryOrderEngine.create_delivery_order(payload_invalid_phone, catalog)

    # Case 3: Short Address (< 10 chars, e.g. "Q1 TP")
    payload_short_address = {
        "branchId": "b1",
        "recipientPhone": "0987654321",
        "deliveryAddress": "Q1 TP",
        "items": [{"productId": "p1", "size": "M", "quantity": 1}]
    }
    s3, r3, c3 = DeliveryOrderEngine.create_delivery_order(payload_short_address, catalog)

    return {
        "case1_valid_order_with_20k_fee": (s1 and c1 == 201 and r1["deliveryFee"] == 20000 and r1["finalAmount"] == 98000 and r1["status"] == "PendingPayment"),
        "case2_invalid_phone_rejected": (not s2 and c2 == 400),
        "case3_short_address_rejected": (not s3 and c3 == 400)
    }


# ==============================================================================
# SCENARIO 5: Dine-In Branch A vs Branch B Order & Payment Flow Contracts
# ==============================================================================

class DineInFlowEngine:
    @staticmethod
    def create_prepaid_branch_a(payload: dict, catalog: dict) -> Tuple[bool, dict, int]:
        """Branch A: VietQR Prepaid, Status: PendingPayment, returns VietQR, NO Kitchen notification yet."""
        if not payload.get("branchId") or not payload.get("tableId"):
            return False, {"error": "Chi nhánh và Bàn bắt buộc"}, 400
        
        items = payload.get("items", [])
        if not items:
            return False, {"error": "Đơn hàng phải có ít nhất 1 món"}, 400

        subtotal = sum(catalog[i["productId"]]["basePrice"] * i.get("quantity", 1) for i in items)
        discount = payload.get("discountAmount", 0)
        final_amount = max(0, subtotal - discount)

        return True, {
            "orderId": "o-dinein-a-01",
            "orderNumber": "ORD-20260823-0042",
            "subtotalAmount": subtotal,
            "discountAmount": discount,
            "deliveryFee": 0,
            "finalAmount": final_amount,
            "status": "PendingPayment",
            "kitchenNotified": False, # KDS will only receive ticket AFTER PayOS webhook confirms 'Paid'
            "vietQr": {
                "qrCodeUrl": f"https://img.vietqr.io/image/ICB-0001882199201-compact2.png?amount={final_amount}&addInfo=ORD0042",
                "accountNumber": "0001882199201",
                "transferContent": "ORD0042",
                "expiresAtUtc": "2026-08-23T14:40:00Z"
            }
        }, 201

    @staticmethod
    def create_postpaid_branch_b(payload: dict, catalog: dict) -> Tuple[bool, dict, int]:
        """Branch B: Cash Postpaid, Status: Confirmed, INSTANTLY pushes to KDS via SignalR, NO VietQR in initial response."""
        if not payload.get("branchId") or not payload.get("tableId"):
            return False, {"error": "Chi nhánh và Bàn bắt buộc"}, 400
        
        items = payload.get("items", [])
        if not items:
            return False, {"error": "Đơn hàng phải có ít nhất 1 món"}, 400

        subtotal = sum(catalog[i["productId"]]["basePrice"] * i.get("quantity", 1) for i in items)
        discount = payload.get("discountAmount", 0)
        final_amount = max(0, subtotal - discount)

        return True, {
            "orderId": "o-dinein-b-01",
            "orderNumber": "ORD-20260823-0043",
            "finalAmount": final_amount,
            "status": "Confirmed",
            "estimatedMinutes": 7,
            "kitchenNotified": True, # Sent immediately to KitchenHub (OrderConfirmedCash)
            "vietQr": None, # Initial creation does not generate upfront payment QR
            "message": "Bếp đã tiếp nhận đơn và đang pha chế. Nhân viên sẽ mang đồ uống kèm hóa đơn ra bàn."
        }, 201


def test_dine_in_branches() -> Dict[str, Any]:
    catalog = {
        "p1": {"name": "Cà Phê Muối", "basePrice": 35000},
        "p2": {"name": "Bạc Xỉu", "basePrice": 39000}
    }

    payload = {
        "branchId": "b1",
        "tableId": "t5",
        "items": [{"productId": "p1", "quantity": 1}, {"productId": "p2", "quantity": 1}]
    }

    # Test Branch A
    s_a, r_a, c_a = DineInFlowEngine.create_prepaid_branch_a(payload, catalog)

    # Test Branch B
    s_b, r_b, c_b = DineInFlowEngine.create_postpaid_branch_b(payload, catalog)

    branch_a_correct = (s_a and c_a == 201 and r_a["status"] == "PendingPayment" and r_a["kitchenNotified"] is False and r_a["vietQr"] is not None)
    branch_b_correct = (s_b and c_b == 201 and r_b["status"] == "Confirmed" and r_b["kitchenNotified"] is True and r_b["vietQr"] is None and r_b["estimatedMinutes"] == 7)

    return {
        "branch_a_prepaid_verified": branch_a_correct,
        "branch_b_postpaid_verified": branch_b_correct
    }


# ==============================================================================
# MAIN TEST RUNNER
# ==============================================================================

if __name__ == "__main__":
    print("=== EMPIRICAL TEST RUNNER: MILESTONE M2 ===")
    
    t1 = test_payos_webhook_and_idempotency()
    print("\n[Scenario 1] PayOS Webhook HMAC & Idempotency:")
    print(json.dumps(t1, indent=2))

    t2 = test_wifi_attendance()
    print("\n[Scenario 2] WiFi Attendance Dual-Check:")
    print(json.dumps(t2, indent=2))

    t3 = test_takeaway_pos_and_loyalty()
    print("\n[Scenario 3] Takeaway POS & 10-Cup Loyalty:")
    print(json.dumps(t3, indent=2))

    t4 = test_delivery_order_api()
    print("\n[Scenario 4] Delivery Order 20k Fee & Constraints:")
    print(json.dumps(t4, indent=2))

    t5 = test_dine_in_branches()
    print("\n[Scenario 5] Dine-In Branch A vs Branch B:")
    print(json.dumps(t5, indent=2))

    all_passed = (
        t1["payos_standard_signature_valid"] and
        t1["correct_idempotency_blocks_duplicate"] and
        t2["all_cases_passed"] and
        t3["case1_redemption_success"] and
        t3["case2_insufficient_cups_rejected_422"] and
        t3["case3_insufficient_cash_rejected_400"] and
        t4["case1_valid_order_with_20k_fee"] and
        t4["case2_invalid_phone_rejected"] and
        t4["case3_short_address_rejected"] and
        t5["branch_a_prepaid_verified"] and
        t5["branch_b_postpaid_verified"]
    )

    print("\n=======================================================")
    print(f"OVERALL EMPIRICAL TEST RESULT: {'SUCCESS (ALL CHECKS PASSED)' if all_passed else 'FAILED'}")
    print("=======================================================")
