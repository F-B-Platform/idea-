using SmartFB.Domain.Common;
using SmartFB.Domain.Enums;

namespace SmartFB.Domain.Entities;

public class Table : BaseEntity
{
    public Guid BranchId { get; set; }
    public string TableNumber { get; set; } = string.Empty;
    public string Zone { get; set; } = "Tầng 1";
    public int Capacity { get; set; } = 4;
    public string? QrCodeUrl { get; set; }
    public TableStatus Status { get; set; } = TableStatus.Available;
    public bool IsActive { get; set; } = true;

    // Navigation Properties
    public virtual Branch Branch { get; set; } = null!;
    public virtual ICollection<Order> Orders { get; set; } = new List<Order>();
}
