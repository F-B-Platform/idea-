"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";
import { useCartStore } from "@/stores/useCartStore";

export default function TableLandingPage({ params }: { params: { tableId: string } }) {
  const router = useRouter();
  const { setTableAndBranch } = useCartStore();

  useEffect(() => {
    setTableAndBranch(params.tableId, params.tableId, "default-branch");
    router.replace("/menu");
  }, [params.tableId, router, setTableAndBranch]);

  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-50 text-slate-600 text-xs font-mono">
      Đang nhận diện Bàn {params.tableId}...
    </div>
  );
}
