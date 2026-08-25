using SmartFB.Domain.Common;

namespace SmartFB.Domain.Entities;

public class ReviewImage : BaseEntity
{
    public Guid ReviewId { get; set; }
    public string ImageUrl { get; set; } = string.Empty;
    public bool IsApproved { get; set; } = false;

    // Navigation Properties
    public virtual CustomerReview Review { get; set; } = null!;
}
