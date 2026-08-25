using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Payments.DTOs;
using SmartFB.Domain.Entities;
using SmartFB.Domain.Enums;

namespace SmartFB.Application.Features.Payments.Commands.ConfirmCashPayment;

public record ConfirmCashPaymentCommand(
    Guid OrderId,
    decimal ReceivedAmount
) : IRequest<ApiResponse<CashConfirmationResultDto>>;

public class ConfirmCashPaymentCommandHandler : IRequestHandler<ConfirmCashPaymentCommand, ApiResponse<CashConfirmationResultDto>>
{
    private readonly IApplicationDbContext _context;
    private readonly ISignalRHubService _signalRService;

    public ConfirmCashPaymentCommandHandler(IApplicationDbContext context, ISignalRHubService signalRService)
    {
        _context = context;
        _signalRService = signalRService;
    }

    public async Task<ApiResponse<CashConfirmationResultDto>> Handle(ConfirmCashPaymentCommand request, CancellationToken cancellationToken)
    {
        var order = await _context.Orders
            .FirstOrDefaultAsync(o => o.Id == request.OrderId && !o.IsDeleted, cancellationToken);

        if (order == null)
        {
            throw new NotFoundException("Order", request.OrderId);
        }

        if (request.ReceivedAmount < order.TotalAmount)
        {
            throw new AppException($"Số tiền khách đưa ({request.ReceivedAmount:N0} đ) nhỏ hơn tổng hóa đơn ({order.TotalAmount:N0} đ).");
        }

        decimal changeAmount = request.ReceivedAmount - order.TotalAmount;

        order.Status = OrderStatus.Completed;
        order.PaidAt = DateTime.UtcNow;
        order.CompletedAt = DateTime.UtcNow;

        var payment = new Payment
        {
            OrderId = order.Id,
            PaymentMethod = PaymentMethod.Cash,
            Amount = order.TotalAmount,
            TransactionCode = $"CASH-{DateTime.UtcNow:yyMMddHHmmss}-{Random.Shared.Next(100, 999)}",
            Status = PaymentStatus.Paid,
            PaidAt = DateTime.UtcNow
        };

        _context.Payments.Add(payment);

        // Update active shift system cash calculated
        var activeShift = await _context.Shifts
            .FirstOrDefaultAsync(s => s.BranchId == order.BranchId && s.Status == ShiftStatus.Open && !s.IsDeleted, cancellationToken);

        if (activeShift != null)
        {
            activeShift.SystemCashCalculated += order.TotalAmount;
        }

        await _context.SaveChangesAsync(cancellationToken);

        await _signalRService.NotifyOrderStatusChangedAsync(order.Id, order.OrderCode, order.Status.ToString());
        await _signalRService.NotifyPaymentSuccessAsync(order.Id, payment.TransactionCode, payment.Amount);

        var result = new CashConfirmationResultDto(
            order.Id,
            order.OrderCode,
            order.TotalAmount,
            request.ReceivedAmount,
            changeAmount,
            order.Status,
            payment.Status
        );

        return ApiResponse<CashConfirmationResultDto>.SuccessResult(result, "Xác nhận thanh toán tiền mặt thành công.");
    }
}
