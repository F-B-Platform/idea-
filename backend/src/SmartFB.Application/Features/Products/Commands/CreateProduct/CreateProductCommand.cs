using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Products.DTOs;
using SmartFB.Domain.Entities;

namespace SmartFB.Application.Features.Products.Commands.CreateProduct;

public record CreateProductCommand(
    Guid CategoryId,
    string Sku,
    string Name,
    string? Description,
    decimal BasePrice,
    string? ImageUrl,
    int CaloriesApprox = 0,
    string? AllergenInfo = null
) : IRequest<ApiResponse<ProductDto>>;

public class CreateProductCommandHandler : IRequestHandler<CreateProductCommand, ApiResponse<ProductDto>>
{
    private readonly IApplicationDbContext _context;

    public CreateProductCommandHandler(IApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<ApiResponse<ProductDto>> Handle(CreateProductCommand request, CancellationToken cancellationToken)
    {
        var category = await _context.Categories
            .FirstOrDefaultAsync(c => c.Id == request.CategoryId && !c.IsDeleted, cancellationToken);

        if (category == null)
        {
            throw new NotFoundException("Category", request.CategoryId);
        }

        var skuExists = await _context.Products
            .AnyAsync(p => p.Sku == request.Sku && !p.IsDeleted, cancellationToken);

        if (skuExists)
        {
            throw new AppException($"Mã SKU \"{request.Sku}\" đã tồn tại.");
        }

        var product = new Product
        {
            CategoryId = request.CategoryId,
            Sku = request.Sku,
            Name = request.Name,
            Description = request.Description,
            BasePrice = request.BasePrice,
            ImageUrl = request.ImageUrl,
            CaloriesApprox = request.CaloriesApprox,
            AllergenInfo = request.AllergenInfo,
            IsAvailable = true
        };

        // Create default sizes: Size M (standard, +0)
        var defaultSize = new ProductSize
        {
            ProductId = product.Id,
            SizeName = "Size M",
            PriceAdjustment = 0,
            DisplayOrder = 1
        };
        product.ProductSizes.Add(defaultSize);

        _context.Products.Add(product);
        await _context.SaveChangesAsync(cancellationToken);

        var dto = new ProductDto(
            product.Id,
            category.Id,
            category.Name,
            product.Sku,
            product.Name,
            product.Description,
            product.BasePrice,
            product.BasePrice,
            product.ImageUrl,
            product.IsAvailable,
            product.IsBestSeller,
            product.CaloriesApprox,
            product.AllergenInfo,
            new List<ProductSizeDto>
            {
                new(defaultSize.Id, defaultSize.ProductId, defaultSize.SizeName, defaultSize.PriceAdjustment, defaultSize.DisplayOrder)
            },
            new List<ModifierDto>()
        );

        return ApiResponse<ProductDto>.SuccessResult(dto, "Tạo mới món ăn thành công.");
    }
}
