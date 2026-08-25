"use client";

import React from "react";
import Link from "next/link";
import { Coffee, User, Bell } from "lucide-react";
import { useAuthStore } from "@/stores/useAuthStore";

export const Navbar: React.FC = () => {
  const user = useAuthStore((state) => state.user);

  return (
    <header className="h-16 bg-white border-b border-slate-200 px-6 flex items-center justify-between sticky top-0 z-30">
      <div className="flex items-center gap-3">
        <Link href="/" className="flex items-center gap-2">
          <div className="w-8 h-8 rounded-lg bg-amber-700 text-white flex items-center justify-center font-bold">
            <Coffee className="h-4 w-4" />
          </div>
          <span className="font-extrabold text-sm text-slate-900">SMART F&B OS</span>
        </Link>
      </div>

      <div className="flex items-center gap-4">
        {user ? (
          <div className="flex items-center gap-2 text-xs">
            <div className="w-8 h-8 rounded-full bg-amber-100 text-amber-900 font-bold flex items-center justify-center border border-amber-200">
              <User className="h-4 w-4" />
            </div>
            <div className="hidden sm:block">
              <span className="font-bold text-slate-900 block">{user.fullName}</span>
              <span className="text-[10px] text-slate-500">{user.role}</span>
            </div>
          </div>
        ) : (
          <Link
            href="/pos"
            className="text-xs font-bold text-amber-800 hover:text-amber-900 bg-amber-50 px-3 py-1.5 rounded-lg border border-amber-200"
          >
            Đăng Nhập POS
          </Link>
        )}
      </div>
    </header>
  );
};
