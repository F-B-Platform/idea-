using SmartFB.Domain.Common;
using SmartFB.Domain.Enums;

namespace SmartFB.Domain.Entities;

public class Voucher : AuditableEntity, IAggregateRoot
{
    public string Code { get; set; } = string.Empty;
    public VoucherDiscountType DiscountType { get; set; }
    public decimal DiscountValue { get; set; }
    public decimal MinOrderValue { get; set; } = 0;
    public decimal? MaxDiscountAmount { get; set; }
    public DateTime StartDate { get; set; }
    public DateTime EndDate { get; set; }
    public int UsageLimit { get; set; } = 1000;
    public int UsedCount { get; set; } = 0;
    public bool IsActive { get; set; } = true;
}
