"use client";

import React, { useState } from "react";
import { useShiftStore } from "@/stores/useShiftStore";
import { formatCurrencyVND } from "@/lib/utils";
import { DenominationCounter } from "@/components/manager/DenominationCounter";
import { ZReportPrint } from "@/components/manager/ZReportPrint";
import { Button } from "@/components/ui/Button";
import { Input } from "@/components/ui/Input";
import { Modal } from "@/components/ui/Modal";
import { ZReportDto } from "@/types";
import {
  DollarSign,
  Lock,
  Unlock,
  Printer,
  CheckCircle2,
  FileCheck,
  AlertTriangle,
} from "lucide-react";

export default function CashShiftManagerPage() {
  const {
    currentShiftId,
    shiftCode,
    openingCash,
    cashSales,
    vietQrSales,
    theoreticalCash,
    denominations,
    physicalCashTotal,
    variance,
    justificationReason,
    isClosed,
    openShift,
    setSalesAmounts,
    setDenominationCount,
    setJustificationReason,
    closeShift,
    resetShift,
  } = useShiftStore();

  const [inputOpeningCash, setInputOpeningCash] = useState(1000000);
  const [closedZReport, setClosedZReport] = useState<ZReportDto | null>(null);
  const [showZReportModal, setShowZReportModal] = useState(false);

  const handleOpenShift = () => {
    const newShiftId = `shift-${Date.now()}`;
    const newShiftCode = `SHIFT-${new Date().toISOString().slice(0, 10).replace(/-/g, "")}-01`;
    openShift(newShiftId, newShiftCode, "branch-q1", inputOpeningCash);
    // Simulate some sales during the shift
    setSalesAmounts(1450000, 3200000);
  };

  const handleCloseShift = () => {
    if (variance !== 0 && !justificationReason.trim()) {
      alert("Phát hiện chênh lệch tiền két! Vui lòng nhập lý do giải trình bắt buộc.");
      return;
    }

    const report: ZReportDto = {
      id: `zrep-${Date.now()}`,
      shiftId: currentShiftId || "shift-01",
      shiftCode: shiftCode || "SHIFT-01",
      branchName: "Smart F&B Chi nhánh Quận 1",
      cashierName: "Nguyễn Văn Thu Ngân",
      openedAtUtc: "2026-08-25T07:00:00Z",
      closedAtUtc: new Date().toISOString(),
      openingCash,
      cashSales,
      vietQrSales,
      totalRevenue: cashSales + vietQrSales,
      totalOrdersCount: 42,
      discountTotal: 35000,
      theoreticalCash,
      physicalCash: physicalCashTotal,
      variance,
      justificationReason,
      denominations,
    };

    closeShift();
    setClosedZReport(report);
    setShowZReportModal(true);
  };

  return (
    <div className="max-w-5xl mx-auto space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between bg-white p-5 rounded-3xl border border-slate-200 shadow-sm">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-2xl bg-amber-700 text-white flex items-center justify-center font-black shadow-sm">
            <DollarSign className="h-5 w-5" />
          </div>
          <div>
            <h1 className="text-lg font-black text-slate-900 leading-tight">
              Quản Lý Ca Két Tiền & Đối Soát Z-Report
            </h1>
            <span className="text-xs text-slate-500">
              Kiểm đếm 6 mệnh giá tiền mặt, đối soát lý thuyết và in biên bản chốt ca
            </span>
          </div>
        </div>

        <div className="flex items-center gap-2">
          <span
            className={`px-3 py-1 rounded-full text-xs font-bold ${
              !isClosed
                ? "bg-emerald-100 text-emerald-800 border border-emerald-300"
                : "bg-slate-100 text-slate-700 border border-slate-300"
            }`}
          >
            {!isClosed ? "Ca Đang Mở" : "Ca Đã Đóng"}
          </span>
        </div>
      </div>

      {isClosed && !closedZReport ? (
        /* Open Shift Box */
        <div className="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4 max-w-md">
          <div className="flex items-center gap-2 text-amber-900 font-bold text-sm">
            <Unlock className="h-5 w-5" />
            <span>Mở Ca Két Tiền Mới</span>
          </div>
          <p className="text-xs text-slate-500">
            Khai báo số tiền mặt tồn đầu ca (Opening Float) để bắt đầu ca bán hàng.
          </p>

          <Input
            label="Tiền mặt đầu ca (₫)"
            type="number"
            value={inputOpeningCash}
            onChange={(e) => setInputOpeningCash(Number(e.target.value))}
          />

          <Button
            type="button"
            onClick={handleOpenShift}
            variant="primary"
            className="w-full font-bold"
          >
            Xác Nhận Mở Ca Két ({formatCurrencyVND(inputOpeningCash)})
          </Button>
        </div>
      ) : (
        /* Active Shift Reconciliation & Z-Report */
        <div className="space-y-6">
          {/* Shift Financial Overview */}
          <div className="grid grid-cols-1 sm:grid-cols-4 gap-4">
            <div className="bg-white p-4 rounded-2xl border border-slate-200 shadow-2xs space-y-1">
              <span className="text-xs text-slate-500 font-medium">Tiền Đầu Ca:</span>
              <span className="text-lg font-bold text-slate-900">
                {formatCurrencyVND(openingCash)}
              </span>
            </div>

            <div className="bg-white p-4 rounded-2xl border border-slate-200 shadow-2xs space-y-1">
              <span className="text-xs text-slate-500 font-medium">Thu Tiền Mặt:</span>
              <span className="text-lg font-bold text-slate-900">
                {formatCurrencyVND(cashSales)}
              </span>
            </div>

            <div className="bg-white p-4 rounded-2xl border border-slate-200 shadow-2xs space-y-1">
              <span className="text-xs text-slate-500 font-medium">Thu VietQR:</span>
              <span className="text-lg font-bold text-amber-800">
                {formatCurrencyVND(vietQrSales)}
              </span>
            </div>

            <div className="bg-white p-4 rounded-2xl border border-slate-200 shadow-2xs space-y-1">
              <span className="text-xs text-slate-500 font-medium">Lý Thuyết Trong Két:</span>
              <span className="text-lg font-black text-amber-950">
                {formatCurrencyVND(theoreticalCash)}
              </span>
            </div>
          </div>

          {/* Denomination Counter for 6 Denominations */}
          <DenominationCounter
            denominations={denominations}
            onCountChange={setDenominationCount}
            theoreticalCash={theoreticalCash}
            physicalCashTotal={physicalCashTotal}
            variance={variance}
            justificationReason={justificationReason}
            onJustificationChange={setJustificationReason}
          />

          {/* Close Shift Actions */}
          <div className="flex justify-end gap-3 pt-2">
            <Button
              type="button"
              onClick={handleCloseShift}
              size="lg"
              variant="primary"
              className="font-bold shadow-md"
              leftIcon={<Lock className="h-4 w-4" />}
            >
              XÁC NHẬN ĐÓNG CA KÉT & IN Z-REPORT
            </Button>
          </div>
        </div>
      )}

      {/* Z-Report Modal */}
      <Modal
        isOpen={showZReportModal}
        onClose={() => setShowZReportModal(false)}
        maxWidth="md"
        title="Biên Bản Chốt Ca Z-Report"
        footer={
          <Button
            variant="secondary"
            onClick={() => {
              setShowZReportModal(false);
              resetShift();
            }}
          >
            Đóng & Bắt Đầu Ca Mới
          </Button>
        }
      >
        {closedZReport && <ZReportPrint report={closedZReport} />}
      </Modal>
    </div>
  );
}
