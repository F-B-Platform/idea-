using SmartFB.Domain.Enums;

namespace SmartFB.Application.Features.Products.DTOs;

public record CategoryDto(
    Guid Id,
    string Name,
    string? Description,
    int DisplayOrder,
    string? ImageUrl,
    bool IsActive
);

public record ProductSizeDto(
    Guid Id,
    Guid ProductId,
    string SizeName,
    decimal PriceAdjustment,
    int DisplayOrder
);

public record ModifierDto(
    Guid Id,
    string Name,
    ModifierType Type,
    decimal ExtraPrice,
    bool IsAvailable
);

public record RecipeBomDto(
    Guid Id,
    Guid ProductId,
    Guid SizeId,
    Guid IngredientId,
    string IngredientName,
    string IngredientUnit,
    decimal StandardQuantity,
    decimal WastagePercentage
);

public record ProductDto(
    Guid Id,
    Guid CategoryId,
    string CategoryName,
    string Sku,
    string Name,
    string? Description,
    decimal BasePrice,
    decimal? EffectivePrice,
    string? ImageUrl,
    bool IsAvailable,
    bool IsBestSeller,
    int CaloriesApprox,
    string? AllergenInfo,
    List<ProductSizeDto> Sizes,
    List<ModifierDto> Modifiers
);

public record CreateProductRequestDto(
    Guid CategoryId,
    string Sku,
    string Name,
    string? Description,
    decimal BasePrice,
    string? ImageUrl,
    int CaloriesApprox,
    string? AllergenInfo
);

public record SetRegionalPriceRequestDto(
    Guid BranchId,
    Guid ProductId,
    decimal PriceOverride,
    bool IsAvailable86
);
