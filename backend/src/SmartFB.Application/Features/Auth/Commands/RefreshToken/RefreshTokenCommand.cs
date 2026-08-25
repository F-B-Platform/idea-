using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Auth.DTOs;

namespace SmartFB.Application.Features.Auth.Commands.RefreshToken;

public record RefreshTokenCommand(string RefreshToken) : IRequest<ApiResponse<AuthResultDto>>;

public class RefreshTokenCommandHandler : IRequestHandler<RefreshTokenCommand, ApiResponse<AuthResultDto>>
{
    private readonly IApplicationDbContext _context;
    private readonly IJwtTokenProvider _tokenProvider;

    public RefreshTokenCommandHandler(IApplicationDbContext context, IJwtTokenProvider tokenProvider)
    {
        _context = context;
        _tokenProvider = tokenProvider;
    }

    public async Task<ApiResponse<AuthResultDto>> Handle(RefreshTokenCommand request, CancellationToken cancellationToken)
    {
        var principal = _tokenProvider.GetPrincipalFromToken(request.RefreshToken);
        if (principal.UserId == null)
        {
            throw new UnauthorizedException("Refresh Token không hợp lệ hoặc đã hết hạn.");
        }

        var user = await _context.Users
            .AsNoTracking()
            .FirstOrDefaultAsync(u => u.Id == principal.UserId.Value && !u.IsDeleted, cancellationToken);

        if (user == null || user.Status != "Active")
        {
            throw new UnauthorizedException("Tài khoản không tồn tại hoặc đã bị khóa.");
        }

        var roles = new[] { user.Role.ToString() };
        var tokenResult = _tokenProvider.GenerateTokens(user, roles);

        var profile = new UserProfileDto(
            user.Id,
            user.Username,
            user.FullName,
            user.Email,
            user.Phone,
            user.EmployeeCode,
            user.Role.ToString(),
            user.BranchId,
            user.Status
        );

        var authResult = new AuthResultDto(
            tokenResult.AccessToken,
            tokenResult.RefreshToken,
            tokenResult.ExpiresInSeconds,
            profile
        );

        return ApiResponse<AuthResultDto>.SuccessResult(authResult, "Làm mới token thành công.");
    }
}
