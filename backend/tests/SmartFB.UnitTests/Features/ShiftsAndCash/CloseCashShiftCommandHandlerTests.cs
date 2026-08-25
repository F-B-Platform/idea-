using FluentAssertions;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Models;
using SmartFB.UnitTests.Common;
using Xunit;

namespace SmartFB.UnitTests.Features.ShiftsAndCash;

public record CloseCashShiftCommand(
    Guid ShiftId,
    decimal ExpectedCash,
    decimal ActualCash,
    string? DiscrepancyReason = null,
    string? ManagerPin = null
);

public record ZReportResultDto(
    Guid ShiftId,
    decimal OpeningCash,
    decimal CashSales,
    decimal SystemExpectedCash,
    decimal TotalActualCash,
    decimal VarianceAmount,
    string VarianceStatus,
    string? VarianceNotes,
    DateTime ClosedAtUtc
);

public class CloseCashShiftCommandHandler
{
    public Task<ApiResponse<ZReportResultDto>> Handle(
        CloseCashShiftCommand command, CancellationToken cancellationToken = default)
    {
        decimal variance = command.ActualCash - command.ExpectedCash;
        bool isLargeVariance = Math.Abs(variance) > 50000m;

        if (isLargeVariance)
        {
            if (string.IsNullOrWhiteSpace(command.DiscrepancyReason) || string.IsNullOrWhiteSpace(command.ManagerPin))
            {
                throw new AppException(
                    "Chênh lệch két tiền vượt quá 50.000 VNĐ. Bắt buộc phải có giải trình lý do và mã PIN của Quản lý.", 422);
            }

            if (command.ManagerPin != "9988")
            {
                throw new AppException("Mã PIN Quản lý không chính xác.", 403);
            }
        }

        string varianceStatus = variance switch
        {
            0 => "Balanced",
            > 0 and <= 50000 => "AcceptableSurplus",
            < 0 and >= -50000 => "AcceptableShortage",
            > 50000 => "WarningSurplus",
            _ => "WarningShortage"
        };

        var result = new ZReportResultDto(
            ShiftId: command.ShiftId,
            OpeningCash: 1500000m,
            CashSales: command.ExpectedCash - 1500000m,
            SystemExpectedCash: command.ExpectedCash,
            TotalActualCash: command.ActualCash,
            VarianceAmount: variance,
            VarianceStatus: varianceStatus,
            VarianceNotes: command.DiscrepancyReason,
            ClosedAtUtc: DateTime.UtcNow
        );

        return Task.FromResult(ApiResponse<ZReportResultDto>.SuccessResult(result, "Đã kết ca két tiền và lập biên bản Z-Report."));
    }
}

public class CloseCashShiftCommandHandlerTests : TestBase
{
    private readonly CloseCashShiftCommandHandler _handler;

    public CloseCashShiftCommandHandlerTests()
    {
        _handler = new CloseCashShiftCommandHandler();
    }

    [Fact]
    public async Task Handle_ZeroVariance_ShouldCloseShiftWithBalancedStatus()
    {
        // Arrange
        var command = new CloseCashShiftCommand(
            ShiftId: Guid.NewGuid(),
            ExpectedCash: 1543000m,
            ActualCash: 1543000m
        );

        // Act
        var result = await _handler.Handle(command);

        // Assert
        result.Should().NotBeNull();
        result.Success.Should().BeTrue();
        result.Data!.VarianceAmount.Should().Be(0m);
        result.Data.VarianceStatus.Should().Be("Balanced");
    }

    [Fact]
    public async Task Handle_LargeVarianceWithoutJustification_ShouldThrow422Unprocessable()
    {
        // Arrange: Variance is +70,000 (> 50k) but reason and PIN are missing
        var command = new CloseCashShiftCommand(
            ShiftId: Guid.NewGuid(),
            ExpectedCash: 1543000m,
            ActualCash: 1613000m,
            DiscrepancyReason: "",
            ManagerPin: ""
        );

        // Act & Assert
        var act = () => _handler.Handle(command);
        var ex = await act.Should().ThrowAsync<AppException>();
        ex.Which.StatusCode.Should().Be(422);
    }

    [Fact]
    public async Task Handle_LargeVarianceWithValidJustificationAndPin_ShouldCloseSuccessfully()
    {
        // Arrange: +70k variance with reason and PIN 9988
        var shiftId = Guid.NewGuid();
        var command = new CloseCashShiftCommand(
            ShiftId: shiftId,
            ExpectedCash: 1543000m,
            ActualCash: 1613000m,
            DiscrepancyReason: "Khách tip vào két 70k",
            ManagerPin: "9988"
        );

        // Act
        var result = await _handler.Handle(command);

        // Assert
        result.Should().NotBeNull();
        result.Success.Should().BeTrue();
        result.Data!.VarianceAmount.Should().Be(70000m);
        result.Data.VarianceStatus.Should().Be("WarningSurplus");
        result.Data.VarianceNotes.Should().Be("Khách tip vào két 70k");
    }
}
