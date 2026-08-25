"use client";

import React, { useState } from "react";
import { AuditLogDto } from "@/types";
import { formatDateTime } from "@/lib/utils";
import { SearchInput } from "@/components/ui/SearchInput";
import { Table, TableHeader, TableBody, TableRow, TableHead, TableCell } from "@/components/ui/Table";
import { Badge } from "@/components/ui/Badge";
import { ShieldCheck, User, Clock, Terminal } from "lucide-react";

const initialAuditLogs: AuditLogDto[] = [
  {
    id: "log-01",
    userId: "usr-01",
    userName: "Trần Quản Lý (BranchManager)",
    userRole: "BranchManager",
    action: "CLOSE_CASH_SHIFT",
    entityName: "CashShift",
    entityId: "shift-20260825-01",
    ipAddress: "192.168.1.105",
    newValuesJson: '{"physicalCash": 2450000, "variance": 0}',
    timestampUtc: "2026-08-25T08:45:00Z",
  },
  {
    id: "log-02",
    userId: "usr-02",
    userName: "Nguyễn Barista (BaristaStaff)",
    userRole: "BaristaStaff",
    action: "86_TOGGLE_OUT_OF_STOCK",
    entityName: "Product",
    entityId: "prod-08",
    ipAddress: "192.168.1.110",
    newValuesJson: '{"isAvailable": false, "productName": "Bánh Croissant Bơ Tỏi"}',
    timestampUtc: "2026-08-25T08:30:00Z",
  },
  {
    id: "log-03",
    userId: "usr-admin",
    userName: "Admin Tổng Chuỗi (ChainAdmin)",
    userRole: "ChainAdmin",
    action: "APPROVE_AI_COMBO",
    entityName: "ComboCampaign",
    entityId: "combo-01",
    ipAddress: "118.69.182.5",
    newValuesJson: '{"comboName": "Combo Cà Phê Muối + Croissant", "finalPrice": 57000}',
    timestampUtc: "2026-08-25T08:00:00Z",
  },
  {
    id: "log-04",
    userId: "usr-admin",
    userName: "Admin Tổng Chuỗi (ChainAdmin)",
    userRole: "ChainAdmin",
    action: "UPDATE_REGIONAL_MULTIPLIER",
    entityName: "PriceGroup",
    entityId: "HCM_Q1_PREMIUM",
    ipAddress: "118.69.182.5",
    oldValuesJson: '{"priceMultiplier": 1.10}',
    newValuesJson: '{"priceMultiplier": 1.15}',
    timestampUtc: "2026-08-24T18:00:00Z",
  },
];

export default function AdminAuditLogsPage() {
  const [logs] = useState<AuditLogDto[]>(initialAuditLogs);
  const [search, setSearch] = useState("");

  const filtered = logs.filter(
    (l) =>
      l.userName?.toLowerCase().includes(search.toLowerCase()) ||
      l.action.toLowerCase().includes(search.toLowerCase()) ||
      l.entityName.toLowerCase().includes(search.toLowerCase())
  );

  const getActionBadge = (action: string) => {
    if (action.includes("CLOSE") || action.includes("SHIFT")) {
      return <Badge variant="warning">{action}</Badge>;
    }
    if (action.includes("86") || action.includes("DELETE")) {
      return <Badge variant="danger">{action}</Badge>;
    }
    if (action.includes("APPROVE") || action.includes("CREATE")) {
      return <Badge variant="success">{action}</Badge>;
    }
    return <Badge variant="info">{action}</Badge>;
  };

  return (
    <div className="max-w-7xl mx-auto space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between bg-white p-5 rounded-3xl border border-slate-200 shadow-sm">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-2xl bg-amber-700 text-white flex items-center justify-center font-black shadow-sm">
            <ShieldCheck className="h-5 w-5" />
          </div>
          <div>
            <h1 className="text-lg font-black text-slate-900 leading-tight">
              Nhật Ký Kiểm Toán Bất Biến (Immutable Audit Logs)
            </h1>
            <span className="text-xs text-slate-500">
              Truy vết 100% thao tác nhạy cảm: sửa giá, khóa món, đóng ca két, phê duyệt combo
            </span>
          </div>
        </div>
      </div>

      {/* Search */}
      <SearchInput
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        onClear={() => setSearch("")}
        placeholder="Tìm kiếm theo hành động, người thực hiện hoặc thực thể..."
        className="max-w-md"
      />

      {/* Audit Table */}
      <div className="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Thời Gian (UTC)</TableHead>
              <TableHead>Người Thực Hiện</TableHead>
              <TableHead>Hành Động</TableHead>
              <TableHead>Thực Thể</TableHead>
              <TableHead>Chi Tiết Thay Đổi (JSON Payload)</TableHead>
              <TableHead className="text-right">Địa Chỉ IP</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {filtered.map((log) => (
              <TableRow key={log.id}>
                <TableCell className="font-mono text-xs text-slate-500 whitespace-nowrap">
                  {formatDateTime(log.timestampUtc)}
                </TableCell>
                <TableCell className="font-semibold text-slate-900 text-xs">
                  {log.userName}
                </TableCell>
                <TableCell>{getActionBadge(log.action)}</TableCell>
                <TableCell className="font-mono text-xs font-bold text-slate-700">
                  {log.entityName}
                </TableCell>
                <TableCell className="font-mono text-[11px] text-slate-600 max-w-xs truncate">
                  {log.newValuesJson}
                </TableCell>
                <TableCell className="text-right font-mono text-xs text-slate-400">
                  {log.ipAddress}
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>
    </div>
  );
}
