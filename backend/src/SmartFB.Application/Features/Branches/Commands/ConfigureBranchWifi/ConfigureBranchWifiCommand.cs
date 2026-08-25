using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Branches.DTOs;
using SmartFB.Domain.Entities;

namespace SmartFB.Application.Features.Branches.Commands.ConfigureBranchWifi;

public record ConfigureBranchWifiCommand(
    Guid BranchId,
    string SsidName,
    string BssidList,
    string AllowedIpSubnets,
    bool IsActive
) : IRequest<ApiResponse<BranchWifiConfigDto>>;

public class ConfigureBranchWifiCommandHandler : IRequestHandler<ConfigureBranchWifiCommand, ApiResponse<BranchWifiConfigDto>>
{
    private readonly IApplicationDbContext _context;

    public ConfigureBranchWifiCommandHandler(IApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<ApiResponse<BranchWifiConfigDto>> Handle(ConfigureBranchWifiCommand request, CancellationToken cancellationToken)
    {
        var branch = await _context.Branches
            .FirstOrDefaultAsync(b => b.Id == request.BranchId && !b.IsDeleted, cancellationToken);

        if (branch == null)
        {
            throw new NotFoundException("Branch", request.BranchId);
        }

        var config = await _context.BranchWifiConfigs
            .FirstOrDefaultAsync(c => c.BranchId == request.BranchId && !c.IsDeleted, cancellationToken);

        if (config == null)
        {
            config = new BranchWifiConfig
            {
                BranchId = request.BranchId,
                SsidName = request.SsidName,
                BssidList = request.BssidList,
                AllowedIpSubnets = request.AllowedIpSubnets,
                IsActive = request.IsActive
            };
            _context.BranchWifiConfigs.Add(config);
        }
        else
        {
            config.SsidName = request.SsidName;
            config.BssidList = request.BssidList;
            config.AllowedIpSubnets = request.AllowedIpSubnets;
            config.IsActive = request.IsActive;
        }

        await _context.SaveChangesAsync(cancellationToken);

        var dto = new BranchWifiConfigDto(
            config.Id,
            config.BranchId,
            config.SsidName,
            config.BssidList,
            config.AllowedIpSubnets,
            config.IsActive
        );

        return ApiResponse<BranchWifiConfigDto>.SuccessResult(dto, "Cập nhật cấu hình WiFi chi nhánh thành công.");
    }
}
