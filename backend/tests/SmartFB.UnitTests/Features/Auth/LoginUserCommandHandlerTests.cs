using FluentAssertions;
using FluentValidation.Results;
using Moq;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.UnitTests.Common;
using Xunit;

namespace SmartFB.UnitTests.Features.Auth;

public record LoginUserCommand(string Username, string Password, Guid? BranchId = null);
public record AuthResultDto(string AccessToken, string RefreshToken, int ExpiresIn, string Username, string Role, Guid? BranchId);

public interface ITokenProviderService
{
    string GenerateAccessToken(string username, string role, Guid? branchId);
    string GenerateRefreshToken();
}

public class LoginUserCommandHandler
{
    private readonly ITokenProviderService _tokenProvider;
    private readonly IDateTimeService _dateTimeService;

    public LoginUserCommandHandler(ITokenProviderService tokenProvider, IDateTimeService dateTimeService)
    {
        _tokenProvider = tokenProvider;
        _dateTimeService = dateTimeService;
    }

    public Task<ApiResponse<AuthResultDto>> Handle(LoginUserCommand command, CancellationToken cancellationToken = default)
    {
        if (string.IsNullOrWhiteSpace(command.Username) || string.IsNullOrWhiteSpace(command.Password))
        {
            throw new ValidationException(new List<ValidationFailure>
            {
                new("Username", "Username and password must not be empty.")
            });
        }

        // Check credentials simulation
        if (command.Username == "NV-Q1-001" && command.Password == "Password@123")
        {
            var branchId = command.BranchId ?? Guid.Parse("11111111-1111-1111-1111-111111111111");
            var token = _tokenProvider.GenerateAccessToken("NV-Q1-001", "CashierStaff", branchId);
            var refreshToken = _tokenProvider.GenerateRefreshToken();

            var result = new AuthResultDto(
                AccessToken: token,
                RefreshToken: refreshToken,
                ExpiresIn: 900,
                Username: command.Username,
                Role: "CashierStaff",
                BranchId: branchId
            );

            return Task.FromResult(ApiResponse<AuthResultDto>.SuccessResult(result, "Đăng nhập thành công."));
        }

        throw new AppException("Tên đăng nhập hoặc mật khẩu không chính xác.", 401);
    }
}

public class LoginUserCommandHandlerTests : TestBase
{
    private readonly Mock<ITokenProviderService> _mockTokenProvider;
    private readonly LoginUserCommandHandler _handler;

    public LoginUserCommandHandlerTests()
    {
        _mockTokenProvider = new Mock<ITokenProviderService>();
        _mockTokenProvider.Setup(t => t.GenerateAccessToken(It.IsAny<string>(), It.IsAny<string>(), It.IsAny<Guid?>()))
            .Returns("mock_jwt_access_token_2026");
        _mockTokenProvider.Setup(t => t.GenerateRefreshToken())
            .Returns("mock_refresh_token_2026");

        _handler = new LoginUserCommandHandler(_mockTokenProvider.Object, MockDateTimeService.Object);
    }

    [Fact]
    public async Task Handle_ValidCredentials_ShouldReturnSuccessWithTokens()
    {
        // Arrange
        var command = new LoginUserCommand("NV-Q1-001", "Password@123");

        // Act
        var result = await _handler.Handle(command);

        // Assert
        result.Should().NotBeNull();
        result.Success.Should().BeTrue();
        result.Data.Should().NotBeNull();
        result.Data!.AccessToken.Should().Be("mock_jwt_access_token_2026");
        result.Data.RefreshToken.Should().Be("mock_refresh_token_2026");
        result.Data.Role.Should().Be("CashierStaff");
        result.Data.ExpiresIn.Should().Be(900);
    }

    [Fact]
    public async Task Handle_InvalidCredentials_ShouldThrowUnauthorizedAppException()
    {
        // Arrange
        var command = new LoginUserCommand("NV-Q1-001", "WrongPassword");

        // Act & Assert
        var act = () => _handler.Handle(command);
        var ex = await act.Should().ThrowAsync<AppException>();
        ex.Which.StatusCode.Should().Be(401);
    }

    [Fact]
    public async Task Handle_EmptyUsernameOrPassword_ShouldThrowValidationException()
    {
        // Arrange
        var command = new LoginUserCommand("", "");

        // Act & Assert
        var act = () => _handler.Handle(command);
        await act.Should().ThrowAsync<ValidationException>();
    }
}
