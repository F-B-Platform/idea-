import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Smart F&B OS — Nền tảng F&B Thông minh",
  description: "Hệ thống vận hành quán cà phê thông minh: Gọi món QR, Web POS, KDS Bếp, Chấm công WiFi",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="vi">
      <body className="min-h-screen bg-slate-50 antialiased">
        {children}
      </body>
    </html>
  );
}
