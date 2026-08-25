using SmartFB.Domain.Common;

namespace SmartFB.Domain.Entities;

public class PayOSTransaction : BaseEntity
{
    public Guid OrderId { get; set; }
    public Guid? PaymentId { get; set; }
    public string PaymentLinkId { get; set; } = string.Empty;
    public long OrderCode { get; set; }
    public decimal Amount { get; set; }
    public string Currency { get; set; } = "VND";
    public string? Description { get; set; }
    public string Status { get; set; } = "PENDING";
    public string? WebhookData { get; set; }
    public DateTime? ProcessedAt { get; set; }

    // Navigation Properties
    public virtual Order Order { get; set; } = null!;
    public virtual Payment? Payment { get; set; }
}
