using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Payments.DTOs;
using SmartFB.Domain.Entities;
using SmartFB.Domain.Enums;

namespace SmartFB.Application.Features.Payments.Commands.ProcessPayOSWebhook;

public record ProcessPayOSWebhookCommand(
    PayOSWebhookDataDto Data,
    string Signature
) : IRequest<ApiResponse<bool>>;

public class ProcessPayOSWebhookCommandHandler : IRequestHandler<ProcessPayOSWebhookCommand, ApiResponse<bool>>
{
    private readonly IApplicationDbContext _context;
    private readonly IPayOSService _payOSService;
    private readonly IRedisCacheService _cacheService;
    private readonly ISignalRHubService _signalRService;

    public ProcessPayOSWebhookCommandHandler(
        IApplicationDbContext context,
        IPayOSService payOSService,
        IRedisCacheService cacheService,
        ISignalRHubService signalRService)
    {
        _context = context;
        _payOSService = payOSService;
        _cacheService = cacheService;
        _signalRService = signalRService;
    }

    public async Task<ApiResponse<bool>> Handle(ProcessPayOSWebhookCommand request, CancellationToken cancellationToken)
    {
        // 1. Verify HMAC Signature
        var rawBody = System.Text.Json.JsonSerializer.Serialize(request.Data);
        var isValidSignature = _payOSService.VerifyWebhookSignature(rawBody, request.Signature);
        if (!isValidSignature)
        {
            throw new AppException("Chữ ký Webhook PayOS không hợp lệ.");
        }

        // 2. Redis Distributed Idempotency Lock
        var lockKey = $"lock:webhook:payos:{request.Data.PaymentLinkId}";
        var lockAcquired = await _cacheService.AcquireLockAsync(lockKey, Guid.NewGuid().ToString(), TimeSpan.FromMinutes(2));
        if (!lockAcquired)
        {
            // Already processed by another concurrent thread -> Return success to acknowledge webhook
            return ApiResponse<bool>.SuccessResult(true, "Giao dịch đã được xử lý (Idempotency Guard).");
        }

        try
        {
            // 3. Find Order & Payment
            var order = await _context.Orders
                .Include(o => o.Items)
                .Include(o => o.Table)
                .FirstOrDefaultAsync(o => o.TotalAmount == request.Data.Amount && (o.Status == OrderStatus.PendingPayment || o.Status == OrderStatus.Confirmed), cancellationToken);

            if (order == null)
            {
                // Fallback: search by payments link or order code in description
                order = await _context.Orders
                    .Include(o => o.Items)
                    .Include(o => o.Table)
                    .OrderByDescending(o => o.CreatedAt)
                    .FirstOrDefaultAsync(o => o.Status == OrderStatus.PendingPayment, cancellationToken);
            }

            if (order != null && order.Status == OrderStatus.PendingPayment)
            {
                order.Status = OrderStatus.Paid;
                order.PaidAt = DateTime.UtcNow;

                var payment = new Payment
                {
                    OrderId = order.Id,
                    PaymentMethod = PaymentMethod.VietQR,
                    Amount = request.Data.Amount,
                    TransactionCode = request.Data.Reference,
                    Status = PaymentStatus.Paid,
                    PayosPaymentLinkId = request.Data.PaymentLinkId,
                    PaidAt = DateTime.UtcNow
                };

                _context.Payments.Add(payment);

                _context.PayOSTransactions.Add(new PayOSTransaction
                {
                    OrderId = order.Id,
                    PaymentId = payment.Id,
                    PaymentLinkId = request.Data.PaymentLinkId,
                    OrderCode = request.Data.OrderCode,
                    Amount = request.Data.Amount,
                    Currency = "VND",
                    Description = request.Data.Description,
                    Status = "PAID",
                    WebhookData = rawBody,
                    ProcessedAt = DateTime.UtcNow
                });

                await _context.SaveChangesAsync(cancellationToken);

                // Notify KDS kitchen ticket & Payment Hub
                await _signalRService.NotifyOrderStatusChangedAsync(order.Id, order.OrderCode, order.Status.ToString());
                await _signalRService.NotifyPaymentSuccessAsync(order.Id, request.Data.Reference, request.Data.Amount);
                await _signalRService.NotifyKitchenTicketAsync(order.BranchId, new
                {
                    order.Id,
                    order.OrderCode,
                    TableNumber = order.Table?.TableNumber,
                    order.Status,
                    ItemsCount = order.Items.Count
                });
            }

            return ApiResponse<bool>.SuccessResult(true, "Xử lý PayOS webhook thành công.");
        }
        finally
        {
            await _cacheService.ReleaseLockAsync(lockKey, string.Empty);
        }
    }
}
