// ==============================================================================
// SMART F&B OPERATING SYSTEM — SHARED FRONTEND TYPES & INTERFACES (v2.5.0)
// Complete 100% Zero-Placeholder DTOs matching .NET 8 Clean Architecture
// ==============================================================================

// ==============================================================================
// 1. DOMAIN ENUMS
// ==============================================================================
export type OrderType = 'DineIn' | 'TakeAway' | 'Delivery';

export type OrderStatus =
  | 'PendingPayment'
  | 'Paid'
  | 'Confirmed'
  | 'Preparing'
  | 'Ready'
  | 'Served'
  | 'Delivering'
  | 'Completed'
  | 'Cancelled';

export type PaymentMethod = 'VIETQR' | 'CASH' | 'CARD';

export type PaymentStatus = 'Pending' | 'Success' | 'Paid' | 'Failed' | 'Expired' | 'Refunded';

export type UserRole =
  | 'CashierStaff'
  | 'BaristaStaff'
  | 'BranchManager'
  | 'ChainAdmin'
  | 'Admin'
  | 'Manager'
  | 'Staff'
  | 'Customer';

export type TableStatus =
  | 'Available'
  | 'Occupied_Paid'
  | 'Occupied_PendingPayment'
  | 'ServiceRequested';

export type SugarLevel = '0%' | '30%' | '50%' | '70%' | '100%';
export type IceLevel = '0%' | '30%' | '50%' | '70%' | '100%';
export type ProductSizeName = 'S' | 'M' | 'L' | 'Regular' | 'Large';

// ==============================================================================
// 2. RESPONSE ENVELOPES & ERROR PROTOCOLS (RFC 7807)
// ==============================================================================
export interface ApiResponse<T> {
  success: boolean;
  statusCode?: number;
  message: string;
  data: T | null;
  errors?: Record<string, string[]> | null;
  timestamp?: string;
  timestampUtc?: string;
}

export interface PagedResponse<T> extends ApiResponse<T[]> {
  pageIndex: number;
  pageSize: number;
  totalCount: number;
  totalPages: number;
  hasPreviousPage: boolean;
  hasNextPage: boolean;
}

export interface ProblemDetails {
  type?: string;
  title: string;
  status: number;
  detail: string;
  instance?: string;
  errors?: Record<string, string[]>;
  timestampUtc?: string;
}

// ==============================================================================
// 3. USER PROFILE & AUTHENTICATION
// ==============================================================================
export interface UserProfile {
  id: string;
  employeeCode: string;
  fullName: string;
  email?: string;
  phoneNumber?: string;
  role: UserRole;
  branchId?: string;
  branchName?: string;
  avatarUrl?: string;
  isActive: boolean;
}

export interface LoginResponseDto {
  accessToken: string;
  refreshToken: string;
  expiresInSeconds: number;
  user: UserProfile;
}

// ==============================================================================
// 4. PRODUCTS, SIZES, MODIFIERS, CATEGORIES & BOM
// ==============================================================================
export interface ProductModifierDto {
  id: string;
  productId?: string;
  name: string;
  priceAdjustment: number;
  isDefault: boolean;
  maxQuantity?: number;
}

export interface ProductSizeDto {
  id: string;
  productId?: string;
  sizeName: ProductSizeName;
  price: number;
  isDefault: boolean;
}

export interface IngredientDto {
  id: string;
  code: string;
  name: string;
  unit: string;
  costPerUnit: number;
  currentStock: number;
  minThreshold: number;
  isLowStock?: boolean;
}

export interface ProductBOMItemDto {
  id: string;
  productId: string;
  productName?: string;
  sizeId: string;
  sizeName: ProductSizeName;
  ingredientId: string;
  ingredientName: string;
  ingredientUnit: string;
  quantityRequired: number;
  costContribution: number;
}

export interface ProductDto {
  id: string;
  productCode?: string;
  sku: string;
  name: string;
  description?: string;
  basePrice: number;
  imageUrl?: string;
  categoryId: string;
  categoryName?: string;
  isAvailable: boolean;
  isBestSeller?: boolean;
  isSeasonal?: boolean;
  displayOrder?: number;
  sizes: ProductSizeDto[];
  modifiers: ProductModifierDto[];
  bomItems?: ProductBOMItemDto[];
}

