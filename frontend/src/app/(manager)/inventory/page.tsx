"use client";

import React, { useState } from "react";
import { StockAuditItemDto } from "@/types";
import { StockAuditTable } from "@/components/manager/StockAuditTable";
import { Button } from "@/components/ui/Button";
import { Modal } from "@/components/ui/Modal";
import { Input } from "@/components/ui/Input";
import {
  Package,
  Plus,
  ArrowRightLeft,
  FileCheck,
  Upload,
  AlertTriangle,
  CheckCircle2,
} from "lucide-react";

const initialStockItems: StockAuditItemDto[] = [
  {
    ingredientId: "ing-01",
    ingredientCode: "ING-CF-01",
    ingredientName: "Hạt Cà Phê Robusta Đắk Lắk",
    unit: "kg",
    theoreticalStock: 18.5,
    physicalStock: 18.2,
    variance: -0.3,
    wastagePercent: 1.6,
    costPerUnit: 180000,
    varianceCost: 54000,
    isDiscrepancySevere: false,
  },
  {
    ingredientId: "ing-02",
    ingredientCode: "ING-MILK-02",
    ingredientName: "Sữa Tươi Thanh Trùng 1L",
    unit: "hộp",
    theoreticalStock: 40.0,
    physicalStock: 37.0,
    variance: -3.0,
    wastagePercent: 7.5, // > 3% Alert
    costPerUnit: 35000,
    varianceCost: 105000,
    isDiscrepancySevere: true,
  },
  {
    ingredientId: "ing-03",
    ingredientCode: "ING-SUGAR-03",
    ingredientName: "Nước Đường Fructose Tinh Khiết",
    unit: "lít",
    theoreticalStock: 25.0,
    physicalStock: 24.8,
    variance: -0.2,
    wastagePercent: 0.8,
    costPerUnit: 25000,
    varianceCost: 5000,
    isDiscrepancySevere: false,
  },
  {
    ingredientId: "ing-04",
    ingredientCode: "ING-PEACH-04",
    ingredientName: "Đào Ngâm Miếng Đóng Hộp",
    unit: "hộp",
    theoreticalStock: 15.0,
    physicalStock: 14.0,
    variance: -1.0,
    wastagePercent: 6.7, // > 3% Alert
    costPerUnit: 42000,
    varianceCost: 42000,
    isDiscrepancySevere: true,
  },
];

