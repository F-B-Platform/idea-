using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.ShiftsAndCash.DTOs;
using SmartFB.Domain.Enums;

namespace SmartFB.Application.Features.ShiftsAndCash.Queries.GetActiveShift;

public record GetActiveShiftQuery(Guid BranchId) : IRequest<ApiResponse<ShiftDto?>>;

public class GetActiveShiftQueryHandler : IRequestHandler<GetActiveShiftQuery, ApiResponse<ShiftDto?>>
{
    private readonly IApplicationDbContext _context;

    public GetActiveShiftQueryHandler(IApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<ApiResponse<ShiftDto?>> Handle(GetActiveShiftQuery request, CancellationToken cancellationToken)
    {
        var shift = await _context.Shifts
            .AsNoTracking()
            .Include(s => s.Cashier)
            .FirstOrDefaultAsync(s => s.BranchId == request.BranchId && s.Status == ShiftStatus.Open && !s.IsDeleted, cancellationToken);

        if (shift == null)
        {
            return ApiResponse<ShiftDto?>.SuccessResult(null, "Chi nhánh hiện chưa có ca két tiền đang mở.");
        }

        var dto = new ShiftDto(
            shift.Id,
            shift.BranchId,
            shift.CashierId,
            shift.Cashier.FullName,
            shift.OpeningTime,
            shift.ClosingTime,
            shift.InitialCash,
            shift.ActualCashCounted,
            shift.SystemCashCalculated,
            shift.CashDifference,
            shift.ShiftNotes,
            shift.Status
        );

        return ApiResponse<ShiftDto?>.SuccessResult(dto, "Lấy thông tin ca hiện tại thành công.");
    }
}
