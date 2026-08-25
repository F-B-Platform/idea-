"use client";

import React, { useRef } from "react";
import { OrderDto, OrderDetailDto } from "@/types";
import { formatCurrencyVND, formatDateTime } from "@/lib/utils";
import { Printer, QrCode } from "lucide-react";
import { Button } from "@/components/ui/Button";

export interface ReceiptPrintProps {
  order: OrderDto | OrderDetailDto;
  onPrintComplete?: () => void;
}

export const ReceiptPrint: React.FC<ReceiptPrintProps> = ({
  order,
  onPrintComplete,
}) => {
  const receiptRef = useRef<HTMLDivElement>(null);

  const handlePrint = () => {
    window.print();
    if (onPrintComplete) onPrintComplete();
  };

  return (
    <div className="space-y-4">
      {/* Visual thermal paper mockup */}
      <div
        ref={receiptRef}
        className="w-[320px] mx-auto bg-white p-6 rounded-lg border border-slate-300 shadow-xl font-mono text-xs text-slate-900 space-y-4 print:w-full print:shadow-none print:border-none print:m-0"
      >
        {/* Header */}
        <div className="text-center space-y-1 border-b border-dashed border-slate-300 pb-3">
          <h2 className="font-extrabold text-sm uppercase">
            {order.branchName || "SMART F&B COFFEE & TEA"}
          </h2>
          <p className="text-[10px] text-slate-500">123 Đường Nguyễn Huệ, Quận 1, TP.HCM</p>
          <p className="text-[10px] text-slate-500">Hotline: 1900 6868 • Wifi: SmartFB@2026</p>
          <h3 className="font-bold text-xs pt-1 uppercase tracking-wider">HÓA ĐƠN BÁN HÀNG</h3>
        </div>

        {/* Order Meta */}
        <div className="space-y-1 text-[11px] border-b border-dashed border-slate-300 pb-2">
          <div className="flex justify-between">
            <span>Mã HĐ:</span>
            <strong className="text-slate-900">#{order.orderCode || order.orderNumber}</strong>
          </div>
          <div className="flex justify-between">
            <span>Thời gian:</span>
            <span>{formatDateTime(order.createdAt || order.createdAtUtc)}</span>
          </div>
          {order.tableNumber && (
            <div className="flex justify-between">
              <span>Vị trí:</span>
              <strong className="text-slate-900">BÀN #{order.tableNumber}</strong>
            </div>
          )}
          <div className="flex justify-between">
            <span>Loại đơn:</span>
            <span>
              {order.orderType === "DineIn"
                ? "Tại Bàn"
                : order.orderType === "TakeAway"
                ? "Mang Về"
                : "Giao Hàng"}
            </span>
          </div>
        </div>

        {/* Items List */}
        <div className="space-y-2 border-b border-dashed border-slate-300 pb-3">
          <div className="flex justify-between font-bold text-[10px] uppercase text-slate-500">
            <span>Món</span>
            <span>SL</span>
            <span>Thành tiền</span>
          </div>

          <div className="space-y-1.5 divide-y divide-slate-100">
            {order.items.map((item, idx) => (
              <div key={idx} className="pt-1 first:pt-0">
                <div className="flex justify-between font-semibold">
                  <span className="truncate pr-2">
                    {item.productName} ({item.size || item.sizeName || "M"})
                  </span>
                  <span>{item.quantity}</span>
                  <span className="text-right shrink-0">
                    {formatCurrencyVND(item.totalPrice).replace(" ₫", "")}
                  </span>
                </div>
                {(item.sugarLevel || item.iceLevel) && (
                  <p className="text-[10px] text-slate-400">
                    {">"} Đ: {item.sugarLevel || "100%"} • Đá: {item.iceLevel || "100%"}
                  </p>
                )}
              </div>
            ))}
          </div>
        </div>

        {/* Financial Breakdown */}
        <div className="space-y-1.5 text-[11px] border-b border-dashed border-slate-300 pb-3">
          <div className="flex justify-between">
            <span>Tạm tính:</span>
            <span>{formatCurrencyVND(order.subTotal || order.subtotalAmount || 0)}</span>
          </div>
          {order.discountAmount > 0 && (
            <div className="flex justify-between text-rose-600 font-medium">
              <span>Chiết khấu (10 Ly/Voucher):</span>
              <span>-{formatCurrencyVND(order.discountAmount)}</span>
            </div>
          )}
          {order.deliveryFee > 0 && (
            <div className="flex justify-between">
              <span>Phí giao hàng:</span>
              <span>{formatCurrencyVND(order.deliveryFee)}</span>
            </div>
          )}
          <div className="flex justify-between font-black text-sm pt-1 border-t border-slate-200">
            <span>TỔNG CỘNG:</span>
            <span className="text-amber-900">{formatCurrencyVND(order.totalAmount)}</span>
          </div>
          <div className="flex justify-between text-[10px] text-slate-500">
            <span>Hình thức:</span>
            <span>{order.paymentMethod === "VIETQR" ? "VietQR Chuyển Khoản" : "Tiền Mặt"}</span>
          </div>
        </div>

        {/* Dynamic VietQR for Postpaid / Receipt verification */}
        {order.paymentMethod === "VIETQR" && (
          <div className="text-center space-y-2 py-1">
            <div className="w-28 h-28 mx-auto bg-slate-100 border border-slate-300 rounded-lg flex items-center justify-center p-2">
              {order.qrCodeUrl ? (
                <img src={order.qrCodeUrl} alt="VietQR" className="w-full h-full object-contain" />
              ) : (
                <div className="text-center">
                  <QrCode className="h-16 w-16 mx-auto text-slate-800" />
                  <span className="text-[9px] text-slate-500 block">Quét VietQR</span>
                </div>
              )}
            </div>
            <p className="text-[9px] text-slate-500">Quét mã VietQR để thanh toán / đối soát</p>
          </div>
        )}

        {/* Footer Note */}
        <div className="text-center text-[10px] text-slate-500 space-y-1 pt-1">
          <p className="font-semibold">CẢM ƠN QUÝ KHÁCH & HẸN GẶP LẠI!</p>
          <p>Hóa đơn điện tử khởi tạo từ Smart F&B OS</p>
        </div>
      </div>

      {/* Trigger Print Button */}
      <div className="text-center print:hidden">
        <Button
          type="button"
          onClick={handlePrint}
          variant="primary"
          className="shadow-md"
          leftIcon={<Printer className="h-4 w-4" />}
        >
          In Hóa Đơn Nhiệt ESC/POS
        </Button>
      </div>
    </div>
  );
};
