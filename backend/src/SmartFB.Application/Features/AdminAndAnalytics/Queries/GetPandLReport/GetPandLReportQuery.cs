using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.AdminAndAnalytics.DTOs;
using SmartFB.Domain.Enums;

namespace SmartFB.Application.Features.AdminAndAnalytics.Queries.GetPandLReport;

public record GetPandLReportQuery(
    DateTime FromDate,
    DateTime ToDate,
    Guid? BranchId = null
) : IRequest<ApiResponse<PandLReportDto>>;

public class GetPandLReportQueryHandler : IRequestHandler<GetPandLReportQuery, ApiResponse<PandLReportDto>>
{
    private readonly IApplicationDbContext _context;

    public GetPandLReportQueryHandler(IApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<ApiResponse<PandLReportDto>> Handle(GetPandLReportQuery request, CancellationToken cancellationToken)
    {
        var ordersQuery = _context.Orders
            .AsNoTracking()
            .Where(o => o.CreatedAt >= request.FromDate && o.CreatedAt <= request.ToDate && (o.Status == OrderStatus.Completed || o.Status == OrderStatus.Paid) && !o.IsDeleted);

        if (request.BranchId.HasValue)
        {
            ordersQuery = ordersQuery.Where(o => o.BranchId == request.BranchId.Value);
        }

        var orders = await ordersQuery
            .Include(o => o.Items)
            .ToListAsync(cancellationToken);

        decimal grossRevenue = orders.Sum(o => o.SubTotal);
        decimal totalDiscounts = orders.Sum(o => o.DiscountAmount);
        decimal netRevenue = orders.Sum(o => o.TotalAmount);

        // Calculate COGS via Recipe BOM and Ingredient Unit Costs
        var bomQuery = await _context.RecipeBoms
            .AsNoTracking()
            .Include(r => r.Ingredient)
            .Where(r => !r.IsDeleted)
            .ToListAsync(cancellationToken);

        var bomMap = bomQuery
            .GroupBy(r => (r.ProductId, r.SizeId))
            .ToDictionary(
                g => g.Key,
                g => g.Sum(r => r.StandardQuantity * (1 + (r.WastagePercentage / 100)) * r.Ingredient.UnitCost)
            );

        decimal totalCogsCost = 0;
        foreach (var order in orders)
        {
            foreach (var item in order.Items)
            {
                if (bomMap.TryGetValue((item.ProductId, item.SizeId), out var unitCost))
                {
                    totalCogsCost += unitCost * item.Quantity;
                }
                else
                {
                    // Fallback estimate 30% of unit price if recipe not explicitly mapped
                    totalCogsCost += item.UnitPrice * 0.30m * item.Quantity;
                }
            }
        }

        decimal grossProfit = netRevenue - totalCogsCost;
        decimal grossMarginPercentage = netRevenue > 0 ? (grossProfit / netRevenue) * 100 : 0;
        decimal estimatedLaborCost = netRevenue * 0.18m; // Benchmark 18% revenue for F&B labor
        decimal netOperatingProfit = grossProfit - estimatedLaborCost;

        var report = new PandLReportDto(
            request.FromDate,
            request.ToDate,
            grossRevenue,
            totalDiscounts,
            netRevenue,
            totalCogsCost,
            grossProfit,
            Math.Round(grossMarginPercentage, 2),
            estimatedLaborCost,
            netOperatingProfit
        );

        return ApiResponse<PandLReportDto>.SuccessResult(report, "Xuất báo cáo P&L tài chính thành công.");
    }
}
