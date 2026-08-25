using Microsoft.AspNetCore.SignalR;

namespace SmartFB.API.Hubs;

public class PaymentHub : Hub
{
    public async Task JoinOrderPaymentGroup(string orderId)
    {
        await Groups.AddToGroupAsync(Context.ConnectionId, $"payment_order_{orderId}");
    }

    public async Task LeaveOrderPaymentGroup(string orderId)
    {
        await Groups.RemoveFromGroupAsync(Context.ConnectionId, $"payment_order_{orderId}");
    }
}
