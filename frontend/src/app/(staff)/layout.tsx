import Link from "next/link";
import { Store, UserCheck, LayoutGrid, FileText, ArrowLeft } from "lucide-react";

export default function StaffLayout({
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
          <span className="font-bold text-orange-400">Phân Hệ Nhân Viên (Web Staff)</span>
        </div>
        <div className="flex items-center gap-3">
          <Link href="/pos" className="hover:text-orange-400 flex items-center gap-1">
            <Store className="w-3.5 h-3.5" /> POS Quầy
          </Link>
          <Link href="/tables" className="hover:text-orange-400 flex items-center gap-1">
            <LayoutGrid className="w-3.5 h-3.5" /> Sơ Đồ Bàn
          </Link>
          <Link href="/attendance" className="hover:text-orange-400 flex items-center gap-1">
            <UserCheck className="w-3.5 h-3.5" /> Chấm Công WiFi
          </Link>
          <Link href="/shift-report" className="hover:text-orange-400 flex items-center gap-1">
            <FileText className="w-3.5 h-3.5" /> Báo Cáo Ca
          </Link>
        </div>
      </div>
      <div className="flex-1">{children}</div>
    </div>
  );
}
