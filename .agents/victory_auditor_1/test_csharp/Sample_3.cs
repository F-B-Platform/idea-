// ============================================================================
// File: src/SmartFB.Application/Features/Orders/Commands/CreateDineInOrder/CreateDineInOrderCommand.cs
// Project: Smart F&B Operating System (v2.5.0-Production-Ready)
// Description: CQRS Command & DTOs khởi tạo đơn hàng tại bàn (Dine-In).
// ============================================================================

using MediatR;
using SmartFB.Application.Common.Models;
using SmartFB.Domain.Enums;

namespace SmartFB.Application.Features.Orders.Commands.CreateDineInOrder;

public sealed record CreateDineInOrderCommand(
    Guid BranchId,
    Guid TableId,
    PaymentMethod PaymentMethod,
    string? Note,
    IReadOnlyList<OrderItemRequestDto> Items
) : IRequest<Result<CreateOrderResponseDto>>;

public sealed record OrderItemRequestDto(
    Guid MenuItemId,
    Guid ItemSizeId,
    int Quantity,
    string? Note,
    IReadOnlyList<OrderItemToppingRequestDto>? Toppings
);

public sealed record OrderItemToppingRequestDto(
    Guid ToppingId,
    string ToppingName,
    decimal Price
);

public sealed record CreateOrderResponseDto(
    Guid OrderId,
    string OrderCode,
    OrderStatus Status,
    PaymentStatus PaymentStatus,
    decimal TotalAmount,
    string? PaymentQrUrl,
    DateTime CreatedAtUtc
);