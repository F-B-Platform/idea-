using System.Net;
using System.Net.Http.Json;
using System.Text.Json;
using FluentAssertions;
using SmartFB.Application.Features.Attendances.Commands.WifiClockIn;
using SmartFB.Application.Features.Attendances.Commands.WifiClockOut;
using SmartFB.IntegrationTests.Fixtures;
using Xunit;

namespace SmartFB.IntegrationTests.Endpoints;

public class WifiAttendanceFlowTests : IClassFixture<CustomWebApplicationFactory>
{
    private readonly HttpClient _client;

    public WifiAttendanceFlowTests(CustomWebApplicationFactory factory)
    {
        _client = factory.CreateClient();
    }

    [Fact]
    public async Task UAT_WifiAttendance_ValidBranchWifi_ShouldClockInSuccessfully()
    {
        // Arrange (TC-ATT-01): Correct branch BSSID and subnet IP
        var checkInReq = new WifiClockInCommand(
            BranchId: SeedDataConstants.BranchQ1Id,
            EmployeeCode: "NV-Q1-008",
            ClientIp: SeedDataConstants.ValidSubnetIp,
            ClientBssid: SeedDataConstants.ValidBssid
        );

        // Act
        var response = await _client.PostAsJsonAsync("/api/v1/attendances/clock-in", checkInReq);

        // Assert
        response.StatusCode.Should().Be(HttpStatusCode.OK);
        var result = await response.Content.ReadFromJsonAsync<JsonElement>();
        var data = result.GetProperty("data");

        data.GetProperty("employeeCode").GetString().Should().Be("NV-Q1-008");
        data.GetProperty("verifiedBssid").GetString().Should().Be(SeedDataConstants.ValidBssid);
    }

    [Fact]
    public async Task UAT_WifiAttendance_Cellular4GIp_ShouldFailValidation()
    {
        // Arrange (TC-ATT-02): Outside public 4G IP
        var checkInReq = new WifiClockInCommand(
            BranchId: SeedDataConstants.BranchQ1Id,
            EmployeeCode: "NV-Q1-008",
            ClientIp: SeedDataConstants.Cellular4GIp, // 14.169.12.88
            ClientBssid: SeedDataConstants.ValidBssid
        );

        // Act
        var response = await _client.PostAsJsonAsync("/api/v1/attendances/clock-in", checkInReq);

        // Assert
        response.StatusCode.Should().Be(HttpStatusCode.BadRequest);
    }

    [Fact]
    public async Task UAT_WifiAttendance_UnknownEmployeeCode_ShouldFailValidation()
    {
        // Arrange (TC-ATT-03): Non-existent employee code
        var checkInReq = new WifiClockInCommand(
            BranchId: SeedDataConstants.BranchQ1Id,
            EmployeeCode: "NV-999-UNKNOWN",
            ClientIp: SeedDataConstants.ValidSubnetIp,
            ClientBssid: SeedDataConstants.ValidBssid
        );

        // Act
        var response = await _client.PostAsJsonAsync("/api/v1/attendances/clock-in", checkInReq);

        // Assert
        response.StatusCode.Should().Be(HttpStatusCode.BadRequest);
    }
}
