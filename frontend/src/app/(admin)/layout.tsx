import Link from "next/link";
import { ShieldCheck, Coffee, DollarSign, Users, Sparkles, FileText, ArrowLeft } from "lucide-react";

export default function AdminLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="min-h-screen bg-slate-100 flex flex-col">
      <div className="bg-slate-950 text-white px-4 py-2.5 flex items-center justify-between text-xs border-b border-slate-800">
        <div className="flex items-center gap-4">
          <Link href="/" className="flex items-center gap-1 text-slate-400 hover:text-white font-medium">
            <ArrowLeft className="w-4 h-4" /> Cổng Portal
          </Link>
          <span className="text-slate-700">|</span>
          <span className="font-bold text-rose-400 flex items-center gap-1">
            <ShieldCheck className="w-4 h-4 text-rose-500" /> Chuỗi Trụ Sở (Admin HQ Portal)
          </span>
        </div>
        <div className="flex items-center gap-3">
          <Link href="/admin-dashboard" className="hover:text-rose-400">P&L Hợp Nhất</Link>
          <Link href="/menu/products" className="hover:text-rose-400 flex items-center gap-1">
            <Coffee className="w-3.5 h-3.5" /> Menu & BOM
          </Link>
          <Link href="/pricing" className="hover:text-rose-400 flex items-center gap-1">
            <DollarSign className="w-3.5 h-3.5" /> Giá Vùng
          </Link>
          <Link href="/crm" className="hover:text-rose-400 flex items-center gap-1">
            <Users className="w-3.5 h-3.5" /> CRM 10 Ly
          </Link>
          <Link href="/ai/combos" className="hover:text-rose-400 flex items-center gap-1">
            <Sparkles className="w-3.5 h-3.5 text-purple-400" /> AI-2 Combo
          </Link>
          <Link href="/audit-logs" className="hover:text-rose-400 flex items-center gap-1">
            <FileText className="w-3.5 h-3.5" /> Nhật Ký
          </Link>
        </div>
      </div>
      <div className="flex-1">{children}</div>
    </div>
  );
}
