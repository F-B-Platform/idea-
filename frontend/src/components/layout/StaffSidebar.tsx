"use client";

import React from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { Coffee, LayoutGrid, Clock, Wifi, FileText, Bell, LogOut } from "lucide-react";
import { useTableStore } from "@/stores/useTableStore";
import { useAuthStore } from "@/stores/useAuthStore";
import { cn } from "@/lib/utils";

export const StaffSidebar: React.FC = () => {
  const pathname = usePathname();
  const serviceAlertsCount = useTableStore((state) => state.getServiceAlertsCount());
  const logout = useAuthStore((state) => state.logout);
  const user = useAuthStore((state) => state.user);

  const navItems = [
    { href: "/pos", label: "Web POS Quầy", icon: Coffee },
    {
      href: "/tables",
      label: "Sơ Đồ Bàn & Chuông",
      icon: LayoutGrid,
      badge: serviceAlertsCount > 0 ? serviceAlertsCount : null,
    },
    { href: "/attendance", label: "Chấm Công WiFi", icon: Wifi },
    { href: "/shift-report", label: "Tổng Kết Ca", icon: FileText },
  ];

  return (
    <aside className="w-64 bg-slate-900 text-slate-100 flex flex-col justify-between border-r border-slate-800 shrink-0 select-none min-h-screen">
      <div>
        {/* Brand Header */}
        <div className="h-16 flex items-center gap-3 px-6 border-b border-slate-800">
          <div className="w-9 h-9 rounded-xl bg-amber-600 text-white flex items-center justify-center font-black">
            <Coffee className="h-5 w-5" />
          </div>
          <div>
            <span className="font-extrabold text-sm tracking-tight text-white block">
              SMART F&B POS
            </span>
            <span className="text-[10px] text-amber-400 font-semibold">Cổng Nhân Viên Vận Hành</span>
          </div>
        </div>

        {/* User Info Bar */}
        <div className="p-4 mx-3 my-3 bg-slate-800/60 rounded-xl border border-slate-700/60 text-xs">
          <span className="text-slate-400 block text-[10px] uppercase">Nhân viên:</span>
          <span className="font-bold text-white block truncate">{user?.fullName || "Thu Ngân Quầy"}</span>
          <span className="text-[11px] text-amber-400 font-semibold">Chi nhánh Quận 1</span>
        </div>

        {/* Navigation Items */}
        <nav className="px-3 space-y-1 mt-2">
          {navItems.map((item) => {
            const isActive = pathname === item.href || pathname?.startsWith(`${item.href}/`);
            const Icon = item.icon;

            return (
              <Link
                key={item.href}
                href={item.href}
                className={cn(
                  "flex items-center justify-between px-3.5 py-3 rounded-xl text-sm font-semibold transition-colors min-h-[44px]",
                  isActive
                    ? "bg-amber-700 text-white shadow-sm"
                    : "text-slate-400 hover:text-slate-100 hover:bg-slate-800"
                )}
              >
                <div className="flex items-center gap-3">
                  <Icon className="h-4 w-4 shrink-0" />
                  <span>{item.label}</span>
                </div>
                {item.badge && (
                  <span className="bg-rose-600 text-white text-[10px] font-bold px-2 py-0.5 rounded-full animate-pulse">
                    {item.badge}
                  </span>
                )}
              </Link>
            );
          })}
        </nav>
      </div>

      {/* Footer / Logout */}
      <div className="p-4 border-t border-slate-800">
        <button
          onClick={logout}
          className="w-full flex items-center justify-center gap-2 py-2.5 rounded-xl text-xs font-bold text-slate-400 hover:text-rose-400 hover:bg-rose-950/30 transition-colors"
        >
          <LogOut className="h-4 w-4" />
          <span>Đăng Xuất Ca</span>
        </button>
      </div>
    </aside>
  );
};
