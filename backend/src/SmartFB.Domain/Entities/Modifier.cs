using SmartFB.Domain.Common;
using SmartFB.Domain.Enums;

namespace SmartFB.Domain.Entities;

public class Modifier : BaseEntity
{
    public string Name { get; set; } = string.Empty;
    public ModifierType Type { get; set; }
    public decimal ExtraPrice { get; set; } = 0;
    public bool IsAvailable { get; set; } = true;

    // Navigation Properties
    public virtual ICollection<ProductModifier> ProductModifiers { get; set; } = new List<ProductModifier>();
    public virtual ICollection<OrderItemModifier> OrderItemModifiers { get; set; } = new List<OrderItemModifier>();
}
