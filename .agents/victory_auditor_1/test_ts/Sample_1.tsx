// ============================================================================
// File: src/app/(customer)/table/[branchId]/[tableCode]/page.tsx
// Project: Smart F&B Operating System (v2.5.0-Production-Ready)
// Description: React Server Component nạp dữ liệu thông tin bàn và thực đơn chi nhánh.
// ============================================================================

import { Suspense } from "react";
import { notFound } from "next/navigation";
import type { Metadata } from "next";
import { TableHeaderBanner } from "@/components/customer/TableHeaderBanner";
import { CategoryNavTabs } from "@/components/customer/CategoryNavTabs";
import { MenuItemGrid } from "@/components/customer/MenuItemGrid";
import { FloatingCartBar } from "@/components/customer/FloatingCartBar";
import { SkeletonMenuLoading } from "@/components/customer/SkeletonMenuLoading";

interface PageProps {
  params: {
    branchId: string;
    tableCode: string;
  };
}

interface TableMetadata {
  id: string;
  code: string;
  branchId: string;
  branchName: string;
  isActive: boolean;
}

export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
  return {
    title: `Gọi Món Tại Bàn ${params.tableCode} - Smart F&B`,
    description: `Đặt đồ uống trực tiếp tại bàn ${params.tableCode} không cần chờ đợi.`,
  };
}

async function fetchTableMetadata(branchId: string, tableCode: string): Promise<TableMetadata | null> {
  const apiUrl = process.env.INTERNAL_API_URL || "https://api.smartfb.vn/api/v1";

  try {
    const res = await fetch(`${apiUrl}/branches/${branchId}/tables/${tableCode}`, {
      next: { revalidate: 60 }, // ISR Caching trong 60 giây
      headers: { "Content-Type": "application/json" }
    });

    if (!res.ok) {
      if (res.status === 404) return null;
      throw new Error(`Lỗi nạp thông tin bàn: ${res.statusText}`);
    }

    return (await res.json()) as TableMetadata;
  } catch (error: unknown) {
    console.error("Lỗi khi kết nối đến API Gateway:", error);
    return null;
  }
}

export default async function TableOrderPage({ params }: PageProps) {
  const table = await fetchTableMetadata(params.branchId, params.tableCode);

  if (!table || !table.isActive) {
    notFound();
  }

  return (
    <main className="min-h-screen bg-neutral-950 text-neutral-50 pb-28">
      {/* Banner thông tin Chi nhánh & Tên Bàn */}
      <TableHeaderBanner
        branchName={table.branchName}
        tableCode={table.code}
      />

      {/* Thanh điều hướng Danh mục món dính trên cùng */}
      <div className="sticky top-0 z-20 bg-neutral-950/90 backdrop-blur-md border-b border-neutral-800">
        <CategoryNavTabs branchId={params.branchId} />
      </div>

      {/* Danh sách món ăn có phân luồng Suspense Streaming */}
      <div className="max-w-md mx-auto px-4 py-4">
        <Suspense fallback={<SkeletonMenuLoading />}>
          <MenuItemGrid branchId={params.branchId} />
        </Suspense>
      </div>

      {/* Thanh hiển thị giỏ hàng nổi chân trang */}
      <FloatingCartBar
        branchId={params.branchId}
        tableId={table.id}
        tableCode={table.code}
      />
    </main>
  );
}