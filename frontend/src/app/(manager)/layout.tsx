import Link from "next/link";
import { Utensils, DollarSign, Package, Wifi, MessageSquare, ArrowLeft } from "lucide-react";

export default function ManagerLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="min-h-screen bg-slate-100 flex flex-col">
      <div className="bg-slate-900 text-white px-4 py-2 flex items-center justify-between text-xs border-b border-slate-800">
        <div className="flex items-center gap-4">
          <Link href="/" className="flex items-center gap-1 text-slate-400 hover:text-white font-medium">
            <ArrowLeft className="w-4 h-4" /> Cổng Portal
          </Link>
          <span className="text-slate-600">|</span>
          <span className="font-bold text-purple-400">Quản Lý Chi Nhánh (Manager Portal)</span>
        </div>
        <div className="flex items-center gap-3">
          <Link href="/branch-dashboard" className="hover:text-purple-400 flex items-center gap-1">
            <Utensils className="w-3.5 h-3.5" /> Tổng Quan
          </Link>
          <Link href="/shifts" className="hover:text-purple-400 flex items-center gap-1">
            <DollarSign className="w-3.5 h-3.5" /> Ca Két Z-Report
          </Link>
          <Link href="/inventory" className="hover:text-purple-400 flex items-center gap-1">
            <Package className="w-3.5 h-3.5" /> Kho BOM
          </Link>
          <Link href="/wifi-configs" className="hover:text-purple-400 flex items-center gap-1">
            <Wifi className="w-3.5 h-3.5" /> WiFi Chấm Công
          </Link>
          <Link href="/reviews" className="hover:text-purple-400 flex items-center gap-1">
            <MessageSquare className="w-3.5 h-3.5" /> Đánh Giá
          </Link>
        </div>
      </div>
      <div className="flex-1">{children}</div>
    </div>
  );
}
