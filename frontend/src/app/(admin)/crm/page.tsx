"use client";

import React, { useState } from "react";
import { CustomerDto } from "@/types";
import { SearchInput } from "@/components/ui/SearchInput";
import { Table, TableHeader, TableBody, TableRow, TableHead, TableCell } from "@/components/ui/Table";
import { Badge } from "@/components/ui/Badge";
import { Users, Gift, ShoppingBag, Calendar, Phone } from "lucide-react";
import { formatCurrencyVND, formatDateTime } from "@/lib/utils";

const initialCustomers: CustomerDto[] = [
  {
    id: "cust-01",
    phoneNumber: "0908123456",
    phone: "0908123456",
    fullName: "Nguyễn Văn VIP",
    takeawayCupCount: 14,
    cupBalance: 4, // 14 total cups, redeemed 10, balance 4
    totalLoyaltyPoints: 420,
    eligibleForFreeCup: false,
    totalOrdersCount: 22,
    totalSpent: 1250000,
    lastOrderDate: "2026-08-25T08:30:00Z",
    segment: "VIP",
  },
  {
    id: "cust-02",
    phoneNumber: "0912345678",
    phone: "0912345678",
    fullName: "Trần Thị Thân Thiết",
    takeawayCupCount: 10,
    cupBalance: 10,
    totalLoyaltyPoints: 310,
    eligibleForFreeCup: true,
    totalOrdersCount: 10,
    totalSpent: 420000,
    lastOrderDate: "2026-08-24T15:00:00Z",
    segment: "Loyal",
  },
  {
    id: "cust-03",
    phoneNumber: "0987654321",
    phone: "0987654321",
    fullName: "Lê Hoàng Khách Mới",
    takeawayCupCount: 2,
    cupBalance: 2,
    totalLoyaltyPoints: 70,
    eligibleForFreeCup: false,
    totalOrdersCount: 2,
    totalSpent: 74000,
    lastOrderDate: "2026-08-20T10:00:00Z",
    segment: "New",
  },
  {
    id: "cust-04",
    phoneNumber: "0977112233",
    phone: "0977112233",
    fullName: "Phạm Văn Lâu Ngày",
    takeawayCupCount: 8,
    cupBalance: 8,
    totalLoyaltyPoints: 240,
    eligibleForFreeCup: false,
    totalOrdersCount: 8,
    totalSpent: 310000,
    lastOrderDate: "2026-07-10T12:00:00Z", // > 45 days
    segment: "AtRisk",
  },
];

export default function AdminCrmPage() {
  const [customers, setCustomers] = useState<CustomerDto[]>(initialCustomers);
  const [search, setSearch] = useState("");
  const [selectedSegment, setSelectedSegment] = useState<string>("ALL");

  const filtered = customers.filter((c) => {
    const matchSearch =
      c.fullName.toLowerCase().includes(search.toLowerCase()) ||
      c.phoneNumber.includes(search);
    const matchSegment = selectedSegment === "ALL" || c.segment === selectedSegment;
    return matchSearch && matchSegment;
  });

  const getSegmentBadge = (segment?: string) => {
    switch (segment) {
      case "VIP":
        return <Badge variant="amber">VIP Diamond</Badge>;
      case "Loyal":
        return <Badge variant="success">Khách Thân Thiết</Badge>;
      case "New":
        return <Badge variant="info">Khách Hàng Mới</Badge>;
      case "AtRisk":
        return <Badge variant="warning">Nguy Cơ Rời Bỏ</Badge>;
      case "Lost":
        return <Badge variant="danger">Đã Rời Bỏ</Badge>;
      default:
        return <Badge variant="neutral">Thành Viên</Badge>;
    }
  };

  return (
    <div className="max-w-7xl mx-auto space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between bg-white p-5 rounded-3xl border border-slate-200 shadow-sm">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-2xl bg-amber-700 text-white flex items-center justify-center font-black shadow-sm">
            <Users className="h-5 w-5" />
          </div>
          <div>
            <h1 className="text-lg font-black text-slate-900 leading-tight">
              Quản Trị Khách Hàng CRM & Phân Khúc RFM
            </h1>
            <span className="text-xs text-slate-500">
              Theo dõi quỹ 10 ly mang về, điểm tích lũy và hành vi mua hàng
            </span>
          </div>
        </div>
      </div>

      {/* Segment Filters & Search */}
      <div className="flex flex-col sm:flex-row gap-4 items-center justify-between">
        <SearchInput
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          onClear={() => setSearch("")}
          placeholder="Tìm theo tên hoặc số điện thoại..."
          className="max-w-md"
        />

        <div className="flex gap-1.5 bg-white p-1.5 rounded-2xl border border-slate-200 shadow-2xs">
          {["ALL", "VIP", "Loyal", "New", "AtRisk"].map((seg) => (
            <button
              key={seg}
              onClick={() => setSelectedSegment(seg)}
              className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all ${
                selectedSegment === seg
                  ? "bg-amber-700 text-white shadow-xs"
                  : "text-slate-600 hover:bg-slate-100"
              }`}
            >
              {seg === "ALL"
                ? "Tất Cả"
                : seg === "VIP"
                ? "VIP"
                : seg === "Loyal"
                ? "Thân Thiết"
                : seg === "New"
                ? "Mới"
                : "Nguy Cơ"}
            </button>
          ))}
        </div>
      </div>

      {/* Customers Table */}
      <div className="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Khách Hàng</TableHead>
              <TableHead>Số Điện Thoại</TableHead>
              <TableHead className="text-center">Quỹ Ly (10 Ly Đổi 1)</TableHead>
              <TableHead className="text-right">Tổng Đơn</TableHead>
              <TableHead className="text-right">Tổng Chi Tiêu</TableHead>
              <TableHead>Lần Mua Gần Nhất</TableHead>
              <TableHead className="text-center">Phân Khúc</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {filtered.map((c) => (
              <TableRow key={c.id}>
                <TableCell className="font-bold text-slate-900">{c.fullName}</TableCell>
                <TableCell className="font-mono text-xs font-semibold text-slate-600">
                  {c.phoneNumber}
                </TableCell>
                <TableCell className="text-center">
                  <span
                    className={`font-black font-mono text-xs px-2.5 py-1 rounded-full ${
                      (c.cupBalance || 0) >= 10
                        ? "bg-emerald-100 text-emerald-800 border border-emerald-300"
                        : "bg-amber-100 text-amber-900"
                    }`}
                  >
                    {c.cupBalance || 0} / 10 Ly {(c.cupBalance || 0) >= 10 ? "🎁" : ""}
                  </span>
                </TableCell>
                <TableCell className="text-right font-mono font-semibold">
                  {c.totalOrdersCount} đơn
                </TableCell>
                <TableCell className="text-right font-mono font-bold text-amber-900">
                  {formatCurrencyVND(c.totalSpent || 0)}
                </TableCell>
                <TableCell className="text-xs text-slate-500">
                  {formatDateTime(c.lastOrderDate)}
                </TableCell>
                <TableCell className="text-center">{getSegmentBadge(c.segment)}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>
    </div>
  );
}
