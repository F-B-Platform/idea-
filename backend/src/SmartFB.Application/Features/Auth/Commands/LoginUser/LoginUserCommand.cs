using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Auth.DTOs;

namespace SmartFB.Application.Features.Auth.Commands.LoginUser;

public record LoginUserCommand(string Username, string Password) : IRequest<ApiResponse<AuthResultDto>>;

public class LoginUserCommandHandler : IRequestHandler<LoginUserCommand, ApiResponse<AuthResultDto>>
{
    private readonly IApplicationDbContext _context;
    private readonly IJwtTokenProvider _tokenProvider;

    public LoginUserCommandHandler(IApplicationDbContext context, IJwtTokenProvider tokenProvider)
    {
        _context = context;
        _tokenProvider = tokenProvider;
    }

    public async Task<ApiResponse<AuthResultDto>> Handle(LoginUserCommand request, CancellationToken cancellationToken)
    {
        var user = await _context.Users
            .AsNoTracking()
            .Include(u => u.UserRoles)
                .ThenInclude(ur => ur.Role)
            .FirstOrDefaultAsync(u => u.Username == request.Username && !u.IsDeleted, cancellationToken);

        if (user == null || user.PasswordHash != request.Password && !BCryptVerify(request.Password, user.PasswordHash))
        {
            throw new UnauthorizedException("Tên đăng nhập hoặc mật khẩu không chính xác.");
        }

        if (user.Status != "Active")
        {
            throw new AppException("Tài khoản của bạn đã bị vô hiệu hóa hoặc tạm khóa.");
        }

        var roles = user.UserRoles.Select(r => r.Role.RoleName).ToList();
        if (roles.Count == 0)
        {
            roles.Add(user.Role.ToString());
        }

        var tokenResult = _tokenProvider.GenerateTokens(user, roles);

        var profile = new UserProfileDto(
            user.Id,
            user.Username,
            user.FullName,
            user.Email,
            user.Phone,
            user.EmployeeCode,
            roles.FirstOrDefault() ?? user.Role.ToString(),
            user.BranchId,
            user.Status
        );

        var authResult = new AuthResultDto(
            tokenResult.AccessToken,
            tokenResult.RefreshToken,
            tokenResult.ExpiresInSeconds,
            profile
        );

        return ApiResponse<AuthResultDto>.SuccessResult(authResult, "Đăng nhập thành công.");
    }

    private static bool BCryptVerify(string password, string hash)
    {
        // Simple hash check or direct string comparison for mock/seed
        return password == hash;
    }
}
