using SmartFB.Domain.Common;
using SmartFB.Domain.Enums;

namespace SmartFB.Domain.Entities;

public class Payment : BaseEntity, IAggregateRoot
{
    public Guid OrderId { get; set; }
    public PaymentMethod PaymentMethod { get; set; }
    public PaymentMethod Method { get => PaymentMethod; set => PaymentMethod = value; }
    public decimal Amount { get; set; }
    public string? TransactionCode { get; set; }
    public string? PaymentCode { get => TransactionCode; set => TransactionCode = value; }
    public PaymentStatus Status { get; set; } = PaymentStatus.Pending;
    public string? PayosPaymentLinkId { get; set; }
    public DateTime? PaidAt { get; set; }

    // Navigation Properties
    public virtual Order Order { get; set; } = null!;
}
