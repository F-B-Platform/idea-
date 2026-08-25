using SmartFB.Domain.Common;
using SmartFB.Domain.Enums;

namespace SmartFB.Domain.Entities;

public class Order : AuditableEntity, IAggregateRoot
{
    public string OrderCode { get; set; } = string.Empty;
    public Guid BranchId { get; set; }
    public Guid? TableId { get; set; }
    public Guid? CustomerId { get; set; }
    public OrderType OrderType { get; set; }
    public OrderStatus Status { get; set; } = OrderStatus.PendingPayment;
    public decimal SubTotal { get; set; }
    public decimal DiscountAmount { get; set; } = 0;
    public decimal DeliveryFee { get; set; } = 0;
    public decimal TotalAmount { get; set; }
    public string? CustomerName { get; set; }
    public string? CustomerPhone { get; set; }
    public string? RecipientName { get => CustomerName; set => CustomerName = value; }
    public string? RecipientPhone { get => CustomerPhone; set => CustomerPhone = value; }
    public string? DeliveryAddress { get; set; }
    public string? Note { get; set; }
    public string? DeliveryNotes { get => Note; set => Note = value; }
    public DateTime? ExpiresAt { get; set; }
    public DateTime? PaidAt { get; set; }
    public DateTime? CompletedAt { get; set; }

    // Navigation Properties
    public virtual Branch Branch { get; set; } = null!;
    public virtual Table? Table { get; set; }
    public virtual Customer? Customer { get; set; }
    public virtual ICollection<OrderItem> Items { get; set; } = new List<OrderItem>();
    public virtual ICollection<OrderItem> OrderItems { get => Items; set => Items = value; }
    public virtual ICollection<Payment> Payments { get; set; } = new List<Payment>();
    public virtual ICollection<PayOSTransaction> PayOSTransactions { get; set; } = new List<PayOSTransaction>();
    public virtual ICollection<CustomerReview> CustomerReviews { get; set; } = new List<CustomerReview>();
    public virtual ICollection<LoyaltyCupTransaction> LoyaltyCupTransactions { get; set; } = new List<LoyaltyCupTransaction>();
}
