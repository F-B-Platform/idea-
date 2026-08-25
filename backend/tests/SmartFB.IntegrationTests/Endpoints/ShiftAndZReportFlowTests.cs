using System.Net;
using System.Net.Http.Json;
using System.Text.Json;
using FluentAssertions;
using SmartFB.Application.Features.ShiftsAndCash.Commands.CloseCashShift;
using SmartFB.Application.Features.ShiftsAndCash.Commands.OpenCashShift;
using SmartFB.IntegrationTests.Fixtures;
using Xunit;

namespace SmartFB.IntegrationTests.Endpoints;

public class ShiftAndZReportFlowTests : IClassFixture<CustomWebApplicationFactory>
{
    private readonly HttpClient _client;

    public ShiftAndZReportFlowTests(CustomWebApplicationFactory factory)
    {
        _client = factory.CreateClient();
    }

    [Fact]
    public async Task UAT_ShiftOpenAndClose_ShouldHandleCashShiftCycleAndZReport()
    {
        // 1. Arrange & Act (TC-SHIFT-01): Open Shift with 1,500,000 VND initial cash
        var openReq = new OpenCashShiftCommand(
            BranchId: SeedDataConstants.BranchQ1Id,
            CashierId: SeedDataConstants.CashierUserId,
            InitialCash: 1500000m,
            Notes: "Dau ca sang"
        );

        var openResponse = await _client.PostAsJsonAsync("/api/v1/shifts/open", openReq);
        openResponse.StatusCode.Should().Be(HttpStatusCode.OK);
        var openResult = await openResponse.Content.ReadFromJsonAsync<JsonElement>();
        var shiftData = openResult.GetProperty("data");
        Guid shiftId = Guid.Parse(shiftData.GetProperty("id").GetString()!);
        shiftData.GetProperty("initialCash").GetDecimal().Should().Be(1500000m);

        // 2. Act (TC-SHIFT-02): Close Shift with large variance (> 50k) without justification -> Should fail
        var closeWithoutNotesReq = new CloseCashShiftCommand(
            ShiftId: shiftId,
            ActualCashCounted: 1613000m, // +113k variance > 50k threshold
            VarianceNotes: null
        );

        var failCloseResponse = await _client.PostAsJsonAsync("/api/v1/shifts/close", closeWithoutNotesReq);
        failCloseResponse.IsSuccessStatusCode.Should().BeFalse();

        // 3. Act (TC-SHIFT-02/03): Close Shift with explanation -> Should generate Z-Report
        var closeWithNotesReq = new CloseCashShiftCommand(
            ShiftId: shiftId,
            ActualCashCounted: 1613000m,
            VarianceNotes: "Khach tip tien mat 113.000d vao ket"
        );

        var successCloseResponse = await _client.PostAsJsonAsync("/api/v1/shifts/close", closeWithNotesReq);
        successCloseResponse.StatusCode.Should().Be(HttpStatusCode.OK);
        var zReportResult = await successCloseResponse.Content.ReadFromJsonAsync<JsonElement>();
        var zReportData = zReportResult.GetProperty("data");

        zReportData.GetProperty("actualCash").GetDecimal().Should().Be(1613000m);
        zReportData.GetProperty("varianceAmount").GetDecimal().Should().Be(113000m);
        zReportData.GetProperty("varianceReason").GetString().Should().Contain("Khach tip");
    }
}
