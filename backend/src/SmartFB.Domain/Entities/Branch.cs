using SmartFB.Domain.Common;

namespace SmartFB.Domain.Entities;

public class Branch : AuditableEntity, IAggregateRoot
{
    public string Code { get; set; } = string.Empty;
    public string Name { get; set; } = string.Empty;
    public string Address { get; set; } = string.Empty;
    public string Phone { get; set; } = string.Empty;
    public string OperatingHours { get; set; } = "07:00 - 22:30";
    public bool IsActive { get; set; } = true;

    // Navigation Properties
    public virtual ICollection<BranchWifiConfig> WifiConfigs { get; set; } = new List<BranchWifiConfig>();
    public virtual ICollection<Table> Tables { get; set; } = new List<Table>();
    public virtual ICollection<User> Users { get; set; } = new List<User>();
    public virtual ICollection<Order> Orders { get; set; } = new List<Order>();
    public virtual ICollection<Shift> Shifts { get; set; } = new List<Shift>();
    public virtual ICollection<Attendance> Attendances { get; set; } = new List<Attendance>();
    public virtual ICollection<ProductBranchPrice> ProductBranchPrices { get; set; } = new List<ProductBranchPrice>();
    public virtual ICollection<InventoryTransaction> InventoryTransactions { get; set; } = new List<InventoryTransaction>();
}
