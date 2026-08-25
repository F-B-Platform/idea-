using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.ShiftsAndCash.DTOs;
using SmartFB.Domain.Entities;
using SmartFB.Domain.Enums;

namespace SmartFB.Application.Features.ShiftsAndCash.Commands.OpenCashShift;

public record OpenCashShiftCommand(
    Guid BranchId,
    Guid CashierId,
    decimal InitialCash,
    string? Notes
) : IRequest<ApiResponse<ShiftDto>>;

public class OpenCashShiftCommandHandler : IRequestHandler<OpenCashShiftCommand, ApiResponse<ShiftDto>>
{
    private readonly IApplicationDbContext _context;

    public OpenCashShiftCommandHandler(IApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<ApiResponse<ShiftDto>> Handle(OpenCashShiftCommand request, CancellationToken cancellationToken)
    {
        var existingOpenShift = await _context.Shifts
            .FirstOrDefaultAsync(s => s.BranchId == request.BranchId && s.Status == ShiftStatus.Open && !s.IsDeleted, cancellationToken);

        if (existingOpenShift != null)
        {
            throw new AppException("Chi nhánh hiện đang có một ca két tiền đang mở. Vui lòng kết ca trước khi mở ca mới.");
        }

        var cashier = await _context.Users
            .FirstOrDefaultAsync(u => u.Id == request.CashierId && !u.IsDeleted, cancellationToken);

        if (cashier == null)
        {
            throw new NotFoundException("User", request.CashierId);
        }

        var shift = new Shift
        {
            BranchId = request.BranchId,
            CashierId = request.CashierId,
            OpeningTime = DateTime.UtcNow,
            InitialCash = request.InitialCash,
            SystemCashCalculated = request.InitialCash, // Starting with initial float cash
            ShiftNotes = request.Notes,
            Status = ShiftStatus.Open
        };

        _context.Shifts.Add(shift);
        await _context.SaveChangesAsync(cancellationToken);

        var dto = new ShiftDto(
            shift.Id,
            shift.BranchId,
            shift.CashierId,
            cashier.FullName,
            shift.OpeningTime,
            shift.ClosingTime,
            shift.InitialCash,
            shift.ActualCashCounted,
            shift.SystemCashCalculated,
            shift.CashDifference,
            shift.ShiftNotes,
            shift.Status
        );

        return ApiResponse<ShiftDto>.SuccessResult(dto, "Mở ca làm việc két tiền thành công.");
    }
}
