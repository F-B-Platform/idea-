"use client";

import Link from "next/link";
import { ArrowLeft, Star, Send } from "lucide-react";
import { useState } from "react";

export default function OrderReviewPage({ params }: { params: { orderId: string } }) {
  const [rating, setRating] = useState(5);
  const [comment, setComment] = useState("");

  return (
    <div className="min-h-screen bg-slate-50 text-slate-800 p-4 max-w-md mx-auto space-y-4">
      <header className="flex items-center gap-2 py-2 border-b border-slate-200">
        <Link href={`/tracking/${params.orderId}`} className="p-2 rounded-full hover:bg-slate-200 text-slate-600">
          <ArrowLeft className="w-5 h-5" />
        </Link>
        <div>
          <h1 className="text-base font-bold text-slate-900">Đánh Giá Trải Nghiệm</h1>
          <p className="text-xs text-slate-500 font-mono">Đơn #{params.orderId}</p>
        </div>
      </header>

      <div className="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-4 text-center">
        <div>
          <h2 className="text-sm font-bold text-slate-900">Chất lượng đồ uống hôm nay thế nào?</h2>
          <p className="text-xs text-slate-500">Ý kiến của bạn giúp chúng tôi cải thiện chất lượng phục vụ</p>
        </div>

        <div className="flex justify-center gap-2">
          {[1, 2, 3, 4, 5].map((star) => (
            <button
              key={star}
              type="button"
              onClick={() => setRating(star)}
              className="p-2 hover:scale-110 transition-transform"
            >
              <Star
                className={`w-8 h-8 ${
                  star <= rating ? "text-amber-400 fill-amber-400" : "text-slate-300"
                }`}
              />
            </button>
          ))}
        </div>

        <textarea
          rows={3}
          value={comment}
          onChange={(e) => setComment(e.target.value)}
          placeholder="Hãy chia sẻ cảm nhận chi tiết của bạn về hương vị đồ uống..."
          className="w-full text-xs p-3 rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-orange-500"
        />

        <button
          type="button"
          className="w-full py-2.5 rounded-xl bg-orange-500 hover:bg-orange-600 text-white font-bold text-xs flex items-center justify-center gap-1.5 shadow"
        >
          <Send className="w-4 h-4" /> Gửi Đánh Giá
        </button>
      </div>
    </div>
  );
}
