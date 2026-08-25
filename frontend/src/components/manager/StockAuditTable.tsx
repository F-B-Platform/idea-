"use client";

import React from "react";
import { StockAuditItemDto } from "@/types";
import { formatCurrencyVND } from "@/lib/utils";
import { Table, TableHeader, TableBody, TableRow, TableHead, TableCell } from "@/components/ui/Table";
import { Badge } from "@/components/ui/Badge";
import { AlertTriangle, CheckCircle2 } from "lucide-react";

export interface StockAuditTableProps {
  items: StockAuditItemDto[];
  onPhysicalStockChange?: (ingredientId: string, physicalCount: number) => void;
  readOnly?: boolean;
}

export const StockAuditTable: React.FC<StockAuditTableProps> = ({
  items,
  onPhysicalStockChange,
  readOnly = false,
}) => {
  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead>Mã</TableHead>
          <TableHead>Nguyên Vật Liệu</TableHead>
          <TableHead>Đơn Vị</TableHead>
          <TableHead className="text-right">Tồn Lý Thuyết (BOM)</TableHead>
          <TableHead className="text-right">Thực Đếm</TableHead>
          <TableHead className="text-right">Hao Hụt / Chênh Lệch</TableHead>
          <TableHead className="text-right">% Hao Hụt</TableHead>
          <TableHead className="text-center">Trạng Thái Đối Soát</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        {items.map((item) => {
          const isHighWastage = item.wastagePercent > 3.0 || item.isDiscrepancySevere;

          return (
            <TableRow key={item.ingredientId} className={isHighWastage ? "bg-rose-50/40" : ""}>
              <TableCell className="font-mono text-xs font-semibold text-slate-500">
                {item.ingredientCode}
              </TableCell>
              <TableCell className="font-bold text-slate-900">{item.ingredientName}</TableCell>
              <TableCell className="text-slate-600">{item.unit}</TableCell>
              <TableCell className="text-right font-mono font-semibold text-slate-700">
                {item.theoreticalStock}
              </TableCell>
              <TableCell className="text-right">
                {readOnly ? (
                  <span className="font-mono font-bold text-slate-900">{item.physicalStock}</span>
                ) : (
                  <input
                    type="number"
                    min="0"
                    step="0.1"
                    value={item.physicalStock}
                    onChange={(e) =>
                      onPhysicalStockChange &&
                      onPhysicalStockChange(item.ingredientId, Number(e.target.value) || 0)
                    }
                    className="w-24 px-2.5 py-1.5 text-right font-mono font-bold text-xs rounded border border-slate-300 focus:outline-none focus:ring-2 focus:ring-amber-600"
                  />
                )}
              </TableCell>
              <TableCell
                className={`text-right font-mono font-bold ${
                  item.variance < 0 ? "text-rose-600" : "text-emerald-600"
                }`}
              >
                {item.variance > 0 ? "+" : ""}
                {item.variance} {item.unit}
              </TableCell>
              <TableCell
                className={`text-right font-mono font-bold ${
                  isHighWastage ? "text-rose-600" : "text-slate-700"
                }`}
              >
                {item.wastagePercent.toFixed(1)}%
              </TableCell>
              <TableCell className="text-center">
                {isHighWastage ? (
                  <Badge variant="danger" size="sm" className="gap-1">
                    <AlertTriangle className="h-3 w-3" />
                    <span>Lệch &gt; 3%</span>
                  </Badge>
                ) : (
                  <Badge variant="success" size="sm" className="gap-1">
                    <CheckCircle2 className="h-3 w-3" />
                    <span>Chuẩn BOM</span>
                  </Badge>
                )}
              </TableCell>
            </TableRow>
          );
        })}
      </TableBody>
    </Table>
  );
};
