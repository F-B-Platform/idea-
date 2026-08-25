using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Attendances.DTOs;
using SmartFB.Domain.Entities;
using SmartFB.Domain.Enums;

namespace SmartFB.Application.Features.Attendances.Commands.WifiClockIn;

public record WifiClockInCommand(
    Guid BranchId,
    string EmployeeCode,
    string ClientIp,
    string ClientBssid
) : IRequest<ApiResponse<AttendanceDto>>;

public class WifiClockInCommandHandler : IRequestHandler<WifiClockInCommand, ApiResponse<AttendanceDto>>
{
    private readonly IApplicationDbContext _context;
    private readonly IWifiAttendanceValidator _wifiValidator;

    public WifiClockInCommandHandler(IApplicationDbContext context, IWifiAttendanceValidator wifiValidator)
    {
        _context = context;
        _wifiValidator = wifiValidator;
    }

    public async Task<ApiResponse<AttendanceDto>> Handle(WifiClockInCommand request, CancellationToken cancellationToken)
    {
        // 1. Pillar 4: Dual WiFi Verification (Router BSSID + Branch Subnet IP)
        var validation = await _wifiValidator.ValidateWifiAsync(request.BranchId, request.ClientIp, request.ClientBssid, cancellationToken);
        if (!validation.IsValid)
        {
            throw new AppException(validation.ErrorMessage ?? "Xác thực WiFi chi nhánh thất bại. Bạn chưa kết nối đúng WiFi chi nhánh.");
        }

        // 2. Validate User/Employee
        var user = await _context.Users
            .FirstOrDefaultAsync(u => (u.EmployeeCode == request.EmployeeCode || u.Username == request.EmployeeCode) && !u.IsDeleted, cancellationToken);

        if (user == null)
        {
            throw new AppException($"Mã nhân viên \"{request.EmployeeCode}\" không tồn tại trong hệ thống.");
        }

        // 3. Prevent duplicate active check-in without checkout
        var today = DateTime.UtcNow.Date;
        var existingActive = await _context.Attendances
            .FirstOrDefaultAsync(a => a.UserId == user.Id && a.CheckInTime >= today && a.CheckOutTime == null && !a.IsDeleted, cancellationToken);

        if (existingActive != null)
        {
            throw new AppException("Bạn đã chấm công vào ca hôm nay và chưa thực hiện ra ca.");
        }

        // 4. Calculate OnTime vs Late based on standard morning shift (07:00 AM)
        var now = DateTime.UtcNow.AddHours(7); // Vietnam local time
        var shiftStartTime = new DateTime(now.Year, now.Month, now.Day, 7, 15, 0); // 15 mins grace period
        var status = (now > shiftStartTime && now.Hour < 12) ? AttendanceStatus.Late : AttendanceStatus.OnTime;

        var attendance = new Attendance
        {
            BranchId = request.BranchId,
            UserId = user.Id,
            EmployeeCode = request.EmployeeCode,
            CheckInTime = DateTime.UtcNow,
            VerifiedIp = request.ClientIp,
            VerifiedBssid = request.ClientBssid,
            Status = status
        };

        _context.Attendances.Add(attendance);
        await _context.SaveChangesAsync(cancellationToken);

        var dto = new AttendanceDto(
            attendance.Id,
            attendance.BranchId,
            attendance.UserId,
            attendance.EmployeeCode,
            user.FullName,
            attendance.CheckInTime,
            attendance.CheckOutTime,
            attendance.VerifiedIp,
            attendance.VerifiedBssid,
            attendance.Status
        );

        return ApiResponse<AttendanceDto>.SuccessResult(dto, $"Chấm công vào ca thành công ({attendance.Status}).");
    }
}
