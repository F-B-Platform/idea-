using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Auth.DTOs;

namespace SmartFB.Application.Features.Auth.Queries.GetUserProfile;

public record GetUserProfileQuery(Guid UserId) : IRequest<ApiResponse<UserProfileDto>>;

public class GetUserProfileQueryHandler : IRequestHandler<GetUserProfileQuery, ApiResponse<UserProfileDto>>
{
    private readonly IApplicationDbContext _context;

    public GetUserProfileQueryHandler(IApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<ApiResponse<UserProfileDto>> Handle(GetUserProfileQuery request, CancellationToken cancellationToken)
    {
        var user = await _context.Users
            .AsNoTracking()
            .FirstOrDefaultAsync(u => u.Id == request.UserId && !u.IsDeleted, cancellationToken);

        if (user == null)
        {
            throw new NotFoundException("User", request.UserId);
        }

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

        return ApiResponse<UserProfileDto>.SuccessResult(profile, "Lấy thông tin tài khoản thành công.");
    }
}
