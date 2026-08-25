"use client";

import { MessageSquare, Star, AlertTriangle } from "lucide-react";

export default function ManagerReviewsPage() {
  const reviews = [
    { id: "1", customer: "Nguyễn Văn A", stars: 5, comment: "Cà phê muối rất đậm đà, kem béo vừa vặn, phục vụ nhanh!", date: "Hôm nay, 09:30" },
    { id: "2", customer: "Khách Bàn 04", stars: 2, comment: "Trà hơi ngọt so với yêu cầu 30% đường.", date: "Hôm qua, 14:15" },
  ];

  return (
    <div className="p-6 max-w-5xl mx-auto space-y-6">
      <header>
        <h1 className="text-xl font-bold text-slate-900 flex items-center gap-2">
          <MessageSquare className="w-5 h-5 text-purple-600" /> Quản Lý Đánh Giá & Phản Hồi Khách Hàng
        </h1>
        <p className="text-xs text-slate-500">Hệ thống kích hoạt cảnh báo đỏ khẩn cấp khi có đánh giá &le; 2 sao.</p>
      </header>

      <div className="space-y-3">
        {reviews.map((r) => (
          <div
            key={r.id}
            className={`p-4 rounded-2xl border shadow-sm space-y-2 bg-white ${
              r.stars <= 2 ? "border-rose-300 bg-rose-50/20" : "border-slate-200"
            }`}
          >
            <div className="flex justify-between items-center text-xs">
              <span className="font-bold text-slate-900">{r.customer}</span>
              <span className="text-slate-400">{r.date}</span>
            </div>
            <div className="flex items-center gap-1">
              {[...Array(5)].map((_, i) => (
                <Star
                  key={i}
                  className={`w-4 h-4 ${
                    i < r.stars ? "text-amber-400 fill-amber-400" : "text-slate-200"
                  }`}
                />
              ))}
            </div>
            <p className="text-xs text-slate-700">{r.comment}</p>
            {r.stars <= 2 && (
              <div className="p-2 rounded-lg bg-rose-50 text-rose-800 text-[11px] flex items-center gap-1.5 border border-rose-200">
                <AlertTriangle className="w-3.5 h-3.5 text-rose-600" />
                <span>Cảnh báo quản lý: Đã ghi nhận phản hồi để chấn chỉnh khâu pha chế.</span>
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}
