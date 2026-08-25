using SmartFB.Domain.Common;

namespace SmartFB.Domain.Entities;

public class Branch : BaseEntity, IAggregateRoot
{
    public string BranchCode { get; set; } = string.Empty;
    public string BranchName { get; set; } = string.Empty;
    public string Address { get; set; } = string.Empty;
    public string PhoneNumber { get; set; } = string.Empty;
    public bool IsActive { get; set; } = true;

    // Navigation Properties
    public ICollection<BranchWifiConfig> WifiConfigs { get; set; } = new List<BranchWifiConfig>();
    public ICollection<Order> Orders { get; set; } = new List<Order>();
}
