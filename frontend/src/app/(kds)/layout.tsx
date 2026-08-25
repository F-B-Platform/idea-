import React from "react";

export default function KdsLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="min-h-screen bg-[#0F172A] text-slate-100 antialiased selection:bg-amber-600 selection:text-white">
      {children}
    </div>
  );
}
