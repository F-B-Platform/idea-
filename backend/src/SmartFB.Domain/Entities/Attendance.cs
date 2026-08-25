using SmartFB.Domain.Common;
using SmartFB.Domain.Enums;

namespace SmartFB.Domain.Entities;

public class Attendance : BaseEntity, IAggregateRoot
{
    public Guid BranchId { get; set; }
    public Guid UserId { get; set; }
    public string EmployeeCode { get; set; } = string.Empty;
    public string StaffCode { get => EmployeeCode; set => EmployeeCode = value; }
    public DateTime CheckInTime { get; set; } = DateTime.UtcNow;
    public DateTime? CheckOutTime { get; set; }
    public string VerifiedIp { get; set; } = string.Empty;
    public string ClientIpAddress { get => VerifiedIp; set => VerifiedIp = value; }
    public string VerifiedBssid { get; set; } = string.Empty;
    public bool IsWifiVerified { get; set; } = true;
    public AttendanceStatus Status { get; set; } = AttendanceStatus.OnTime;

    // Navigation Properties
    public virtual Branch Branch { get; set; } = null!;
    public virtual User User { get; set; } = null!;
}
