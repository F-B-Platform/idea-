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

        var response = new AuthResponse(
            Token: "starter_jwt_token_sample",
            RefreshToken: "starter_refresh_token_sample",
            Username: request.Username,
            Role: "Admin",
            BranchId: Guid.Empty
        );

        return Ok(ApiResponse<AuthResponse>.SuccessResult(response, "Đăng nhập thành công."));
    }
}
