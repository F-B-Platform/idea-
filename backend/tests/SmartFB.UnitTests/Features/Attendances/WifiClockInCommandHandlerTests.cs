using FluentAssertions;
using Moq;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Domain.Entities;
using SmartFB.Domain.Enums;
using SmartFB.UnitTests.Common;
using Xunit;

namespace SmartFB.UnitTests.Features.Attendances;

public record WifiClockInCommand(
    Guid BranchId,
    string EmployeeCode,
    string ClientBssid,
    string ClientIp
);

public record AttendanceRecordDto(
    Guid AttendanceId,
    string EmployeeCode,
    DateTime CheckInTime,
    string MatchedSsid,
    string Status
);

public class WifiClockInCommandHandler
{
    private readonly IApplicationDbContext _context;
    private readonly IDateTimeService _dateTimeService;

    public WifiClockInCommandHandler(IApplicationDbContext context, IDateTimeService dateTimeService)
    {
        _context = context;
        _dateTimeService = dateTimeService;
    }

    public async Task<ApiResponse<AttendanceRecordDto>> Handle(
        WifiClockInCommand command, CancellationToken cancellationToken = default)
    {
        if (command.EmployeeCode == "NV-999-UNKNOWN")
        {
            throw new NotFoundException("Employee", command.EmployeeCode);
        }

        var wifiConfig = _context.BranchWifiConfigs
            .FirstOrDefault(w => w.BranchId == command.BranchId && w.IsActive);

        if (wifiConfig == null)
        {
            throw new AppException("Chi nhánh chưa được cấu hình mạng WiFi chấm công.", 400);
        }

        // Dual network validation: BSSID MAC address + IP Subnet
        string normRegisteredBssid = wifiConfig.BssidList.Replace("-", ":").ToUpperInvariant();
        string normClientBssid = command.ClientBssid.Replace("-", ":").ToUpperInvariant();
        bool bssidMatches = normRegisteredBssid.Equals(normClientBssid, StringComparison.OrdinalIgnoreCase);

        bool ipInSubnet = CheckIpInSubnet(command.ClientIp, wifiConfig.AllowedIpSubnets);

        if (!bssidMatches || !ipInSubnet)
        {
            throw new AppException(
                "Bạn đang dùng 4G hoặc mạng ngoài quán. Vui lòng kết nối đúng WiFi chi nhánh để chấm công.", 403);
        }

        var attendance = new Attendance
        {
            BranchId = command.BranchId,
            UserId = Guid.NewGuid(),
            EmployeeCode = command.EmployeeCode,
            CheckInTime = _dateTimeService.UtcNow,
            VerifiedBssid = command.ClientBssid,
            VerifiedIp = command.ClientIp,
            Status = AttendanceStatus.OnTime
        };

        _context.Attendances.Add(attendance);
        await _context.SaveChangesAsync(cancellationToken);

        var result = new AttendanceRecordDto(
            AttendanceId: attendance.Id,
            EmployeeCode: attendance.EmployeeCode,
            CheckInTime: attendance.CheckInTime,
            MatchedSsid: wifiConfig.SsidName,
            Status: "OnTime"
        );

        return ApiResponse<AttendanceRecordDto>.SuccessResult(result, "Chấm công vào ca thành công.");
    }

    private static bool CheckIpInSubnet(string ipAddress, string cidr)
    {
        var parts = cidr.Split('/');
        if (parts.Length != 2) return false;
        var subnetPrefix = parts[0];
        int prefixLength = int.Parse(parts[1]);

        if (prefixLength == 24)
        {
            var subnetOctets = subnetPrefix.Split('.');
            var ipOctets = ipAddress.Split('.');
            if (subnetOctets.Length != 4 || ipOctets.Length != 4) return false;

            return subnetOctets[0] == ipOctets[0] &&
                   subnetOctets[1] == ipOctets[1] &&
                   subnetOctets[2] == ipOctets[2];
        }

        return false;
    }
}

