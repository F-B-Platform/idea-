"use client";

import { FileText, Send } from "lucide-react";

export default function StaffShiftReportPage() {
  return (
    <div className="p-6 max-w-xl mx-auto space-y-6">
      <header>
        <h1 className="text-xl font-bold text-slate-900 flex items-center gap-2">
          <FileText className="w-5 h-5 text-orange-600" /> Báo Cáo & Bàn Giao Ca Làm Việc
        </h1>
        <p className="text-xs text-slate-500">Nhân viên ghi chú các vấn đề phát sinh trong ca để bàn giao cho ca tiếp theo.</p>
      </header>

      <div className="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-4">
        <div>
          <label className="text-xs font-bold text-slate-700">Ca Làm Việc Hiện Tại</label>
          <div className="text-sm font-semibold text-slate-900 mt-1">Ca Sáng (06:30 - 14:30) • Nhân viên: Lê Văn B</div>
        </div>

        <div>
          <label className="text-xs font-bold text-slate-700">Ghi Chú Bàn Giao (Nguyên liệu thiếu, sự cố máy móc...)</label>
          <textarea
            rows={4}
            placeholder="Nhập nội dung bàn giao..."
            className="w-full mt-1 p-3 text-xs rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-orange-500"
          />
        </div>

        <button
          type="button"
          className="w-full py-2.5 rounded-xl bg-orange-500 hover:bg-orange-600 text-white text-xs font-bold flex items-center justify-center gap-2 shadow"
        >
          <Send className="w-4 h-4" /> Gửi Báo Cáo Bàn Giao
        </button>
      </div>
    </div>
  );
}
