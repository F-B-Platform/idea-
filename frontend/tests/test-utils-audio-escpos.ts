import {
  formatCurrencyVND,
  formatDateTime,
  formatTimeOnly,
  calculateSlaStatus,
  validateVietnamesePhone,
  generateEscPosReceipt,
  cn,
} from "../src/lib/utils";
import { OrderDto } from "../src/types";

let passed = 0;
let failed = 0;

function assert(condition: boolean, msg: string) {
  if (!condition) {
    console.error(`❌ FAIL: ${msg}`);
    failed++;
    throw new Error(`Assertion failed: ${msg}`);
  } else {
    console.log(`✅ PASS: ${msg}`);
    passed++;
  }
}

async function runUtilsTests() {
  console.log("==========================================");
  console.log("TEST SUITE: Utilities, ESC/POS & Formatting");
  console.log("==========================================");

  // 1. cn helper
  assert(cn("base-class", false && "hidden", "active-class") === "base-class active-class", "cn merges classes properly");
  assert(cn("p-4", "p-2") === "p-2", "cn merges conflicting tailwind classes with precedence");

  // 2. formatCurrencyVND
  assert(formatCurrencyVND(35000).includes("35.000"), "formatCurrencyVND formats 35000 correctly");
  assert(formatCurrencyVND(0).includes("0"), "formatCurrencyVND handles 0");
  assert(formatCurrencyVND(NaN) === "0 ₫", "formatCurrencyVND handles NaN safely");
  assert(formatCurrencyVND(-50000).includes("50.000"), "formatCurrencyVND handles negative amount");

  // 3. formatDateTime & formatTimeOnly
  const validIso = "2026-08-25T14:30:00Z";
  assert(formatDateTime(validIso) !== "--:--", "formatDateTime formats valid ISO");
  assert(formatDateTime("") === "--:--", "formatDateTime handles empty string");
  assert(formatDateTime(undefined) === "--:--", "formatDateTime handles undefined");
  assert(formatDateTime("invalid-date-string") === "--:--", "formatDateTime handles invalid string");

  assert(formatTimeOnly(validIso) !== "--:--", "formatTimeOnly formats valid ISO");
  assert(formatTimeOnly("") === "--:--", "formatTimeOnly handles empty string");
  assert(formatTimeOnly(undefined) === "--:--", "formatTimeOnly handles undefined");
  assert(formatTimeOnly("invalid-date-string") === "--:--", "formatTimeOnly handles invalid date");

  // 4. calculateSlaStatus
  const slaGreen0 = calculateSlaStatus(0);
  assert(slaGreen0.variant === "success" && slaGreen0.label === "00:00", "SLA 0s is green");

  const slaGreen179 = calculateSlaStatus(179);
  assert(slaGreen179.variant === "success" && slaGreen179.label === "02:59", "SLA 179s is green");

  const slaAmber180 = calculateSlaStatus(180);
  assert(slaAmber180.variant === "warning" && slaAmber180.label === "03:00", "SLA 180s is warning (amber)");

  const slaAmber300 = calculateSlaStatus(300);
  assert(slaAmber300.variant === "warning" && slaAmber300.label === "05:00", "SLA 300s is warning (amber)");

  const slaRed301 = calculateSlaStatus(301);
  assert(slaRed301.variant === "danger" && slaRed301.label.includes("QUÁ HẠN"), "SLA 301s is danger (red pulsing)");

  // 5. validateVietnamesePhone
  assert(validateVietnamesePhone("0901234567").isValid === true, "Valid 090 phone passes");
  assert(validateVietnamesePhone("0388776655").isValid === true, "Valid 038 phone passes");
  assert(validateVietnamesePhone("0561234567").isValid === true, "Valid 056 phone passes");
  assert(validateVietnamesePhone("0701234567").isValid === true, "Valid 070 phone passes");
  assert(validateVietnamesePhone("0861234567").isValid === true, "Valid 086 phone passes");
  assert(validateVietnamesePhone(" 090 123 4567 ").isValid === true, "Phone with whitespace cleans and passes");
  assert(validateVietnamesePhone("090-123-4567").isValid === true, "Phone with hyphens cleans and passes");

  assert(validateVietnamesePhone("").isValid === false, "Empty phone rejected");
  assert(validateVietnamesePhone("1234567890").isValid === false, "Phone not starting with 03/05/07/08/09 rejected");
  assert(validateVietnamesePhone("090123456").isValid === false, "9-digit phone rejected");
  assert(validateVietnamesePhone("09012345678").isValid === false, "11-digit phone rejected");
  assert(validateVietnamesePhone("090abcd567").isValid === false, "Non-digit phone rejected");

  // 6. generateEscPosReceipt
  console.log("\n--- Testing ESC/POS Thermal Receipt Generation ---");
  const fullOrder: OrderDto = {
    id: "ord-123",
    orderCode: "ORD-20260825-001",
    branchId: "br-01",
    branchName: "SMART F&B NGUYEN HUE",
    tableNumber: "T05",
    orderType: "DineIn",
    status: "Completed",
    subTotal: 85000,
    discountAmount: 10000,
    deliveryFee: 0,
    totalAmount: 75000,
    paymentMethod: "VIETQR",
    paymentStatus: "Paid",
    createdAt: "2026-08-25T10:00:00Z",
    items: [
      {
        productId: "p-01",
        productName: "Cà Phê Muối Hoàng Gia Đặc Biệt Thượng Hạng",
        size: "L",
        quantity: 2,
        unitPrice: 40000,
        totalPrice: 80000,
        sugarLevel: "50%",
        iceLevel: "70%",
      },
      {
        productId: "p-02",
        productName: "Bánh Croissant",
        size: "Regular",
        quantity: 1,
        unitPrice: 5000,
        totalPrice: 5000,
      },
    ],
  };

  const receiptOutput = generateEscPosReceipt(fullOrder);
  assert(receiptOutput.includes("SMART F&B NGUYEN HUE"), "Receipt contains branch name");
  assert(receiptOutput.includes("HÓA ĐƠN BÁN HÀNG"), "Receipt contains header");
  assert(receiptOutput.includes("ORD-20260825-001"), "Receipt contains order code");
  assert(receiptOutput.includes("Vị Trí: T05"), "Receipt contains table number");
  assert(receiptOutput.includes("Tại Bàn"), "Receipt contains DineIn label");
  assert(receiptOutput.includes("Chiết khấu:"), "Receipt displays discount line");
  assert(receiptOutput.includes("VietQR Chuyển Khoản"), "Receipt displays payment method");
  assert(receiptOutput.includes("SmartFB@2026"), "Receipt contains wifi footer");

  // Stress-test ESC/POS with null/edge values
  const minimalOrder: OrderDto = {
    id: "ord-min",
    orderCode: "ORD-MIN-001",
    branchId: "br-01",
    orderType: "TakeAway",
    status: "Paid",
    subTotal: 0,
    discountAmount: 0,
    deliveryFee: 0,
    totalAmount: 0,
    paymentMethod: "CASH",
    paymentStatus: "Paid",
    createdAt: "2026-08-25T10:00:00Z",
    items: [],
  };

  const minReceipt = generateEscPosReceipt(minimalOrder);
  assert(minReceipt.includes("SMART F&B COFFEE & TEA"), "Receipt defaults missing branchName safely");
  assert(!minReceipt.includes("Vị Trí:"), "Receipt safely skips missing tableNumber");
  assert(minReceipt.includes("Mang Về"), "Receipt displays TakeAway label");
  assert(minReceipt.includes("Tiền Mặt"), "Receipt displays CASH payment method");

  console.log("\n==========================================");
  console.log(`SUMMARY: ${passed} PASSED, ${failed} FAILED`);
  console.log("==========================================");

  if (failed > 0) {
    process.exit(1);
  }
}

runUtilsTests().catch((err) => {
  console.error("FATAL ERROR in utils test runner:", err);
  process.exit(1);
});
