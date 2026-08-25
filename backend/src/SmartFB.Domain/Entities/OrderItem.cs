using SmartFB.Domain.Common;

namespace SmartFB.Domain.Entities;

public class OrderItem : BaseEntity
{
    public Guid OrderId { get; set; }
    public Guid ProductId { get; set; }
    public string ProductName { get; set; } = string.Empty;
    public Guid SizeId { get; set; }
    public string Size { get; set; } = string.Empty;
    public int Quantity { get; set; } = 1;
    public decimal UnitPrice { get; set; }
    public decimal SubtotalPrice { get; set; }
    public decimal TotalPrice { get => SubtotalPrice; set => SubtotalPrice = value; }
    public string? Note { get; set; }
    public string ItemStatus { get; set; } = "Pending";

    // Navigation Properties
    public virtual Order Order { get; set; } = null!;
    public virtual Product Product { get; set; } = null!;
    public virtual ProductSize ProductSize { get; set; } = null!;
    public virtual ICollection<OrderItemModifier> Modifiers { get; set; } = new List<OrderItemModifier>();
    public virtual ICollection<OrderItemModifier> OrderItemModifiers { get => Modifiers; set => Modifiers = value; }
}
