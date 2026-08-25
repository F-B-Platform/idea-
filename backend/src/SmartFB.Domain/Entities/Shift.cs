using SmartFB.Domain.Common;
using SmartFB.Domain.Enums;

namespace SmartFB.Domain.Entities;

public class Shift : BaseEntity, IAggregateRoot
{
    public Guid BranchId { get; set; }
    public Guid CashierId { get; set; }
    public DateTime OpeningTime { get; set; } = DateTime.UtcNow;
    public DateTime? ClosingTime { get; set; }
    public decimal InitialCash { get; set; }
    public decimal? ActualCashCounted { get; set; }
    public decimal SystemCashCalculated { get; set; } = 0;
    public decimal CashDifference { get; set; } = 0;
    public string? ShiftNotes { get; set; }
    public ShiftStatus Status { get; set; } = ShiftStatus.Open;

    // Navigation Properties
    public virtual Branch Branch { get; set; } = null!;
    public virtual User Cashier { get; set; } = null!;
    public virtual ZReport? ZReport { get; set; }
}
