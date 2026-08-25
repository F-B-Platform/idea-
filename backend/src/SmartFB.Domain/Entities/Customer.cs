using SmartFB.Domain.Common;

namespace SmartFB.Domain.Entities;

public class Customer : AuditableEntity, IAggregateRoot
{
    public string PhoneNumber { get; set; } = string.Empty;
    public string? FullName { get; set; }
    public string? Email { get; set; }
    public DateOnly? BirthDate { get; set; }
    public string MembershipTier { get; set; } = "Standard";
    public int CupBalance { get; set; } = 0;
    public int TakeawayCupCount { get => CupBalance; set => CupBalance = value; }
    public int TotalPoints { get; set; } = 0;
    public int TotalLoyaltyPoints { get => TotalPoints; set => TotalPoints = value; }
    public DateTime? LastVisitedAt { get; set; } = DateTime.UtcNow;

    // Navigation Properties
    public virtual ICollection<Order> Orders { get; set; } = new List<Order>();
    public virtual ICollection<LoyaltyCupTransaction> LoyaltyCupTransactions { get; set; } = new List<LoyaltyCupTransaction>();
    public virtual ICollection<CustomerReview> CustomerReviews { get; set; } = new List<CustomerReview>();
}
