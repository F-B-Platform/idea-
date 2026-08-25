using FluentAssertions;
using FluentValidation;
using SmartFB.UnitTests.Features.Auth;
using Xunit;

namespace SmartFB.UnitTests.Validators;

public class LoginUserCommandValidator : AbstractValidator<LoginUserCommand>
{
    public LoginUserCommandValidator()
    {
        RuleFor(x => x.Username).NotEmpty().WithMessage("Tên đăng nhập hoặc mã nhân viên không được để trống.");
        RuleFor(x => x.Password).NotEmpty().MinimumLength(6).WithMessage("Mật khẩu phải từ 6 ký tự trở lên.");
    }
}

public class LoginUserCommandValidatorTests
{
    private readonly LoginUserCommandValidator _validator = new();

    [Fact]
    public void Validate_ValidUsernameAndPassword_ShouldPass()
    {
        var command = new LoginUserCommand("NV-Q1-001", "Password@123");
        var result = _validator.Validate(command);
        result.IsValid.Should().BeTrue();
    }

    [Theory]
    [InlineData("", "123456")]
    [InlineData("user", "")]
    [InlineData("user", "123")] // Short password
    public void Validate_InvalidInputs_ShouldFail(string username, string password)
    {
        var command = new LoginUserCommand(username, password);
        var result = _validator.Validate(command);
        result.IsValid.Should().BeFalse();
    }
}
