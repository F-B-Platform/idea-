using SmartFB.Domain.Entities;

namespace SmartFB.Application.Common.Interfaces;

public record GeneratedTokenResult(
    string AccessToken,
    string RefreshToken,
    int ExpiresInSeconds
);

public interface IJwtTokenProvider
{
    GeneratedTokenResult GenerateTokens(User user, IEnumerable<string> roles);
    bool ValidateToken(string token);
    (Guid? UserId, string? Username, string? Role, Guid? BranchId) GetPrincipalFromToken(string token);
}
