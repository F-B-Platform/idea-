using Microsoft.AspNetCore.Mvc;
using SmartFB.Application.Common.Models;

namespace SmartFB.API.Controllers;

public class AuthController : BaseApiController
{
    public record LoginRequest(string Username, string Password);
    public record AuthResponse(string Token, string RefreshToken, string Username, string Role, Guid? BranchId);

    [HttpPost("login")]
    public ActionResult<ApiResponse<AuthResponse>> Login([FromBody] LoginRequest request)
    {
        if (string.IsNullOrWhiteSpace(request.Username) || string.IsNullOrWhiteSpace(request.Password))
        {
            return BadRequest(ApiResponse<AuthResponse>.FailureResult("Tên đăng nhập và mật khẩu không được để trống."));
        }

        // Demo seed credentials response for initial setup
        var response = new AuthResponse(
            Token: "mock_jwt_token_for_development_purposes_2026",
            RefreshToken: "mock_refresh_token_2026",
            Username: request.Username,
            Role: "Admin",
            BranchId: Guid.Parse("11111111-1111-1111-1111-111111111111")
        );

        return Ok(ApiResponse<AuthResponse>.SuccessResult(response, "Đăng nhập thành công."));
    }
}
