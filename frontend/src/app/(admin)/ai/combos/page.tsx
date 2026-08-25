"use client";

import React, { useState } from "react";
import { ComboCandidateDto } from "@/types";
import { ComboApprovalCard } from "@/components/admin/ComboApprovalCard";
import { Button } from "@/components/ui/Button";
import { Input } from "@/components/ui/Input";
import { Slider } from "@/components/ui/Slider";
import { Sparkles, Play, CheckCircle2, History } from "lucide-react";

const initialCandidates: ComboCandidateDto[] = [
  {
    id: "combo-cand-01",
    productIds: ["prod-01", "prod-05"],
    productNames: ["Cà Phê Muối Hoàng Gia", "Bánh Croissant Bơ Tỏi"],
    originalPrice: 67000,
    bomCost: 22000,
    grossMarginPercent: 67,
    support: 0.18, // 18% of orders buy together
    confidence: 0.65, // 65% who buy coffee also buy croissant
    lift: 2.45,
    suggestedDiscountPercent: 15,
    proposedPrice: 57000,
    projectedProfit: 35000,
  },
  {
    id: "combo-cand-02",
    productIds: ["prod-02", "prod-03"],
    productNames: ["Trà Đào Cam Sả", "Trà Sữa Oolong Nướng"],
    originalPrice: 81000,
    bomCost: 28000,
    grossMarginPercent: 65,
    support: 0.12,
    confidence: 0.48,
    lift: 1.85,
    suggestedDiscountPercent: 12,
    proposedPrice: 71000,
    projectedProfit: 43000,
  },
];

export default function AiCombosPage() {
  const [candidates, setCandidates] = useState<ComboCandidateDto[]>(initialCandidates);
  const [minSupport, setMinSupport] = useState(10);
  const [minConfidence, setMinConfidence] = useState(40);
  const [isMining, setIsMining] = useState(false);
  const [toastMessage, setToastMessage] = useState<string | null>(null);

  const handleRunMining = () => {
    setIsMining(true);
    setTimeout(() => {
      setIsMining(false);
      setToastMessage("Đã phân tích 1.250 đơn hàng lịch sử và tìm thấy 2 cặp Combo tiềm năng (Lift > 1.8)!");
      setTimeout(() => setToastMessage(null), 3500);
    }, 1000);
  };

  const handleApprove = (
    comboId: string,
    comboName: string,
    discountPercent: number,
    finalPrice: number
  ) => {
    setCandidates((prev) => prev.filter((c) => c.id !== comboId));
    setToastMessage(
      `ĐÃ PHÊ DUYỆT & PHÁT HÀNH: "${comboName}" (${finalPrice.toLocaleString()}₫) lên Menu PWA Khách Hàng!`
    );
    setTimeout(() => setToastMessage(null), 4000);
  };

  const handleReject = (comboId: string) => {
    setCandidates((prev) => prev.filter((c) => c.id !== comboId));
    setToastMessage("Đã từ chối ứng viên combo.");
    setTimeout(() => setToastMessage(null), 2500);
  };

  return (
    <div className="max-w-6xl mx-auto space-y-8">
      {/* Top Header */}
      <div className="flex items-center justify-between bg-white p-5 rounded-3xl border border-slate-200 shadow-sm">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-2xl bg-amber-700 text-white flex items-center justify-center font-black shadow-sm">
            <Sparkles className="h-5 w-5" />
          </div>
          <div>
            <h1 className="text-lg font-black text-slate-900 leading-tight">
              AI-2 Khai Phá Giỏ Hàng & Phê Duyệt Combo (Apriori Engine)
            </h1>
            <span className="text-xs text-slate-500">
              Thuật toán học máy khai phá mẫu phổ biến, đề xuất cặp món mua kèm có Lift cao
            </span>
          </div>
        </div>
      </div>

      {toastMessage && (
        <div className="p-4 bg-emerald-50 border border-emerald-300 text-emerald-900 text-xs font-bold rounded-2xl flex items-center gap-2 animate-in fade-in">
          <CheckCircle2 className="h-5 w-5 text-emerald-600 shrink-0" />
          <span>{toastMessage}</span>
        </div>
      )}

      {/* Mining Parameters Control Bar */}
      <div className="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4">
        <h3 className="font-bold text-xs uppercase tracking-wider text-slate-700 border-b border-slate-100 pb-3">
          Thiết Lập Tham Số Khai Phá Luật Kết Hợp
        </h3>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <Slider
            label="Độ Hỗ Trợ Tối Thiểu (Min Support)"
            min={5}
            max={30}
            step={1}
            value={minSupport}
            valueSuffix="%"
            onChange={setMinSupport}
          />
          <Slider
            label="Độ Tin Cậy Tối Thiểu (Min Confidence)"
            min={20}
            max={80}
            step={5}
            value={minConfidence}
            valueSuffix="%"
            onChange={setMinConfidence}
          />
        </div>

        <div className="flex justify-end pt-2">
          <Button
            type="button"
            onClick={handleRunMining}
            isLoading={isMining}
            variant="primary"
            leftIcon={<Play className="h-4 w-4 fill-current" />}
          >
            Chạy Khai Phá Giỏ Hàng (Apriori Run)
          </Button>
        </div>
      </div>

      {/* Candidates List with Discount Sliders & Margin Check */}
      <div className="space-y-4">
        <h3 className="font-bold text-xs uppercase tracking-wider text-slate-500">
          Các Ứng Viên Combo Chờ Phê Duyệt ({candidates.length})
        </h3>

        {candidates.length === 0 ? (
          <div className="p-12 text-center bg-white rounded-3xl border border-slate-200 text-slate-400 space-y-2">
            <Sparkles className="h-10 w-10 mx-auto text-slate-300" />
            <p className="text-sm font-semibold">Tất cả combo đã được phê duyệt hoặc xử lý.</p>
            <p className="text-xs">Bấm "Chạy Khai Phá Giỏ Hàng" để quét lại dữ liệu mới nhất.</p>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {candidates.map((combo) => (
              <ComboApprovalCard
                key={combo.id}
                combo={combo}
                onApprove={handleApprove}
                onReject={handleReject}
              />
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
