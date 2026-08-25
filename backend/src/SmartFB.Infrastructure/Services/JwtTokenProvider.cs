using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Text;
using Microsoft.Extensions.Configuration;
using Microsoft.IdentityModel.Tokens;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Domain.Entities;

namespace SmartFB.Infrastructure.Services;

public class JwtTokenProvider : IJwtTokenProvider
{
    private readonly IConfiguration _configuration;

    public JwtTokenProvider(IConfiguration configuration)
    {
        _configuration = configuration;
    }

    public GeneratedTokenResult GenerateTokens(User user, IEnumerable<string> roles)
    {
        var secret = _configuration["Jwt:Secret"] ?? "super_secret_jwt_key_smart_fb_os_production_standard_256bit_min_length_2026";
        var issuer = _configuration["Jwt:Issuer"] ?? "SmartFB_AuthServer";
        var audience = _configuration["Jwt:Audience"] ?? "SmartFB_AppClients";
        var key = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(secret));
        var creds = new SigningCredentials(key, SecurityAlgorithms.HmacSha256);

        var claims = new List<Claim>
        {
            new(ClaimTypes.NameIdentifier, user.Id.ToString()),
            new(ClaimTypes.Name, user.Username),
            new("fullName", user.FullName)
        };

        if (user.BranchId.HasValue)
        {
            claims.Add(new("branchId", user.BranchId.Value.ToString()));
        }

        foreach (var role in roles)
        {
            claims.Add(new(ClaimTypes.Role, role));
        }

        var expires = DateTime.UtcNow.AddHours(8);
        var token = new JwtSecurityToken(
            issuer: issuer,
            audience: audience,
            claims: claims,
            expires: expires,
            signingCredentials: creds
        );

        var accessToken = new JwtSecurityTokenHandler().WriteToken(token);
        var refreshToken = Guid.NewGuid().ToString("N") + Guid.NewGuid().ToString("N");

        return new GeneratedTokenResult(accessToken, refreshToken, (int)(expires - DateTime.UtcNow).TotalSeconds);
    }

    public bool ValidateToken(string token)
    {
        var secret = _configuration["Jwt:Secret"] ?? "super_secret_jwt_key_smart_fb_os_production_standard_256bit_min_length_2026";
        var key = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(secret));
        var handler = new JwtSecurityTokenHandler();

        try
        {
            handler.ValidateToken(token, new TokenValidationParameters
            {
                ValidateIssuerSigningKey = true,
                IssuerSigningKey = key,
                ValidateIssuer = false,
                ValidateAudience = false,
                ClockSkew = TimeSpan.Zero
            }, out _);

            return true;
        }
        catch
        {
            return false;
        }
    }

    public (Guid? UserId, string? Username, string? Role, Guid? BranchId) GetPrincipalFromToken(string token)
    {
        var handler = new JwtSecurityTokenHandler();
        if (!handler.CanReadToken(token))
        {
            return (null, null, null, null);
        }

        var jwt = handler.ReadJwtToken(token);
        var userIdStr = jwt.Claims.FirstOrDefault(c => c.Type == ClaimTypes.NameIdentifier)?.Value;
        var username = jwt.Claims.FirstOrDefault(c => c.Type == ClaimTypes.Name)?.Value;
        var role = jwt.Claims.FirstOrDefault(c => c.Type == ClaimTypes.Role)?.Value;
        var branchIdStr = jwt.Claims.FirstOrDefault(c => c.Type == "branchId")?.Value;

        Guid? userId = Guid.TryParse(userIdStr, out var uid) ? uid : null;
        Guid? branchId = Guid.TryParse(branchIdStr, out var bid) ? bid : null;

        return (userId, username, role, branchId);
    }
}
