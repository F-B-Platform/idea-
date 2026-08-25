using FluentValidation;
using SmartFB.Application.Features.KitchenKDS.Commands.Toggle86Product;
using SmartFB.Application.Features.KitchenKDS.Commands.UpdateKdsItemStatus;

namespace SmartFB.Application.Features.KitchenKDS.Validators;

public class UpdateKdsItemStatusCommandValidator : AbstractValidator<UpdateKdsItemStatusCommand>
{
    public UpdateKdsItemStatusCommandValidator()
    {
        RuleFor(x => x.OrderItemId).NotEmpty().WithMessage("ID món trong đơn không hợp lệ.");
        RuleFor(x => x.NewStatus)
            .NotEmpty().WithMessage("Trạng thái mới không được để trống.")
            .Must(s => s is "Preparing" or "Ready" or "Served" or "Cancelled")
            .WithMessage("Trạng thái KDS phải là Preparing, Ready, Served hoặc Cancelled.");
    }
}

public class Toggle86ProductCommandValidator : AbstractValidator<Toggle86ProductCommand>
{
    public Toggle86ProductCommandValidator()
    {
        RuleFor(x => x.BranchId).NotEmpty().WithMessage("Chi nhánh không được để trống.");
        RuleFor(x => x.ProductId).NotEmpty().WithMessage("Món ăn không được để trống.");
    }
}
