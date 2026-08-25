using SmartFB.Domain.Common;

namespace SmartFB.Domain.Entities;

public class OrderItemModifier
{
    public Guid ItemModId { get; set; } = Guid.NewGuid();
    public Guid OrderItemId { get; set; }
    public Guid ModifierId { get; set; }
    public int Quantity { get; set; } = 1;
    public decimal ExtraPrice { get; set; } = 0;
    public DateTime CreatedAt { get; set; } = DateTime.UtcNow;

    // Navigation Properties
    public virtual OrderItem OrderItem { get; set; } = null!;
    public virtual Modifier Modifier { get; set; } = null!;
}
