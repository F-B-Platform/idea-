using FluentAssertions;
using FluentValidation;
using SmartFB.UnitTests.Features.ShiftsAndCash;
using Xunit;

namespace SmartFB.UnitTests.Validators;

public class CloseCashShiftValidator : AbstractValidator<CloseCashShiftCommand>
{
    public CloseCashShiftValidator()
    {
        RuleFor(x => x.ShiftId).NotEmpty().WithMessage("Mã ca làm việc không được để trống.");
        RuleFor(x => x.ActualCash).GreaterThanOrEqualTo(0).WithMessage("Tiền thực đếm không thể là số âm.");

        When(x => Math.Abs(x.ActualCash - x.ExpectedCash) > 50000m, () =>
        {
            RuleFor(x => x.DiscrepancyReason)
                .NotEmpty().WithMessage("Bắt buộc phải nhập lý do giải trình khi độ lệch két tiền lớn hơn 50.000 VNĐ.");
            RuleFor(x => x.ManagerPin)
                .NotEmpty().WithMessage("Bắt buộc phải nhập mã PIN của Quản lý khi độ lệch két tiền lớn hơn 50.000 VNĐ.");
        });
    }
}

public class CloseCashShiftValidatorTests
{
    private readonly CloseCashShiftValidator _validator = new();

    [Fact]
    public void Validate_WithinThresholdVariance_WithoutJustification_ShouldPass()
    {
        // Arrange: Variance is +20,000 VND (<= 50k)
        var command = new CloseCashShiftCommand(
            ShiftId: Guid.NewGuid(),
            ExpectedCash: 1543000m,
            ActualCash: 1563000m
        );

        // Act
        var result = _validator.Validate(command);

        // Assert
        result.IsValid.Should().BeTrue();
    }

    [Fact]
    public void Validate_OverThresholdVariance_WithoutJustification_ShouldFail()
    {
        // Arrange: Variance is +70,000 VND (> 50k)
        var command = new CloseCashShiftCommand(
            ShiftId: Guid.NewGuid(),
            ExpectedCash: 1543000m,
            ActualCash: 1613000m,
            DiscrepancyReason: "",
            ManagerPin: ""
        );

        // Act
        var result = _validator.Validate(command);

        // Assert
        result.IsValid.Should().BeFalse();
        result.Errors.Should().Contain(e => e.PropertyName == nameof(CloseCashShiftCommand.DiscrepancyReason));
        result.Errors.Should().Contain(e => e.PropertyName == nameof(CloseCashShiftCommand.ManagerPin));
    }

    [Fact]
    public void Validate_OverThresholdVariance_WithJustification_ShouldPass()
    {
        // Arrange: Variance is +70,000 VND with explanation and PIN
        var command = new CloseCashShiftCommand(
            ShiftId: Guid.NewGuid(),
            ExpectedCash: 1543000m,
            ActualCash: 1613000m,
            DiscrepancyReason: "Khách tip vào két",
            ManagerPin: "9988"
        );

        // Act
        var result = _validator.Validate(command);

        // Assert
        result.IsValid.Should().BeTrue();
    }
}
