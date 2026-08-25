"use client";

import React, { useState } from "react";
import { formatCurrencyVND, formatDateTime } from "@/lib/utils";
import { Button } from "@/components/ui/Button";
import { Textarea } from "@/components/ui/Textarea";
import { FileText, DollarSign, Coffee, CheckCircle2, UserCheck } from "lucide-react";

export default function ShiftReportPage() {
  const [handoverNote, setHandoverNote] = useState("");
  const [isSubmitted, setIsSubmitted] = useState(false);

  const mockShiftSummary = {
    shiftCode: "SHIFT-20260825-S1",
    cashierName: "Nguyễn Văn Thu Ngân",
    openedAt: "2026-08-25T07:00:00Z",
    closedAt: new Date().toISOString(),
    totalOrders: 38,
    cashSales: 1250000,
    vietQrSales: 2480000,
    totalSales: 3730000,
  };

  const handleHandover = () => {
    setIsSubmitted(true);
  };

  return (
    <div className="max-w-4xl mx-auto space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between bg-white p-5 rounded-3xl border border-slate-200 shadow-sm">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-2xl bg-amber-700 text-white flex items-center justify-center font-black shadow-sm">
            <FileText className="h-5 w-5" />
          </div>
          <div>
            <h1 className="text-lg font-black text-slate-900 leading-tight">
              Báo Cáo Tổng Kết Ca & Bàn Giao Nhân Viên
            </h1>
            <span className="text-xs text-slate-500">Mã Ca: #{mockShiftSummary.shiftCode}</span>
          </div>
        </div>
      </div>

      {isSubmitted && (
        <div className="p-4 bg-emerald-50 border border-emerald-300 text-emerald-900 text-xs font-bold rounded-2xl flex items-center gap-2 animate-in fade-in">
          <CheckCircle2 className="h-5 w-5 text-emerald-600 shrink-0" />
          <span>Biên bản bàn giao ca đã được gửi thành công tới Quản lý chi nhánh!</span>
        </div>
      )}

      {/* KPI Sales Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <div className="bg-white p-5 rounded-3xl border border-slate-200 shadow-sm space-y-1">
          <span className="text-xs font-semibold text-slate-500 block">Tổng Đơn Phục Vụ</span>
          <span className="text-2xl font-black text-slate-900">{mockShiftSummary.totalOrders} đơn</span>
        </div>

        <div className="bg-white p-5 rounded-3xl border border-slate-200 shadow-sm space-y-1">
          <span className="text-xs font-semibold text-slate-500 block">Doanh Thu Tiền Mặt</span>
          <span className="text-2xl font-black text-slate-900">
            {formatCurrencyVND(mockShiftSummary.cashSales)}
          </span>
        </div>

        <div className="bg-white p-5 rounded-3xl border border-slate-200 shadow-sm space-y-1">
          <span className="text-xs font-semibold text-slate-500 block">Doanh Thu VietQR</span>
          <span className="text-2xl font-black text-amber-800">
            {formatCurrencyVND(mockShiftSummary.vietQrSales)}
          </span>
        </div>
      </div>

      {/* Handover Form */}
      <div className="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4">
        <h3 className="font-bold text-xs uppercase tracking-wider text-slate-700 border-b border-slate-100 pb-3">
          Ghi Chú Bàn Giao Ca Kế Tiếp
        </h3>

        <Textarea
          label="Ghi chú tồn đọng / Sự cố trong ca"
          placeholder="Ví dụ: Đã vệ sinh máy pha espresso, quầy bar còn 2 hộp sữa tươi, bàn 02 để quên ô..."
          value={handoverNote}
          onChange={(e) => setHandoverNote(e.target.value)}
          rows={3}
        />

        <div className="flex justify-end pt-2">
          <Button
            type="button"
            onClick={handleHandover}
            disabled={isSubmitted}
            variant="primary"
            className="font-bold"
            leftIcon={<UserCheck className="h-4 w-4" />}
          >
            Xác Nhận Bàn Giao Ca
          </Button>
        </div>
      </div>
    </div>
  );
}
