"use client";

import React, { useState } from "react";
import { ProductDto, ProductBOMItemDto } from "@/types";
import { formatCurrencyVND } from "@/lib/utils";
import { Button } from "@/components/ui/Button";
import { Modal } from "@/components/ui/Modal";
import { Input } from "@/components/ui/Input";
import { Textarea } from "@/components/ui/Textarea";
import { SearchInput } from "@/components/ui/SearchInput";
import { Table, TableHeader, TableBody, TableRow, TableHead, TableCell } from "@/components/ui/Table";
import {
  UtensilsCrossed,
  Plus,
  Edit2,
  Trash2,
  Beaker,
  RefreshCw,
  CheckCircle2,
  Upload,
} from "lucide-react";

const initialAdminProducts: ProductDto[] = [
  {
    id: "prod-01",
    sku: "CF-SALT-01",
    name: "Cà Phê Muối Hoàng Gia",
    description: "Cà phê Robusta Đắk Lắk đậm đà hòa quyện kem muối béo ngậy.",
    basePrice: 35000,
    imageUrl: "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=400&q=80",
    categoryId: "cat-01",
    categoryName: "Cà Phê Đặc Sản",
    isAvailable: true,
    sizes: [
      { id: "s-01", sizeName: "S", price: 32000, isDefault: false },
      { id: "s-02", sizeName: "M", price: 35000, isDefault: true },
      { id: "s-03", sizeName: "L", price: 42000, isDefault: false },
    ],
    modifiers: [
      { id: "mod-01", name: "Thêm Shot Espresso", priceAdjustment: 10000, isDefault: false },
      { id: "mod-02", name: "Thêm Kem Muối Béo", priceAdjustment: 8000, isDefault: false },
    ],
  },
  {
    id: "prod-02",
    sku: "TEA-PEACH-02",
    name: "Trà Đào Cam Sả Tươi",
    description: "Trà đen ủ lạnh cao cấp kết hợp đào miếng giòn và sả tươi.",
    basePrice: 39000,
    imageUrl: "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=400&q=80",
    categoryId: "cat-02",
    categoryName: "Trà Trái Cây",
    isAvailable: true,
    sizes: [
      { id: "s-04", sizeName: "M", price: 39000, isDefault: true },
      { id: "s-05", sizeName: "L", price: 45000, isDefault: false },
    ],
    modifiers: [
      { id: "mod-03", name: "Thêm Đào Miếng Giòn", priceAdjustment: 10000, isDefault: false },
    ],
  },
  {
    id: "prod-03",
    sku: "MILKTEA-OOLONG-03",
    name: "Trà Sữa Oolong Nướng",
    description: "Trà Oolong nướng thơm đượm khói than và sữa tươi.",
    basePrice: 42000,
    imageUrl: "https://images.unsplash.com/photo-1558857563-b37cf05d8a58?w=400&q=80",
    categoryId: "cat-03",
    categoryName: "Trà Sữa Oolong",
    isAvailable: true,
    sizes: [
      { id: "s-06", sizeName: "M", price: 42000, isDefault: true },
      { id: "s-07", sizeName: "L", price: 49000, isDefault: false },
    ],
    modifiers: [
      { id: "mod-05", name: "Trân Châu Hoàng Kim", priceAdjustment: 8000, isDefault: false },
    ],
  },
];

