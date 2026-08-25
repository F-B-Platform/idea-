using Microsoft.AspNetCore.SignalR;

namespace SmartFB.API.Hubs;

public class KitchenHub : Hub
{
    public async Task JoinKitchenGroup(string branchId)
    {
        await Groups.AddToGroupAsync(Context.ConnectionId, $"kitchen_{branchId}");
    }

    public async Task LeaveKitchenGroup(string branchId)
    {
        await Groups.RemoveFromGroupAsync(Context.ConnectionId, $"kitchen_{branchId}");
    }
}
