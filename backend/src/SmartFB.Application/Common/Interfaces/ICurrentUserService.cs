namespace SmartFB.Application.Common.Interfaces;

public interface ICurrentUserService
{
    Guid? UserId { get; }
    string? Username { get; }
    string? Role { get; }
    Guid? BranchId { get; }
    bool IsAuthenticated { get; }
}
