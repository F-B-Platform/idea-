"use client";

import React from "react";
import { ProductDto, PriceGroupDto } from "@/types";
import { formatCurrencyVND } from "@/lib/utils";
import { Table, TableHeader, TableBody, TableRow, TableHead, TableCell } from "@/components/ui/Table";

export interface PricingMatrixTableProps {
  products: ProductDto[];
  priceGroups: PriceGroupDto[];
  onMultiplierChange?: (groupId: string, multiplier: number) => void;
}

export const PricingMatrixTable: React.FC<PricingMatrixTableProps> = ({
  products,
  priceGroups,
  onMultiplierChange,
}) => {
  return (
    <div className="space-y-4">
      {/* Region Groups Multipliers Top Bar */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
        {priceGroups.map((group) => (
          <div
            key={group.id}
            className="p-3.5 rounded-xl border border-slate-200 bg-white shadow-sm space-y-1.5"
          >
            <div className="flex items-center justify-between">
              <span className="font-bold text-xs text-slate-800">{group.name}</span>
              <span className="text-[10px] font-semibold text-slate-500 font-mono">
                {group.regionCode}
              </span>
            </div>
            <div className="flex items-center gap-2">
              <span className="text-xs text-slate-500">Hệ số giá:</span>
              <span className="font-extrabold text-amber-800 text-sm">
                x{group.priceMultiplier.toFixed(2)}
              </span>
              <span className="text-[10px] text-slate-400">
                ({group.priceMultiplier > 1 ? `+${Math.round((group.priceMultiplier - 1) * 100)}%` : "Giá Gốc"})
              </span>
            </div>
          </div>
        ))}
      </div>

      {/* Regional Matrix Table */}
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Món Ăn / Đồ Uống</TableHead>
            <TableHead>Danh Mục</TableHead>
            <TableHead className="text-right">Giá Gốc (Hồ Chí Minh)</TableHead>
            {priceGroups.map((group) => (
              <TableHead key={group.id} className="text-right">
                {group.name} (x{group.priceMultiplier})
              </TableHead>
            ))}
          </TableRow>
        </TableHeader>
        <TableBody>
          {products.map((product) => (
            <TableRow key={product.id}>
              <TableCell className="font-bold text-slate-900">{product.name}</TableCell>
              <TableCell className="text-xs text-slate-500">{product.categoryName || "Đồ Uống"}</TableCell>
              <TableCell className="text-right font-mono font-semibold text-slate-700">
                {formatCurrencyVND(product.basePrice)}
              </TableCell>
              {priceGroups.map((group) => {
                const adjustedPrice = Math.round((product.basePrice * group.priceMultiplier) / 1000) * 1000;
                return (
                  <TableCell key={group.id} className="text-right font-mono font-bold text-amber-900">
                    {formatCurrencyVND(adjustedPrice)}
                  </TableCell>
                );
              })}
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  );
};
