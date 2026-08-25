using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Attendances.DTOs;

namespace SmartFB.Application.Features.Attendances.Commands.WifiClockOut;

public record WifiClockOutCommand(Guid AttendanceId) : IRequest<ApiResponse<AttendanceDto>>;

public class WifiClockOutCommandHandler : IRequestHandler<WifiClockOutCommand, ApiResponse<AttendanceDto>>
{
    private readonly IApplicationDbContext _context;

    public WifiClockOutCommandHandler(IApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<ApiResponse<AttendanceDto>> Handle(WifiClockOutCommand request, CancellationToken cancellationToken)
    {
        var attendance = await _context.Attendances
            .Include(a => a.User)
            .FirstOrDefaultAsync(a => a.Id == request.AttendanceId && !a.IsDeleted, cancellationToken);

        if (attendance == null)
        {
            throw new NotFoundException("Attendance", request.AttendanceId);
        }

        if (attendance.CheckOutTime != null)
        {
            throw new AppException("Lượt chấm công này đã được kết thúc trước đó.");
        }

        attendance.CheckOutTime = DateTime.UtcNow;
        await _context.SaveChangesAsync(cancellationToken);

        var dto = new AttendanceDto(
            attendance.Id,
            attendance.BranchId,
            attendance.UserId,
            attendance.EmployeeCode,
            attendance.User.FullName,
            attendance.CheckInTime,
            attendance.CheckOutTime,
            attendance.VerifiedIp,
            attendance.VerifiedBssid,
            attendance.Status
        );

        return ApiResponse<AttendanceDto>.SuccessResult(dto, "Chấm công ra ca thành công.");
    }
}
