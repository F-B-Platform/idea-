using SmartFB.Domain.Common;
using SmartFB.Domain.Enums;

namespace SmartFB.Domain.Entities;

public class InventoryTransaction : BaseEntity
{
    public Guid IngredientId { get; set; }
    public Guid BranchId { get; set; }
    public InventoryTransactionType TransactionType { get; set; }
    public decimal Quantity { get; set; }
    public decimal UnitPrice { get; set; } = 0;
    public decimal TotalCost { get; set; } = 0;
    public string? SupplierName { get; set; }
    public string? InvoiceImageUrl { get; set; }
    public string? Notes { get; set; }
    public Guid? CreatedByUserId { get; set; }

    // Navigation Properties
    public virtual Ingredient Ingredient { get; set; } = null!;
    public virtual Branch Branch { get; set; } = null!;
    public virtual User? CreatedByUser { get; set; }
}
