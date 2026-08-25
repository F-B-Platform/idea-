import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";
import { OrderDetailDto, OrderDto } from "@/types";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

/**
 * Formats a number to Vietnamese Dong currency (e.g. 35.000 ₫).
 */
export function formatCurrencyVND(amount: number): string {
  if (isNaN(amount)) return "0 ₫";
  return new Intl.NumberFormat("vi-VN", {
    style: "currency",
    currency: "VND",
  }).format(amount);
}

/**
 * Formats an ISO date string to Vietnamese localized format.
 */
export function formatDateTime(isoString?: string): string {
  if (!isoString) return "--:--";
  const date = new Date(isoString);
  if (isNaN(date.getTime())) return "--:--";
  return new Intl.DateTimeFormat("vi-VN", {
    day: "2-digit",
    month: "2-digit",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  }).format(date);
}

export function formatTimeOnly(isoString?: string): string {
  if (!isoString) return "--:--";
  const date = new Date(isoString);
  if (isNaN(date.getTime())) return "--:--";
  return new Intl.DateTimeFormat("vi-VN", {
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  }).format(date);
}

/**
 * Calculates KDS SLA status and color coding:
 * - Success (Green): elapsed < 180s (3 mins)
 * - Warning (Amber): 180s <= elapsed <= 300s (3 - 5 mins)
 * - Danger (Red Pulsing): elapsed > 300s (> 5 mins)
 */
export function calculateSlaStatus(elapsedSeconds: number): {
  variant: 'success' | 'warning' | 'danger';
  label: string;
  badgeClass: string;
  cardBorderClass: string;
} {
  const minutes = Math.floor(elapsedSeconds / 60);
  const seconds = elapsedSeconds % 60;
  const timeString = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;

  if (elapsedSeconds < 180) {
    return {
      variant: 'success',
      label: timeString,
      badgeClass: 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/40',
      cardBorderClass: 'border-emerald-500/30 hover:border-emerald-500/60',
    };
  }
  if (elapsedSeconds <= 300) {
    return {
      variant: 'warning',
      label: timeString,
      badgeClass: 'bg-amber-500/20 text-amber-300 border border-amber-500/40',
      cardBorderClass: 'border-amber-500/40 hover:border-amber-500/70',
    };
  }
  return {
    variant: 'danger',
    label: `${timeString} (QUÁ HẠN)`,
    badgeClass: 'bg-rose-600/30 text-rose-300 border border-rose-500 animate-pulse font-bold',
    cardBorderClass: 'border-rose-500 shadow-lg shadow-rose-950/50 animate-pulse',
  };
}

/**
 * Validates 10-digit Vietnamese phone numbers starting with 03, 05, 07, 08, 09.
 */
export function validateVietnamesePhone(phone: string): {
  isValid: boolean;
  message?: string;
} {
  const cleanPhone = phone.trim().replace(/[\s.-]/g, '');
  const vnPhoneRegex = /^(03|05|07|08|09)\d{8}$/;

  if (!cleanPhone) {
    return { isValid: false, message: "Số điện thoại không được để trống" };
  }
  if (!vnPhoneRegex.test(cleanPhone)) {
    return {
      isValid: false,
      message: "Số điện thoại không hợp lệ (Phải có 10 chữ số, bắt đầu bằng 03, 05, 07, 08, 09)",
    };
  }
  return { isValid: true };
}

/**
 * Generates formatted ESC/POS thermal receipt string for POS thermal printers (58mm/80mm).
 */
