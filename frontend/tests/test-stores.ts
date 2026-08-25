import { useAuthStore } from "../src/stores/useAuthStore";
import { useCartStore } from "../src/stores/useCartStore";
import { usePosStore } from "../src/stores/usePosStore";
import { useShiftStore } from "../src/stores/useShiftStore";
import { useKdsStore } from "../src/stores/useKdsStore";
import { useTableStore } from "../src/stores/useTableStore";
import { KdsTicketDto, TableDto, UserProfile } from "../src/types";

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

async function runStoreTests() {
  console.log("==========================================");
  console.log("TEST SUITE 1: useAuthStore");
  console.log("==========================================");
  {
    useAuthStore.getState().logout();
    assert(useAuthStore.getState().isAuthenticated === false, "Initial unauthenticated");
    assert(useAuthStore.getState().user === null, "Initial user is null");

    const mockUser: UserProfile = {
      id: "u-01",
      employeeCode: "EMP001",
      fullName: "Nguyễn Văn Thu Ngân",
      role: "CashierStaff",
      branchId: "br-01",
      isActive: true,
    };

    useAuthStore.getState().login({ accessToken: "mock-jwt-token", refreshToken: "mock-refresh" }, mockUser);
    assert(useAuthStore.getState().isAuthenticated === true, "Authenticated after login");
    assert(useAuthStore.getState().token === "mock-jwt-token", "Token set correctly");
    assert(useAuthStore.getState().user?.fullName === "Nguyễn Văn Thu Ngân", "User data preserved");

    useAuthStore.getState().updateUser({ fullName: "Nguyễn Văn A - Updated" });
    assert(useAuthStore.getState().user?.fullName === "Nguyễn Văn A - Updated", "Partial user update works");

    useAuthStore.getState().logout();
    assert(useAuthStore.getState().isAuthenticated === false, "Logged out successfully");
    assert(useAuthStore.getState().token === null, "Token cleared");
    assert(useAuthStore.getState().user === null, "User cleared");
  }

  console.log("\n==========================================");
  console.log("TEST SUITE 2: useCartStore");
  console.log("==========================================");
  {
    useCartStore.getState().clearCart();
    assert(useCartStore.getState().items.length === 0, "Cart empty initially");
    assert(useCartStore.getState().getSubtotal() === 0, "Subtotal is 0 when empty");
    assert(useCartStore.getState().getTotalAmount() === 0, "Total amount is 0 when empty");

    // Add item 1: Cà phê muối M
    useCartStore.getState().addItem({
      productId: "prod-01",
      productName: "Cà Phê Muối Hoàng Gia",
      sizeId: "size-m",
      sizeName: "M",
      unitPrice: 35000,
      quantity: 2,
      sugarLevel: "50%",
      iceLevel: "70%",
      toppings: [{ modifierId: "top-01", name: "Kem Muối Thêm", price: 10000 }],
      notes: "Ít ngọt",
    });

    assert(useCartStore.getState().items.length === 1, "Item added to cart");
    assert(useCartStore.getState().getTotalItemsCount() === 2, "Quantity is 2");
    // (35000 + 10000) * 2 = 90000
    assert(useCartStore.getState().getSubtotal() === 90000, "Subtotal is 90,000 VND");

    // Add identical item -> should merge and increase quantity
    useCartStore.getState().addItem({
      productId: "prod-01",
      productName: "Cà Phê Muối Hoàng Gia",
      sizeId: "size-m",
      sizeName: "M",
      unitPrice: 35000,
      quantity: 1,
      sugarLevel: "50%",
      iceLevel: "70%",
      toppings: [{ modifierId: "top-01", name: "Kem Muối Thêm", price: 10000 }],
      notes: "Ít ngọt",
    });

    assert(useCartStore.getState().items.length === 1, "Merged identical item into existing entry");
    assert(useCartStore.getState().getTotalItemsCount() === 3, "Quantity increased to 3");
    assert(useCartStore.getState().getSubtotal() === 135000, "Subtotal updated to 135,000 VND");

    // Add different modifier item -> should create separate entry
    useCartStore.getState().addItem({
      productId: "prod-01",
      productName: "Cà Phê Muối Hoàng Gia",
      sizeId: "size-m",
      sizeName: "M",
      unitPrice: 35000,
      quantity: 1,
      sugarLevel: "100%",
      iceLevel: "100%",
      toppings: [],
    });

    assert(useCartStore.getState().items.length === 2, "Different item added separately");
    // 135000 + 35000 = 170000
    assert(useCartStore.getState().getSubtotal() === 170000, "Subtotal is 170,000 VND");

    // Test voucher discount
    useCartStore.getState().applyVoucher("SUMMER20", 20000);
    assert(useCartStore.getState().discountAmount === 20000, "Voucher applied");
    assert(useCartStore.getState().getTotalAmount() === 150000, "Total with discount is 150,000 VND");

    // Test delivery mode
    useCartStore.getState().setDeliveryInfo({
      recipientName: "Trần Thị B",
      recipientPhone: "0901234567",
      deliveryAddress: "123 Lê Lợi, Q1",
    });
    assert(useCartStore.getState().orderType === "Delivery", "Order type switched to Delivery");
    assert(useCartStore.getState().deliveryFee === 20000, "Delivery fee is 20,000 VND");
    assert(useCartStore.getState().paymentMethod === "VIETQR", "Delivery enforces VietQR prepaid");
    // 170000 - 20000 (discount) + 20000 (ship) = 170000
    assert(useCartStore.getState().getTotalAmount() === 170000, "Total amount with delivery fee is 170,000 VND");

    // Test quantity reduction & removal
    const firstItemId = useCartStore.getState().items[0].cartItemId;
    useCartStore.getState().updateItemQuantity(firstItemId, -2); // 3 - 2 = 1
    assert(useCartStore.getState().items[0].quantity === 1, "Quantity reduced to 1");

    useCartStore.getState().updateItemQuantity(firstItemId, -1); // 1 - 1 = 0 -> removed
    assert(useCartStore.getState().items.length === 1, "Item removed when quantity reaches 0");

    useCartStore.getState().clearCart();
    assert(useCartStore.getState().items.length === 0, "Cart cleared successfully");
  }

  console.log("\n==========================================");
  console.log("TEST SUITE 3: usePosStore");
  console.log("==========================================");
  {
    usePosStore.getState().resetPos();
    assert(usePosStore.getState().cartItems.length === 0, "POS initial empty");

    // Test CRM Customer lookup & Free Cup redemption
    usePosStore.getState().setCustomer({
      customerId: "cust-01",
      phone: "0988776655",
      fullName: "Lê Hoàng Nam",
      cupBalance: 12,
      eligibleForFreeCup: true,
    });

    assert(usePosStore.getState().currentCustomer?.cupBalance === 12, "Customer attached");

    // Add 2 drinks to POS
    usePosStore.getState().addItem({
      cartItemId: "pos-item-1",
      productId: "prod-01",
      productName: "Cà phê Muối M",
      sizeId: "m",
      sizeName: "M",
      unitPrice: 35000,
      quantity: 1,
      sugarLevel: "100%",
      iceLevel: "100%",
      toppings: [],
      totalItemPrice: 35000,
    });

    usePosStore.getState().addItem({
      cartItemId: "pos-item-2",
      productId: "prod-02",
      productName: "Trà Đào Cam Sả L",
      sizeId: "l",
      sizeName: "L",
      unitPrice: 45000,
      quantity: 1,
      sugarLevel: "50%",
      iceLevel: "70%",
      toppings: [],
      totalItemPrice: 45000,
    });

    assert(usePosStore.getState().getGrossTotal() === 80000, "Gross total is 80,000 VND");

    // Redeem free cup: 100% discount on most expensive cup (45,000 VND)
    usePosStore.getState().redeemFreeCup();
    assert(usePosStore.getState().freeCupRedeemed === true, "Free cup redeemed");
    assert(usePosStore.getState().getDiscountTotal() === 45000, "Discount is 45,000 VND (highest item)");
    assert(usePosStore.getState().getNetTotal() === 35000, "Net total is 35,000 VND");

    // Cash tender & change calculation
    usePosStore.getState().setPaymentMethod("CASH");
    usePosStore.getState().setTenderAmount(100000);
    assert(usePosStore.getState().getChangeAmount() === 65000, "Change amount is 65,000 VND (100k - 35k)");

    // VietQR payment -> change should be 0
    usePosStore.getState().setPaymentMethod("VIETQR");
    assert(usePosStore.getState().getChangeAmount() === 0, "VietQR change amount is always 0");

    usePosStore.getState().resetPos();
    assert(usePosStore.getState().cartItems.length === 0, "POS reset successfully");
  }

  console.log("\n==========================================");
  console.log("TEST SUITE 4: useShiftStore");
  console.log("==========================================");
  {
    useShiftStore.getState().resetShift();
    assert(useShiftStore.getState().isClosed === true, "Initial shift is closed");

    // Open shift with 1,000,000 VND opening cash
    useShiftStore.getState().openShift("shift-001", "SHF-20260825-01", "br-01", 1000000);
    assert(useShiftStore.getState().isClosed === false, "Shift opened");
    assert(useShiftStore.getState().openingCash === 1000000, "Opening cash recorded");
    assert(useShiftStore.getState().theoreticalCash === 1000000, "Initial theoretical cash matches opening cash");

    // Record sales: Cash = 500,000 VND, VietQR = 1,200,000 VND
    useShiftStore.getState().setSalesAmounts(500000, 1200000);
    // Theoretical cash in drawer = 1,000,000 (opening) + 500,000 (cash sales) = 1,500,000 VND
    assert(useShiftStore.getState().theoreticalCash === 1500000, "Theoretical cash is 1,500,000 VND");

    // Count denominations in drawer:
    // 2 x 500,000 = 1,000,000
    // 2 x 200,000 = 400,000
    // 1 x 100,000 = 100,000
    // Total physical = 1,500,000 -> Variance = 0
    useShiftStore.getState().setDenominationCount(500000, 2);
    useShiftStore.getState().setDenominationCount(200000, 2);
    useShiftStore.getState().setDenominationCount(100000, 1);

    assert(useShiftStore.getState().physicalCashTotal === 1500000, "Physical total is 1,500,000 VND");
    assert(useShiftStore.getState().variance === 0, "Variance is 0 VND (exact match)");

    // Test shortage scenario: 1 x 500,000 less -> physical = 1,000,000 -> variance = -500,000
    useShiftStore.getState().setDenominationCount(500000, 1);
    assert(useShiftStore.getState().physicalCashTotal === 1000000, "Physical total updated to 1,000,000 VND");
    assert(useShiftStore.getState().variance === -500000, "Variance is -500,000 VND (shortage)");

    useShiftStore.getState().setJustificationReason("Đổi tiền lẻ cho khách chưa hoàn lại");
    assert(useShiftStore.getState().justificationReason === "Đổi tiền lẻ cho khách chưa hoàn lại", "Justification saved");

    useShiftStore.getState().closeShift();
    assert(useShiftStore.getState().isClosed === true, "Shift closed successfully");
  }

  console.log("\n==========================================");
  console.log("TEST SUITE 5: useKdsStore");
  console.log("==========================================");
  {
    useKdsStore.getState().setTickets([]);
    assert(useKdsStore.getState().tickets.length === 0, "KDS initial empty");

    const ticket1: KdsTicketDto = {
      orderId: "ord-01",
      orderNumber: "ORD-001",
      orderType: "DineIn",
      tableNumber: "T01",
      createdAtUtc: new Date().toISOString(),
      elapsedSeconds: 45,
      status: "Pending",
      paymentStatus: "Paid",
      paymentMethod: "VIETQR",
      station: "BAR",
      items: [
        {
          orderItemId: "item-01",
          productId: "prod-01",
          productName: "Cà Phê Muối",
          sizeName: "M",
          quantity: 2,
          sugarLevel: "50%",
          iceLevel: "70%",
          toppings: [],
        },
      ],
    };

    const ticket2: KdsTicketDto = {
      orderId: "ord-02",
      orderNumber: "ORD-002",
      orderType: "TakeAway",
      createdAtUtc: new Date().toISOString(),
      elapsedSeconds: 120,
      status: "Preparing",
      paymentStatus: "Paid",
      paymentMethod: "CASH",
      station: "BAR",
      items: [
        {
          orderItemId: "item-02",
          productId: "prod-01",
          productName: "Cà Phê Muối",
          sizeName: "M",
          quantity: 3,
          sugarLevel: "50%",
          iceLevel: "70%",
          toppings: [],
        },
      ],
    };

    useKdsStore.getState().addTicket(ticket1);
    useKdsStore.getState().addTicket(ticket2);
    assert(useKdsStore.getState().tickets.length === 2, "2 tickets added");

    // Test batch summary grouping
    const summaries = useKdsStore.getState().getBatchSummaries();
    assert(summaries.length === 1, "1 grouped item in batch summary");
    assert(summaries[0].productId === "prod-01", "Grouped by product");
    assert(summaries[0].totalQuantity === 5, "Total batch quantity is 5 (2 + 3)");
    assert(summaries[0].orderCount === 2, "Aggregated from 2 distinct orders");

    // Test status transition
    useKdsStore.getState().updateTicketStatus("ord-01", "Ready");
    assert(useKdsStore.getState().tickets.find((t) => t.orderId === "ord-01")?.status === "Ready", "Ticket 1 transitioned to Ready");

    // Timer increment
    const initialElapsed = useKdsStore.getState().tickets[0].elapsedSeconds;
    useKdsStore.getState().incrementTimers();
    assert(useKdsStore.getState().tickets[0].elapsedSeconds === initialElapsed + 1, "Timers incremented by 1s");
  }

  console.log("\n==========================================");
  console.log("TEST SUITE 6: useTableStore");
  console.log("==========================================");
  {
    const mockTables: TableDto[] = [
      { id: "t-101", tableNumber: "T101", branchId: "br-01", floor: 1, capacity: 4, status: "Available" },
      { id: "t-102", tableNumber: "T102", branchId: "br-01", floor: 1, capacity: 2, status: "ServiceRequested" },
      { id: "t-201", tableNumber: "T201", branchId: "br-01", floor: 2, capacity: 6, status: "Occupied_Paid", activeOrderId: "ord-99" },
    ];

    useTableStore.getState().setTables(mockTables);
    assert(useTableStore.getState().tables.length === 3, "Tables initialized");
    assert(useTableStore.getState().floors.length === 2, "2 distinct floors detected (1, 2)");
    assert(useTableStore.getState().getServiceAlertsCount() === 1, "1 active service alert detected");

    // Test floor filtering
    useTableStore.getState().setSelectedFloor(2);
    const floor2Tables = useTableStore.getState().getTablesForSelectedFloor();
    assert(floor2Tables.length === 1 && floor2Tables[0].id === "t-201", "Floor 2 tables correctly filtered");

    // Resolve service call
    useTableStore.getState().resolveServiceCall("t-102");
    assert(useTableStore.getState().getServiceAlertsCount() === 0, "Service call resolved to 0 alerts");
  }

  console.log("\n==========================================");
  console.log(`SUMMARY: ${passed} PASSED, ${failed} FAILED`);
  console.log("==========================================");

  if (failed > 0) {
    process.exit(1);
  }
}

runStoreTests().catch((err) => {
  console.error("FATAL ERROR in store test runner:", err);
  process.exit(1);
});
