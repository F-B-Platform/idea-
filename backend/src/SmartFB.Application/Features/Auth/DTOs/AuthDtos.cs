using SmartFB.Domain.Enums;

namespace SmartFB.Application.Features.Auth.DTOs;

public record AuthResultDto(
    string AccessToken,
    string RefreshToken,
    int ExpiresIn,
    UserProfileDto User
);

public record UserProfileDto(
    Guid Id,
    string Username,
    string FullName,
    string? Email,
    string? Phone,
    string? EmployeeCode,
    string Role,
    Guid? BranchId,
    string Status
);

public record LoginRequestDto(
    string Username,
    string Password
);

public record RegisterUserRequestDto(
    string Username,
    string Password,
    string FullName,
    string? Email,
    string? Phone,
    string? EmployeeCode,
    UserRole Role,
    Guid? BranchId
);

public record RefreshTokenRequestDto(
    string RefreshToken
);
