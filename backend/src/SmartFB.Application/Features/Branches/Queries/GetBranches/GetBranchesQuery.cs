using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Branches.DTOs;

namespace SmartFB.Application.Features.Branches.Queries.GetBranches;

public record GetBranchesQuery(bool? OnlyActive = null) : IRequest<ApiResponse<List<BranchDto>>>;

public class GetBranchesQueryHandler : IRequestHandler<GetBranchesQuery, ApiResponse<List<BranchDto>>>
{
    private readonly IApplicationDbContext _context;

    public GetBranchesQueryHandler(IApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<ApiResponse<List<BranchDto>>> Handle(GetBranchesQuery request, CancellationToken cancellationToken)
    {
        var query = _context.Branches
            .AsNoTracking()
            .Include(b => b.WifiConfigs)
            .Where(b => !b.IsDeleted);

        if (request.OnlyActive == true)
        {
            query = query.Where(b => b.IsActive);
        }

        var branches = await query.ToListAsync(cancellationToken);

        var dtos = branches.Select(b => new BranchDto(
            b.Id,
            b.Code,
            b.Name,
            b.Address,
            b.Phone,
            b.OperatingHours,
            b.IsActive,
            b.WifiConfigs.Where(w => !w.IsDeleted).Select(w => new BranchWifiConfigDto(
                w.Id,
                w.BranchId,
                w.SsidName,
                w.BssidList,
                w.AllowedIpSubnets,
                w.IsActive
            )).ToList()
        )).ToList();

        return ApiResponse<List<BranchDto>>.SuccessResult(dtos, "Lấy danh sách chi nhánh thành công.");
    }
}
