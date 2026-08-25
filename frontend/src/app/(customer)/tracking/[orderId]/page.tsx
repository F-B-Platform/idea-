"use client";

import React, { useState, useEffect } from "react";
import { useParams, useRouter } from "next/navigation";
import { OrderDto, OrderStatus } from "@/types";
import { formatCurrencyVND, formatDateTime } from "@/lib/utils";
import { LiveStepper } from "@/components/order/LiveStepper";
import { Button } from "@/components/ui/Button";
import { Modal } from "@/components/ui/Modal";
import { ReceiptPrint } from "@/components/pos/ReceiptPrint";
import {
  Bell,
  CheckCircle2,
  FileText,
  Star,
  Coffee,
  MapPin,
  Clock,
  ArrowLeft,
} from "lucide-react";
import { useSignalR } from "@/hooks/useSignalR";

export default function OrderTrackingPage() {
  const params = useParams();
  const router = useRouter();
  const orderId = (params?.orderId as string) || "ORD-0042";

  const [orderStatus, setOrderStatus] = useState<OrderStatus>("Preparing");
  const [bellCooldownSeconds, setBellCooldownSeconds] = useState(0);
  const [bellAlertSuccess, setBellAlertSuccess] = useState(false);
  const [showReceiptModal, setShowReceiptModal] = useState(false);

  // Mock Order Data for full UI rendering
  const [orderData, setOrderData] = useState<OrderDto>({
    id: orderId,
    orderCode: orderId,
    orderNumber: orderId,
    branchId: "branch-q1",
    branchName: "Smart F&B Coffee & Tea (Chi nhánh Q1)",
    tableId: "05",
    tableNumber: "05",
    orderType: "DineIn",
    status: orderStatus,
    subTotal: 74000,
    discountAmount: 0,
    deliveryFee: 0,
    totalAmount: 74000,
    paymentMethod: "VIETQR",
    paymentStatus: "Paid",
    createdAt: new Date().toISOString(),
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
        selectedModifiers: [{ modifierId: "mod-02", name: "Kem Muối Béo", price: 8000 }],
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
  });

  // SignalR OrderHub subscription
  const { registerHandler } = useSignalR({
    hubPath: "/hubs/orders",
    groupName: orderId,
    joinGroupMethod: "JoinOrderGroup",
  });

  useEffect(() => {
    registerHandler("OrderStatusUpdated", (payload: { orderId: string; status: OrderStatus }) => {
      if (payload.orderId === orderId) {
        setOrderStatus(payload.status);
        setOrderData((prev) => ({ ...prev, status: payload.status }));
      }
    });
  }, [registerHandler, orderId]);

  // 60s Debounce Timer for Service Bell
  useEffect(() => {
    if (bellCooldownSeconds <= 0) return;
    const timer = setInterval(() => {
      setBellCooldownSeconds((prev) => prev - 1);
    }, 1000);
    return () => clearInterval(timer);
  }, [bellCooldownSeconds]);

  const handleCallService = () => {
    if (bellCooldownSeconds > 0) return;
    setBellCooldownSeconds(60);
    setBellAlertSuccess(true);
    setTimeout(() => setBellAlertSuccess(null as any), 4000);
  };

  return (
    <div className="space-y-6 px-4 pt-4 pb-12">
      {/* Header */}
      <div className="flex items-center justify-between">
        <button
          type="button"
          onClick={() => router.push("/menu")}
          className="flex items-center gap-1.5 text-xs font-bold text-slate-600 hover:text-slate-900"
        >
          <ArrowLeft className="h-4 w-4" />
          <span>Về Thực Đơn</span>
        </button>
        <span className="text-xs font-bold text-amber-800 bg-amber-100 px-3 py-1 rounded-full">
          Bàn #{orderData.tableNumber}
        </span>
      </div>

      <div className="space-y-1">
        <div className="flex items-center gap-2">
          <span className="font-mono text-xs font-bold text-slate-500">MÃ ĐƠN:</span>
          <h2 className="text-xl font-black text-slate-950">#{orderId}</h2>
        </div>
        <p className="text-xs text-slate-500">
          Cập nhật tiến độ pha chế và phục vụ thời gian thực qua SignalR WebSocket.
        </p>
      </div>

      {/* Live Stepper Tracker */}
      <LiveStepper
        status={orderStatus}
        orderType={orderData.orderType}
        estimatedMinutes={4}
        queuePosition={2}
      />

      {/* Service Bell Calling Card */}
      <div className="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm space-y-3">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Bell className="h-5 w-5 text-amber-700" />
            <h3 className="font-bold text-xs uppercase tracking-wider text-slate-900">
              Cần Hỗ Trợ Tại Bàn?
            </h3>
          </div>
          {bellCooldownSeconds > 0 && (
            <span className="text-xs font-mono font-bold text-amber-800 bg-amber-50 px-2 py-0.5 rounded">
              Chờ {bellCooldownSeconds}s
            </span>
          )}
        </div>

        {bellAlertSuccess && (
          <div className="bg-emerald-50 border border-emerald-300 text-emerald-900 text-xs p-3 rounded-xl flex items-center gap-2 animate-in fade-in">
            <CheckCircle2 className="h-4 w-4 text-emerald-600 shrink-0" />
            <span>Đã gửi chuông gọi phục vụ tới nhân viên quầy thành công!</span>
          </div>
        )}

        <Button
          type="button"
          onClick={handleCallService}
          disabled={bellCooldownSeconds > 0}
          variant="outline"
          size="lg"
          className="w-full font-bold border-2 border-amber-700 text-amber-900 hover:bg-amber-50"
          leftIcon={<Bell className="h-5 w-5" />}
        >
          {bellCooldownSeconds > 0
            ? `Vui lòng đợi ${bellCooldownSeconds}s để bấm lại`
            : "🔔 BẤM CHUÔNG GỌI PHỤC VỤ (BÀN #" + orderData.tableNumber + ")"}
        </Button>
      </div>

      {/* Order Item Details Card */}
      <div className="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm space-y-4">
        <div className="flex items-center justify-between border-b border-slate-100 pb-3">
          <h3 className="font-bold text-xs uppercase tracking-wider text-slate-800">
            Chi Tiết Món Trong Đơn
          </h3>
          <span className="text-xs font-bold text-emerald-700 bg-emerald-50 px-2.5 py-0.5 rounded-full border border-emerald-200">
            Đã Thanh Toán
          </span>
        </div>

        <div className="space-y-3 divide-y divide-slate-100">
          {orderData.items.map((item, idx) => (
            <div key={idx} className="pt-2 first:pt-0 flex items-start justify-between text-xs">
              <div>
                <span className="font-bold text-slate-900">
                  {item.quantity}x {item.productName}
                </span>
                <span className="text-slate-500 ml-1 font-semibold">({item.size})</span>
                {(item.sugarLevel || item.iceLevel) && (
                  <p className="text-[11px] text-slate-500">
                    Đường: {item.sugarLevel} • Đá: {item.iceLevel}
                  </p>
                )}
                {item.selectedModifiers && item.selectedModifiers.length > 0 && (
                  <p className="text-[11px] text-amber-800">
                    + {item.selectedModifiers.map((m) => m.name).join(", ")}
                  </p>
                )}
              </div>
              <span className="font-bold text-slate-800">
                {formatCurrencyVND(item.totalPrice)}
              </span>
            </div>
          ))}
        </div>

        <div className="pt-3 border-t border-slate-200 flex justify-between font-black text-sm text-slate-900">
          <span>Tổng thanh toán:</span>
          <span className="text-amber-900">{formatCurrencyVND(orderData.totalAmount)}</span>
        </div>
      </div>

      {/* E-Receipt & Review Navigation Buttons */}
      <div className="grid grid-cols-2 gap-3">
        <Button
          type="button"
          onClick={() => setShowReceiptModal(true)}
          variant="secondary"
          className="font-bold text-xs"
          leftIcon={<FileText className="h-4 w-4" />}
        >
          Xem Hóa Đơn Điện Tử
        </Button>

        <Button
          type="button"
          onClick={() => router.push(`/review/${orderId}`)}
          variant="amber"
          className="font-bold text-xs"
          leftIcon={<Star className="h-4 w-4" />}
        >
          Đánh Giá Trải Nghiệm
        </Button>
      </div>

      {/* E-Receipt Modal */}
      <Modal
        isOpen={showReceiptModal}
        onClose={() => setShowReceiptModal(false)}
        maxWidth="md"
        title="Hóa Đơn Điện Tử"
        footer={
          <Button variant="secondary" onClick={() => setShowReceiptModal(false)}>
            Đóng
          </Button>
        }
      >
        <ReceiptPrint order={orderData} />
      </Modal>
    </div>
  );
}
