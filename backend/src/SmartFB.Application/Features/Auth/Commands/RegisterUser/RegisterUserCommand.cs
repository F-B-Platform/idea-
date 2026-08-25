using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Auth.DTOs;
using SmartFB.Domain.Entities;
using SmartFB.Domain.Enums;

namespace SmartFB.Application.Features.Auth.Commands.RegisterUser;

public record RegisterUserCommand(
    string Username,
    string Password,
    string FullName,
    string? Email,
    string? Phone,
    string? EmployeeCode,
    UserRole Role,
    Guid? BranchId
) : IRequest<ApiResponse<UserProfileDto>>;

public class RegisterUserCommandHandler : IRequestHandler<RegisterUserCommand, ApiResponse<UserProfileDto>>
{
    private readonly IApplicationDbContext _context;

    public RegisterUserCommandHandler(IApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<ApiResponse<UserProfileDto>> Handle(RegisterUserCommand request, CancellationToken cancellationToken)
    {
        var existing = await _context.Users
            .AnyAsync(u => u.Username == request.Username && !u.IsDeleted, cancellationToken);

        if (existing)
        {
            throw new AppException("Tên đăng nhập đã tồn tại trong hệ thống.");
        }

        var user = new User
        {
            Username = request.Username,
            PasswordHash = request.Password, // Production will use hash
            FullName = request.FullName,
            Email = request.Email,
            Phone = request.Phone,
            EmployeeCode = request.EmployeeCode,
            Role = request.Role,
            BranchId = request.BranchId,
            Status = "Active"
        };

        _context.Users.Add(user);
        await _context.SaveChangesAsync(cancellationToken);

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

        return ApiResponse<UserProfileDto>.SuccessResult(profile, "Đăng ký người dùng thành công.");
    }
}
