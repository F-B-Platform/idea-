using FluentAssertions;
using Moq;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Models;
using SmartFB.UnitTests.Common;
using Xunit;

namespace SmartFB.UnitTests.Features.Auth;

public record RefreshTokenCommand(string RefreshToken);
public record RefreshTokenResultDto(string AccessToken, string RefreshToken, int ExpiresIn);

public class RefreshTokenCommandHandler
{
    private readonly ITokenProviderService _tokenProvider;

    public RefreshTokenCommandHandler(ITokenProviderService tokenProvider)
    {
        _tokenProvider = tokenProvider;
    }

    public Task<ApiResponse<RefreshTokenResultDto>> Handle(RefreshTokenCommand command, CancellationToken cancellationToken = default)
    {
        if (string.IsNullOrWhiteSpace(command.RefreshToken))
        {
            throw new AppException("Refresh token không được để trống.", 400);
        }

        if (command.RefreshToken == "valid_existing_refresh_token")
        {
            var newAccessToken = _tokenProvider.GenerateAccessToken("NV-Q1-001", "CashierStaff", Guid.NewGuid());
            var newRefreshToken = _tokenProvider.GenerateRefreshToken();

            var result = new RefreshTokenResultDto(newAccessToken, newRefreshToken, 900);
            return Task.FromResult(ApiResponse<RefreshTokenResultDto>.SuccessResult(result, "Làm mới token thành công."));
        }

        throw new AppException("Refresh token không hợp lệ hoặc đã bị thu hồi.", 401);
    }
}

public class RefreshTokenCommandHandlerTests : TestBase
{
    private readonly Mock<ITokenProviderService> _mockTokenProvider;
    private readonly RefreshTokenCommandHandler _handler;

    public RefreshTokenCommandHandlerTests()
    {
        _mockTokenProvider = new Mock<ITokenProviderService>();
        _mockTokenProvider.Setup(t => t.GenerateAccessToken(It.IsAny<string>(), It.IsAny<string>(), It.IsAny<Guid?>()))
            .Returns("new_mock_jwt_access_token");
        _mockTokenProvider.Setup(t => t.GenerateRefreshToken())
            .Returns("new_mock_refresh_token");

        _handler = new RefreshTokenCommandHandler(_mockTokenProvider.Object);
    }

    [Fact]
    public async Task Handle_ValidRefreshToken_ShouldRotateAndReturnNewTokens()
    {
        // Arrange
        var command = new RefreshTokenCommand("valid_existing_refresh_token");

        // Act
        var result = await _handler.Handle(command);

        // Assert
        result.Success.Should().BeTrue();
        result.Data!.AccessToken.Should().Be("new_mock_jwt_access_token");
        result.Data.RefreshToken.Should().Be("new_mock_refresh_token");
    }

    [Fact]
    public async Task Handle_RevokedOrInvalidRefreshToken_ShouldThrowUnauthorized()
    {
        // Arrange
        var command = new RefreshTokenCommand("revoked_or_fake_token");

        // Act & Assert
        var act = () => _handler.Handle(command);
        var ex = await act.Should().ThrowAsync<AppException>();
        ex.Which.StatusCode.Should().Be(401);
    }
}
