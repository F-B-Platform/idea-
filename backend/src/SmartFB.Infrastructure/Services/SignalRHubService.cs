using Microsoft.Extensions.Logging;
using SmartFB.Application.Common.Interfaces;

namespace SmartFB.Infrastructure.Services;

public class SignalRHubService : ISignalRHubService
{
    private readonly ILogger<SignalRHubService> _logger;

    public SignalRHubService(ILogger<SignalRHubService> logger)
    {
        _logger = logger;
    }

    public Task NotifyOrderCreatedAsync(Guid branchId, object orderData)
    {
        _logger.LogInformation("[SignalR:OrderHub] Broadcast OrderCreated to Branch {BranchId}", branchId);
        return Task.CompletedTask;
    }

    public Task NotifyOrderStatusChangedAsync(Guid orderId, string orderCode, string status)
    {
        _logger.LogInformation("[SignalR:OrderHub] Broadcast OrderStatusChanged for Order {OrderCode} -> {Status}", orderCode, status);
        return Task.CompletedTask;
    }

    public Task NotifyKitchenTicketAsync(Guid branchId, object ticketData)
    {
        _logger.LogInformation("[SignalR:KitchenHub] Broadcast KitchenTicket to Branch {BranchId}", branchId);
        return Task.CompletedTask;
    }

    public Task Notify86ToggledAsync(Guid branchId, Guid productId, bool isAvailable)
    {
        _logger.LogInformation("[SignalR:KitchenHub] Broadcast 86Toggled to Branch {BranchId}: Product {ProductId} IsAvailable={IsAvailable}", branchId, productId, isAvailable);
        return Task.CompletedTask;
    }

    public Task NotifyPaymentSuccessAsync(Guid orderId, string transactionCode, decimal amount)
    {
        _logger.LogInformation("[SignalR:PaymentHub] Broadcast PaymentSuccess for Order {OrderId}, TransCode: {TransCode}, Amount: {Amount}", orderId, transactionCode, amount);
        return Task.CompletedTask;
    }

    public Task NotifyUrgentAlertAsync(Guid branchId, string title, string message, object? payload = null)
    {
        _logger.LogWarning("[SignalR:NotificationHub] Broadcast UrgentAlert to Branch {BranchId}: {Title} - {Message}", branchId, title, message);
        return Task.CompletedTask;
    }

    public Task NotifyServiceCallAsync(Guid branchId, Guid tableId, string tableNumber, string reason)
    {
        _logger.LogInformation("[SignalR:NotificationHub] Service call from Table {TableNumber} at Branch {BranchId}: {Reason}", tableNumber, branchId, reason);
        return Task.CompletedTask;
    }
}
