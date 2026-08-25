using SmartFB.Domain.Enums;

namespace SmartFB.Application.Features.KitchenKDS.DTOs;

public record KdsItemDto(
    Guid OrderItemId,
    Guid ProductId,
    string ProductName,
    string SizeName,
    int Quantity,
    string? Note,
    string ItemStatus,
    List<string> Modifiers
);

public record KdsTicketDto(
    Guid OrderId,
    string OrderCode,
    OrderType OrderType,
    string? TableNumber,
    OrderStatus OrderStatus,
    DateTime CreatedAt,
    int SlaMinutes,
    List<KdsItemDto> Items
);

public record UpdateKdsItemStatusRequestDto(
    Guid OrderItemId,
    string NewStatus // "Preparing", "Ready", "Served"
);

public record Toggle86RequestDto(
    Guid BranchId,
    Guid ProductId,
    bool IsAvailable
);

public record BatchKdsItemsRequestDto(
    List<Guid> OrderItemIds
);