export default function AdminProductsPage() {
  const [products, setProducts] = useState<ProductDto[]>(initialAdminProducts);
  const [search, setSearch] = useState("");
  const [editingProduct, setEditingProduct] = useState<ProductDto | null>(null);
  const [showBomModal, setShowBomModal] = useState<ProductDto | null>(null);
  const [toastMessage, setToastMessage] = useState<string | null>(null);

  const filtered = products.filter(
    (p) =>
      p.name.toLowerCase().includes(search.toLowerCase()) ||
      p.sku.toLowerCase().includes(search.toLowerCase())
  );

  const handleSaveProduct = (e: React.FormEvent) => {
    e.preventDefault();
    if (!editingProduct) return;

    if (products.some((p) => p.id === editingProduct.id)) {
      setProducts((prev) =>
        prev.map((p) => (p.id === editingProduct.id ? editingProduct : p))
      );
      setToastMessage("Đã cập nhật thông tin món ăn thành công!");
    } else {
      setProducts((prev) => [...prev, editingProduct]);
      setToastMessage("Đã thêm món ăn mới vào thực đơn toàn chuỗi!");
    }

    setEditingProduct(null);
    setTimeout(() => setToastMessage(null), 3000);
  };

  const handleDelete = (id: string) => {
    if (confirm("Bạn có chắc chắn muốn xóa món này khỏi thực đơn toàn chuỗi?")) {
      setProducts((prev) => prev.filter((p) => p.id !== id));
      setToastMessage("Đã xóa món ăn thành công!");
      setTimeout(() => setToastMessage(null), 3000);
    }
  };

  return (
    <div className="max-w-7xl mx-auto space-y-6">
      {/* Top Header */}
      <div className="flex items-center justify-between bg-white p-5 rounded-3xl border border-slate-200 shadow-sm">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-2xl bg-amber-700 text-white flex items-center justify-center font-black shadow-sm">
            <UtensilsCrossed className="h-5 w-5" />
          </div>
          <div>
            <h1 className="text-lg font-black text-slate-900 leading-tight">
              Quản Trị Thực Đơn & Định Mức BOM Từng Size
            </h1>
            <span className="text-xs text-slate-500">
              Quản lý danh mục món, kích cỡ S/M/L, định lượng nguyên vật liệu và thay thế món
            </span>
          </div>
        </div>

        <Button
          type="button"
          onClick={() =>
            setEditingProduct({
              id: `prod-${Date.now()}`,
              sku: `PROD-${Math.floor(100 + Math.random() * 900)}`,
              name: "",
              description: "",
              basePrice: 35000,
              categoryId: "cat-01",
              categoryName: "Cà Phê Đặc Sản",
              isAvailable: true,
              sizes: [
                { id: `s-m-${Date.now()}`, sizeName: "M", price: 35000, isDefault: true },
                { id: `s-l-${Date.now()}`, sizeName: "L", price: 42000, isDefault: false },
              ],
              modifiers: [],
            })
          }
          variant="primary"
          size="sm"
          leftIcon={<Plus className="h-4 w-4" />}
        >
          Thêm Món Mới
        </Button>
      </div>

      {toastMessage && (
        <div className="p-4 bg-emerald-50 border border-emerald-300 text-emerald-900 text-xs font-bold rounded-2xl flex items-center gap-2 animate-in fade-in">
          <CheckCircle2 className="h-5 w-5 text-emerald-600 shrink-0" />
          <span>{toastMessage}</span>
        </div>
      )}

      {/* Search Bar */}
      <SearchInput
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        onClear={() => setSearch("")}
        placeholder="Tìm kiếm theo tên món hoặc mã SKU..."
      />

      {/* Products Table */}
      <div className="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Mã SKU</TableHead>
              <TableHead>Tên Món</TableHead>
              <TableHead>Danh Mục</TableHead>
              <TableHead className="text-right">Giá Cơ Bản (M)</TableHead>
              <TableHead className="text-center">Kích Cỡ</TableHead>
              <TableHead className="text-center">BOM Recipe</TableHead>
              <TableHead className="text-right">Thao Tác</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {filtered.map((p) => (
              <TableRow key={p.id}>
                <TableCell className="font-mono text-xs font-bold text-slate-500">
                  {p.sku}
                </TableCell>
                <TableCell className="font-bold text-slate-900">{p.name}</TableCell>
                <TableCell className="text-xs text-slate-600">{p.categoryName}</TableCell>
                <TableCell className="text-right font-mono font-bold text-amber-900">
                  {formatCurrencyVND(p.basePrice)}
                </TableCell>
                <TableCell className="text-center">
                  <div className="flex justify-center gap-1">
                    {p.sizes.map((s) => (
                      <span
                        key={s.id}
                        className="text-[10px] bg-slate-100 border border-slate-200 px-1.5 py-0.5 rounded font-bold"
                      >
                        {s.sizeName}
                      </span>
                    ))}
                  </div>
                </TableCell>
                <TableCell className="text-center">
                  <button
                    type="button"
                    onClick={() => setShowBomModal(p)}
                    className="inline-flex items-center gap-1 text-xs font-bold text-amber-800 hover:text-amber-950 bg-amber-50 hover:bg-amber-100 px-2.5 py-1 rounded-lg border border-amber-200"
                  >
                    <Beaker className="h-3.5 w-3.5" />
                    <span>Xem BOM</span>
                  </button>
                </TableCell>
                <TableCell className="text-right">
                  <div className="flex justify-end gap-2">
                    <button
                      type="button"
                      onClick={() => setEditingProduct(p)}
                      className="p-1.5 text-slate-500 hover:text-amber-800 rounded-lg hover:bg-slate-100"
                    >
                      <Edit2 className="h-4 w-4" />
                    </button>
                    <button
                      type="button"
                      onClick={() => handleDelete(p.id)}
                      className="p-1.5 text-slate-500 hover:text-rose-600 rounded-lg hover:bg-rose-50"
                    >
                      <Trash2 className="h-4 w-4" />
                    </button>
                  </div>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>

      {/* Edit / Create Product Modal */}
      <Modal
        isOpen={!!editingProduct}
        onClose={() => setEditingProduct(null)}
        maxWidth="lg"
        title={editingProduct?.id && products.some((p) => p.id === editingProduct.id) ? "Chỉnh Sửa Món Ăn" : "Thêm Món Mới"}
        footer={
          <div className="flex justify-end gap-2">
            <Button variant="secondary" onClick={() => setEditingProduct(null)}>
              Hủy
            </Button>
            <Button variant="primary" onClick={handleSaveProduct}>
              Lưu Món Ăn
            </Button>
          </div>
        }
      >
        {editingProduct && (
          <form onSubmit={handleSaveProduct} className="space-y-4 text-xs">
            <div className="grid grid-cols-2 gap-3">
              <Input
                label="Mã SKU"
                required
                value={editingProduct.sku}
                onChange={(e) =>
                  setEditingProduct({ ...editingProduct, sku: e.target.value })
                }
              />
              <Input
                label="Tên Món Ăn / Đồ Uống"
                required
                value={editingProduct.name}
                onChange={(e) =>
                  setEditingProduct({ ...editingProduct, name: e.target.value })
                }
              />
            </div>

            <Textarea
              label="Mô tả món ăn"
              value={editingProduct.description || ""}
              onChange={(e) =>
                setEditingProduct({ ...editingProduct, description: e.target.value })
              }
              rows={2}
            />

            <div className="grid grid-cols-2 gap-3">
              <Input
                label="Giá Bán Cơ Bản (Size M - ₫)"
                type="number"
                value={editingProduct.basePrice}
                onChange={(e) =>
                  setEditingProduct({
                    ...editingProduct,
                    basePrice: Number(e.target.value) || 0,
                  })
                }
              />
              <Input
                label="URL Hình Ảnh WebP"
                value={editingProduct.imageUrl || ""}
                onChange={(e) =>
                  setEditingProduct({ ...editingProduct, imageUrl: e.target.value })
                }
              />
            </div>
          </form>
        )}
      </Modal>

      {/* BOM Formula Details Modal */}
      <Modal
        isOpen={!!showBomModal}
        onClose={() => setShowBomModal(null)}
        maxWidth="md"
        title={showBomModal ? `Định Mức BOM — ${showBomModal.name}` : ""}
        footer={
          <Button variant="secondary" onClick={() => setShowBomModal(null)}>
            Đóng
          </Button>
        }
      >
        {showBomModal && (
          <div className="space-y-3 text-xs">
            <p className="text-slate-500">
              Công thức tiêu chuẩn được hệ thống tự động trừ kho mỗi khi Barista bấm [HOÀN TẤT].
            </p>
            <div className="p-3 bg-slate-50 rounded-xl border border-slate-200 space-y-2">
              <div className="flex justify-between font-semibold">
                <span>Cốt Cà Phê Robusta:</span>
                <strong className="text-amber-900">45 ml</strong>
              </div>
              <div className="flex justify-between font-semibold">
                <span>Sữa Đặc Có Đường:</span>
                <strong className="text-amber-900">25 ml</strong>
              </div>
              <div className="flex justify-between font-semibold">
                <span>Kem Muối Béo:</span>
                <strong className="text-amber-900">30 ml</strong>
              </div>
            </div>
          </div>
        )}
      </Modal>
    </div>
  );
}
