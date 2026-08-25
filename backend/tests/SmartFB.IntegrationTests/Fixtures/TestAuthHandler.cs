using System.Security.Claims;
using System.Text.Encodings.Web;
using Microsoft.AspNetCore.Authentication;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Options;

namespace SmartFB.IntegrationTests.Fixtures;

public class TestAuthHandlerOptions : AuthenticationSchemeOptions
{
    public const string Scheme = "TestScheme";
}

public class TestAuthHandler : AuthenticationHandler<TestAuthHandlerOptions>
{
    public const string AuthenticationScheme = "TestScheme";

    public TestAuthHandler(
        IOptionsMonitor<TestAuthHandlerOptions> options,
        ILoggerFactory logger,
        UrlEncoder encoder)
        : base(options, logger, encoder)
    {
    }

    protected override Task<AuthenticateResult> HandleAuthenticateAsync()
    {
        // If request specifies anonymous bypass
        if (Request.Headers.TryGetValue("X-Test-Anonymous", out var anonymous) && anonymous == "true")
        {
            return Task.FromResult(AuthenticateResult.NoResult());
        }

        var role = Request.Headers["X-Test-Role"].FirstOrDefault() ?? "Customer";
        var userId = Request.Headers["X-Test-UserId"].FirstOrDefault() ?? SeedDataConstants.CustomerNamId.ToString();
        var branchId = Request.Headers["X-Test-BranchId"].FirstOrDefault() ?? SeedDataConstants.BranchQ1Id.ToString();
        var userName = Request.Headers["X-Test-UserName"].FirstOrDefault() ?? "TestUser";

        var claims = new List<Claim>
        {
            new(ClaimTypes.NameIdentifier, userId),
            new(ClaimTypes.Name, userName),
            new(ClaimTypes.Role, role),
            new("BranchId", branchId),
            new("Role", role)
        };

        // Add additional permission claims based on role
        if (role == "ChainAdmin")
        {
            claims.Add(new Claim("Permissions", "admin:all"));
            claims.Add(new Claim("Permissions", "reports:pnl"));
        }
        else if (role == "BranchManager")
        {
            claims.Add(new Claim("Permissions", "shifts:manage"));
            claims.Add(new Claim("Permissions", "kds:manage"));
        }
        else if (role == "BaristaStaff")
        {
            claims.Add(new Claim("Permissions", "kds:read"));
            claims.Add(new Claim("Permissions", "kds:update_status"));
            claims.Add(new Claim("Permissions", "kds:toggle_86"));
        }
        else if (role == "CashierStaff")
        {
            claims.Add(new Claim("Permissions", "pos:create_order"));
            claims.Add(new Claim("Permissions", "crm:lookup"));
            claims.Add(new Claim("Permissions", "crm:redeem"));
        }

        var identity = new ClaimsIdentity(claims, AuthenticationScheme);
        var principal = new ClaimsPrincipal(identity);
        var ticket = new AuthenticationTicket(principal, AuthenticationScheme);

        return Task.FromResult(AuthenticateResult.Success(ticket));
    }
}
