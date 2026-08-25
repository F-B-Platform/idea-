"use client";

import React, { useState } from "react";
import { Modal } from "@/components/ui/Modal";
import { Switch } from "@/components/ui/Switch";
import { SearchInput } from "@/components/ui/SearchInput";
import { AlertOctagon, RefreshCw, CheckCircle2 } from "lucide-react";
import { Product86ToggleDto } from "@/types";

export interface Emergency86ModalProps {
  isOpen: boolean;
  onClose: () => void;
  products?: Product86ToggleDto[];
  onToggleProduct?: (productId: string, isAvailable: boolean) => void;
}

const mockInitialProducts: Product86ToggleDto[] = [
  { productId: "prod-01", productName: "Cà Phê Muối Hoàng Gia", categoryName: "Cà Phê Đặc Sản", isAvailable: true },
  { productId: "prod-02", productName: "Trà Đào Cam Sả Tươi", categoryName: "Trà Trái Cây", isAvailable: true },
  { productId: "prod-03", productName: "Matcha Latte Kem Trứng", categoryName: "Đá Xay & Matcha", isAvailable: false },
  { productId: "prod-04", productName: "Trà Sữa Oolong Nướng", categoryName: "Trà Sữa", isAvailable: true },
  { productId: "prod-05", productName: "Bạc Xỉu Sữa Hạnh Nhân", categoryName: "Cà Phê Đặc Sản", isAvailable: true },
  { productId: "prod-06", productName: "Cà Phê Đen Đá Phin", categoryName: "Cà Phê Truyền Thống", isAvailable: true },
  { productId: "prod-07", productName: "Sinh Tố Bơ Sáp Dừa", categoryName: "Đá Xay & Sinh Tố", isAvailable: true },
  { productId: "prod-08", productName: "Bánh Croissant Bơ Tỏi", categoryName: "Bánh Ngọt & Pastry", isAvailable: false },
];

export const Emergency86Modal: React.FC<Emergency86ModalProps> = ({
  isOpen,
  onClose,
  products = mockInitialProducts,
  onToggleProduct,
}) => {
  const [search, setSearch] = useState("");
  const [items, setItems] = useState<Product86ToggleDto[]>(products);
  const [successMsg, setSuccessMsg] = useState<string | null>(null);

  const filteredItems = items.filter(
    (item) =>
      item.productName.toLowerCase().includes(search.toLowerCase()) ||
      item.categoryName.toLowerCase().includes(search.toLowerCase())
  );

  const handleToggle = (productId: string, isAvailable: boolean) => {
    setItems((prev) =>
      prev.map((item) => (item.productId === productId ? { ...item, isAvailable } : item))
    );

    if (onToggleProduct) {
      onToggleProduct(productId, isAvailable);
    }

    const changedItem = items.find((i) => i.productId === productId);
    setSuccessMsg(
      isAvailable
        ? `Đã mở bán lại: ${changedItem?.productName}`
        : `ĐÃ KHÓA HẾT HÀNG (86'd): ${changedItem?.productName}`
    );
    setTimeout(() => setSuccessMsg(null), 3000);
  };

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      dark
      maxWidth="2xl"
      title={
        <div className="flex items-center gap-2 text-rose-400">
          <AlertOctagon className="h-6 w-6 text-rose-500" />
          <span>Công Tắc Khẩn Cấp Khóa Hết Món (86-Toggle)</span>
        </div>
      }
      description="Gạt tắt để khóa món ngay lập tức trên Menu Khách Hàng và Web POS Quầy khi quầy bar hết nguyên liệu."
      footer={
        <button
          onClick={onClose}
          className="px-6 py-2.5 bg-slate-700 hover:bg-slate-600 text-white text-xs font-bold rounded-xl"
        >
          Xong & Đóng
        </button>
      }
    >
      <div className="space-y-4">
        {successMsg && (
          <div className="bg-emerald-950/80 border border-emerald-500 text-emerald-300 text-xs px-3.5 py-2.5 rounded-xl flex items-center gap-2 animate-in fade-in">
            <CheckCircle2 className="h-4 w-4 shrink-0" />
            <span>{successMsg}</span>
          </div>
        )}

        <SearchInput
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          onClear={() => setSearch("")}
          placeholder="Tìm món cần khóa nhanh..."
          className="bg-slate-800 border-slate-700 text-white placeholder:text-slate-400"
        />

        <div className="space-y-2 max-h-[380px] overflow-y-auto pr-1">
          {filteredItems.map((item) => (
            <div
              key={item.productId}
              className="flex items-center justify-between p-3.5 rounded-xl bg-slate-800/70 border border-slate-700 hover:border-slate-600 transition-colors"
            >
              <div>
                <span className="font-bold text-sm text-white block">{item.productName}</span>
                <span className="text-xs text-slate-400">{item.categoryName}</span>
              </div>

              <div className="flex items-center gap-3">
                <span
                  className={`text-xs font-bold ${
                    item.isAvailable ? "text-emerald-400" : "text-rose-400"
                  }`}
                >
                  {item.isAvailable ? "ĐANG BÁN" : "HẾT HÀNG (86)"}
                </span>
                <Switch
                  checked={item.isAvailable}
                  onCheckedChange={(checked) => handleToggle(item.productId, checked)}
                />
              </div>
            </div>
          ))}
        </div>
      </div>
    </Modal>
  );
};
