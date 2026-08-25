using SmartFB.Domain.Common;

namespace SmartFB.Domain.Entities;

public class Attendance : BaseEntity
{
    public Guid BranchId { get; set; }
    public Guid UserId { get; set; }
    public string StaffCode { get; set; } = string.Empty;
    public DateTime CheckInTime { get; set; } = DateTime.UtcNow;
    public DateTime? CheckOutTime { get; set; }
    public string VerifiedBssid { get; set; } = string.Empty;
    public string ClientIpAddress { get; set; } = string.Empty;
    public bool IsWifiVerified { get; set; } = true;
    public string? Note { get; set; }

    // Navigation Properties
    public Branch Branch { get; set; } = null!;
}
