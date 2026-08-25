using SmartFB.Domain.Common;

namespace SmartFB.Domain.Entities;

public class Product : BaseEntity, IAggregateRoot
{
    public string ProductCode { get; set; } = string.Empty;
    public string Name { get; set; } = string.Empty;
    public string Description { get; set; } = string.Empty;
    public decimal BasePrice { get; set; }
    public string? ImageUrl { get; set; }
    public Guid CategoryId { get; set; }
    public bool IsAvailable { get; set; } = true; // 86-Toggle status
}
