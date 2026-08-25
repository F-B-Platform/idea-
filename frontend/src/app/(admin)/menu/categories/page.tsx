"use client";

import React, { useState } from "react";
import { CategoryDto } from "@/types";
import { Button } from "@/components/ui/Button";
import { Input } from "@/components/ui/Input";
import { Modal } from "@/components/ui/Modal";
import { Layers, Plus, ArrowUp, ArrowDown, Edit2, Trash2, CheckCircle2 } from "lucide-react";

const initialCategories: CategoryDto[] = [
  { id: "cat-01", name: "Cà Phê Đặc Sản", displayOrder: 1, isActive: true, itemCount: 8 },
  { id: "cat-02", name: "Trà Trái Cây", displayOrder: 2, isActive: true, itemCount: 6 },
  { id: "cat-03", name: "Trà Sữa Oolong", displayOrder: 3, isActive: true, itemCount: 5 },
  { id: "cat-04", name: "Đá Xay & Sinh Tố", displayOrder: 4, isActive: true, itemCount: 4 },
  { id: "cat-05", name: "Bánh Ngọt & Pastry", displayOrder: 5, isActive: true, itemCount: 3 },
];

export default function AdminCategoriesPage() {
  const [categories, setCategories] = useState<CategoryDto[]>(initialCategories);
  const [newCatName, setNewCatName] = useState("");
  const [toastMessage, setToastMessage] = useState<string | null>(null);

  const moveCategory = (index: number, direction: "up" | "down") => {
    const targetIndex = direction === "up" ? index - 1 : index + 1;
    if (targetIndex < 0 || targetIndex >= categories.length) return;

    const updated = [...categories];
    const temp = updated[index];
    updated[index] = updated[targetIndex];
    updated[targetIndex] = temp;

    // Re-assign display order
    const reordered = updated.map((cat, i) => ({ ...cat, displayOrder: i + 1 }));
    setCategories(reordered);
    setToastMessage("Đã cập nhật thứ tự hiển thị danh mục trên ứng dụng khách!");
    setTimeout(() => setToastMessage(null), 2500);
  };

  const handleAddCategory = () => {
    if (!newCatName.trim()) return;
    const newCat: CategoryDto = {
      id: `cat-${Date.now()}`,
      name: newCatName.trim(),
      displayOrder: categories.length + 1,
      isActive: true,
      itemCount: 0,
    };
    setCategories((prev) => [...prev, newCat]);
    setNewCatName("");
    setToastMessage("Đã tạo danh mục món mới!");
    setTimeout(() => setToastMessage(null), 2500);
  };

  const handleDelete = (id: string) => {
    setCategories((prev) => prev.filter((c) => c.id !== id));
  };

  return (
    <div className="max-w-4xl mx-auto space-y-6">
      {/* Top Header */}
      <div className="flex items-center justify-between bg-white p-5 rounded-3xl border border-slate-200 shadow-sm">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-2xl bg-amber-700 text-white flex items-center justify-center font-black shadow-sm">
            <Layers className="h-5 w-5" />
          </div>
          <div>
            <h1 className="text-lg font-black text-slate-900 leading-tight">
              Quản Trị Danh Mục & Sắp Xếp Thứ Tự
            </h1>
            <span className="text-xs text-slate-500">
              Điều chỉnh thứ tự hiển thị các tab danh mục trên PWA khách hàng và POS
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

      {/* Add Category Card */}
      <div className="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm flex gap-3 items-center">
        <Input
          placeholder="Nhập tên danh mục mới (ví dụ: Nước Ép Tươi, Bingsu)..."
          value={newCatName}
          onChange={(e) => setNewCatName(e.target.value)}
        />
        <Button
          type="button"
          onClick={handleAddCategory}
          variant="primary"
          leftIcon={<Plus className="h-4 w-4" />}
          className="shrink-0"
        >
          Thêm Danh Mục
        </Button>
      </div>

      {/* Categories Reorder List */}
      <div className="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-3">
        <h3 className="font-bold text-xs uppercase tracking-wider text-slate-500 border-b border-slate-100 pb-3">
          Danh Sách Danh Mục Hiển Thị ({categories.length})
        </h3>

        <div className="space-y-2">
          {categories.map((cat, idx) => (
            <div
              key={cat.id}
              className="p-4 rounded-2xl border border-slate-200 bg-slate-50/70 hover:bg-slate-50 flex items-center justify-between transition-colors"
            >
              <div className="flex items-center gap-4">
                <span className="w-7 h-7 rounded-lg bg-amber-100 text-amber-900 font-bold text-xs flex items-center justify-center">
                  {cat.displayOrder}
                </span>
                <div>
                  <span className="font-bold text-sm text-slate-900 block">{cat.name}</span>
                  <span className="text-xs text-slate-400">{cat.itemCount || 0} món đang bán</span>
                </div>
              </div>

              <div className="flex items-center gap-1.5">
                <button
                  type="button"
                  disabled={idx === 0}
                  onClick={() => moveCategory(idx, "up")}
                  className="p-2 rounded-lg bg-white border border-slate-200 text-slate-600 hover:text-amber-800 disabled:opacity-30"
                  title="Di chuyển lên trên"
                >
                  <ArrowUp className="h-4 w-4" />
                </button>
                <button
                  type="button"
                  disabled={idx === categories.length - 1}
                  onClick={() => moveCategory(idx, "down")}
                  className="p-2 rounded-lg bg-white border border-slate-200 text-slate-600 hover:text-amber-800 disabled:opacity-30"
                  title="Di chuyển xuống dưới"
                >
                  <ArrowDown className="h-4 w-4" />
                </button>
                <button
                  type="button"
                  onClick={() => handleDelete(cat.id)}
                  className="p-2 rounded-lg text-slate-400 hover:text-rose-600 hover:bg-rose-50 ml-2"
                >
                  <Trash2 className="h-4 w-4" />
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
