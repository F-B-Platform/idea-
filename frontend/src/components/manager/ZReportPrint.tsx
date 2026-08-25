"use client";

import React, { useRef } from "react";
import { ZReportDto } from "@/types";
import { formatCurrencyVND, formatDateTime } from "@/lib/utils";
import { Printer, FileText } from "lucide-react";
import { Button } from "@/components/ui/Button";

export interface ZReportPrintProps {
  report: ZReportDto;
}

export const ZReportPrint: React.FC<ZReportPrintProps> = ({ report }) => {
  const printRef = useRef<HTMLDivElement>(null);

  const handlePrint = () => {
    window.print();
  };

  return (
    <div className="space-y-4">
      {/* Report Paper View */}
      <div
        ref={printRef}
        className="w-[360px] mx-auto bg-white p-6 rounded-xl border border-slate-300 shadow-xl font-mono text-xs text-slate-900 space-y-4 print:w-full print:shadow-none print:border-none print:m-0"
      >
        {/* Header */}
        <div className="text-center space-y-1 border-b border-dashed border-slate-400 pb-3">
          <h2 className="font-extrabold text-sm uppercase">{report.branchName}</h2>
          <h3 className="font-bold text-xs uppercase tracking-wider">
            BIÊN BẢN CHỐT CA KÉT (Z-REPORT)
          </h3>
          <p className="text-[10px] text-slate-500">Mã Ca: #{report.shiftCode || report.shiftId}</p>
        </div>

        {/* Timestamps & Staff */}
        <div className="space-y-1 text-[11px] border-b border-dashed border-slate-300 pb-2">
          <div className="flex justify-between">
            <span>Thu ngân:</span>
            <strong className="text-slate-900">{report.cashierName}</strong>
          </div>
          <div className="flex justify-between">
            <span>Mở ca:</span>
            <span>{formatDateTime(report.openedAtUtc)}</span>
          </div>
          <div className="flex justify-between">
            <span>Đóng ca:</span>
            <span>{formatDateTime(report.closedAtUtc)}</span>
          </div>
          <div className="flex justify-between">
            <span>Tổng số đơn:</span>
            <span>{report.totalOrdersCount || 0} đơn</span>
          </div>
        </div>

        {/* Sales Breakdown */}
        <div className="space-y-1.5 border-b border-dashed border-slate-300 pb-3">
          <div className="flex justify-between font-bold text-[10px] uppercase text-slate-500">
            <span>Doanh Thu Theo Kênh</span>
            <span>Số Tiền</span>
          </div>
          <div className="flex justify-between">
            <span>Doanh thu Tiền mặt:</span>
            <span className="font-semibold">{formatCurrencyVND(report.cashSales)}</span>
          </div>
          <div className="flex justify-between">
            <span>Doanh thu VietQR:</span>
            <span className="font-semibold">{formatCurrencyVND(report.vietQrSales)}</span>
          </div>
          <div className="flex justify-between font-black text-sm pt-1 border-t border-slate-200">
            <span>TỔNG DOANH THU:</span>
            <span className="text-amber-900">{formatCurrencyVND(report.totalRevenue)}</span>
          </div>
        </div>

        {/* Cash Drawer Reconciliation */}
        <div className="space-y-1.5 border-b border-dashed border-slate-300 pb-3">
          <div className="flex justify-between font-bold text-[10px] uppercase text-slate-500">
            <span>Đối Soát Két Tiền</span>
            <span>Số Tiền</span>
          </div>
          <div className="flex justify-between">
            <span>Tiền đầu ca:</span>
            <span>{formatCurrencyVND(report.openingCash)}</span>
          </div>
          <div className="flex justify-between">
            <span>Thu tiền mặt trong ca:</span>
            <span>+{formatCurrencyVND(report.cashSales)}</span>
          </div>
          <div className="flex justify-between font-semibold border-t border-slate-200 pt-1">
            <span>Lý thuyết hệ thống:</span>
            <span>{formatCurrencyVND(report.theoreticalCash)}</span>
          </div>
          <div className="flex justify-between font-bold text-amber-900">
            <span>Thực đếm trong két:</span>
            <span>{formatCurrencyVND(report.physicalCash)}</span>
          </div>
          <div className="flex justify-between font-black text-xs pt-1 border-t border-slate-300">
            <span>CHÊNH LỆCH (VARIANCE):</span>
            <span
              className={
                report.variance === 0
                  ? "text-emerald-700"
                  : report.variance > 0
                  ? "text-sky-700"
                  : "text-rose-700"
              }
            >
              {report.variance > 0 ? "+" : ""}
              {formatCurrencyVND(report.variance)}
            </span>
          </div>
          {report.justificationReason && (
            <div className="pt-2 text-[10px] text-slate-600 bg-slate-50 p-2 rounded border border-slate-200">
              <span className="font-bold block">Giải trình chênh lệch:</span>
              <p className="italic">{report.justificationReason}</p>
            </div>
          )}
        </div>

        {/* Signatures */}
        <div className="grid grid-cols-2 text-center text-[10px] pt-4 pb-2">
          <div>
            <span className="font-bold block">Thu Ngân Bàn Giao</span>
            <span className="text-slate-400 mt-8 block">(Ký và ghi rõ họ tên)</span>
          </div>
          <div>
            <span className="font-bold block">Quản Lý Nhận Ca</span>
            <span className="text-slate-400 mt-8 block">(Ký và ghi rõ họ tên)</span>
          </div>
        </div>
      </div>

      {/* Trigger Button */}
      <div className="text-center print:hidden">
        <Button
          type="button"
          onClick={handlePrint}
          variant="primary"
          leftIcon={<Printer className="h-4 w-4" />}
        >
          In Báo Cáo Z-Report
        </Button>
      </div>
    </div>
  );
};
