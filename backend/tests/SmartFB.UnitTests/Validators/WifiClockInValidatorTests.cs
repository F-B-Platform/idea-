using FluentAssertions;
using FluentValidation;
using SmartFB.UnitTests.Features.Attendances;
using Xunit;

namespace SmartFB.UnitTests.Validators;

public class WifiClockInValidator : AbstractValidator<WifiClockInCommand>
{
    public WifiClockInValidator()
    {
        RuleFor(x => x.BranchId).NotEmpty().WithMessage("Chi nhánh không được để trống.");
        RuleFor(x => x.EmployeeCode).NotEmpty().WithMessage("Mã nhân viên không được để trống.");
        RuleFor(x => x.ClientBssid)
            .NotEmpty().WithMessage("Địa chỉ BSSID không được để trống.")
            .Matches(@"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$").WithMessage("Định dạng địa chỉ MAC BSSID không hợp lệ.");
        RuleFor(x => x.ClientIp)
            .NotEmpty().WithMessage("Địa chỉ IP client không được để trống.")
            .Matches(@"^(\d{1,3}\.){3}\d{1,3}$").WithMessage("Định dạng địa chỉ IP không hợp lệ.");
    }
}

public class WifiClockInValidatorTests
{
    private readonly WifiClockInValidator _validator = new();

    [Fact]
    public void Validate_ValidWifiParameters_ShouldPass()
    {
        // Arrange
        var command = new WifiClockInCommand(
            BranchId: Guid.NewGuid(),
            EmployeeCode: "NV-Q1-008",
            ClientBssid: "00:14:22:01:23:45",
            ClientIp: "192.168.1.45"
        );

        // Act
        var result = _validator.Validate(command);

        // Assert
        result.IsValid.Should().BeTrue();
    }

    [Theory]
    [InlineData("invalid-mac")]
    [InlineData("00:14:22:01:23")] // Only 5 octets
    [InlineData("00:14:22:01:23:ZZ")] // Non-hex char
    public void Validate_InvalidBssid_ShouldFail(string bssid)
    {
        // Arrange
        var command = new WifiClockInCommand(
            BranchId: Guid.NewGuid(),
            EmployeeCode: "NV-Q1-008",
            ClientBssid: bssid,
            ClientIp: "192.168.1.45"
        );

        // Act
        var result = _validator.Validate(command);

        // Assert
        result.IsValid.Should().BeFalse();
        result.Errors.Should().Contain(e => e.PropertyName == nameof(WifiClockInCommand.ClientBssid));
    }

    [Theory]
    [InlineData("")]
    [InlineData("not-an-ip")]
    public void Validate_InvalidClientIp_ShouldFail(string ip)
    {
        // Arrange
        var command = new WifiClockInCommand(
            BranchId: Guid.NewGuid(),
            EmployeeCode: "NV-Q1-008",
            ClientBssid: "00:14:22:01:23:45",
            ClientIp: ip
        );

        // Act
        var result = _validator.Validate(command);

        // Assert
        result.IsValid.Should().BeFalse();
        result.Errors.Should().Contain(e => e.PropertyName == nameof(WifiClockInCommand.ClientIp));
    }
}
