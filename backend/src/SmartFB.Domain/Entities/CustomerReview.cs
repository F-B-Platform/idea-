using SmartFB.Domain.Common;

namespace SmartFB.Domain.Entities;

public class CustomerReview : BaseEntity, IAggregateRoot
{
    public Guid OrderId { get; set; }
    public Guid? ProductId { get; set; }
    public Guid? CustomerId { get; set; }
    public int RatingStars { get; set; }
    public string? Comment { get; set; }
    public string? PhotoUrls { get; set; }
    public bool IsAnonymous { get; set; } = false;
    public bool IsApproved { get; set; } = false;
    public bool IsUrgentAlert { get; set; } = false; // Auto true if RatingStars <= 2

    // Navigation Properties
    public virtual Order Order { get; set; } = null!;
    public virtual Product? Product { get; set; }
    public virtual Customer? Customer { get; set; }
    public virtual ICollection<ReviewImage> ReviewImages { get; set; } = new List<ReviewImage>();
}
