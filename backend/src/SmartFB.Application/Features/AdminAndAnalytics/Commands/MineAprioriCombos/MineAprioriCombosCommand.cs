using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.AdminAndAnalytics.DTOs;
using SmartFB.Domain.Enums;

namespace SmartFB.Application.Features.AdminAndAnalytics.Commands.MineAprioriCombos;

public record MineAprioriCombosCommand(
    Guid? BranchId = null,
    double MinSupport = 0.02,
    double MinConfidence = 0.40,
    double MinLift = 1.20
) : IRequest<ApiResponse<List<AiComboCandidateDto>>>;

public class MineAprioriCombosCommandHandler : IRequestHandler<MineAprioriCombosCommand, ApiResponse<List<AiComboCandidateDto>>>
{
    private readonly IApplicationDbContext _context;

    public MineAprioriCombosCommandHandler(IApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<ApiResponse<List<AiComboCandidateDto>>> Handle(MineAprioriCombosCommand request, CancellationToken cancellationToken)
    {
        var ordersQuery = _context.Orders
            .AsNoTracking()
            .Include(o => o.Items)
                .ThenInclude(i => i.Product)
            .Where(o => (o.Status == OrderStatus.Completed || o.Status == OrderStatus.Paid) && !o.IsDeleted);

        if (request.BranchId.HasValue)
        {
            ordersQuery = ordersQuery.Where(o => o.BranchId == request.BranchId.Value);
        }

        var orders = await ordersQuery.ToListAsync(cancellationToken);
        int totalTransactions = orders.Count;

        if (totalTransactions < 1)
        {
            return ApiResponse<List<AiComboCandidateDto>>.SuccessResult(new List<AiComboCandidateDto>(), "Chưa đủ dữ liệu giao dịch để khai phá combo Apriori.");
        }

        // Count item frequencies
        var itemFrequency = new Dictionary<Guid, (string Name, decimal Price, int Count)>();
        var pairFrequency = new Dictionary<(Guid, Guid), int>();

        foreach (var order in orders)
        {
            var distinctProductIds = order.Items.Select(i => (i.ProductId, i.Product.Name, i.Product.BasePrice)).DistinctBy(x => x.ProductId).ToList();

            foreach (var item in distinctProductIds)
            {
                if (itemFrequency.TryGetValue(item.ProductId, out var existing))
                {
                    itemFrequency[item.ProductId] = (item.Name, item.BasePrice, existing.Count + 1);
                }
                else
                {
                    itemFrequency[item.ProductId] = (item.Name, item.BasePrice, 1);
                }
            }

            for (int i = 0; i < distinctProductIds.Count; i++)
            {
                for (int j = i + 1; j < distinctProductIds.Count; j++)
                {
                    var pA = distinctProductIds[i].ProductId;
                    var pB = distinctProductIds[j].ProductId;
                    var pairKey = pA.CompareTo(pB) < 0 ? (pA, pB) : (pB, pA);

                    pairFrequency[pairKey] = pairFrequency.GetValueOrDefault(pairKey, 0) + 1;
                }
            }
        }

        var candidates = new List<AiComboCandidateDto>();

        foreach (var (pair, pairCount) in pairFrequency)
        {
            double support = (double)pairCount / totalTransactions;
            if (support < request.MinSupport) continue;

            var (pA, pB) = pair;
            var itemA = itemFrequency[pA];
            var itemB = itemFrequency[pB];

            double probA = (double)itemA.Count / totalTransactions;
            double probB = (double)itemB.Count / totalTransactions;

            double confidenceAtoB = (double)pairCount / itemA.Count;
            double lift = confidenceAtoB / probB;

            if (confidenceAtoB >= request.MinConfidence && lift >= request.MinLift)
            {
                decimal combinedPrice = itemA.Price + itemB.Price;
                decimal suggestedPrice = Math.Round(combinedPrice * 0.85m, 0); // 15% discount for combo
                decimal estimatedBomCost = combinedPrice * 0.35m;
                decimal estimatedMargin = suggestedPrice > 0 ? (suggestedPrice - estimatedBomCost) / suggestedPrice * 100 : 0;

                candidates.Add(new AiComboCandidateDto(
                    pA,
                    itemA.Name,
                    pB,
                    itemB.Name,
                    Math.Round(support, 4),
                    Math.Round(confidenceAtoB, 4),
                    Math.Round(lift, 2),
                    combinedPrice,
                    suggestedPrice,
                    estimatedBomCost,
                    Math.Round(estimatedMargin, 2)
                ));
            }
        }

        return ApiResponse<List<AiComboCandidateDto>>.SuccessResult(candidates, $"Khai phá thành công {candidates.Count} gợi ý combo AI-2 Apriori.");
    }
}
