using SmartFB.Domain.Common;

namespace SmartFB.Domain.Entities;

public class RecipeBom : AuditableEntity
{
    public Guid ProductId { get; set; }
    public Guid SizeId { get; set; }
    public Guid IngredientId { get; set; }
    public decimal StandardQuantity { get; set; } // Precision(10,3) in grams/ml
    public decimal WastagePercentage { get; set; } = 0;

    // Navigation Properties
    public virtual Product Product { get; set; } = null!;
    public virtual ProductSize ProductSize { get; set; } = null!;
    public virtual Ingredient Ingredient { get; set; } = null!;
}
