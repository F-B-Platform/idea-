"use client";

import React, { useState } from "react";
import { ReviewDto } from "@/types";
import { formatDateTime } from "@/lib/utils";
import { Button } from "@/components/ui/Button";
import {
  Star,
  ShieldAlert,
  Check,
  X,
  Phone,
  Clock,
  MessageSquare,
  CheckCircle2,
} from "lucide-react";

const initialReviews: ReviewDto[] = [
  {
    id: "rev-01",
    orderId: "ord-04",
    orderCode: "ORD-0042",
    branchId: "branch-q1",
    tableNumber: "04",
    customerPhone: "0908123456",
    rating: 1, // Red Alert
    tags: ["Pha chế lâu", "Đồ uống nhạt"],
    comment: "Đợi cà phê muối 15 phút chưa thấy mang ra, lúc uống thì bị tan hết đá.",
    isAnonymous: false,
    isRedAlert: true,
    isResolved: false,
    createdAtUtc: new Date().toISOString(),
    images: [],
  },
  {
    id: "rev-02",
    orderId: "ord-05",
    orderCode: "ORD-0039",
    branchId: "branch-q1",
    tableNumber: "02",
    customerPhone: "0912345678",
    rating: 5,
    tags: ["Đồ uống ngon", "Không gian sạch đẹp"],
    comment: "Trà đào ngon giòn, quán trang trí rất xinh!",
    isAnonymous: false,
    isRedAlert: false,
    isResolved: true,
    createdAtUtc: "2026-08-25T08:15:00Z",
    images: [
      {
        id: "img-01",
        imageUrl: "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=400&q=80",
        isApproved: false,
        uploadedAtUtc: "2026-08-25T08:15:00Z",
      },
    ],
  },
];

