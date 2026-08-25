using SmartFB.Domain.Common;

namespace SmartFB.Domain.Entities;

public class ProductBranchPrice : BaseEntity
{
    public Guid ProductId { get; set; }
    public Guid BranchId { get; set; }
    public decimal PriceOverride { get; set; }
    public bool IsAvailable86 { get; set; } = true;

    // Navigation Properties
    public virtual Product Product { get; set; } = null!;
    public virtual Branch Branch { get; set; } = null!;
}
