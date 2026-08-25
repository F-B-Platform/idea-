"use client";

import React from "react";
import { Modal } from "@/components/ui/Modal";
import { KdsTicketDto } from "@/types";
import { Beaker, Coffee, Info } from "lucide-react";

export interface BomRecipeModalProps {
  isOpen: boolean;
  onClose: () => void;
  ticket: KdsTicketDto | null;
}

export const BomRecipeModal: React.FC<BomRecipeModalProps> = ({
  isOpen,
  onClose,
  ticket,
}) => {
  if (!ticket) return null;

  // Mock standard BOM recipes for display in Barista view
  const getMockBomIngredients = (productName: string, sizeName: string) => {
    const sizeMultiplier = sizeName === "L" ? 1.4 : sizeName === "S" ? 0.8 : 1.0;
    if (productName.toLowerCase().includes("cà phê") || productName.toLowerCase().includes("espresso")) {
      return [
        { name: "Cốt Cà Phê Robusta/Arabica", quantity: Math.round(45 * sizeMultiplier), unit: "ml" },
        { name: "Sữa đặc có đường", quantity: Math.round(25 * sizeMultiplier), unit: "ml" },
        { name: "Sữa tươi thanh trùng", quantity: Math.round(60 * sizeMultiplier), unit: "ml" },
        { name: "Đá viên sạch", quantity: Math.round(180 * sizeMultiplier), unit: "g" },
      ];
    }
    if (productName.toLowerCase().includes("trà sữa") || productName.toLowerCase().includes("trà")) {
      return [
        { name: "Cốt Trà Đen / Oolong ủ lạnh", quantity: Math.round(120 * sizeMultiplier), unit: "ml" },
        { name: "Bột sữa béo thực vật", quantity: Math.round(30 * sizeMultiplier), unit: "g" },
        { name: "Nước đường Fructose", quantity: Math.round(20 * sizeMultiplier), unit: "ml" },
        { name: "Trân châu hoàng kim", quantity: Math.round(50 * sizeMultiplier), unit: "g" },
      ];
    }
    return [
      { name: "Cốt Trà Trái Cây", quantity: Math.round(100 * sizeMultiplier), unit: "ml" },
      { name: "Mứt quả tươi / Puree", quantity: Math.round(35 * sizeMultiplier), unit: "g" },
      { name: "Nước cốt chanh tươi", quantity: Math.round(10 * sizeMultiplier), unit: "ml" },
      { name: "Đá viên sạch", quantity: Math.round(200 * sizeMultiplier), unit: "g" },
    ];
  };

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      dark
      title={
        <div className="flex items-center gap-2 text-amber-400">
          <Beaker className="h-5 w-5" />
          <span>Công Thức BOM Định Lượng — #{ticket.orderNumber || ticket.orderCode}</span>
        </div>
      }
      description="Chi tiết thành phần nguyên vật liệu chính xác theo từng kích cỡ để Barista pha chế đồng bộ."
      footer={
        <button
          onClick={onClose}
          className="px-5 py-2.5 bg-slate-700 hover:bg-slate-600 text-white text-xs font-bold rounded-xl"
        >
          Đóng Cửa Sổ
        </button>
      }
    >
      <div className="space-y-6">
        {ticket.items.map((item, idx) => {
          const bomList = item.bomIngredients || getMockBomIngredients(item.productName, item.sizeName);

          return (
            <div key={idx} className="bg-slate-800/80 rounded-xl p-4 border border-slate-700 space-y-3">
              <div className="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <div className="flex items-center gap-2">
                  <Coffee className="h-4 w-4 text-amber-400" />
                  <span className="font-bold text-sm text-white">
                    {item.quantity}x {item.productName}
                  </span>
                </div>
                <span className="text-xs font-bold text-amber-300 bg-amber-950/60 px-2 py-0.5 rounded border border-amber-800">
                  Size {item.sizeName}
                </span>
              </div>

              {/* Ingredients Table */}
              <div className="space-y-1.5">
                <div className="text-[11px] font-semibold text-slate-400 uppercase grid grid-cols-12 px-2">
                  <span className="col-span-8">Nguyên Liệu</span>
                  <span className="col-span-4 text-right">Định Lượng / 1 Ly</span>
                </div>
                <div className="space-y-1 divide-y divide-slate-700/30">
                  {bomList.map((ing, iIdx) => (
                    <div key={iIdx} className="grid grid-cols-12 px-2 py-1 text-xs text-slate-200">
                      <span className="col-span-8 font-medium">{ing.name}</span>
                      <span className="col-span-4 text-right font-bold text-amber-300">
                        {ing.quantity * item.quantity} {ing.unit}
                      </span>
                    </div>
                  ))}
                </div>
              </div>

              {/* Modifiers Notes */}
              {(item.sugarLevel || item.iceLevel) && (
                <div className="text-[11px] text-slate-400 bg-slate-900/60 p-2 rounded flex items-center gap-2">
                  <Info className="h-3.5 w-3.5 text-sky-400 shrink-0" />
                  <span>Điều chỉnh độ ngọt: {item.sugarLevel || "100%"} • Độ đá: {item.iceLevel || "100%"}</span>
                </div>
              )}
            </div>
          );
        })}
      </div>
    </Modal>
  );
};