export interface CategoryDto {
  id: string;
  name: string;
  code?: string;
  description?: string;
  displayOrder: number;
  isActive: boolean;
  itemCount?: number;
  iconUrl?: string;
}

export interface SeasonalMenuDto {
  id: string;
  name: string;
  description?: string;
  startDateUtc: string;
  endDateUtc: string;
  isActive: boolean;
  productIds: string[];
  products?: ProductDto[];
}

export interface PriceGroupDto {
  id: string;
  name: string;
  regionCode: string;
  description?: string;
  priceMultiplier: number;
  assignedBranchCount?: number;
}

// ==============================================================================
// 5. ORDERS & ORDER ITEMS
// ==============================================================================
export interface OrderModifierSelection {
  modifierId: string;
  name: string;
  price: number;
}

export interface OrderItemDto {
  id?: string;
  productId: string;
  productName: string;
  size?: ProductSizeName | string;
  sizeName?: ProductSizeName | string;
  sizeId?: string;
  quantity: number;
  unitPrice: number;
  totalPrice: number;
  sugarLevel?: SugarLevel | string;
  iceLevel?: IceLevel | string;
  selectedModifiers?: OrderModifierSelection[];
  selectedModifiersJson?: string;
  notes?: string;
  specialInstructions?: string;
}

export interface OrderDto {
  id: string;
  orderCode: string;
  orderNumber?: string;
  branchId: string;
  branchName?: string;
  tableId?: string;
  tableNumber?: string;
  customerId?: string;
  customerName?: string;
  customerPhone?: string;
  recipientName?: string;
  recipientPhone?: string;
  recipientAddress?: string;
  deliveryAddress?: string;
  shipperNotes?: string;
  orderType: OrderType;
  status: OrderStatus;
  subTotal: number;
  subtotalAmount?: number;
  discountAmount: number;
  deliveryFee: number;
  totalAmount: number;
  paymentMethod: PaymentMethod;
  paymentStatus: PaymentStatus;
  qrCodeUrl?: string;
  paymentDeepLink?: string;
  payOsPaymentUrl?: string;
  items: OrderItemDto[];
  queuePosition?: number;
  estimatedMinutes?: number;
  note?: string;
  createdAt: string;
  createdAtUtc?: string;
  servedAtUtc?: string;
}

export interface OrderDetailDto extends OrderDto {}

// ==============================================================================
// 6. ORDER CREATION REQUESTS
// ==============================================================================
export interface OrderItemRequest {
  productId: string;
  sizeId: string;
  quantity: number;
  sugarLevel: SugarLevel | string;
  iceLevel: IceLevel | string;
  selectedModifierIds: string[];
  notes?: string;
}

export interface CreateDineInPrepaidOrderRequest {
  branchId: string;
  tableId: string;
  customerPhone?: string;
  voucherCode?: string;
  items: OrderItemRequest[];
}

export interface CreateDineInPostpaidOrderRequest {
  branchId: string;
  tableId: string;
  customerPhone?: string;
  voucherCode?: string;
  items: OrderItemRequest[];
}

export interface CreateDeliveryOrderRequest {
  branchId: string;
  recipientName: string;
  recipientPhone: string;
  deliveryAddress: string;
  shipperNotes?: string;
  voucherCode?: string;
  items: OrderItemRequest[];
}

export interface CreateTakeawayOrderRequest {
  branchId: string;
  customerPhone: string;
  redeemFreeCup: boolean;
  paymentMethod: PaymentMethod;
  tenderAmount: number;
  voucherCode?: string;
  items: OrderItemRequest[];
}

// ==============================================================================
// 7. CRM, LOYALTY & CUSTOMER MODELS
// ==============================================================================
export interface CustomerDto {
  id: string;
  phoneNumber: string;
  phone?: string;
  fullName: string;
  takeawayCupCount: number;
  cupBalance?: number;
  totalLoyaltyPoints: number;
  eligibleForFreeCup?: boolean;
  totalOrdersCount?: number;
  totalSpent?: number;
  lastOrderDate?: string;
  segment?: 'VIP' | 'Loyal' | 'AtRisk' | 'Lost' | 'New';
}

export interface CustomerLookupDto {
  id: string;
  phone: string;
  fullName: string;
  cupBalance: number;
  eligibleForFreeCup: boolean;
  totalOrdersCount: number;
  lastOrderDate?: string;
}

