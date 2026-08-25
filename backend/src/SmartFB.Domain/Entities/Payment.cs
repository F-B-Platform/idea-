using SmartFB.Domain.Common;
using SmartFB.Domain.Enums;

namespace SmartFB.Domain.Entities;

public class Payment : BaseEntity
{
    public Guid OrderId { get; set; }
    public string PaymentCode { get; set; } = string.Empty;
    public PaymentMethod Method { get; set; }
    public PaymentStatus Status { get; set; } = PaymentStatus.Pending;
    public decimal Amount { get; set; }
    public string? TransactionReference { get; set; } // PayOS paymentLinkId or OrderCode
    public string? QrCodeUrl { get; set; }
    public DateTime? PaidAt { get; set; }
    public string? PayOsWebhookDataJson { get; set; }

    // Navigation Properties
    public Order Order { get; set; } = null!;
}