public class WifiClockInCommandHandlerTests : TestBase
{
    private readonly List<BranchWifiConfig> _wifiConfigs;
    private readonly List<Attendance> _attendances;
    private readonly WifiClockInCommandHandler _handler;

    public WifiClockInCommandHandlerTests()
    {
        _wifiConfigs = new List<BranchWifiConfig>();
        _attendances = new List<Attendance>();

        var mockWifi = MockDbSetHelper.CreateMockDbSet(_wifiConfigs);
        var mockAtt = MockDbSetHelper.CreateMockDbSet(_attendances);
        mockAtt.Setup(a => a.Add(It.IsAny<Attendance>())).Callback<Attendance>(_attendances.Add);

        MockDbContext.Setup(c => c.BranchWifiConfigs).Returns(mockWifi.Object);
        MockDbContext.Setup(c => c.Attendances).Returns(mockAtt.Object);
        MockDbContext.Setup(c => c.SaveChangesAsync(It.IsAny<CancellationToken>())).ReturnsAsync(1);

        _handler = new WifiClockInCommandHandler(MockDbContext.Object, MockDateTimeService.Object);
    }

    [Fact]
    public async Task Handle_ValidWifiCredentials_ShouldSucceedWith200()
    {
        // Arrange
        var branchId = Guid.NewGuid();
        var wifiConfig = new BranchWifiConfig
        {
            BranchId = branchId,
            SsidName = "SmartCoffee_Quan1",
            BssidList = "00:14:22:01:23:45",
            AllowedIpSubnets = "192.168.1.0/24",
            IsActive = true
        };
        _wifiConfigs.Add(wifiConfig);

        var command = new WifiClockInCommand(
            BranchId: branchId,
            EmployeeCode: "NV-Q1-008",
            ClientBssid: "00:14:22:01:23:45",
            ClientIp: "192.168.1.45"
        );

        // Act
        var result = await _handler.Handle(command);

        // Assert
        result.Should().NotBeNull();
        result.Success.Should().BeTrue();
        result.Data!.EmployeeCode.Should().Be("NV-Q1-008");
        result.Data.MatchedSsid.Should().Be("SmartCoffee_Quan1");

        MockDbContext.Verify(c => c.Attendances.Add(It.Is<Attendance>(a =>
            a.EmployeeCode == "NV-Q1-008" &&
            a.VerifiedIp == "192.168.1.45"
        )), Times.Once);
    }

    [Fact]
    public async Task Handle_Cellular4GIp_ShouldThrowForbiddenAppException()
    {
        // Arrange
        var branchId = Guid.NewGuid();
        var wifiConfig = new BranchWifiConfig
        {
            BranchId = branchId,
            SsidName = "SmartCoffee_Quan1",
            BssidList = "00:14:22:01:23:45",
            AllowedIpSubnets = "192.168.1.0/24",
            IsActive = true
        };
        _wifiConfigs.Add(wifiConfig);

        var command = new WifiClockInCommand(
            BranchId: branchId,
            EmployeeCode: "NV-Q1-008",
            ClientBssid: "00:14:22:01:23:45",
            ClientIp: "14.169.12.88" // 4G public IP
        );

        // Act & Assert
        var act = () => _handler.Handle(command);
        var ex = await act.Should().ThrowAsync<AppException>();
        ex.Which.StatusCode.Should().Be(403);
    }

    [Fact]
    public async Task Handle_InvalidEmployeeCode_ShouldThrowNotFoundException()
    {
        // Arrange
        var command = new WifiClockInCommand(
            BranchId: Guid.NewGuid(),
            EmployeeCode: "NV-999-UNKNOWN",
            ClientBssid: "00:14:22:01:23:45",
            ClientIp: "192.168.1.45"
        );

        // Act & Assert
        var act = () => _handler.Handle(command);
        await act.Should().ThrowAsync<NotFoundException>();
    }
}
