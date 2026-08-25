namespace SmartFB.Domain.Entities;

public class ProductModifier
{
    public Guid ProductId { get; set; }
    public Guid ModifierId { get; set; }
    public bool IsDefault { get; set; } = false;
    public int MaxQuantity { get; set; } = 1;

    // Navigation Properties
    public virtual Product Product { get; set; } = null!;
    public virtual Modifier Modifier { get; set; } = null!;
}
