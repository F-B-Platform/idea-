using SmartFB.Domain.Common;

namespace SmartFB.Domain.Entities;

public class Customer : BaseEntity, IAggregateRoot
{
    public string PhoneNumber { get; set; } = string.Empty;
    public string FullName { get; set; } = string.Empty;
    public int TakeawayCupCount { get; set; } = 0; // Takeaway loyalty 10 cups -> 1 free
    public int TotalLoyaltyPoints { get; set; } = 0;
    public DateTime? LastVisitedAt { get; set; }
}
