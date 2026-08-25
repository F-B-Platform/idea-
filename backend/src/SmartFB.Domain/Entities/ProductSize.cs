using SmartFB.Domain.Common;

namespace SmartFB.Domain.Entities;

public class ProductSize : BaseEntity
{
    public Guid ProductId { get; set; }
    public string SizeName { get; set; } = string.Empty;
    public decimal PriceAdjustment { get; set; } = 0;
    public int DisplayOrder { get; set; } = 0;

    // Navigation Properties
    public virtual Product Product { get; set; } = null!;
    public virtual ICollection<RecipeBom> RecipeBoms { get; set; } = new List<RecipeBom>();
    public virtual ICollection<OrderItem> OrderItems { get; set; } = new List<OrderItem>();
}
