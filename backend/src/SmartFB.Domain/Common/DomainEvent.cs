namespace SmartFB.Domain.Common;

public abstract class DomainEvent
{
    public DateTime DateOccurred { get; protected set; } = DateTime.UtcNow;
    public bool IsPublished { get; set; } = false;
}
