"use client";

import React from "react";
import { PlSummaryDto } from "@/types";
import { formatCurrencyVND } from "@/lib/utils";
import { TrendingUp, DollarSign, PieChart, Building2 } from "lucide-react";

export interface PlSummaryCardProps {
  summary: PlSummaryDto;
}

export const PlSummaryCard: React.FC<PlSummaryCardProps> = ({ summary }) => {
  return (
    <div className="space-y-6">
      {/* 4 Core Financial KPI Tiles */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        {/* Total Revenue */}
        <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-2">
          <div className="flex items-center justify-between text-slate-500">
            <span className="text-xs font-semibold uppercase tracking-wider">Doanh Thu Thuần</span>
            <DollarSign className="h-4 w-4 text-amber-700" />
          </div>
          <div className="font-extrabold text-2xl text-slate-900">
            {formatCurrencyVND(summary.totalRevenue)}
          </div>
          <span className="text-xs text-emerald-600 font-medium">+14.2% so với tháng trước</span>
        </div>

        {/* COGS (BOM Cost) */}
        <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-2">
          <div className="flex items-center justify-between text-slate-500">
            <span className="text-xs font-semibold uppercase tracking-wider">Giá Vốn BOM (COGS)</span>
            <PieChart className="h-4 w-4 text-slate-400" />
          </div>
          <div className="font-extrabold text-2xl text-slate-700">
            {formatCurrencyVND(summary.cogsAmount)}
          </div>
          <span className="text-xs text-slate-500 font-medium">
            Tỷ lệ COGS: {((summary.cogsAmount / (summary.totalRevenue || 1)) * 100).toFixed(1)}%
          </span>
        </div>

        {/* Gross Profit */}
        <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-2">
          <div className="flex items-center justify-between text-slate-500">
            <span className="text-xs font-semibold uppercase tracking-wider">Lãi Gộp (Gross)</span>
            <TrendingUp className="h-4 w-4 text-emerald-600" />
          </div>
          <div className="font-extrabold text-2xl text-emerald-700">
            {formatCurrencyVND(summary.grossProfit)}
          </div>
          <span className="text-xs text-emerald-700 font-bold bg-emerald-50 px-2 py-0.5 rounded-full inline-block">
            Biên Lãi Gộp: {summary.grossMarginPercent}%
          </span>
        </div>

        {/* Net Profit */}
        <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-2">
          <div className="flex items-center justify-between text-slate-500">
            <span className="text-xs font-semibold uppercase tracking-wider">Lãi Ròng (Net P&L)</span>
            <TrendingUp className="h-4 w-4 text-amber-700" />
          </div>
          <div className="font-extrabold text-2xl text-amber-900">
            {formatCurrencyVND(summary.netProfit)}
          </div>
          <span className="text-xs text-amber-800 font-bold bg-amber-100 px-2 py-0.5 rounded-full inline-block">
            Biên Ròng: {summary.netMarginPercent}%
          </span>
        </div>
      </div>

      {/* Multi-Branch Breakdown Table */}
      <div className="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm space-y-4">
        <div className="flex items-center gap-2 border-b border-slate-100 pb-3">
          <Building2 className="h-5 w-5 text-amber-700" />
          <h4 className="font-bold text-sm text-slate-900">
            Phân Rã P&L Hợp Nhất Theo Từng Chi Nhánh
          </h4>
        </div>

        <div className="space-y-3">
          {summary.branchesBreakdown.map((branch) => {
            const margin = Math.round((branch.profit / (branch.revenue || 1)) * 100);
            return (
              <div
                key={branch.branchId}
                className="p-4 rounded-xl border border-slate-200 bg-slate-50/50 flex flex-col sm:flex-row sm:items-center justify-between gap-3"
              >
                <div>
                  <span className="font-bold text-sm text-slate-900 block">{branch.branchName}</span>
                  <span className="text-xs text-slate-500 font-medium">
                    Giá vốn BOM: {formatCurrencyVND(branch.cogs)}
                  </span>
                </div>

                <div className="flex items-center gap-6">
                  <div className="text-right">
                    <span className="text-xs text-slate-400 block">Doanh Thu</span>
                    <span className="font-bold text-sm text-slate-800">
                      {formatCurrencyVND(branch.revenue)}
                    </span>
                  </div>

                  <div className="text-right">
                    <span className="text-xs text-slate-400 block">Lợi Nhuận Thuần</span>
                    <span className="font-bold text-sm text-emerald-700">
                      {formatCurrencyVND(branch.profit)}
                    </span>
                  </div>

                  <span className="text-xs font-bold bg-emerald-100 text-emerald-800 px-2.5 py-1 rounded-lg">
                    {margin}% Lãi
                  </span>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};
