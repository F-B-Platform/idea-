using SmartFB.Domain.Common;

namespace SmartFB.Domain.Entities;

public class BranchWifiConfig : BaseEntity
{
    public Guid BranchId { get; set; }
    public string Ssid { get; set; } = string.Empty;
    public string Bssid { get; set; } = string.Empty; // MAC address of router
    public string IpSubnet { get; set; } = string.Empty; // Subnet range e.g., 192.168.1.0/24
    public bool IsActive { get; set; } = true;

    // Navigation Properties
    public Branch Branch { get; set; } = null!;
}
