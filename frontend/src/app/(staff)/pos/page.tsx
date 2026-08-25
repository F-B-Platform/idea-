"use client";

import React, { useState } from "react";
import { usePosStore } from "@/stores/usePosStore";
import { ProductDto, OrderDto } from "@/types";
import { formatCurrencyVND } from "@/lib/utils";
import { CrmLookupBar } from "@/components/pos/CrmLookupBar";
import { LoyaltyProgress } from "@/components/pos/LoyaltyProgress";
import { CashTenderCalculator } from "@/components/pos/CashTenderCalculator";
import { ReceiptPrint } from "@/components/pos/ReceiptPrint";
import { CustomizationDrawer } from "@/components/order/CustomizationDrawer";
import { Button } from "@/components/ui/Button";
import { Modal } from "@/components/ui/Modal";
import {
  Coffee,
  ShoppingBag,
  Printer,
  Trash2,
  Plus,
  Minus,
  Banknote,
  QrCode,
  CheckCircle2,
} from "lucide-react";

const posProducts: ProductDto[] = [
  {
    id: "prod-01",
    sku: "CF-SALT-01",
    name: "Cà Phê Muối Hoàng Gia",
    basePrice: 35000,
    imageUrl: "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=400&q=80",
    categoryId: "cat-01",
    categoryName: "Cà Phê Đặc Sản",
    isAvailable: true,
    sizes: [
      { id: "s-01", sizeName: "S", price: 32000, isDefault: false },
      { id: "s-02", sizeName: "M", price: 35000, isDefault: true },
      { id: "s-03", sizeName: "L", price: 42000, isDefault: false },
    ],
    modifiers: [
      { id: "mod-01", name: "Thêm Shot Espresso", priceAdjustment: 10000, isDefault: false },
      { id: "mod-02", name: "Thêm Kem Muối Béo", priceAdjustment: 8000, isDefault: false },
    ],
  },
  {
    id: "prod-02",
    sku: "TEA-PEACH-02",
    name: "Trà Đào Cam Sả Tươi",
    basePrice: 39000,
    imageUrl: "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=400&q=80",
    categoryId: "cat-02",
    categoryName: "Trà Trái Cây",
    isAvailable: true,
    sizes: [
      { id: "s-04", sizeName: "M", price: 39000, isDefault: true },
      { id: "s-05", sizeName: "L", price: 45000, isDefault: false },
    ],
    modifiers: [
      { id: "mod-03", name: "Thêm Đào Miếng Giòn", priceAdjustment: 10000, isDefault: false },
    ],
  },
  {
    id: "prod-03",
    sku: "MILKTEA-OOLONG-03",
    name: "Trà Sữa Oolong Nướng",
    basePrice: 42000,
    imageUrl: "https://images.unsplash.com/photo-1558857563-b37cf05d8a58?w=400&q=80",
    categoryId: "cat-03",
    categoryName: "Trà Sữa Oolong",
    isAvailable: true,
    sizes: [
      { id: "s-06", sizeName: "M", price: 42000, isDefault: true },
      { id: "s-07", sizeName: "L", price: 49000, isDefault: false },
    ],
    modifiers: [
      { id: "mod-05", name: "Trân Châu Hoàng Kim", priceAdjustment: 8000, isDefault: false },
    ],
  },
  {
    id: "prod-04",
    sku: "CF-BACXIU-04",
    name: "Bạc Xỉu Sữa Hạnh Nhân",
    basePrice: 38000,
    imageUrl: "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=400&q=80",
    categoryId: "cat-01",
    categoryName: "Cà Phê Đặc Sản",
    isAvailable: true,
    sizes: [
      { id: "s-08", sizeName: "M", price: 38000, isDefault: true },
      { id: "s-09", sizeName: "L", price: 45000, isDefault: false },
    ],
    modifiers: [],
  },
];

