import React from "react";
import { OrderDto, OrderDetailDto } from "@/types";
import { formatCurrencyVND, formatDateTime } from "@/lib/utils";
import { Badge } from "@/components/ui/Badge";
import { Clock, MapPin, ReceiptText, Phone } from "lucide-react";

export interface OrderCardProps {
  order: OrderDto | OrderDetailDto;
  onSelect?: (order: OrderDto | OrderDetailDto) => void;
  showActions?: boolean;
  onActionClick?: (orderId: string, action: string) => void;
}

export const OrderCard: React.FC<OrderCardProps> = ({
  order,
  onSelect,
  showActions = false,
  onActionClick,
}) => {
  const getStatusBadge = () => {
    switch (order.status) {
      case "PendingPayment":
        return <Badge variant="warning">Chờ Thanh Toán</Badge>;
      case "Paid":
        return <Badge variant="info">Đã Thanh Toán</Badge>;
      case "Confirmed":
        return <Badge variant="info">Đã Tiếp Nhận</Badge>;
      case "Preparing":
        return <Badge variant="amber">Đang Pha Chế</Badge>;
      case "Ready":
        return <Badge variant="success">Sẵn Sàng / Hoàn Tất</Badge>;
      case "Delivering":
        return <Badge variant="info">Đang Giao Hàng</Badge>;
      case "Served":
      case "Completed":
        return <Badge variant="neutral">Đã Phục Vụ</Badge>;
      case "Cancelled":
        return <Badge variant="danger">Đã Hủy</Badge>;
      default:
        return <Badge variant="neutral">{order.status}</Badge>;
    }
  };

  const getOrderTypeBadge = () => {
    switch (order.orderType) {
      case "DineIn":
        return <Badge variant="amber">Tại Bàn {order.tableNumber ? `#${order.tableNumber}` : ""}</Badge>;
      case "TakeAway":
        return <Badge variant="neutral">Mang Về</Badge>;
      case "Delivery":
        return <Badge variant="info">Giao Hàng (Ship 20k)</Badge>;
    }
  };

  return (
    <div
      onClick={() => onSelect && onSelect(order)}
      className="bg-white rounded-2xl p-5 border border-slate-200 shadow-sm hover:shadow-md transition-all space-y-4 cursor-pointer"
    >
      {/* Top row: Order Code & Badges */}
      <div className="flex items-start justify-between gap-3">
        <div>
          <div className="flex items-center gap-2">
            <span className="font-bold text-base text-slate-900">
              #{order.orderCode || order.orderNumber}
            </span>
            {getOrderTypeBadge()}
          </div>
          <div className="flex items-center gap-1.5 text-xs text-slate-500 mt-1">
            <Clock className="h-3.5 w-3.5" />
            <span>{formatDateTime(order.createdAt || order.createdAtUtc)}</span>
          </div>
        </div>
        <div>{getStatusBadge()}</div>
      </div>

      {/* Customer / Location Info */}
      {(order.recipientAddress || order.deliveryAddress || order.recipientPhone || order.customerPhone) && (
        <div className="text-xs text-slate-600 bg-slate-50 p-2.5 rounded-lg space-y-1">
          {(order.recipientPhone || order.customerPhone) && (
            <div className="flex items-center gap-1.5 font-medium">
              <Phone className="h-3.5 w-3.5 text-slate-400" />
              <span>{order.recipientPhone || order.customerPhone}</span>
              {order.recipientName && <span>({order.recipientName})</span>}
            </div>
          )}
          {(order.deliveryAddress || order.recipientAddress) && (
            <div className="flex items-center gap-1.5">
              <MapPin className="h-3.5 w-3.5 text-slate-400 shrink-0" />
              <span className="truncate">{order.deliveryAddress || order.recipientAddress}</span>
            </div>
          )}
        </div>
      )}

      {/* Items list */}
      <div className="space-y-1.5 divide-y divide-slate-100">
        {order.items.map((item, idx) => (
          <div key={idx} className="pt-1.5 first:pt-0 flex items-start justify-between text-xs">
            <div>
              <span className="font-semibold text-slate-800">
                {item.quantity}x {item.productName}
              </span>
              <span className="text-slate-400 ml-1">({item.size || item.sizeName || "M"})</span>
              {(item.sugarLevel || item.iceLevel) && (
                <p className="text-[11px] text-slate-500">
                  Đường: {item.sugarLevel || "100%"} • Đá: {item.iceLevel || "100%"}
                </p>
              )}
            </div>
            <span className="font-medium text-slate-700">
              {formatCurrencyVND(item.totalPrice)}
            </span>
          </div>
        ))}
      </div>

      {/* Total row */}
      <div className="flex items-center justify-between pt-3 border-t border-slate-100 font-bold">
        <span className="text-sm text-slate-600">Tổng cộng:</span>
        <span className="text-base text-amber-800">
          {formatCurrencyVND(order.totalAmount)}
        </span>
      </div>

      {showActions && (
        <div className="flex gap-2 pt-2">
          <button
            onClick={(e) => {
              e.stopPropagation();
              onActionClick && onActionClick(order.id, "view");
            }}
            className="flex-1 py-2 text-xs font-semibold rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700"
          >
            Xem Chi Tiết
          </button>
        </div>
      )}
    </div>
  );
};
