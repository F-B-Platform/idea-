"use client";

import React, { useState } from "react";
import { PlSummaryDto, BcgMatrixItemDto } from "@/types";
import { PlSummaryCard } from "@/components/admin/PlSummaryCard";
import { Button } from "@/components/ui/Button";
import {
  Crown,
  Download,
  Calendar,
  Building2,
  TrendingUp,
  Sparkles,
  Award,
} from "lucide-react";

const initialPlSummary: PlSummaryDto = {
  period: "Tháng 08/2026 (01/08 - 25/08)",
  totalRevenue: 458000000,
  cogsAmount: 137400000, // 30% BOM COGS
  grossProfit: 320600000,
  grossMarginPercent: 70.0,
  staffCost: 85000000,
  operatingCost: 65000000,
  netProfit: 170600000,
  netMarginPercent: 37.2,
  branchesBreakdown: [
    {
      branchId: "branch-q1",
      branchName: "Chi nhánh 1 — Quận 1 (Trụ Sở)",
      revenue: 215000000,
      cogs: 64500000,
      profit: 82000000,
    },
    {
      branchId: "branch-q3",
      branchName: "Chi nhánh 2 — Quận 3 (Võ Văn Tần)",
      revenue: 145000000,
      cogs: 43500000,
      profit: 54000000,
    },
    {
      branchId: "branch-td",
      branchName: "Chi nhánh 3 — TP. Thủ Đức (Làng Đại Học)",
      revenue: 98000000,
      cogs: 29400000,
      profit: 34600000,
    },
  ],
};

const bcgItems: BcgMatrixItemDto[] = [
  {
    productId: "prod-01",
    productName: "Cà Phê Muối Hoàng Gia",
    categoryName: "Cà Phê",
    salesVolume: 4200,
    profitMarginPercent: 72,
    category: "Star",
  },
  {
    productId: "prod-02",
    productName: "Trà Đào Cam Sả Tươi",
    categoryName: "Trà Trái Cây",
    salesVolume: 3800,
    profitMarginPercent: 68,
    category: "Star",
  },
  {
    productId: "prod-06",
    productName: "Cà Phê Đen Đá Phin",
    categoryName: "Cà Phê",
    salesVolume: 5100,
    profitMarginPercent: 82,
    category: "CashCow",
  },
  {
    productId: "prod-03",
    productName: "Matcha Latte Kem Trứng",
    categoryName: "Matcha",
    salesVolume: 850,
    profitMarginPercent: 64,
    category: "QuestionMark",
  },
  {
    productId: "prod-08",
    productName: "Bánh Croissant Bơ Tỏi",
    categoryName: "Bánh Ngọt",
    salesVolume: 420,
    profitMarginPercent: 45,
    category: "Dog",
  },
];