export function generateEscPosReceipt(order: OrderDto | OrderDetailDto): string {
  const line = "================================";
  const subLine = "--------------------------------";
  const branchName = order.branchName || "SMART F&B COFFEE & TEA";
  const dateStr = formatDateTime(order.createdAt || order.createdAtUtc);

  let output = "";
  output += `${centerText(branchName, 32)}\n`;
  output += `${centerText("HÓA ĐƠN BÁN HÀNG", 32)}\n`;
  output += `${line}\n`;
  output += `Mã Đơn: ${order.orderCode || order.orderNumber}\n`;
  output += `Ngày:   ${dateStr}\n`;
  if (order.tableNumber) {
    output += `Vị Trí: ${order.tableNumber}\n`;
  }
  output += `Loại:   ${order.orderType === 'DineIn' ? 'Tại Bàn' : order.orderType === 'TakeAway' ? 'Mang Về' : 'Giao Hàng'}\n`;
  output += `${subLine}\n`;
  output += `Tên Món            SL   Thành Tiền\n`;
  output += `${subLine}\n`;

  order.items.forEach((item) => {
    const nameWithSize = `${item.productName} (${item.size || item.sizeName || 'M'})`;
    const qtyStr = item.quantity.toString().padStart(2, " ");
    const priceStr = formatCurrencyVND(item.totalPrice).replace(" ₫", "").padStart(9, " ");
    
    output += `${padRight(nameWithSize.slice(0, 18), 18)} ${qtyStr} ${priceStr}\n`;
    if (item.sugarLevel || item.iceLevel) {
      output += `  > Đ: ${item.sugarLevel || "100%"} | Đá: ${item.iceLevel || "100%"}\n`;
    }
  });

  output += `${subLine}\n`;
  output += `Tạm tính:        ${padLeft(formatCurrencyVND(order.subTotal || order.subtotalAmount || 0), 15)}\n`;
  if (order.discountAmount > 0) {
    output += `Chiết khấu:     -${padLeft(formatCurrencyVND(order.discountAmount), 14)}\n`;
  }
  if (order.deliveryFee > 0) {
    output += `Phí ship:        ${padLeft(formatCurrencyVND(order.deliveryFee), 15)}\n`;
  }
  output += `${line}\n`;
  output += `TỔNG CỘNG:       ${padLeft(formatCurrencyVND(order.totalAmount), 15)}\n`;
  output += `Thanh toán:      ${order.paymentMethod === 'VIETQR' ? 'VietQR Chuyển Khoản' : 'Tiền Mặt'}\n`;
  output += `${line}\n`;
  output += `${centerText("CẢM ƠN QUÝ KHÁCH & HẸN GẶP LẠI", 32)}\n`;
  output += `${centerText("Wifi Pass: SmartFB@2026", 32)}\n\n\n`;

  return output;
}

function centerText(text: string, width: number): string {
  if (text.length >= width) return text.slice(0, width);
  const leftPadding = Math.floor((width - text.length) / 2);
  return " ".repeat(leftPadding) + text;
}

function padRight(text: string, width: number): string {
  if (text.length >= width) return text.slice(0, width);
  return text + " ".repeat(width - text.length);
}

function padLeft(text: string, width: number): string {
  if (text.length >= width) return text.slice(0, width);
  return " ".repeat(width - text.length) + text;
}

/**
 * Client-side WebP image compressor.
 * Takes a File or Blob, resizes to max width 1200px, and converts to WebP with 0.8 quality.
 */
export async function compressImageToWebP(file: File): Promise<{
  blob: Blob;
  base64: string;
  sizeKB: number;
}> {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = (event) => {
      const img = new Image();
      img.onload = () => {
        const canvas = document.createElement("canvas");
        let width = img.width;
        let height = img.height;
        const maxDimension = 1200;

        if (width > maxDimension || height > maxDimension) {
          if (width > height) {
            height = Math.round((height * maxDimension) / width);
            width = maxDimension;
          } else {
            width = Math.round((width * maxDimension) / height);
            height = maxDimension;
          }
        }

        canvas.width = width;
        canvas.height = height;
        const ctx = canvas.getContext("2d");
        if (!ctx) {
          reject(new Error("Canvas context is not available"));
          return;
        }

        ctx.drawImage(img, 0, 0, width, height);
        const base64 = canvas.toDataURL("image/webp", 0.8);

        canvas.toBlob(
          (blob) => {
            if (blob) {
              resolve({
                blob,
                base64,
                sizeKB: Math.round(blob.size / 1024),
              });
            } else {
              reject(new Error("Failed to convert canvas to blob"));
            }
          },
          "image/webp",
          0.8
        );
      };
      img.onerror = (err) => reject(err);
      img.src = event.target?.result as string;
    };
    reader.onerror = (err) => reject(err);
    reader.readAsDataURL(file);
  });
}
