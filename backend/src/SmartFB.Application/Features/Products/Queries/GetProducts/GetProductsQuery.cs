using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Products.DTOs;

namespace SmartFB.Application.Features.Products.Queries.GetProducts;

public record GetProductsQuery(
    Guid? BranchId = null,
    Guid? CategoryId = null,
    bool? OnlyAvailable = null
) : IRequest<ApiResponse<List<ProductDto>>>;

public class GetProductsQueryHandler : IRequestHandler<GetProductsQuery, ApiResponse<List<ProductDto>>>
{
    private readonly IApplicationDbContext _context;

    public GetProductsQueryHandler(IApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<ApiResponse<List<ProductDto>>> Handle(GetProductsQuery request, CancellationToken cancellationToken)
    {
        var query = _context.Products
            .AsNoTracking()
            .Include(p => p.Category)
            .Include(p => p.ProductSizes.Where(s => !s.IsDeleted).OrderBy(s => s.DisplayOrder))
            .Include(p => p.ProductModifiers)
                .ThenInclude(pm => pm.Modifier)
            .Where(p => !p.IsDeleted);

        if (request.CategoryId.HasValue)
        {
            query = query.Where(p => p.CategoryId == request.CategoryId.Value);
        }

        if (request.OnlyAvailable == true)
        {
            query = query.Where(p => p.IsAvailable);
        }

        var products = await query.ToListAsync(cancellationToken);

        // Fetch regional prices if branchId is supplied
        Dictionary<Guid, (decimal PriceOverride, bool IsAvailable86)> regionalMap = new();
        if (request.BranchId.HasValue)
        {
            var branchPrices = await _context.ProductBranchPrices
                .AsNoTracking()
                .Where(bp => bp.BranchId == request.BranchId.Value && !bp.IsDeleted)
                .ToListAsync(cancellationToken);

            regionalMap = branchPrices.ToDictionary(bp => bp.ProductId, bp => (bp.PriceOverride, bp.IsAvailable86));
        }

        var dtos = products.Select(p =>
        {
            decimal effectivePrice = p.BasePrice;
            bool isAvailable = p.IsAvailable;

            if (regionalMap.TryGetValue(p.Id, out var reg))
            {
                effectivePrice = reg.PriceOverride;
                isAvailable = isAvailable && reg.IsAvailable86;
            }

            return new ProductDto(
                p.Id,
                p.CategoryId,
                p.Category.Name,
                p.Sku,
                p.Name,
                p.Description,
                p.BasePrice,
                effectivePrice,
                p.ImageUrl,
                isAvailable,
                p.IsBestSeller,
                p.CaloriesApprox,
                p.AllergenInfo,
                p.ProductSizes.Select(s => new ProductSizeDto(
                    s.Id,
                    s.ProductId,
                    s.SizeName,
                    s.PriceAdjustment,
                    s.DisplayOrder
                )).ToList(),
                p.ProductModifiers.Where(pm => !pm.Modifier.IsDeleted).Select(pm => new ModifierDto(
                    pm.Modifier.Id,
                    pm.Modifier.Name,
                    pm.Modifier.Type,
                    pm.Modifier.ExtraPrice,
                    pm.Modifier.IsAvailable
                )).ToList()
            );
        }).ToList();

        return ApiResponse<List<ProductDto>>.SuccessResult(dtos, "Lấy danh sách món ăn thành công.");
    }
}
