"use client";

import React, { useState } from "react";
import { useRouter } from "next/navigation";
import { OrderDto } from "@/types";
import { formatCurrencyVND, formatDateTime, validateVietnamesePhone } from "@/lib/utils";
import { useCartStore } from "@/stores/useCartStore";
import { SearchInput } from "@/components/ui/SearchInput";
import { Button } from "@/components/ui/Button";
import { StatusBadge } from "@/components/layout/StatusBadge";
import { History, ArrowLeft, RotateCcw, Clock, Coffee, Search } from "lucide-react";

export default function OrderHistoryPage() {
  const router = useRouter();
  const addItem = useCartStore((state) => state.addItem);

  const [phone, setPhone] = useState("0908123456");
  const [isSearching, setIsSearching] = useState(false);
  const [orders, setOrders] = useState<OrderDto[]>([
    {
      id: "ORD-9921",
      orderCode: "ORD-9921",
      orderNumber: "ORD-9921",
      branchId: "branch-q1",
      branchName: "Smart F&B Chi nhánh Quận 1",
      tableNumber: "03",
      orderType: "DineIn",
      status: "Completed",
      subTotal: 74000,
      discountAmount: 0,
      deliveryFee: 0,
      totalAmount: 74000,
      paymentMethod: "VIETQR",
      paymentStatus: "Paid",
      createdAt: "2026-08-24T14:30:00Z",
      items: [
        {
          productId: "prod-01",
          productName: "Cà Phê Muối Hoàng Gia",
          size: "M",
          quantity: 1,
          unitPrice: 35000,
          totalPrice: 35000,
          sugarLevel: "50%",
          iceLevel: "100%",
        },
        {
          productId: "prod-02",
          productName: "Trà Đào Cam Sả Tươi",
          size: "M",
          quantity: 1,
          unitPrice: 39000,
          totalPrice: 39000,
          sugarLevel: "70%",
          iceLevel: "100%",
        },
      ],
    },
  ]);

  const handleReorder = (order: OrderDto) => {
    order.items.forEach((item) => {
      addItem({
        productId: item.productId,
        productName: item.productName,
        sizeId: item.sizeId || "default-size",
        sizeName: item.size || "M",
        unitPrice: item.unitPrice,
        quantity: item.quantity,
        sugarLevel: item.sugarLevel || "100%",
        iceLevel: item.iceLevel || "100%",
        toppings: [],
      });
    });

    router.push("/cart");
  };

  const handleSearch = () => {
    setIsSearching(true);
    setTimeout(() => {
      setIsSearching(false);
    }, 400);
  };

  return (
    <div className="space-y-6 px-4 pt-4 pb-12">
      {/* Top Header */}
      <div className="flex items-center justify-between">
        <button
          type="button"
          onClick={() => router.back()}
          className="flex items-center gap-1.5 text-xs font-bold text-slate-600 hover:text-slate-900"
        >
          <ArrowLeft className="h-4 w-4" />
          <span>Quay lại</span>
        </button>
        <span className="text-xs font-bold text-amber-800 bg-amber-100 px-3 py-1 rounded-full">
          Lịch Sử Đơn Hàng
        </span>
      </div>

      <div className="space-y-1">
        <h2 className="text-xl font-black text-slate-950">Đơn Hàng Đã Đặt</h2>
        <p className="text-xs text-slate-500">
          Tra cứu lại các món đồ uống yêu thích theo số điện thoại và đặt lại chỉ bằng 1 thao tác chạm.
        </p>
      </div>

      {/* Phone lookup bar */}
      <div className="flex gap-2">
        <input
          type="tel"
          value={phone}
          onChange={(e) => setPhone(e.target.value)}
          placeholder="Nhập số điện thoại đã đặt..."
          className="flex-1 px-3.5 py-2.5 rounded-xl border border-slate-300 text-sm font-semibold focus:outline-none focus:ring-2 focus:ring-amber-600"
        />
        <Button size="md" variant="primary" onClick={handleSearch} isLoading={isSearching}>
          <Search className="h-4 w-4" />
        </Button>
      </div>

      {/* Orders List */}
      <div className="space-y-4">
        {orders.map((order) => (
          <div
            key={order.id}
            className="p-5 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-3"
          >
            <div className="flex items-start justify-between">
              <div>
                <div className="flex items-center gap-2">
                  <span className="font-extrabold text-base text-slate-900">
                    #{order.orderCode}
                  </span>
                  <StatusBadge status={order.status} />
                </div>
                <div className="flex items-center gap-1.5 text-xs text-slate-400 mt-1">
                  <Clock className="h-3.5 w-3.5" />
                  <span>{formatDateTime(order.createdAt)}</span>
                </div>
              </div>

              <span className="font-extrabold text-base text-amber-900">
                {formatCurrencyVND(order.totalAmount)}
              </span>
            </div>

            {/* Items */}
            <div className="space-y-1.5 border-t border-slate-100 pt-2 text-xs text-slate-700">
              {order.items.map((item, idx) => (
                <div key={idx} className="flex justify-between">
                  <span>
                    {item.quantity}x {item.productName} ({item.size})
                  </span>
                  <span className="font-semibold">{formatCurrencyVND(item.totalPrice)}</span>
                </div>
              ))}
            </div>

            {/* Reorder CTA Button */}
            <div className="pt-2 border-t border-slate-100 flex justify-end">
              <Button
                type="button"
                onClick={() => handleReorder(order)}
                size="sm"
                variant="amber"
                leftIcon={<RotateCcw className="h-3.5 w-3.5" />}
              >
                Đặt Lại 1-Chạm
              </Button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
