using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Attendances.DTOs;

namespace SmartFB.Application.Features.Attendances.Queries.GetAttendances;

public record GetAttendancesQuery(
    Guid? BranchId = null,
    Guid? UserId = null,
    DateTime? FromDate = null,
    DateTime? ToDate = null
) : IRequest<ApiResponse<List<AttendanceDto>>>;

public class GetAttendancesQueryHandler : IRequestHandler<GetAttendancesQuery, ApiResponse<List<AttendanceDto>>>
{
    private readonly IApplicationDbContext _context;

    public GetAttendancesQueryHandler(IApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<ApiResponse<List<AttendanceDto>>> Handle(GetAttendancesQuery request, CancellationToken cancellationToken)
    {
        var query = _context.Attendances
            .AsNoTracking()
            .Include(a => a.User)
            .Where(a => !a.IsDeleted);

        if (request.BranchId.HasValue)
        {
            query = query.Where(a => a.BranchId == request.BranchId.Value);
        }

        if (request.UserId.HasValue)
        {
            query = query.Where(a => a.UserId == request.UserId.Value);
        }

        if (request.FromDate.HasValue)
        {
            query = query.Where(a => a.CheckInTime >= request.FromDate.Value);
        }

        if (request.ToDate.HasValue)
        {
            query = query.Where(a => a.CheckInTime <= request.ToDate.Value);
        }

        var attendances = await query
            .OrderByDescending(a => a.CheckInTime)
            .ToListAsync(cancellationToken);

        var dtos = attendances.Select(a => new AttendanceDto(
            a.Id,
            a.BranchId,
            a.UserId,
            a.EmployeeCode,
            a.User.FullName,
            a.CheckInTime,
            a.CheckOutTime,
            a.VerifiedIp,
            a.VerifiedBssid,
            a.Status
        )).ToList();

        return ApiResponse<List<AttendanceDto>>.SuccessResult(dtos, "Lấy lịch sử chấm công thành công.");
    }
}
