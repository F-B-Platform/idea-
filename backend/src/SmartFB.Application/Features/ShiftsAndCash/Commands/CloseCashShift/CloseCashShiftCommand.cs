using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.ShiftsAndCash.DTOs;
using SmartFB.Domain.Entities;
using SmartFB.Domain.Enums;

namespace SmartFB.Application.Features.ShiftsAndCash.Commands.CloseCashShift;

public record CloseCashShiftCommand(
    Guid ShiftId,
    decimal ActualCashCounted,
    string? VarianceNotes
) : IRequest<ApiResponse<ZReportDto>>;

public class CloseCashShiftCommandHandler : IRequestHandler<CloseCashShiftCommand, ApiResponse<ZReportDto>>
{
    private readonly IApplicationDbContext _context;

    public CloseCashShiftCommandHandler(IApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<ApiResponse<ZReportDto>> Handle(CloseCashShiftCommand request, CancellationToken cancellationToken)
    {
        var shift = await _context.Shifts
            .Include(s => s.Branch)
            .Include(s => s.Cashier)
            .FirstOrDefaultAsync(s => s.Id == request.ShiftId && !s.IsDeleted, cancellationToken);

        if (shift == null)
        {
            throw new NotFoundException("Shift", request.ShiftId);
        }

        if (shift.Status != ShiftStatus.Open)
        {
            throw new AppException("Ca làm việc này đã được kết thúc trước đó.");
        }

        // Calculate all orders and payments in this shift
        var shiftOrders = await _context.Orders
            .Where(o => o.BranchId == shift.BranchId && o.CreatedAt >= shift.OpeningTime && (o.Status == OrderStatus.Completed || o.Status == OrderStatus.Paid) && !o.IsDeleted)
            .ToListAsync(cancellationToken);

        var shiftPayments = await _context.Payments
            .Where(p => p.CreatedAt >= shift.OpeningTime && p.Status == PaymentStatus.Paid && !p.IsDeleted)
            .ToListAsync(cancellationToken);

        decimal totalGrossSales = shiftOrders.Sum(o => o.SubTotal);
        decimal totalDiscounts = shiftOrders.Sum(o => o.DiscountAmount);
        decimal totalNetSales = shiftOrders.Sum(o => o.TotalAmount);
        decimal totalCashPayments = shiftPayments.Where(p => p.PaymentMethod == PaymentMethod.Cash).Sum(p => p.Amount);
        decimal totalVietQrPayments = shiftPayments.Where(p => p.PaymentMethod == PaymentMethod.VietQR).Sum(p => p.Amount);

        decimal systemExpectedCash = shift.InitialCash + totalCashPayments;
        decimal varianceAmount = request.ActualCashCounted - systemExpectedCash;

        // Mandatory Rule: If |varianceAmount| > 50,000 VND, VarianceNotes is strictly required!
        if (Math.Abs(varianceAmount) > 50000 && string.IsNullOrWhiteSpace(request.VarianceNotes))
        {
            throw new BusinessRuleException(
                $"Chênh lệch két tiền ({varianceAmount:N0} đ) vượt ngưỡng cho phép 50.000 VNĐ. Bắt buộc phải nhập nội dung giải trình chi tiết.",
                "CASH_VARIANCE_JUSTIFICATION_REQUIRED"
            );
        }

        shift.ClosingTime = DateTime.UtcNow;
        shift.ActualCashCounted = request.ActualCashCounted;
        shift.SystemCashCalculated = systemExpectedCash;
        shift.CashDifference = varianceAmount;
        shift.Status = ShiftStatus.Closed;
        shift.ShiftNotes = string.IsNullOrWhiteSpace(request.VarianceNotes) ? shift.ShiftNotes : $"{shift.ShiftNotes} | Giải trình: {request.VarianceNotes}";

        // Generate Z-Report
        var zReport = new ZReport
        {
            ShiftId = shift.Id,
            BranchId = shift.BranchId,
            ReportDate = DateTime.UtcNow,
            TotalOrders = shiftOrders.Count,
            TotalGrossSales = totalGrossSales,
            TotalDiscounts = totalDiscounts,
            TotalNetSales = totalNetSales,
            TotalCashPayments = totalCashPayments,
            TotalVietQrPayments = totalVietQrPayments,
            SystemCash = systemExpectedCash,
            ActualCash = request.ActualCashCounted,
            VarianceAmount = varianceAmount,
            VarianceReason = request.VarianceNotes,
            GeneratedByUserId = shift.CashierId
        };

        _context.ZReports.Add(zReport);
        await _context.SaveChangesAsync(cancellationToken);

        var reportDto = new ZReportDto(
            zReport.Id,
            zReport.ShiftId,
            zReport.BranchId,
            shift.Branch.Name,
            zReport.ReportDate,
            zReport.TotalOrders,
            zReport.TotalGrossSales,
            zReport.TotalDiscounts,
            zReport.TotalNetSales,
            zReport.TotalCashPayments,
            zReport.TotalVietQrPayments,
            zReport.SystemCash,
            zReport.ActualCash,
            zReport.VarianceAmount,
            zReport.VarianceReason,
            shift.Cashier.FullName
        );

        return ApiResponse<ZReportDto>.SuccessResult(reportDto, "Kết ca thành công và đã xuất biên bản Z-Report.");
    }
}
