using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.KitchenKDS.DTOs;
using SmartFB.Domain.Enums;

namespace SmartFB.Application.Features.KitchenKDS.Queries.GetKdsTickets;

public record GetKdsTicketsQuery(Guid BranchId) : IRequest<ApiResponse<List<KdsTicketDto>>>;

public class GetKdsTicketsQueryHandler : IRequestHandler<GetKdsTicketsQuery, ApiResponse<List<KdsTicketDto>>>
{
    private readonly IApplicationDbContext _context;

    public GetKdsTicketsQueryHandler(IApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<ApiResponse<List<KdsTicketDto>>> Handle(GetKdsTicketsQuery request, CancellationToken cancellationToken)
    {
        var activeStatuses = new[] { OrderStatus.Paid, OrderStatus.Confirmed, OrderStatus.Preparing, OrderStatus.Ready };

        var orders = await _context.Orders
            .AsNoTracking()
            .Include(o => o.Table)
            .Include(o => o.Items.Where(i => !i.IsDeleted))
                .ThenInclude(i => i.Product)
            .Include(o => o.Items.Where(i => !i.IsDeleted))
                .ThenInclude(i => i.ProductSize)
            .Include(o => o.Items.Where(i => !i.IsDeleted))
                .ThenInclude(i => i.Modifiers)
                    .ThenInclude(m => m.Modifier)
            .Where(o => o.BranchId == request.BranchId && activeStatuses.Contains(o.Status) && !o.IsDeleted)
            .OrderBy(o => o.CreatedAt)
            .ToListAsync(cancellationToken);

        var dtos = orders.Select(o =>
        {
            int elapsedMinutes = (int)(DateTime.UtcNow - o.CreatedAt).TotalMinutes;
            return new KdsTicketDto(
                o.Id,
                o.OrderCode,
                o.OrderType,
                o.Table?.TableNumber,
                o.Status,
                o.CreatedAt,
                SlaMinutes: elapsedMinutes,
                Items: o.Items.Select(i => new KdsItemDto(
                    i.Id,
                    i.ProductId,
                    i.Product.Name,
                    i.ProductSize.SizeName,
                    i.Quantity,
                    i.Note,
                    i.ItemStatus,
                    i.Modifiers.Select(m => $"{m.Modifier.Name} (+{m.ExtraPrice:N0}đ)").ToList()
                )).ToList()
            );
        }).ToList();

        return ApiResponse<List<KdsTicketDto>>.SuccessResult(dtos, "Lấy danh sách vé đơn hàng KDS thành công.");
    }
}
