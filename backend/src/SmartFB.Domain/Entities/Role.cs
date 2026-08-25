using SmartFB.Domain.Common;

namespace SmartFB.Domain.Entities;

public class Role : BaseEntity
{
    public string RoleName { get; set; } = string.Empty;
    public string? Description { get; set; }

    // Navigation Properties
    public virtual ICollection<UserRoleMapping> UserRoles { get; set; } = new List<UserRoleMapping>();
}
