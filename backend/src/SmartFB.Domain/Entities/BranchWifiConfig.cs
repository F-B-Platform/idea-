using SmartFB.Domain.Common;

namespace SmartFB.Domain.Entities;

public class BranchWifiConfig : BaseEntity
{
    public Guid BranchId { get; set; }
    public string SsidName { get; set; } = string.Empty;
    public string Ssid { get => SsidName; set => SsidName = value; }
    public string BssidList { get; set; } = string.Empty;
    public string Bssid { get => BssidList; set => BssidList = value; }
    public string AllowedIpSubnets { get; set; } = string.Empty;
    public string IpSubnet { get => AllowedIpSubnets; set => AllowedIpSubnets = value; }
    public bool IsActive { get; set; } = true;

    // Navigation Properties
    public virtual Branch Branch { get; set; } = null!;
}
