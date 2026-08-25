namespace SmartFB.Application.Features.AdminAndAnalytics.DTOs;

public record BranchRevenueDto(
    Guid BranchId,
    string BranchName,
    int TotalOrders,
    decimal Revenue,
    decimal CashRevenue,
    decimal VietQrRevenue
);

public record ConsolidatedRevenueDto(
    DateTime FromDate,
    DateTime ToDate,
    int TotalOrders,
    decimal TotalRevenue,
    decimal TotalDiscounts,
    decimal NetRevenue,
    List<BranchRevenueDto> BranchBreakdowns
);

public record PandLReportDto(
    DateTime FromDate,
    DateTime ToDate,
    decimal GrossRevenue,
    decimal TotalDiscounts,
    decimal NetRevenue,
    decimal TotalCogsCost, // Cost of Goods Sold from BOM recipes
    decimal GrossProfit,
    decimal GrossMarginPercentage,
    decimal EstimatedLaborCost,
    decimal NetOperatingProfit
);

public record AiComboCandidateDto(
    Guid ProductAId,
    string ProductAName,
    Guid ProductBId,
    string ProductBName,
    double Support,
    double Confidence,
    double Lift,
    decimal OriginalCombinedPrice,
    decimal SuggestedComboPrice,
    decimal EstimatedBomCost,
    decimal EstimatedProfitMargin
);

public record ApproveAiComboRequestDto(
    Guid ProductAId,
    Guid ProductBId,
    string ComboName,
    decimal FinalPrice,
    DateTime ActiveFrom,
    DateTime ActiveTo
);

public record AuditLogEntryDto(
    Guid AuditId,
    Guid? UserId,
    string? UserName,
    string Action,
    string EntityName,
    string EntityId,
    string? OldValues,
    string? NewValues,
    string? IpAddress,
    DateTime Timestamp
);
