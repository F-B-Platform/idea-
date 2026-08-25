import React from "react";
import { StaffSidebar } from "@/components/layout/StaffSidebar";

export default function StaffLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="min-h-screen bg-slate-100 flex">
      <StaffSidebar />
      <main className="flex-1 overflow-y-auto min-h-screen p-6">{children}</main>
    </div>
  );
}
