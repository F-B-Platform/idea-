using SmartFB.Domain.Common;
using SmartFB.Domain.Enums;

namespace SmartFB.Domain.Entities;

public class User : AuditableEntity, IAggregateRoot
{
    public Guid? BranchId { get; set; }
    public string Username { get; set; } = string.Empty;
    public string PasswordHash { get; set; } = string.Empty;
    public string FullName { get; set; } = string.Empty;
    public string? Email { get; set; }
    public string? Phone { get; set; }
    public string? EmployeeCode { get; set; }
    public string Status { get; set; } = "Active";
    public UserRole Role { get; set; } = UserRole.Staff;

    // Navigation Properties
    public virtual Branch? Branch { get; set; }
    public virtual ICollection<UserRoleMapping> UserRoles { get; set; } = new List<UserRoleMapping>();
    public virtual ICollection<AuditLog> AuditLogs { get; set; } = new List<AuditLog>();
    public virtual ICollection<Shift> Shifts { get; set; } = new List<Shift>();
    public virtual ICollection<Attendance> Attendances { get; set; } = new List<Attendance>();
}
