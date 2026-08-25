using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Payments.DTOs;
using SmartFB.Domain.Enums;

namespace SmartFB.Application.Features.Payments.Queries.GetPaymentStatus;

public record GetPaymentStatusQuery(Guid OrderId) : IRequest<ApiResponse<PaymentStatusDto>>;

public class GetPaymentStatusQueryHandler : IRequestHandler<GetPaymentStatusQuery, ApiResponse<PaymentStatusDto>>
{
    private readonly IApplicationDbContext _context;

    public GetPaymentStatusQueryHandler(IApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<ApiResponse<PaymentStatusDto>> Handle(GetPaymentStatusQuery request, CancellationToken cancellationToken)
    {
        var order = await _context.Orders
            .AsNoTracking()
            .FirstOrDefaultAsync(o => o.Id == request.OrderId && !o.IsDeleted, cancellationToken);

        if (order == null)
        {
            throw new NotFoundException("Order", request.OrderId);
        }

        var latestPayment = await _context.Payments
            .AsNoTracking()
            .Where(p => p.OrderId == request.OrderId && !p.IsDeleted)
            .OrderByDescending(p => p.CreatedAt)
            .FirstOrDefaultAsync(cancellationToken);

        bool isPaid = order.Status == OrderStatus.Paid || order.Status == OrderStatus.Completed || (latestPayment != null && latestPayment.Status == PaymentStatus.Paid);

        var result = new PaymentStatusDto(
            order.Id,
            order.OrderCode,
            isPaid,
            latestPayment?.Status ?? (isPaid ? PaymentStatus.Paid : PaymentStatus.Pending),
            order.PaidAt ?? latestPayment?.PaidAt
        );

        return ApiResponse<PaymentStatusDto>.SuccessResult(result, "Lấy trạng thái thanh toán thành công.");
    }
}
