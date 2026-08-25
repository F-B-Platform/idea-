namespace SmartFB.Application.Common.Interfaces;

public interface ISignalRHubService
{
    Task NotifyOrderCreatedAsync(Guid branchId, object orderData);
    Task NotifyOrderStatusChangedAsync(Guid orderId, string orderCode, string status);
    Task NotifyKitchenTicketAsync(Guid branchId, object ticketData);
    Task Notify86ToggledAsync(Guid branchId, Guid productId, bool isAvailable);
    Task NotifyPaymentSuccessAsync(Guid orderId, string transactionCode, decimal amount);
    Task NotifyUrgentAlertAsync(Guid branchId, string title, string message, object? payload = null);
    Task NotifyServiceCallAsync(Guid branchId, Guid tableId, string tableNumber, string reason);
}
