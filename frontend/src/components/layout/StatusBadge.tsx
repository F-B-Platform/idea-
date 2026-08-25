import React from "react";
import { Badge } from "@/components/ui/Badge";
import { OrderStatus, TableStatus, PaymentStatus } from "@/types";

export interface StatusBadgeProps {
  status: OrderStatus | TableStatus | PaymentStatus | string;
}

export const StatusBadge: React.FC<StatusBadgeProps> = ({ status }) => {
  switch (status) {
    // Order Statuses
    case "PendingPayment":
      return <Badge variant="warning">Chờ Thanh Toán</Badge>;
    case "Paid":
      return <Badge variant="info">Đã Thanh Toán</Badge>;
    case "Confirmed":
      return <Badge variant="info">Đã Tiếp Nhận</Badge>;
    case "Preparing":
      return <Badge variant="amber">Đang Pha Chế</Badge>;
    case "Ready":
      return <Badge variant="success">Sẵn Sàng Phục Vụ</Badge>;
    case "Delivering":
      return <Badge variant="info">Đang Giao Hàng</Badge>;
    case "Served":
    case "Completed":
      return <Badge variant="neutral">Hoàn Tất</Badge>;
    case "Cancelled":
      return <Badge variant="danger">Đã Hủy</Badge>;

    // Table Statuses
    case "Available":
      return <Badge variant="success">Bàn Trống</Badge>;
    case "Occupied_Paid":
      return <Badge variant="info">Đang Dùng (Đã TT)</Badge>;
    case "Occupied_PendingPayment":
      return <Badge variant="warning">Đang Dùng (Chờ TT)</Badge>;
    case "ServiceRequested":
      return <Badge variant="danger" className="animate-pulse">Khách Gọi Bàn</Badge>;

    // Payment Statuses
    case "Success":
      return <Badge variant="success">Thành Công</Badge>;
    case "Failed":
      return <Badge variant="danger">Thất Bại</Badge>;
    case "Expired":
      return <Badge variant="neutral">Hết Hạn</Badge>;

    default:
      return <Badge variant="neutral">{status}</Badge>;
  }
};
