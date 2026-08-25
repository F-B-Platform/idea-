using SmartFB.Domain.Common;

namespace SmartFB.Domain.Entities;

public class Ingredient : AuditableEntity, IAggregateRoot
{
    public string Code { get; set; } = string.Empty;
    public string Name { get; set; } = string.Empty;
    public string Unit { get; set; } = "g"; // ml, g, piece, can, pack
    public decimal CurrentStock { get; set; } = 0;
    public decimal MinStockThreshold { get; set; } = 0;
    public decimal UnitCost { get; set; } = 0;

    // Navigation Properties
    public virtual ICollection<RecipeBom> RecipeBoms { get; set; } = new List<RecipeBom>();
    public virtual ICollection<InventoryTransaction> InventoryTransactions { get; set; } = new List<InventoryTransaction>();
}
