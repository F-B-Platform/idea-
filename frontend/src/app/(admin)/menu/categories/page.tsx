"use client";

import { FolderTree, Plus } from "lucide-react";

export default function AdminCategoriesPage() {
  const categories = [
    { name: "Cà Phê", count: 6, sortOrder: 1 },
    { name: "Trà Trái Cây", count: 5, sortOrder: 2 },
    { name: "Trà Sữa", count: 4, sortOrder: 3 },
    { name: "Đá Xay & Sinh Tố", count: 3, sortOrder: 4 },
  ];

  return (
    <div className="p-6 max-w-5xl mx-auto space-y-6">
      <header className="flex justify-between items-center">
        <div>
          <h1 className="text-xl font-bold text-slate-900 flex items-center gap-2">
            <FolderTree className="w-5 h-5 text-rose-600" /> Quản Lý Nhóm Danh Mục
          </h1>
          <p className="text-xs text-slate-500">Phân loại hiển thị món trên Menu PWA và Web POS.</p>
        </div>
        <button className="px-3 py-2 rounded-xl bg-rose-600 hover:bg-rose-700 text-white font-bold text-xs flex items-center gap-1.5 shadow">
          <Plus className="w-4 h-4" /> Thêm Danh Mục
        </button>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {categories.map((c, idx) => (
          <div key={idx} className="p-4 bg-white rounded-2xl border border-slate-200 shadow-sm flex justify-between items-center">
            <div>
              <h2 className="text-sm font-bold text-slate-900">{c.name}</h2>
              <p className="text-xs text-slate-500">{c.count} món đồ uống</p>
            </div>
            <span className="text-xs font-mono px-2 py-1 bg-slate-100 rounded text-slate-600">Thứ tự: {c.sortOrder}</span>
          </div>
        ))}
      </div>
    </div>
  );
}
