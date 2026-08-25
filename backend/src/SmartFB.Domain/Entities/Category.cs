using SmartFB.Domain.Common;

namespace SmartFB.Domain.Entities;

public class Category : AuditableEntity, IAggregateRoot
{
    public string Name { get; set; } = string.Empty;
    public string? Description { get; set; }
    public int DisplayOrder { get; set; } = 0;
    public string? ImageUrl { get; set; }
    public bool IsActive { get; set; } = true;

    // Navigation Properties
    public virtual ICollection<Product> Products { get; set; } = new List<Product>();
}
