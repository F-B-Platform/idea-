using SmartFB.Domain.Common;
using SmartFB.Domain.Enums;

namespace SmartFB.Domain.Entities;

public class Order : BaseEntity, IAggregateRoot
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
    public string? DeliveryAddress { get; set; }
    public string? Note { get; set; }

    // Navigation Properties
    public Branch Branch { get; set; } = null!;
    public ICollection<OrderItem> Items { get; set; } = new List<OrderItem>();
    public ICollection<Payment> Payments { get; set; } = new List<Payment>();
}