export default function ManagerReviewsPage() {
  const [reviews, setReviews] = useState<ReviewDto[]>(initialReviews);
  const [toastMessage, setToastMessage] = useState<string | null>(null);

  const redAlerts = reviews.filter((r) => r.isRedAlert && !r.isResolved);

  const handleResolve = (reviewId: string) => {
    setReviews((prev) =>
      prev.map((r) => (r.id === reviewId ? { ...r, isResolved: true } : r))
    );
    setToastMessage("Đã đánh dấu xử lý khiếu nại khách hàng thành công!");
    setTimeout(() => setToastMessage(null), 3000);
  };

  const handleApproveImage = (reviewId: string, imageId: string, approve: boolean) => {
    setReviews((prev) =>
      prev.map((r) =>
        r.id === reviewId
          ? {
              ...r,
              images: r.images.map((img) =>
                img.id === imageId ? { ...img, isApproved: approve } : img
              ),
            }
          : r
      )
    );
    setToastMessage(approve ? "Đã duyệt ảnh công khai lên menu!" : "Đã từ chối ảnh.");
    setTimeout(() => setToastMessage(null), 3000);
  };

  return (
    <div className="max-w-6xl mx-auto space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between bg-white p-5 rounded-3xl border border-slate-200 shadow-sm">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-2xl bg-amber-700 text-white flex items-center justify-center font-black shadow-sm">
            <Star className="h-5 w-5" />
          </div>
          <div>
            <h1 className="text-lg font-black text-slate-900 leading-tight">
              Cảnh Báo Đánh Giá & Kiểm Duyệt Ảnh Khách Hàng
            </h1>
            <span className="text-xs text-slate-500">
              Tiếp nhận khiếu nại &lt;= 2 sao trong vòng 3 phút và kiểm duyệt hình ảnh tải lên menu
            </span>
          </div>
        </div>

        {redAlerts.length > 0 && (
          <span className="bg-rose-600 text-white text-xs font-black px-4 py-1.5 rounded-full shadow-md animate-bounce">
            {redAlerts.length} RED ALERT CẦN XỬ LÝ!
          </span>
        )}
      </div>

      {toastMessage && (
        <div className="p-4 bg-emerald-50 border border-emerald-300 text-emerald-900 text-xs font-bold rounded-2xl flex items-center gap-2 animate-in fade-in">
          <CheckCircle2 className="h-5 w-5 text-emerald-600 shrink-0" />
          <span>{toastMessage}</span>
        </div>
      )}

      {/* Red Alert Urgent Section */}
      {redAlerts.length > 0 && (
        <div className="space-y-3">
          <h3 className="font-extrabold text-sm uppercase tracking-wider text-rose-700 flex items-center gap-2">
            <ShieldAlert className="h-5 w-5" />
            <span>Hộp Thư Khẩn Cấp (Đánh Giá &lt;= 2 Sao Tại Bàn)</span>
          </h3>

          <div className="space-y-3">
            {redAlerts.map((rev) => (
              <div
                key={rev.id}
                className="p-5 rounded-3xl bg-rose-50 border-2 border-rose-300 shadow-md flex flex-col md:flex-row md:items-center justify-between gap-4 animate-in slide-in-from-top-2"
              >
                <div className="space-y-2">
                  <div className="flex items-center gap-3">
                    <span className="bg-rose-600 text-white text-xs font-black px-3 py-1 rounded-full">
                      BÀN #{rev.tableNumber}
                    </span>
                    <span className="font-bold text-sm text-slate-900">
                      Mã Đơn: #{rev.orderCode}
                    </span>
                    <div className="flex items-center gap-1 text-rose-700 font-black text-sm">
                      <Star className="h-4 w-4 fill-rose-600" />
                      <span>{rev.rating} / 5 Sao</span>
                    </div>
                  </div>

                  <p className="text-xs text-rose-950 font-medium italic bg-white/70 p-2.5 rounded-xl border border-rose-200">
                    "{rev.comment}"
                  </p>

                  <div className="flex items-center gap-4 text-xs text-slate-600">
                    <span className="flex items-center gap-1 font-semibold">
                      <Phone className="h-3.5 w-3.5 text-slate-400" />
                      {rev.customerPhone}
                    </span>
                    <span className="flex items-center gap-1">
                      <Clock className="h-3.5 w-3.5 text-slate-400" />
                      {formatDateTime(rev.createdAtUtc)}
                    </span>
                  </div>
                </div>

                <Button
                  type="button"
                  onClick={() => handleResolve(rev.id)}
                  size="md"
                  variant="primary"
                  className="bg-rose-700 hover:bg-rose-800 font-extrabold text-xs shrink-0"
                  leftIcon={<Check className="h-4 w-4" />}
                >
                  Xác Nhận Đã Đến Bàn Hỗ Trợ
                </Button>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Customer Photos Moderation Section */}
      <div className="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4">
        <h3 className="font-bold text-xs uppercase tracking-wider text-slate-700 border-b border-slate-100 pb-3">
          Kiểm Duyệt Hình Ảnh Khách Hàng Tải Lên Menu
        </h3>

        <div className="space-y-4">
          {reviews.map((rev) => (
            <div key={rev.id} className="p-4 rounded-2xl border border-slate-200 bg-slate-50/50 space-y-3">
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-2">
                  <span className="font-bold text-xs text-slate-900">Đơn #{rev.orderCode}</span>
                  <div className="flex items-center text-amber-500">
                    {Array.from({ length: rev.rating }).map((_, i) => (
                      <Star key={i} className="h-3.5 w-3.5 fill-current" />
                    ))}
                  </div>
                </div>
                <span className="text-xs text-slate-400">{formatDateTime(rev.createdAtUtc)}</span>
              </div>

              <p className="text-xs text-slate-700">{rev.comment}</p>

              {rev.images.length > 0 && (
                <div className="flex items-center gap-4 pt-2">
                  {rev.images.map((img) => (
                    <div key={img.id} className="space-y-2">
                      <img
                        src={img.imageUrl}
                        alt="Customer upload"
                        className="w-28 h-28 object-cover rounded-xl border border-slate-300"
                      />
                      <div className="flex items-center gap-1">
                        <Button
                          type="button"
                          size="sm"
                          variant={img.isApproved ? "secondary" : "primary"}
                          className="text-[10px] py-1 px-2"
                          onClick={() => handleApproveImage(rev.id, img.id, true)}
                        >
                          Duyệt
                        </Button>
                        <Button
                          type="button"
                          size="sm"
                          variant="danger"
                          className="text-[10px] py-1 px-2"
                          onClick={() => handleApproveImage(rev.id, img.id, false)}
                        >
                          Từ Chối
                        </Button>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
