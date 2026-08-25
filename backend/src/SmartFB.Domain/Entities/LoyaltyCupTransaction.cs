namespace SmartFB.Domain.Entities;

using SmartFB.Domain.Enums;

public class LoyaltyCupTransaction
{
    public Guid TransId { get; set; } = Guid.NewGuid();
    public Guid CustomerId { get; set; }
    public Guid? OrderId { get; set; }
    public int CupsEarned { get; set; } = 0;
    public int CupsRedeemed { get; set; } = 0;
    public LoyaltyTransactionType TransactionType { get; set; }
    public string? Notes { get; set; }
    public DateTime CreatedAt { get; set; } = DateTime.UtcNow;

    // Navigation Properties
    public virtual Customer Customer { get; set; } = null!;
    public virtual Order? Order { get; set; }
}
