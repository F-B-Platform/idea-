using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Auth.Commands.LoginUser;
using SmartFB.Application.Features.Auth.Commands.RefreshToken;
using SmartFB.Application.Features.Auth.Commands.RegisterUser;
using SmartFB.Application.Features.Auth.DTOs;
using SmartFB.Application.Features.Auth.Queries.GetUserProfile;

namespace SmartFB.API.Controllers;

public class AuthController : BaseApiController
{
    [HttpPost("login")]
    public async Task<ActionResult<ApiResponse<AuthResultDto>>> Login([FromBody] LoginUserCommand command)
    {
        var result = await Mediator.Send(command);
        return Ok(result);
    }

    [HttpPost("register")]
    public async Task<ActionResult<ApiResponse<UserProfileDto>>> Register([FromBody] RegisterUserCommand command)
    {
        var result = await Mediator.Send(command);
        return Ok(result);
    }

    [HttpPost("refresh-token")]
    public async Task<ActionResult<ApiResponse<AuthResultDto>>> RefreshToken([FromBody] RefreshTokenCommand command)
    {
        var result = await Mediator.Send(command);
        return Ok(result);
    }

    [Authorize]
    [HttpGet("profile/{userId:guid}")]
    public async Task<ActionResult<ApiResponse<UserProfileDto>>> GetProfile(Guid userId)
    {
        var result = await Mediator.Send(new GetUserProfileQuery(userId));
        return Ok(result);
    }
}
