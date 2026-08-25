"use client";

import { Sparkles, Check, X } from "lucide-react";

export default function AdminAiCombosPage() {
  const combos = [
    { name: "Combo Năng Lượng Sáng", items: "Cà Phê Muối + Bánh Croissant", support: "18.5%", confidence: "74.2%", discount: "15%" },
    { name: "Combo Trà Chiều Thư Giãn", items: "Trà Đào Cam Sả + Tiramisu", support: "14.2%", confidence: "68.0%", discount: "10%" },
  ];

  return (
    <div className="p-6 max-w-5xl mx-auto space-y-6">
      <header>
        <h1 className="text-xl font-bold text-slate-900 flex items-center gap-2">
          <Sparkles className="w-5 h-5 text-purple-600" /> Phê Duyệt Gợi Ý Combo Thông Minh (AI-2 Apriori Mining)
        </h1>
        <p className="text-xs text-slate-500">Thuật toán khai phá tập mục phổ biến Apriori đề xuất combo dựa trên dữ liệu giỏ hàng lịch sử.</p>
      </header>

      <div className="space-y-3">
        {combos.map((combo, idx) => (
          <div key={idx} className="p-4 bg-white rounded-2xl border border-slate-200 shadow-sm flex justify-between items-center">
            <div>
              <h2 className="text-sm font-bold text-slate-900">{combo.name}</h2>
              <p className="text-xs text-slate-600">{combo.items} • Giảm giá: <span className="font-bold text-rose-600">{combo.discount}</span></p>
              <p className="text-[11px] text-slate-400 font-mono mt-1">Support: {combo.support} | Confidence: {combo.confidence}</p>
            </div>
            <div className="flex gap-2">
              <button className="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs flex items-center gap-1 shadow">
                <Check className="w-3.5 h-3.5" /> Duyệt Combo
              </button>
              <button className="px-3 py-1.5 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-600 font-semibold text-xs flex items-center gap-1">
                <X className="w-3.5 h-3.5" /> Từ Chối
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
