using Microsoft.AspNetCore.SignalR;

namespace SmartFB.API.Hubs;

public class NotificationHub : Hub
{
    public async Task JoinBranchNotifications(string branchId)
    {
        await Groups.AddToGroupAsync(Context.ConnectionId, $"notifications_branch_{branchId}");
    }

    public async Task LeaveBranchNotifications(string branchId)
    {
        await Groups.RemoveFromGroupAsync(Context.ConnectionId, $"notifications_branch_{branchId}");
    }
}
