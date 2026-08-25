using SmartFB.Domain.Common;

namespace SmartFB.Domain.Entities;

public class Product : AuditableEntity, IAggregateRoot
{
    public Guid CategoryId { get; set; }
    public string Sku { get; set; } = string.Empty;
    public string ProductCode { get => Sku; set => Sku = value; }
    public string Name { get; set; } = string.Empty;
    public string? Description { get; set; }
    public decimal BasePrice { get; set; }
    public string? ImageUrl { get; set; }
    public bool IsAvailable { get; set; } = true;
    public bool IsBestSeller { get; set; } = false;
    public int CaloriesApprox { get; set; } = 0;
    public string? AllergenInfo { get; set; }

    // Navigation Properties
    public virtual Category Category { get; set; } = null!;
    public virtual ICollection<ProductSize> ProductSizes { get; set; } = new List<ProductSize>();
    public virtual ICollection<ProductBranchPrice> BranchPrices { get; set; } = new List<ProductBranchPrice>();
    public virtual ICollection<ProductModifier> ProductModifiers { get; set; } = new List<ProductModifier>();
    public virtual ICollection<RecipeBom> RecipeBoms { get; set; } = new List<RecipeBom>();
    public virtual ICollection<OrderItem> OrderItems { get; set; } = new List<OrderItem>();
    public virtual ICollection<CustomerReview> CustomerReviews { get; set; } = new List<CustomerReview>();
}
