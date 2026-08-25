using SmartFB.Domain.Enums;

namespace SmartFB.Application.Features.Orders.DTOs;

public record OrderItemDto(
    Guid Id,
    Guid ProductId,
    string ProductName,
    Guid SizeId,
    string SizeName,
    int Quantity,
    decimal UnitPrice,
    decimal SubtotalPrice,
    string? Note,
    string ItemStatus,
    List<OrderItemModifierDto> Modifiers
);

public record OrderItemModifierDto(
    Guid Id,
    Guid ModifierId,
    string ModifierName,
    int Quantity,
    decimal ExtraPrice
);

public record OrderDto(
    Guid Id,
    Guid BranchId,
    Guid? TableId,
    string? TableNumber,
    Guid? CustomerId,
    string OrderCode,
    OrderType OrderType,
    OrderStatus Status,
    decimal SubTotal,
    decimal DiscountAmount,
    decimal DeliveryFee,
    decimal TotalAmount,
    string? CustomerName,
    string? CustomerPhone,
    string? DeliveryAddress,
    string? Note,
    DateTime? ExpiresAt,
    DateTime CreatedAt,
    DateTime? PaidAt,
    List<OrderItemDto> Items
);

public record CreateOrderItemRequestDto(
    Guid ProductId,
    Guid SizeId,
    int Quantity,
    string? Note,
    List<Guid>? ModifierIds = null
);

public record PrepaidOrderResultDto(
    Guid OrderId,
    string OrderCode,
    decimal TotalAmount,
    DateTime ExpiresAt,
    string VietQrCodeUrl,
    string DeepLinkCheckoutUrl
);

public record PostpaidOrderResultDto(
    Guid OrderId,
    string OrderCode,
    OrderStatus Status,
    decimal TotalAmount,
    int EstimatedPrepMinutes
);

public record DeliveryOrderResultDto(
    Guid OrderId,
    string OrderCode,
    decimal SubTotal,
    decimal DeliveryFee,
    decimal TotalAmount,
    DateTime ExpiresAt,
    string VietQrCodeUrl
);

public record TakeawayOrderResultDto(
    Guid OrderId,
    string OrderCode,
    decimal SubTotal,
    decimal LoyaltyDiscount,
    decimal TotalAmount,
    int EarnedCups,
    int RemainingCupBalance
);

public record OrderTrackingDto(
    Guid OrderId,
    string OrderCode,
    OrderStatus Status,
    int QueuePosition,
    int EstimatedMinutes,
    DateTime CreatedAt,
    List<OrderItemDto> Items
);
