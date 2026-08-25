// ==============================================================================
// SMART F&B OS - SHARED FRONTEND TYPES & INTERFACES (v2.5.0)
// ==============================================================================

export type OrderType = 'DineIn' | 'TakeAway' | 'Delivery';
export type OrderStatus = 'PendingPayment' | 'Paid' | 'Confirmed' | 'Preparing' | 'Ready' | 'Served' | 'Completed' | 'Cancelled';
export type PaymentMethod = 'VietQR' | 'Cash' | 'Card';
export type PaymentStatus = 'Pending' | 'Paid' | 'Failed' | 'Refunded';
export type UserRole = 'Admin' | 'Manager' | 'Staff' | 'Customer';

export interface ApiResponse<T> {
  success: boolean;
  message: string;
  data: T | null;
  errors?: Record<string, string[]> | null;
  timestamp: string;
}

export interface ProductDto {
  id: string;
  productCode: string;
  name: string;
  description: string;
  basePrice: number;
  imageUrl?: string;
  categoryId: string;
  isAvailable: boolean;
}

export interface OrderItemDto {
  id?: string;
  productId: string;
  productName: string;
  size: 'S' | 'M' | 'L';
  quantity: number;
  unitPrice: number;
  totalPrice: number;
  selectedModifiersJson?: string;
  specialInstructions?: string;
}

export interface OrderDto {
  id: string;
  orderCode: string;
  branchId: string;
  tableId?: string;
  customerId?: string;
  orderType: OrderType;
  status: OrderStatus;
  subTotal: number;
  discountAmount: number;
  deliveryFee: number;
  totalAmount: number;
  customerName?: string;
  customerPhone?: string;
  deliveryAddress?: string;
  note?: string;
  items: OrderItemDto[];
  createdAt: string;
}

export interface CustomerDto {
  id: string;
  phoneNumber: string;
  fullName: string;
  takeawayCupCount: number;
  totalLoyaltyPoints: number;
}