export default function AdminDashboardPage() {
  const [summary] = useState<PlSummaryDto>(initialPlSummary);

  const handleExportCsv = () => {
    alert("Đã xuất báo cáo tài chính P&L hợp nhất ra file SmartFB_PL_Report_2026.csv");
  };

  return (
    <div className="max-w-7xl mx-auto space-y-8">
      {/* Header Bar */}
      <div className="flex items-center justify-between bg-white p-5 rounded-3xl border border-slate-200 shadow-sm">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-2xl bg-amber-700 text-white flex items-center justify-center font-black shadow-sm">
            <Crown className="h-5 w-5" />
          </div>
          <div>
            <h1 className="text-lg font-black text-slate-900 leading-tight">
              Báo Cáo Tài Chính P&L Hợp Nhất Toàn Chuỗi
            </h1>
            <span className="text-xs text-slate-500">
              Kỳ: {summary.period} • 3 Chi nhánh hoạt động
            </span>
          </div>
        </div>

        <Button
          type="button"
          onClick={handleExportCsv}
          variant="secondary"
          size="sm"
          leftIcon={<Download className="h-4 w-4" />}
        >
          Xuất Báo Cáo CSV
        </Button>
      </div>

      {/* Core P&L Summary Cards */}
      <PlSummaryCard summary={summary} />

      {/* BCG Menu Matrix Quadrant Analysis */}
      <div className="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-5">
        <div className="flex items-center justify-between border-b border-slate-100 pb-3">
          <div className="flex items-center gap-2 text-slate-900 font-bold text-sm">
            <Award className="h-5 w-5 text-amber-700" />
            <span>Ma Trận Phân Loại Món Ăn BCG (Boston Consulting Group Matrix)</span>
          </div>
          <span className="text-xs text-slate-400 font-medium">Dữ liệu 30 ngày qua</span>
        </div>

        {/* 4 Quadrants Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {/* Star (Ngôi Sao) */}
          <div className="p-4 rounded-2xl bg-amber-50/70 border border-amber-200 space-y-2">
            <div className="flex items-center justify-between">
              <span className="font-extrabold text-xs text-amber-950 uppercase tracking-wider">
                🌟 Ngôi Sao (Stars - Doanh Số Cao + Biên Lãi Cao)
              </span>
            </div>
            <div className="space-y-1.5 text-xs">
              {bcgItems
                .filter((i) => i.category === "Star")
                .map((item) => (
                  <div
                    key={item.productId}
                    className="flex justify-between bg-white p-2.5 rounded-xl border border-amber-200 shadow-2xs font-semibold"
                  >
                    <span>{item.productName}</span>
                    <span className="text-amber-900 font-bold">
                      {item.salesVolume} ly (Lãi: {item.profitMarginPercent}%)
                    </span>
                  </div>
                ))}
            </div>
          </div>

          {/* Cash Cow (Bò Sữa) */}
          <div className="p-4 rounded-2xl bg-emerald-50/70 border border-emerald-200 space-y-2">
            <div className="flex items-center justify-between">
              <span className="font-extrabold text-xs text-emerald-950 uppercase tracking-wider">
                🐄 Bò Sữa (Cash Cows - Doanh Số Rất Cao + Lợi Nhuận Ổn Định)
              </span>
            </div>
            <div className="space-y-1.5 text-xs">
              {bcgItems
                .filter((i) => i.category === "CashCow")
                .map((item) => (
                  <div
                    key={item.productId}
                    className="flex justify-between bg-white p-2.5 rounded-xl border border-emerald-200 shadow-2xs font-semibold"
                  >
                    <span>{item.productName}</span>
                    <span className="text-emerald-800 font-bold">
                      {item.salesVolume} ly (Lãi: {item.profitMarginPercent}%)
                    </span>
                  </div>
                ))}
            </div>
          </div>

          {/* Question Mark (Dấu Chấm Hỏi) */}
          <div className="p-4 rounded-2xl bg-sky-50/70 border border-sky-200 space-y-2">
            <div className="flex items-center justify-between">
              <span className="font-extrabold text-xs text-sky-950 uppercase tracking-wider">
                ❓ Dấu Chấm Hỏi (Question Marks - Tiềm Năng + Cần Đẩy Marketing)
              </span>
            </div>
            <div className="space-y-1.5 text-xs">
              {bcgItems
                .filter((i) => i.category === "QuestionMark")
                .map((item) => (
                  <div
                    key={item.productId}
                    className="flex justify-between bg-white p-2.5 rounded-xl border border-sky-200 shadow-2xs font-semibold"
                  >
                    <span>{item.productName}</span>
                    <span className="text-sky-800 font-bold">
                      {item.salesVolume} ly (Lãi: {item.profitMarginPercent}%)
                    </span>
                  </div>
                ))}
            </div>
          </div>

          {/* Dog (Chó Mực) */}
          <div className="p-4 rounded-2xl bg-slate-100 border border-slate-200 space-y-2">
            <div className="flex items-center justify-between">
              <span className="font-extrabold text-xs text-slate-700 uppercase tracking-wider">
                🐕 Chó Mực (Dogs - Doanh Số Thấp + Cần Cắt Giảm/Thay Thế)
              </span>
            </div>
            <div className="space-y-1.5 text-xs">
              {bcgItems
                .filter((i) => i.category === "Dog")
                .map((item) => (
                  <div
                    key={item.productId}
                    className="flex justify-between bg-white p-2.5 rounded-xl border border-slate-200 shadow-2xs font-semibold text-slate-600"
                  >
                    <span>{item.productName}</span>
                    <span className="text-rose-700 font-bold">
                      {item.salesVolume} ly (Lãi: {item.profitMarginPercent}%)
                    </span>
                  </div>
                ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