export interface LoyaltyCupTransactionDto {
  id: string;
  customerId: string;
  orderId?: string;
  transactionType: 'Accumulate' | 'Redeem' | 'Adjust';
  cupAmount: number;
  resultingBalance: number;
  notes?: string;
  createdAtUtc: string;
}

// ==============================================================================
// 8. KDS (KITCHEN DISPLAY SYSTEM) & BAR MODELS
// ==============================================================================
export interface KdsTicketItemDto {
  orderItemId: string;
  productId: string;
  productName: string;
  sizeName: ProductSizeName | string;
  quantity: number;
  sugarLevel: string;
  iceLevel: string;
  toppings: string[];
  notes?: string;
  bomIngredients?: { name: string; quantity: number; unit: string }[];
}

export interface KdsTicketDto {
  orderId: string;
  orderNumber: string;
  orderCode?: string;
  orderType: OrderType;
  tableNumber?: string;
  tableId?: string;
  createdAtUtc: string;
  elapsedSeconds: number;
  status: 'Pending' | 'Preparing' | 'Ready';
  paymentStatus: PaymentStatus;
  paymentMethod: PaymentMethod;
  station: 'BAR' | 'KITCHEN' | 'ALL';
  items: KdsTicketItemDto[];
}

export interface Product86ToggleDto {
  productId: string;
  productName: string;
  categoryName: string;
  isAvailable: boolean;
  updatedByStaffName?: string;
  updatedAtUtc?: string;
}

export interface BatchItemSummary {
  productId: string;
  productName: string;
  sizeName: string;
  totalQuantity: number;
  orderCount: number;
  orderIds: string[];
  sugarLevels: Record<string, number>;
  iceLevels: Record<string, number>;
}

// ==============================================================================
// 9. TABLES & SERVICE CALLS
// ==============================================================================
export interface TableDto {
  id: string;
  tableNumber: string;
  branchId: string;
  floor: number;
  capacity: number;
  status: TableStatus;
  activeOrderId?: string;
  activeOrderCode?: string;
  activeAmount?: number;
  serviceRequestedAt?: string;
  qrCodeUrl?: string;
}

export interface FloorDto {
  floorNumber: number;
  floorName: string;
  tables: TableDto[];
}

// ==============================================================================
// 10. SHIFTS, CASH DRAWER & Z-REPORT
// ==============================================================================
export interface DenominationCountDto {
  denomination: 500000 | 200000 | 100000 | 50000 | 20000 | 10000;
  count: number;
  total: number;
}

export interface CashShiftDto {
  id: string;
  shiftCode: string;
  branchId: string;
  branchName?: string;
  cashierUserId: string;
  cashierName: string;
  openedAtUtc: string;
  closedAtUtc?: string;
  openingCash: number;
  cashSales: number;
  vietQrSales: number;
  totalSales: number;
  theoreticalCash: number;
  physicalCash?: number;
  variance?: number;
  justificationReason?: string;
  isClosed: boolean;
  denominations?: Record<number, number>;
}

export interface OpenShiftRequest {
  branchId: string;
  openingCash: number;
}

export interface CloseShiftRequest {
  shiftId: string;
  denominations: Record<number, number>;
  physicalCashTotal: number;
  justificationReason?: string;
}

export interface ZReportDto {
  id: string;
  shiftId: string;
  shiftCode: string;
  branchName: string;
  cashierName: string;
  openedAtUtc: string;
  closedAtUtc: string;
  openingCash: number;
  cashSales: number;
  vietQrSales: number;
  cardSales?: number;
  totalRevenue: number;
  totalOrdersCount: number;
  discountTotal: number;
  theoreticalCash: number;
  physicalCash: number;
  variance: number;
  justificationReason?: string;
  denominations: Record<number, number>;
}

// ==============================================================================
// 11. INVENTORY, PURCHASING & AUDITING
// ==============================================================================
export interface StockAuditItemDto {
  ingredientId: string;
  ingredientCode: string;
  ingredientName: string;
  unit: string;
  theoreticalStock: number;
  physicalStock: number;
  variance: number;
  wastagePercent: number;
  costPerUnit: number;
  varianceCost: number;
  isDiscrepancySevere: boolean; // > 3%
}

export interface StockAuditDto {
  id: string;
  branchId: string;
  branchName: string;
  auditedByUserName: string;
  auditDateUtc: string;
  items: StockAuditItemDto[];
  totalVarianceCost: number;
  notes?: string;
}

