using SmartFB.Domain.Common;

namespace SmartFB.Domain.Entities;

public class ZReport : BaseEntity, IAggregateRoot
{
    public Guid ShiftId { get; set; }
    public Guid BranchId { get; set; }
    public DateTime ReportDate { get; set; } = DateTime.UtcNow;
    public int TotalOrders { get; set; } = 0;
    public decimal TotalGrossSales { get; set; } = 0;
    public decimal TotalDiscounts { get; set; } = 0;
    public decimal TotalNetSales { get; set; } = 0;
    public decimal TotalCashPayments { get; set; } = 0;
    public decimal TotalVietQrPayments { get; set; } = 0;
    public decimal SystemCash { get; set; } = 0;
    public decimal ActualCash { get; set; } = 0;
    public decimal VarianceAmount { get; set; } = 0;
    public string? VarianceReason { get; set; }
    public Guid GeneratedByUserId { get; set; }

    // Navigation Properties
    public virtual Shift Shift { get; set; } = null!;
    public virtual Branch Branch { get; set; } = null!;
    public virtual User GeneratedByUser { get; set; } = null!;
}
