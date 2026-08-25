"use client";

import React, { useState } from "react";
import { useRouter } from "next/navigation";
import { useCartStore } from "@/stores/useCartStore";
import { validateVietnamesePhone, formatCurrencyVND } from "@/lib/utils";
import { Button } from "@/components/ui/Button";
import { Input } from "@/components/ui/Input";
import { Textarea } from "@/components/ui/Textarea";
import {
  Truck,
  ShieldCheck,
  QrCode,
  ArrowLeft,
  AlertCircle,
  MapPin,
  Phone,
  User,
  ShoppingBag,
} from "lucide-react";

export default function DeliveryOrderPage() {
  const router = useRouter();
  const {
    recipientName,
    recipientPhone,
    deliveryAddress,
    shipperNotes,
    setDeliveryInfo,
    items,
    getSubtotal,
    getTotalAmount,
  } = useCartStore();

  const [name, setName] = useState(recipientName || "");
  const [phone, setPhone] = useState(recipientPhone || "");
  const [address, setAddress] = useState(deliveryAddress || "");
  const [notes, setNotes] = useState(shipperNotes || "");

  const [errors, setErrors] = useState<{ name?: string; phone?: string; address?: string }>({});
  const [isSubmitting, setIsSubmitting] = useState(false);

  const subtotal = getSubtotal();
  const fixedDeliveryFee = 20000;
  const total = subtotal + fixedDeliveryFee;

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const newErrors: { name?: string; phone?: string; address?: string } = {};

    if (!name.trim()) newErrors.name = "Họ và tên người nhận không được để trống";
    const phoneVal = validateVietnamesePhone(phone);
    if (!phoneVal.isValid) newErrors.phone = phoneVal.message;
    if (!address.trim()) newErrors.address = "Địa chỉ giao hàng chi tiết không được để trống";

    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
      return;
    }

    setDeliveryInfo({
      recipientName: name.trim(),
      recipientPhone: phone.trim(),
      deliveryAddress: address.trim(),
      shipperNotes: notes.trim(),
    });

    setIsSubmitting(true);
    const orderId = `DEL-${Math.floor(1000 + Math.random() * 9000)}`;

    setTimeout(() => {
      setIsSubmitting(false);
      router.push(`/checkout/vietqr?orderId=${orderId}&amount=${total}`);
    }, 600);
  };

  return (
    <div className="space-y-6 px-4 pt-4 pb-12">
      {/* Header */}
      <div className="flex items-center justify-between">
        <button
          type="button"
          onClick={() => router.back()}
          className="flex items-center gap-1.5 text-xs font-bold text-slate-600 hover:text-slate-900"
        >
          <ArrowLeft className="h-4 w-4" />
          <span>Quay lại</span>
        </button>
        <span className="text-xs font-bold text-indigo-700 bg-indigo-50 px-3 py-1 rounded-full border border-indigo-200">
          QR Delivery (Ship Tận Nơi)
        </span>
      </div>

      <div className="space-y-1">
        <h2 className="text-xl font-black text-slate-950">Thông Tin Đặt Giao Hàng</h2>
        <p className="text-xs text-slate-500">
          Đơn giao hàng áp dụng phí ship cố định <strong>20.000₫</strong> và thanh toán 100% qua VietQR để chống bùng đơn.
        </p>
      </div>

      <form onSubmit={handleSubmit} className="space-y-5">
        {/* Recipient Information Form Card */}
        <div className="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm space-y-4">
          <div className="flex items-center gap-2 border-b border-slate-100 pb-3">
            <User className="h-4 w-4 text-amber-700" />
            <h3 className="font-bold text-xs uppercase tracking-wider text-slate-800">
              Người Nhận Hàng
            </h3>
          </div>

          <Input
            label="Họ và tên người nhận"
            required
            placeholder="Ví dụ: Nguyễn Văn An"
            value={name}
            onChange={(e) => {
              setName(e.target.value);
              if (errors.name) setErrors((prev) => ({ ...prev, name: undefined }));
            }}
            error={errors.name}
            leftIcon={<User className="h-4 w-4" />}
          />

          <Input
            label="Số điện thoại người nhận"
            required
            type="tel"
            placeholder="10 chữ số (03x, 05x, 07x, 08x, 09x)..."
            value={phone}
            onChange={(e) => {
              setPhone(e.target.value);
              if (errors.phone) setErrors((prev) => ({ ...prev, phone: undefined }));
            }}
            error={errors.phone}
            leftIcon={<Phone className="h-4 w-4" />}
          />

          <Input
            label="Địa chỉ giao hàng chi tiết"
            required
            placeholder="Số nhà, tên đường, phường/xã, quận/huyện..."
            value={address}
            onChange={(e) => {
              setAddress(e.target.value);
              if (errors.address) setErrors((prev) => ({ ...prev, address: undefined }));
            }}
            error={errors.address}
            leftIcon={<MapPin className="h-4 w-4" />}
          />

          <Textarea
            label="Ghi chú cho tài xế giao hàng"
            placeholder="Ví dụ: Gửi bảo vệ sảnh tòa nhà, gọi trước khi đến..."
            value={notes}
            onChange={(e) => setNotes(e.target.value)}
            rows={2}
          />
        </div>

        {/* Locked Payment Policy Badge */}
        <div className="bg-amber-50 border border-amber-200/80 rounded-2xl p-4 space-y-2">
          <div className="flex items-center gap-2 text-amber-950 font-bold text-xs">
            <ShieldCheck className="h-5 w-5 text-amber-700" />
            <span>Chính Sách Thanh Toán Giao Hàng (100% VietQR)</span>
          </div>
          <p className="text-[11px] text-amber-900 leading-relaxed">
            Nhằm đảm bảo chất lượng đồ uống tươi mới và chống tình trạng bùng đơn, dịch vụ giao hàng bắt buộc thanh toán trước 100% qua mã VietQR PayOS. Hình thức COD tạm thời khóa.
          </p>
        </div>

        {/* Cost Summary Breakdown */}
        <div className="bg-white rounded-2xl p-5 border border-slate-200 shadow-2xs space-y-2.5 text-xs">
          <div className="flex justify-between text-slate-600">
            <span>Tiền đồ uống ({items.length} món):</span>
            <span className="font-semibold text-slate-900">{formatCurrencyVND(subtotal)}</span>
          </div>
          <div className="flex justify-between text-indigo-700 font-semibold">
            <div className="flex items-center gap-1">
              <Truck className="h-3.5 w-3.5" />
              <span>Phí giao hàng cố định:</span>
            </div>
            <span>+{formatCurrencyVND(fixedDeliveryFee)}</span>
          </div>
          <div className="flex justify-between font-black text-base pt-2 border-t border-slate-100 text-slate-900">
            <span>Tổng thanh toán:</span>
            <span className="text-amber-900">{formatCurrencyVND(total)}</span>
          </div>
        </div>

        {/* Submit Button */}
        <Button
          type="submit"
          isLoading={isSubmitting}
          size="lg"
          variant="primary"
          className="w-full font-bold shadow-md text-base"
          leftIcon={<QrCode className="h-5 w-5" />}
        >
          Xác Nhận & Quét Mã VietQR • {formatCurrencyVND(total)}
        </Button>
      </form>
    </div>
  );
}
