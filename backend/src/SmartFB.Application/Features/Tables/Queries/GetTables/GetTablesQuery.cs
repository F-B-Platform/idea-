using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Tables.DTOs;

namespace SmartFB.Application.Features.Tables.Queries.GetTables;

public record GetTablesQuery(Guid BranchId) : IRequest<ApiResponse<List<TableDto>>>;

public class GetTablesQueryHandler : IRequestHandler<GetTablesQuery, ApiResponse<List<TableDto>>>
{
    private readonly IApplicationDbContext _context;

    public GetTablesQueryHandler(IApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<ApiResponse<List<TableDto>>> Handle(GetTablesQuery request, CancellationToken cancellationToken)
    {
        var tables = await _context.Tables
            .AsNoTracking()
            .Where(t => t.BranchId == request.BranchId && !t.IsDeleted)
            .OrderBy(t => t.Zone)
            .ThenBy(t => t.TableNumber)
            .ToListAsync(cancellationToken);

        var dtos = tables.Select(t => new TableDto(
            t.Id,
            t.BranchId,
            t.TableNumber,
            t.Zone,
            t.Capacity,
            t.QrCodeUrl,
            t.Status,
            t.IsActive
        )).ToList();

        return ApiResponse<List<TableDto>>.SuccessResult(dtos, "Lấy danh sách bàn thành công.");
    }
}
