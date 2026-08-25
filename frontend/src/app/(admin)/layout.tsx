import React from "react";
import { AdminSidebar } from "@/components/layout/AdminSidebar";

export default function AdminLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="min-h-screen bg-slate-100 flex">
      <AdminSidebar />
      <main className="flex-1 overflow-y-auto min-h-screen p-6">{children}</main>
    </div>
  );
}
