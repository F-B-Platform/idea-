import React from "react";
import { ManagerSidebar } from "@/components/layout/ManagerSidebar";

export default function ManagerLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="min-h-screen bg-slate-100 flex">
      <ManagerSidebar />
      <main className="flex-1 overflow-y-auto min-h-screen p-6">{children}</main>
    </div>
  );
}
