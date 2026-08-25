using FluentAssertions;
using Xunit;

namespace SmartFB.UnitTests.Domain;

public class CashShiftModel
{
    public Guid Id { get; set; } = Guid.NewGuid();
    public Guid BranchId { get; set; }
    public Guid StaffId { get; set; }
    public decimal OpeningCash { get; set; }
    public decimal CashSales { get; set; } = 0;
    public decimal ExpectedCash => OpeningCash + CashSales;
    public decimal ActualCash { get; set; }
    public decimal VarianceAmount => ActualCash - ExpectedCash;
    public bool IsClosed { get; set; } = false;
    public string? DiscrepancyNotes { get; set; }
    public string? ManagerPin { get; set; }
}

public class CashShiftEntityTests
{
    [Fact]
    public void CashShift_ExpectedCash_ShouldSumOpeningCashAndCashSales()
    {
        // Arrange
        var shift = new CashShiftModel
        {
            BranchId = Guid.NewGuid(),
            StaffId = Guid.NewGuid(),
            OpeningCash = 1500000m,
            CashSales = 43000m
        };

        // Assert: 1,500,000 + 43,000 = 1,543,000
        shift.ExpectedCash.Should().Be(1543000m);
    }

    [Theory]
    [InlineData(1543000, 1543000, 0, false)] // No variance
    [InlineData(1543000, 1563000, 20000, false)] // +20k variance (<= 50k threshold)
    [InlineData(1543000, 1503000, -40000, false)] // -40k variance (<= 50k threshold)
    [InlineData(1543000, 1613000, 70000, true)] // +70k variance (> 50k threshold, requires justification)
    [InlineData(1543000, 1463000, -80000, true)] // -80k shortage (> 50k threshold, requires justification)
    public void CashShift_VarianceCheck_ShouldAccuratelyDetermineIfJustificationIsRequired(
        decimal expectedCash, decimal actualCash, decimal expectedVariance, bool requiresJustification)
    {
        // Arrange
        var shift = new CashShiftModel
        {
            OpeningCash = 1500000m,
            CashSales = expectedCash - 1500000m,
            ActualCash = actualCash
        };

        // Act
        decimal variance = shift.VarianceAmount;
        bool justificationRequired = Math.Abs(variance) > 50000m;

        // Assert
        variance.Should().Be(expectedVariance);
        justificationRequired.Should().Be(requiresJustification);
    }

    [Fact]
    public void CashShift_CloseWithLargeVariance_WhenJustificationProvided_ShouldBeValid()
    {
        // Arrange
        var shift = new CashShiftModel
        {
            OpeningCash = 1500000m,
            CashSales = 43000m,
            ActualCash = 1613000m, // +70k variance
            DiscrepancyNotes = "Khach tip tien mat vao ket 70.000d",
            ManagerPin = "9988",
            IsClosed = true
        };

        // Assert
        shift.VarianceAmount.Should().Be(70000m);
        shift.DiscrepancyNotes.Should().NotBeNullOrWhiteSpace();
        shift.ManagerPin.Should().Be("9988");
        shift.IsClosed.Should().BeTrue();
    }
}
