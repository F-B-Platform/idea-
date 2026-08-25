using FluentValidation;
using SmartFB.Application.Features.Products.Commands.CreateProduct;
using SmartFB.Application.Features.Products.Commands.SetRegionalPrice;

namespace SmartFB.Application.Features.Products.Validators;

public class CreateProductCommandValidator : AbstractValidator<CreateProductCommand>
{
    public CreateProductCommandValidator()
    {
        RuleFor(x => x.CategoryId).NotEmpty().WithMessage("Danh mục không được để trống.");
        RuleFor(x => x.Sku).NotEmpty().WithMessage("Mã SKU không được để trống.");
        RuleFor(x => x.Name).NotEmpty().WithMessage("Tên món ăn không được để trống.");
        RuleFor(x => x.BasePrice).GreaterThanOrEqualTo(0).WithMessage("Giá cơ sở không được âm.");
    }
}

public class SetRegionalPriceCommandValidator : AbstractValidator<SetRegionalPriceCommand>
{
    public SetRegionalPriceCommandValidator()
    {
        RuleFor(x => x.BranchId).NotEmpty().WithMessage("Chi nhánh không được để trống.");
        RuleFor(x => x.ProductId).NotEmpty().WithMessage("Món ăn không được để trống.");
        RuleFor(x => x.PriceOverride).GreaterThanOrEqualTo(0).WithMessage("Giá ghi đè không được âm.");
    }
}