export default function TakeawayPosPage() {
  const {
    currentCustomer,
    setCustomer,
    cartItems,
    addItem,
    updateQuantity,
    removeItem,
    freeCupRedeemed,
    redeemFreeCup,
    cancelFreeCup,
    tenderAmount,
    setTenderAmount,
    paymentMethod,
    setPaymentMethod,
    resetPos,
    getGrossTotal,
    getDiscountTotal,
    getNetTotal,
    getChangeAmount,
  } = usePosStore();

  const [selectedProduct, setSelectedProduct] = useState<ProductDto | null>(null);
  const [completedOrder, setCompletedOrder] = useState<OrderDto | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);

  const grossTotal = getGrossTotal();
  const discountTotal = getDiscountTotal();
  const netTotal = getNetTotal();
  const changeAmount = getChangeAmount();

  const handleQuickAdd = (product: ProductDto) => {
    setSelectedProduct(product);
  };

  const handleProcessOrder = () => {
    if (cartItems.length === 0) return;
    if (paymentMethod === "CASH" && tenderAmount < netTotal) {
      alert("Số tiền khách đưa chưa đủ để thanh toán!");
      return;
    }

    setIsSubmitting(true);
    const orderId = `TK-${Math.floor(1000 + Math.random() * 9000)}`;

    const orderDto: OrderDto = {
      id: orderId,
      orderCode: orderId,
      orderNumber: orderId,
      branchId: "branch-q1",
      branchName: "Smart F&B Chi nhánh Quận 1",
      orderType: "TakeAway",
      status: "Paid",
      subTotal: grossTotal,
      discountAmount: discountTotal,
      deliveryFee: 0,
      totalAmount: netTotal,
      customerPhone: currentCustomer?.phone,
      customerName: currentCustomer?.fullName,
      paymentMethod,
      paymentStatus: "Paid",
      createdAt: new Date().toISOString(),
      items: cartItems.map((ci) => ({
        productId: ci.productId,
        productName: ci.productName,
        size: ci.sizeName as any,
        quantity: ci.quantity,
        unitPrice: ci.unitPrice,
        totalPrice: ci.totalItemPrice,
        sugarLevel: ci.sugarLevel,
        iceLevel: ci.iceLevel,
        selectedModifiers: ci.toppings,
        notes: ci.notes,
      })),
    };

    setTimeout(() => {
      setIsSubmitting(false);
      setCompletedOrder(orderDto);
      resetPos();
    }, 600);
  };

  return (
    <div className="max-w-7xl mx-auto space-y-6">
      {/* Top Title Bar */}
      <div className="flex items-center justify-between bg-white p-5 rounded-3xl border border-slate-200 shadow-sm">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-2xl bg-amber-700 text-white flex items-center justify-center font-black shadow-sm">
            <Coffee className="h-5 w-5" />
          </div>
          <div>
            <h1 className="text-lg font-black text-slate-900 leading-tight">
              Web POS Quầy Bán Mang Về (Takeaway)
            </h1>
            <span className="text-xs text-slate-500">
              Tra cứu khách hàng, áp dụng tích lũy 10 ly đổi 1 ly & in bill nhiệt
            </span>
          </div>
        </div>

        <div className="flex items-center gap-2">
          <Button type="button" variant="secondary" size="sm" onClick={resetPos}>
            Làm Mới Quầy
          </Button>
        </div>
      </div>

      {/* 2-Column POS Layout */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Left Column: CRM Lookup & Menu Grid (7 Cols) */}
        <div className="lg:col-span-7 space-y-5">
          {/* CRM Lookup Card */}
          <CrmLookupBar
            currentCustomer={currentCustomer}
            onCustomerFound={setCustomer}
            onClearCustomer={() => setCustomer(null)}
          />

          {/* 10-Cup Loyalty Progress */}
          {currentCustomer && (
            <LoyaltyProgress
              cupBalance={currentCustomer.cupBalance}
              freeCupRedeemed={freeCupRedeemed}
              onRedeem={redeemFreeCup}
              onCancelRedeem={cancelFreeCup}
            />
          )}

          {/* Products Grid */}
          <div className="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm space-y-4">
            <div className="flex items-center justify-between border-b border-slate-100 pb-3">
              <h3 className="font-bold text-xs uppercase tracking-wider text-slate-700">
                Thực Đơn Đồ Uống Chạm Nhanh
              </h3>
              <span className="text-xs text-slate-400 font-medium">
                Chạm vào món để chọn size & đường đá
              </span>
            </div>

            <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
              {posProducts.map((product) => (
                <div
                  key={product.id}
                  onClick={() => handleQuickAdd(product)}
                  className="p-3 rounded-2xl border border-slate-200 hover:border-amber-600 bg-white hover:bg-amber-50/30 transition-all cursor-pointer flex flex-col justify-between space-y-2 shadow-2xs group"
                >
                  <div className="relative h-24 rounded-xl overflow-hidden bg-slate-100">
                    <img
                      src={product.imageUrl}
                      alt={product.name}
                      className="w-full h-full object-cover group-hover:scale-105 transition-transform"
                    />
                  </div>
                  <div>
                    <h4 className="font-bold text-xs text-slate-900 line-clamp-1">
                      {product.name}
                    </h4>
                    <span className="font-extrabold text-xs text-amber-800 mt-0.5 block">
                      {formatCurrencyVND(product.basePrice)}
                    </span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Right Column: Active Cart & Tender Calculator (5 Cols) */}
        <div className="lg:col-span-5 space-y-5">
          {/* Active Cart Box */}
          <div className="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm space-y-4">
            <div className="flex items-center justify-between border-b border-slate-100 pb-3">
              <div className="flex items-center gap-2">
                <ShoppingBag className="h-4 w-4 text-amber-700" />
                <h3 className="font-bold text-xs uppercase tracking-wider text-slate-900">
                  Đơn Hàng Hiện Tại ({cartItems.length} món)
                </h3>
              </div>
              {currentCustomer && (
                <span className="text-[11px] font-bold text-amber-900 bg-amber-100 px-2 py-0.5 rounded">
                  {currentCustomer.phone}
                </span>
              )}
            </div>

            {/* Cart Items List */}
            {cartItems.length === 0 ? (
              <div className="py-10 text-center text-slate-400 space-y-1">
                <p className="text-xs">Chưa có món nào trong giỏ hàng</p>
                <span className="text-[11px] text-slate-300">Chạm vào danh sách món bên trái</span>
              </div>
            ) : (
              <div className="space-y-2 max-h-56 overflow-y-auto pr-1 divide-y divide-slate-100">
                {cartItems.map((item) => (
                  <div key={item.cartItemId} className="pt-2 first:pt-0 flex items-start justify-between gap-2">
                    <div className="space-y-0.5">
                      <span className="font-bold text-xs text-slate-900 block">
                        {item.productName} ({item.sizeName})
                      </span>
                      <span className="text-[11px] text-slate-400">
                        Đ: {item.sugarLevel} • Đá: {item.iceLevel}
                      </span>
                    </div>

                    <div className="flex items-center gap-2">
                      <div className="flex items-center gap-1 bg-slate-100 p-0.5 rounded-lg">
                        <button
                          type="button"
                          onClick={() => updateQuantity(item.cartItemId, item.quantity - 1)}
                          className="w-5 h-5 bg-white rounded flex items-center justify-center text-slate-600 shadow-2xs"
                        >
                          <Minus className="h-2.5 w-2.5" />
                        </button>
                        <span className="font-bold text-xs w-4 text-center">{item.quantity}</span>
                        <button
                          type="button"
                          onClick={() => updateQuantity(item.cartItemId, item.quantity + 1)}
                          className="w-5 h-5 bg-white rounded flex items-center justify-center text-slate-600 shadow-2xs"
                        >
                          <Plus className="h-2.5 w-2.5" />
                        </button>
                      </div>

                      <span className="font-bold text-xs text-slate-800 w-16 text-right">
                        {formatCurrencyVND(item.totalItemPrice)}
                      </span>

                      <button
                        type="button"
                        onClick={() => removeItem(item.cartItemId)}
                        className="text-slate-300 hover:text-rose-600 p-1"
                      >
                        <Trash2 className="h-3 w-3" />
                      </button>
                    </div>
                  </div>
                ))}
              </div>
            )}

            {/* Payment Method Selector */}
            <div className="grid grid-cols-2 gap-2 pt-2 border-t border-slate-100">
              <button
                type="button"
                onClick={() => setPaymentMethod("CASH")}
                className={`py-2.5 rounded-xl border-2 text-xs font-bold flex items-center justify-center gap-2 transition-all ${
                  paymentMethod === "CASH"
                    ? "border-amber-700 bg-amber-50 text-amber-950 shadow-xs"
                    : "border-slate-200 text-slate-600 hover:bg-slate-50"
                }`}
              >
                <Banknote className="h-4 w-4" />
                <span>Tiền Mặt</span>
              </button>

              <button
                type="button"
                onClick={() => setPaymentMethod("VIETQR")}
                className={`py-2.5 rounded-xl border-2 text-xs font-bold flex items-center justify-center gap-2 transition-all ${
                  paymentMethod === "VIETQR"
                    ? "border-amber-700 bg-amber-50 text-amber-950 shadow-xs"
                    : "border-slate-200 text-slate-600 hover:bg-slate-50"
                }`}
              >
                <QrCode className="h-4 w-4" />
                <span>VietQR Động</span>
              </button>
            </div>

            {/* Totals Breakdown */}
            <div className="space-y-1.5 text-xs bg-slate-50 p-3.5 rounded-2xl border border-slate-200">
              <div className="flex justify-between text-slate-600">
                <span>Tổng tiền hàng:</span>
                <span className="font-semibold">{formatCurrencyVND(grossTotal)}</span>
              </div>
              {discountTotal > 0 && (
                <div className="flex justify-between text-emerald-700 font-bold">
                  <span>Ưu đãi 10 ly tặng 1:</span>
                  <span>-{formatCurrencyVND(discountTotal)}</span>
                </div>
              )}
              <div className="flex justify-between font-black text-sm pt-1 border-t border-slate-200 text-slate-900">
                <span>CẦN THU:</span>
                <span className="text-amber-900">{formatCurrencyVND(netTotal)}</span>
              </div>
            </div>

            {/* Cash Tender Calculator (Only for Cash payments) */}
            {paymentMethod === "CASH" && (
              <CashTenderCalculator
                netTotal={netTotal}
                tenderAmount={tenderAmount}
                onTenderChange={setTenderAmount}
              />
            )}

            {/* Submit & Print CTA */}
            <Button
              type="button"
              onClick={handleProcessOrder}
              disabled={cartItems.length === 0 || isSubmitting}
              isLoading={isSubmitting}
              size="lg"
              variant="primary"
              className="w-full font-bold shadow-md text-sm"
              leftIcon={<Printer className="h-4 w-4" />}
            >
              IN BILL & GỬI BẾP ({formatCurrencyVND(netTotal)})
            </Button>
          </div>
        </div>
      </div>

      {/* Completed Order Thermal Receipt Modal */}
      <Modal
        isOpen={!!completedOrder}
        onClose={() => setCompletedOrder(null)}
        maxWidth="md"
        title="In Hóa Đơn & Đơn Hàng Đã Gửi Bếp"
        footer={
          <Button variant="primary" onClick={() => setCompletedOrder(null)}>
            Hoàn Tất Đơn Mới
          </Button>
        }
      >
        {completedOrder && <ReceiptPrint order={completedOrder} />}
      </Modal>

      {/* Customization Drawer for Selected Product */}
      <CustomizationDrawer
        isOpen={!!selectedProduct}
        onClose={() => setSelectedProduct(null)}
        product={selectedProduct}
        onAddToCart={(item) => {
          addItem({
            ...item,
            cartItemId: `${item.productId}-${item.sizeId}-${item.sugarLevel}-${item.iceLevel}`,
            totalItemPrice: (item.unitPrice + item.toppings.reduce((s, t) => s + t.price, 0)) * item.quantity,
          });
        }}
      />
    </div>
  );
}