export interface GoodsReceiptItemRequest {
  ingredientId: string;
  quantity: number;
  unitPrice: number;
}

export interface CreateGoodsReceiptRequest {
  branchId: string;
  supplierName: string;
  invoiceNumber: string;
  invoiceImageUrl?: string;
  items: GoodsReceiptItemRequest[];
  notes?: string;
}

export interface BarStockTransferRequest {
  branchId: string;
  items: {
    ingredientId: string;
    quantity: number;
  }[];
  notes?: string;
}

// ==============================================================================
// 12. WIFI & ATTENDANCE
// ==============================================================================
export interface WifiConfigDto {
  id: string;
  branchId: string;
  branchName?: string;
  ssid: string;
  bssid: string; // MAC address e.g. "AA:BB:CC:DD:EE:FF"
  subnetIpRange: string; // CIDR e.g. "192.168.1.0/24"
  gatewayIp?: string;
  isActive: boolean;
}

export interface AttendanceRecordDto {
  id: string;
  employeeCode: string;
  employeeName: string;
  branchId: string;
  branchName: string;
  clockInUtc: string;
  clockOutUtc?: string;
  clockInBssid: string;
  clockInIp: string;
  isClockInValid: boolean;
  clockOutBssid?: string;
  clockOutIp?: string;
  isClockOutValid?: boolean;
  workHours?: number;
  status: 'Working' | 'Completed' | 'InvalidWifi';
}

export interface WifiCheckInRequest {
  employeeCode: string;
  bssid: string;
  clientIp: string;
}

export interface WifiCheckOutRequest {
  employeeCode: string;
  bssid: string;
  clientIp: string;
}

// ==============================================================================
// 13. REVIEWS & RATINGS
// ==============================================================================
export interface ReviewImageDto {
  id: string;
  imageUrl: string;
  isApproved: boolean;
  uploadedAtUtc: string;
}

export interface ReviewDto {
  id: string;
  orderId: string;
  orderCode: string;
  branchId: string;
  branchName?: string;
  tableNumber?: string;
  customerPhone?: string;
  rating: number; // 1 - 5
  tags: string[];
  comment?: string;
  isAnonymous: boolean;
  images: ReviewImageDto[];
  isRedAlert: boolean; // <= 2 stars
  managerNote?: string;
  isResolved?: boolean;
  createdAtUtc: string;
}

export interface CreateReviewRequest {
  orderId: string;
  rating: number;
  tags: string[];
  comment?: string;
  isAnonymous: boolean;
  imagesBase64?: string[];
}

// ==============================================================================
// 14. AI & APRIORI COMBO RECOMMENDATIONS
// ==============================================================================
export interface ComboCandidateDto {
  id: string;
  productIds: string[];
  productNames: string[];
  originalPrice: number;
  bomCost: number;
  grossMarginPercent: number;
  support: number;
  confidence: number;
  lift: number;
  suggestedDiscountPercent: number;
  proposedPrice: number;
  projectedProfit: number;
}

export interface MineCombosRequest {
  minSupport: number;
  minConfidence: number;
  startDateUtc?: string;
  endDateUtc?: string;
}

export interface ApproveComboRequest {
  comboCandidateId: string;
  comboName: string;
  discountPercent: number;
  finalPrice: number;
  startDateUtc: string;
  endDateUtc: string;
}

export interface PlSummaryDto {
  period: string;
  totalRevenue: number;
  cogsAmount: number; // Cost of Goods Sold (BOM)
  grossProfit: number;
  grossMarginPercent: number;
  staffCost: number;
  operatingCost: number;
  netProfit: number;
  netMarginPercent: number;
  branchesBreakdown: {
    branchId: string;
    branchName: string;
    revenue: number;
    cogs: number;
    profit: number;
  }[];
}

export interface BcgMatrixItemDto {
  productId: string;
  productName: string;
  categoryName: string;
  salesVolume: number;
  profitMarginPercent: number;
  category: 'Star' | 'CashCow' | 'QuestionMark' | 'Dog';
}

// ==============================================================================
// 15. AUDIT LOGS
// ==============================================================================
export interface AuditLogDto {
  id: string;
  userId?: string;
  userName?: string;
  userRole?: string;
  action: string;
  entityName: string;
  entityId: string;
  ipAddress?: string;
  oldValuesJson?: string;
  newValuesJson?: string;
  timestampUtc: string;
}
