import React from "react";
import { CustomerNavbar } from "@/components/layout/CustomerNavbar";

export default function CustomerLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="min-h-screen bg-slate-50 text-slate-900 flex flex-col">
      <CustomerNavbar />
      <main className="flex-1 max-w-md mx-auto w-full pb-20">{children}</main>
    </div>
  );
}
