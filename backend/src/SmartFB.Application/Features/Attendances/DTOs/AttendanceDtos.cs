using SmartFB.Domain.Enums;

namespace SmartFB.Application.Features.Attendances.DTOs;

public record AttendanceDto(
    Guid Id,
    Guid BranchId,
    Guid UserId,
    string EmployeeCode,
    string EmployeeName,
    DateTime CheckInTime,
    DateTime? CheckOutTime,
    string VerifiedIp,
    string VerifiedBssid,
    AttendanceStatus Status
);

public record WifiClockInRequestDto(
    Guid BranchId,
    string EmployeeCode,
    string ClientIp,
    string ClientBssid
);

public record WifiClockOutRequestDto(
    Guid AttendanceId
);

public record AttendanceSummaryDto(
    int TotalWorkingDays,
    int OnTimeCount,
    int LateCount,
    double TotalWorkingHours
);
