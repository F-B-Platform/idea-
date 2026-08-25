using FluentAssertions;
using Moq;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Domain.Entities;
using SmartFB.UnitTests.Common;
using Xunit;

namespace SmartFB.UnitTests.Features.Attendances;

public record WifiClockOutCommand(
    Guid BranchId,
    string EmployeeCode,
    string ClientBssid,
    string ClientIp
);

public record ClockOutResultDto(
    Guid AttendanceId,
    string EmployeeCode,
    DateTime CheckInTime,
    DateTime CheckOutTime,
    double TotalHoursWorked
);

public class WifiClockOutCommandHandler
{
    private readonly IApplicationDbContext _context;
    private readonly IDateTimeService _dateTimeService;

    public WifiClockOutCommandHandler(IApplicationDbContext context, IDateTimeService dateTimeService)
    {
        _context = context;
        _dateTimeService = dateTimeService;
    }

    public async Task<ApiResponse<ClockOutResultDto>> Handle(
        WifiClockOutCommand command, CancellationToken cancellationToken = default)
    {
        var attendance = _context.Attendances
            .FirstOrDefault(a => a.StaffCode == command.EmployeeCode && a.CheckOutTime == null);

        if (attendance == null)
        {
            throw new AppException("Không tìm thấy phiên làm việc chưa kết ca của nhân viên này.", 404);
        }

        attendance.CheckOutTime = _dateTimeService.UtcNow;
        var totalHours = (attendance.CheckOutTime.Value - attendance.CheckInTime).TotalHours;

        await _context.SaveChangesAsync(cancellationToken);

        var result = new ClockOutResultDto(
            AttendanceId: attendance.Id,
            EmployeeCode: attendance.StaffCode,
            CheckInTime: attendance.CheckInTime,
            CheckOutTime: attendance.CheckOutTime.Value,
            TotalHoursWorked: Math.Round(totalHours, 2)
        );

        return ApiResponse<ClockOutResultDto>.SuccessResult(result, "Chấm công ra ca thành công.");
    }
}

public class WifiClockOutCommandHandlerTests : TestBase
{
    private readonly List<Attendance> _attendances;
    private readonly WifiClockOutCommandHandler _handler;

    public WifiClockOutCommandHandlerTests()
    {
        _attendances = new List<Attendance>();
        var mockAtt = MockDbSetHelper.CreateMockDbSet(_attendances);
        MockDbContext.Setup(c => c.Attendances).Returns(mockAtt.Object);
        MockDbContext.Setup(c => c.SaveChangesAsync(It.IsAny<CancellationToken>())).ReturnsAsync(1);

        _handler = new WifiClockOutCommandHandler(MockDbContext.Object, MockDateTimeService.Object);
    }

    [Fact]
    public async Task Handle_ValidClockOut_ShouldCalculateTotalHoursWorked()
    {
        // Arrange: Checked in 8 hours earlier
        var checkInTime = MockDateTimeService.Object.UtcNow.AddHours(-8);
        var attendance = new Attendance
        {
            BranchId = Guid.NewGuid(),
            StaffCode = "NV-Q1-008",
            CheckInTime = checkInTime,
            CheckOutTime = null,
            IsWifiVerified = true
        };
        _attendances.Add(attendance);

        var command = new WifiClockOutCommand(
            BranchId: attendance.BranchId,
            EmployeeCode: "NV-Q1-008",
            ClientBssid: "00:14:22:01:23:45",
            ClientIp: "192.168.1.45"
        );

        // Act
        var result = await _handler.Handle(command);

        // Assert
        result.Should().NotBeNull();
        result.Success.Should().BeTrue();
        result.Data!.TotalHoursWorked.Should().Be(8.0);
        attendance.CheckOutTime.Should().NotBeNull();
    }
}
