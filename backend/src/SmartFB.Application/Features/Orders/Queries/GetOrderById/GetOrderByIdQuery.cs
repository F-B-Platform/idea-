using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Orders.DTOs;
using SmartFB.Domain.Enums;

namespace SmartFB.Application.Features.Orders.Queries.GetOrderById;

public record GetOrderByIdQuery(Guid OrderId) : IRequest<ApiResponse<OrderDto>>;

public class GetOrderByIdQueryHandler : IRequestHandler<GetOrderByIdQuery, ApiResponse<OrderDto>>
{
    private readonly IApplicationDbContext _context;

    public GetOrderByIdQueryHandler(IApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<ApiResponse<OrderDto>> Handle(GetOrderByIdQuery request, CancellationToken cancellationToken)
    {
        var order = await _context.Orders
            .AsNoTracking()
            .Include(o => o.Table)
            .Include(o => o.Items.Where(i => !i.IsDeleted))
                .ThenInclude(i => i.Product)
            .Include(o => o.Items.Where(i => !i.IsDeleted))
                .ThenInclude(i => i.ProductSize)
            .Include(o => o.Items.Where(i => !i.IsDeleted))
                .ThenInclude(i => i.Modifiers)
                    .ThenInclude(m => m.Modifier)
            .FirstOrDefaultAsync(o => o.Id == request.OrderId && !o.IsDeleted, cancellationToken);

        if (order == null)
        {
            throw new NotFoundException("Order", request.OrderId);
        }

        var dto = new OrderDto(
            order.Id,
            order.BranchId,
            order.TableId,
            order.Table?.TableNumber,
            order.CustomerId,
            order.OrderCode,
            order.OrderType,
            order.Status,
            order.SubTotal,
            order.DiscountAmount,
            order.DeliveryFee,
            order.TotalAmount,
            order.CustomerName,
            order.CustomerPhone,
            order.DeliveryAddress,
            order.Note,
            order.ExpiresAt,
            order.CreatedAt,
            order.PaidAt,
            order.Items.Select(i => new OrderItemDto(
                i.Id,
                i.ProductId,
                i.Product.Name,
                i.SizeId,
                i.ProductSize.SizeName,
                i.Quantity,
                i.UnitPrice,
                i.SubtotalPrice,
                i.Note,
                i.ItemStatus,
                i.Modifiers.Select(m => new OrderItemModifierDto(
                    m.ItemModId,
                    m.ModifierId,
                    m.Modifier.Name,
                    m.Quantity,
                    m.ExtraPrice
                )).ToList()
            )).ToList()
        );

        return ApiResponse<OrderDto>.SuccessResult(dto, "Lấy thông tin đơn hàng thành công.");
    }
}
