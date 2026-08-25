"use client";

import React, { useState, useEffect, Suspense } from "react";
import { useSearchParams, useRouter } from "next/navigation";
import { formatCurrencyVND } from "@/lib/utils";
import { Button } from "@/components/ui/Button";
import {
  QrCode,
  Clock,
  Copy,
  Check,
  CheckCircle2,
  AlertTriangle,
  ArrowLeft,
  RefreshCw,
  ExternalLink,
} from "lucide-react";
import { useSignalR } from "@/hooks/useSignalR";

function VietQrCheckoutContent() {
  const searchParams = useSearchParams();
  const router = useRouter();
  const orderId = searchParams.get("orderId") || "ORD-5542";
  const amount = Number(searchParams.get("amount")) || 74000;

  const [timeLeftSeconds, setTimeLeftSeconds] = useState(600); // 10 minutes countdown
  const [copiedField, setCopiedField] = useState<string | null>(null);
  const [isChecking, setIsChecking] = useState(false);
  const [paymentSuccess, setPaymentSuccess] = useState(false);

  // Bank transfer specifications
  const bankDetails = {
    bankName: "MBBank (Ngân Hàng Quân Đội)",
    accountNumber: "9999088886666",
    accountName: "CONG TY CP SMART FB VIET NAM",
    transferContent: orderId,
    amount: amount,
  };

  // SignalR Payment Listener for auto-redirect
  const { registerHandler } = useSignalR({
    hubPath: "/hubs/payments",
    groupName: orderId,
    joinGroupMethod: "JoinPaymentGroup",
  });

  useEffect(() => {
    registerHandler("PaymentSucceeded", (data: any) => {
      setPaymentSuccess(true);
      setTimeout(() => {
        router.push(`/tracking/${orderId}?status=paid`);
      }, 1200);
    });
  }, [registerHandler, orderId, router]);

  // 10-Minute Countdown Timer
  useEffect(() => {
    if (timeLeftSeconds <= 0) return;
    const interval = setInterval(() => {
      setTimeLeftSeconds((prev) => prev - 1);
    }, 1000);
    return () => clearInterval(interval);
  }, [timeLeftSeconds]);

  const minutes = Math.floor(timeLeftSeconds / 60);
  const seconds = timeLeftSeconds % 60;
  const timeFormatted = `${minutes.toString().padStart(2, "0")}:${seconds
    .toString()
    .padStart(2, "0")}`;

  const handleCopy = (field: string, text: string) => {
    navigator.clipboard.writeText(text);
    setCopiedField(field);
    setTimeout(() => setCopiedField(null), 2000);
  };

  const handleManualCheck = () => {
    setIsChecking(true);
    setTimeout(() => {
      setIsChecking(false);
      setPaymentSuccess(true);
      setTimeout(() => {
        router.push(`/tracking/${orderId}?status=paid`);
      }, 1000);
    }, 1500);
  };

  if (timeLeftSeconds <= 0) {
    return (
      <div className="px-4 py-16 text-center space-y-4">
        <div className="w-16 h-16 bg-rose-100 text-rose-600 rounded-full flex items-center justify-center mx-auto">
          <AlertTriangle className="h-8 w-8" />
        </div>
        <h3 className="text-lg font-bold text-slate-900">Mã VietQR Đã Hết Hạn</h3>
        <p className="text-xs text-slate-500 max-w-xs mx-auto">
          Thời gian chờ thanh toán 10 phút đã kết thúc. Đơn hàng đã được hoàn kho tự động. Quý khách vui lòng tạo đơn mới.
        </p>
        <Button onClick={() => router.push("/menu")} variant="primary">
          Đặt Lại Đơn Mới
        </Button>
      </div>
    );
  }

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
          <span>Quay lại giỏ hàng</span>
        </button>
        <span className="text-xs font-bold text-slate-500">Mã Đơn: #{orderId}</span>
      </div>

      {paymentSuccess ? (
        <div className="bg-emerald-50 border border-emerald-300 rounded-3xl p-8 text-center space-y-3 animate-in zoom-in-95">
          <CheckCircle2 className="h-16 w-16 text-emerald-600 mx-auto animate-bounce" />
          <h3 className="text-xl font-black text-emerald-950">Thanh Toán Thành Công!</h3>
          <p className="text-xs text-emerald-800">
            Hệ thống đã nhận được tiền và đang chuyển đơn hàng xuống Bếp KDS...
          </p>
        </div>
      ) : (
        <>
          {/* 10-Minute Timer Badge */}
          <div className="bg-amber-50 border border-amber-300 rounded-2xl p-4 flex items-center justify-between shadow-2xs">
            <div className="flex items-center gap-2.5">
              <Clock className="h-5 w-5 text-amber-700 animate-spin" />
              <div>
                <span className="text-xs font-bold text-amber-950 block">Thời Gian Chờ Thanh Toán</span>
                <span className="text-[11px] text-amber-800">Đơn sẽ tự hủy khi đếm ngược về 00:00</span>
              </div>
            </div>
            <span className="font-mono font-black text-xl text-amber-900 bg-amber-200/70 px-3 py-1 rounded-xl">
              {timeFormatted}
            </span>
          </div>

          {/* Dynamic VietQR Code Display Box */}
          <div className="bg-white rounded-3xl p-6 border border-slate-200 shadow-md text-center space-y-4">
            <div className="space-y-1">
              <span className="text-xs uppercase font-bold text-slate-400 tracking-wider">
                Quét Mã Qua Mọi App Ngân Hàng / Ví Điện Tử
              </span>
              <h3 className="text-2xl font-black text-amber-900">
                {formatCurrencyVND(amount)}
              </h3>
            </div>

            {/* VietQR Mockup Image */}
            <div className="relative w-64 h-64 mx-auto p-3 bg-white rounded-2xl border-2 border-slate-200 shadow-inner flex flex-col items-center justify-center">
              {/* Dynamic VietQR SVG Placeholder */}
              <div className="w-full h-full bg-slate-900 rounded-xl flex flex-col items-center justify-center text-white p-4 space-y-2">
                <QrCode className="w-28 h-28 text-white" />
                <span className="text-[10px] tracking-widest font-mono text-amber-300">
                  VIETQR • PAYOS GATEWAY
                </span>
                <span className="text-[9px] text-slate-300 font-mono">
                  ORD: {orderId} | {amount} VND
                </span>
              </div>
            </div>

            <p className="text-[11px] text-slate-500">
              Mở App Ngân hàng bất kỳ (Vietcombank, MB, Techcombank, MoMo...) chọn <strong>Quét QR</strong> để thanh toán.
            </p>
          </div>

          {/* Manual Bank Transfer Information (Copy 1-tap) */}
          <div className="bg-white rounded-2xl p-5 border border-slate-200 shadow-2xs space-y-3">
            <h4 className="font-bold text-xs uppercase tracking-wider text-slate-500 border-b border-slate-100 pb-2">
              Hoặc Chuyển Khoản Thủ Công 24/7
            </h4>

            <div className="space-y-2.5 text-xs">
              {/* Bank Name */}
              <div className="flex items-center justify-between">
                <span className="text-slate-500">Ngân hàng:</span>
                <span className="font-bold text-slate-900">{bankDetails.bankName}</span>
              </div>

              {/* Account Number */}
              <div className="flex items-center justify-between">
                <span className="text-slate-500">Số tài khoản:</span>
                <div className="flex items-center gap-2">
                  <span className="font-mono font-bold text-slate-900">
                    {bankDetails.accountNumber}
                  </span>
                  <button
                    type="button"
                    onClick={() => handleCopy("account", bankDetails.accountNumber)}
                    className="p-1 text-slate-400 hover:text-amber-800 rounded bg-slate-100"
                    title="Sao chép"
                  >
                    {copiedField === "account" ? (
                      <Check className="h-3.5 w-3.5 text-emerald-600" />
                    ) : (
                      <Copy className="h-3.5 w-3.5" />
                    )}
                  </button>
                </div>
              </div>

              {/* Account Holder */}
              <div className="flex items-center justify-between">
                <span className="text-slate-500">Chủ tài khoản:</span>
                <span className="font-bold text-slate-900">{bankDetails.accountName}</span>
              </div>

              {/* Transfer Content */}
              <div className="flex items-center justify-between bg-amber-50 p-2.5 rounded-xl border border-amber-200">
                <span className="text-amber-900 font-semibold">Nội dung chuyển khoản:</span>
                <div className="flex items-center gap-2">
                  <span className="font-mono font-black text-amber-900 text-sm">
                    {bankDetails.transferContent}
                  </span>
                  <button
                    type="button"
                    onClick={() => handleCopy("content", bankDetails.transferContent)}
                    className="p-1 text-amber-800 hover:text-amber-950 rounded bg-amber-200/60"
                    title="Sao chép nội dung"
                  >
                    {copiedField === "content" ? (
                      <Check className="h-3.5 w-3.5 text-emerald-600" />
                    ) : (
                      <Copy className="h-3.5 w-3.5" />
                    )}
                  </button>
                </div>
              </div>
            </div>
          </div>

          {/* Action Check Button */}
          <div className="space-y-2">
            <Button
              type="button"
              onClick={handleManualCheck}
              isLoading={isChecking}
              size="lg"
              variant="amber"
              className="w-full font-bold shadow-md"
              leftIcon={<RefreshCw className="h-4 w-4" />}
            >
              Tôi Đã Chuyển Tiền Thành Công
            </Button>
            <p className="text-[11px] text-center text-slate-400">
              Hệ thống tự động lắng nghe Webhook PayOS qua SignalR WebSocket.
            </p>
          </div>
        </>
      )}
    </div>
  );
}

export default function VietQrCheckoutPage() {
  return (
    <Suspense
      fallback={
        <div className="p-8 text-center text-xs font-semibold text-slate-500">
          Đang tải thông tin thanh toán VietQR...
        </div>
      }
    >
      <VietQrCheckoutContent />
    </Suspense>
  );
}