export default function ManagerInventoryPage() {
  const [stockItems, setStockItems] = useState<StockAuditItemDto[]>(initialStockItems);
  const [showGoodsReceiptModal, setShowGoodsReceiptModal] = useState(false);
  const [showTransferModal, setShowTransferModal] = useState(false);
  const [supplierName, setSupplierName] = useState("");
  const [invoiceNumber, setInvoiceNumber] = useState("");
  const [successToast, setSuccessToast] = useState<string | null>(null);

  const handlePhysicalCountChange = (ingredientId: string, count: number) => {
    setStockItems((prev) =>
      prev.map((item) => {
        if (item.ingredientId === ingredientId) {
          const variance = count - item.theoreticalStock;
          const wastage =
            item.theoreticalStock > 0
              ? Math.abs((variance / item.theoreticalStock) * 100)
              : 0;
          return {
            ...item,
            physicalStock: count,
            variance: Number(variance.toFixed(2)),
            wastagePercent: Number(wastage.toFixed(1)),
            isDiscrepancySevere: wastage > 3.0,
          };
        }
        return item;
      })
    );
  };

  const handleSaveReceipt = () => {
    setShowGoodsReceiptModal(false);
    setSuccessToast("Đã lập phiếu nhập kho nhà cung cấp thành công!");
    setTimeout(() => setSuccessToast(null), 3000);
  };

  const handleSaveTransfer = () => {
    setShowTransferModal(false);
    setSuccessToast("Đã lập phiếu xuất kho tổng ra quầy bar thành công!");
    setTimeout(() => setSuccessToast(null), 3000);
  };

  return (
    <div className="max-w-7xl mx-auto space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between bg-white p-5 rounded-3xl border border-slate-200 shadow-sm">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-2xl bg-amber-700 text-white flex items-center justify-center font-black shadow-sm">
            <Package className="h-5 w-5" />
          </div>
          <div>
            <h1 className="text-lg font-black text-slate-900 leading-tight">
              Quản Lý Kho Định Mức BOM & Kiểm Kê Hao Hụt
            </h1>
            <span className="text-xs text-slate-500">
              Đối soát tồn kho lý thuyết (trừ tự động qua BOM) vs Thực đếm quầy Bar
            </span>
          </div>
        </div>

        <div className="flex items-center gap-2">
          <Button
            type="button"
            variant="secondary"
            size="sm"
            onClick={() => setShowTransferModal(true)}
            leftIcon={<ArrowRightLeft className="h-4 w-4" />}
          >
            Xuất Kho Ra Bar
          </Button>

          <Button
            type="button"
            variant="primary"
            size="sm"
            onClick={() => setShowGoodsReceiptModal(true)}
            leftIcon={<Plus className="h-4 w-4" />}
          >
            Nhập Kho NCC
          </Button>
        </div>
      </div>

      {successToast && (
        <div className="p-4 bg-emerald-50 border border-emerald-300 text-emerald-900 text-xs font-bold rounded-2xl flex items-center gap-2 animate-in fade-in">
          <CheckCircle2 className="h-5 w-5 text-emerald-600 shrink-0" />
          <span>{successToast}</span>
        </div>
      )}

      {/* Stock Audit Table */}
      <div className="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4">
        <div className="flex items-center justify-between border-b border-slate-100 pb-3">
          <h3 className="font-bold text-sm text-slate-900">
            Bảng Kiểm Kê & Báo Cáo Tỷ Lệ Hao Hụt Định Mức
          </h3>
          <span className="text-xs text-amber-800 bg-amber-50 px-3 py-1 rounded-full font-bold border border-amber-200">
            Cảnh báo vàng/đỏ khi hao hụt &gt; 3.0%
          </span>
        </div>

        <StockAuditTable
          items={stockItems}
          onPhysicalStockChange={handlePhysicalCountChange}
        />
      </div>

      {/* Supplier Goods Receipt Modal */}
      <Modal
        isOpen={showGoodsReceiptModal}
        onClose={() => setShowGoodsReceiptModal(false)}
        maxWidth="lg"
        title="Lập Phiếu Nhập Kho Từ Nhà Cung Cấp"
        footer={
          <div className="flex justify-end gap-2">
            <Button variant="secondary" onClick={() => setShowGoodsReceiptModal(false)}>
              Hủy
            </Button>
            <Button variant="primary" onClick={handleSaveReceipt}>
              Lưu Phiếu Nhập
            </Button>
          </div>
        }
      >
        <div className="space-y-4">
          <Input
            label="Tên Nhà Cung Cấp"
            placeholder="Ví dụ: Công ty CP Cà Phê Trung Nguyên"
            value={supplierName}
            onChange={(e) => setSupplierName(e.target.value)}
          />
          <Input
            label="Số Hóa Đơn Chứng Từ"
            placeholder="Ví dụ: HD-2026-0881"
            value={invoiceNumber}
            onChange={(e) => setInvoiceNumber(e.target.value)}
          />
          <div className="space-y-1.5">
            <label className="block text-xs font-semibold text-slate-700">
              Đính kèm ảnh hóa đơn chứng từ giao hàng (Bắt buộc)
            </label>
            <div className="border-2 border-dashed border-slate-300 rounded-xl p-6 text-center text-slate-500 hover:border-amber-600 cursor-pointer">
              <Upload className="h-6 w-6 mx-auto text-slate-400" />
              <span className="text-xs font-semibold block mt-1">Tải ảnh hóa đơn lên</span>
            </div>
          </div>
        </div>
      </Modal>

      {/* Internal Bar Transfer Modal */}
      <Modal
        isOpen={showTransferModal}
        onClose={() => setShowTransferModal(false)}
        maxWidth="md"
        title="Xuất Nguyên Liệu Kho Tổng Ra Quầy Bar"
        footer={
          <div className="flex justify-end gap-2">
            <Button variant="secondary" onClick={() => setShowTransferModal(false)}>
              Hủy
            </Button>
            <Button variant="primary" onClick={handleSaveTransfer}>
              Xác Nhận Xuất
            </Button>
          </div>
        }
      >
        <div className="space-y-3 text-xs">
          <p className="text-slate-500">
            Chuyển nguyên liệu từ Kho dự trữ trung tâm ra tủ thao tác quầy pha chế Barista.
          </p>
          <Input label="Số lượng Hạt Cà Phê (kg)" type="number" placeholder="5" />
          <Input label="Số lượng Sữa Tươi (hộp)" type="number" placeholder="10" />
        </div>
      </Modal>
    </div>
  );
}
