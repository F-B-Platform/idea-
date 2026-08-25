using SmartFB.Domain.Enums;

namespace SmartFB.Application.Features.ShiftsAndCash.DTOs;

public record ShiftDto(
    Guid Id,
    Guid BranchId,
    Guid CashierId,
    string CashierName,
    DateTime OpeningTime,
    DateTime? ClosingTime,
    decimal InitialCash,
    decimal? ActualCashCounted,
    decimal SystemCashCalculated,
    decimal CashDifference,
    string? ShiftNotes,
    ShiftStatus Status
);

public record OpenShiftRequestDto(
    Guid BranchId,
    decimal InitialCash,
    string? Notes
);

public record CloseShiftRequestDto(
    decimal ActualCashCounted,
    string? VarianceNotes
);

public record ZReportDto(
    Guid Id,
    Guid ShiftId,
    Guid BranchId,
    string BranchName,
    DateTime ReportDate,
    int TotalOrders,
    decimal TotalGrossSales,
    decimal TotalDiscounts,
    decimal TotalNetSales,
    decimal TotalCashPayments,
    decimal TotalVietQrPayments,
    decimal SystemCash,
    decimal ActualCash,
    decimal VarianceAmount,
    string? VarianceReason,
    string GeneratedByUserName
);
