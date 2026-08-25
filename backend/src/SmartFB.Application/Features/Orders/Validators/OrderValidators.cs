using FluentValidation;
using SmartFB.Application.Features.Orders.Commands.CreateDeliveryOrder;
using SmartFB.Application.Features.Orders.Commands.CreateDineInPrepaidOrder;
using SmartFB.Application.Features.Orders.Commands.CreateTakeawayOrder;

namespace SmartFB.Application.Features.Orders.Validators;

public class CreateDineInPrepaidOrderCommandValidator : AbstractValidator<CreateDineInPrepaidOrderCommand>
{
    public CreateDineInPrepaidOrderCommandValidator()
    {
        RuleFor(x => x.BranchId).NotEmpty().WithMessage("Chi nhánh không được để trống.");
        RuleFor(x => x.TableId).NotEmpty().WithMessage("Bàn không được để trống.");
        RuleFor(x => x.Items).NotEmpty().WithMessage("Giỏ hàng phải có ít nhất 1 món.");
    }
}

public class CreateDeliveryOrderCommandValidator : AbstractValidator<CreateDeliveryOrderCommand>
{
    public CreateDeliveryOrderCommandValidator()
    {
        RuleFor(x => x.BranchId).NotEmpty().WithMessage("Chi nhánh không được để trống.");
        RuleFor(x => x.RecipientName).NotEmpty().WithMessage("Tên người nhận không được để trống.");
        RuleFor(x => x.RecipientPhone)
            .NotEmpty().WithMessage("Số điện thoại nhận hàng không được để trống.")
            .Matches(@"^[0-9]{10}$").WithMessage("Số điện thoại phải đúng định dạng 10 chữ số.");
        RuleFor(x => x.DeliveryAddress)
            .NotEmpty().WithMessage("Địa chỉ giao hàng không được để trống.")
            .MinimumLength(10).WithMessage("Địa chỉ giao hàng phải có tối thiểu 10 ký tự.");
        RuleFor(x => x.Items).NotEmpty().WithMessage("Giỏ hàng phải có ít nhất 1 món.");
    }
}

public class CreateTakeawayOrderCommandValidator : AbstractValidator<CreateTakeawayOrderCommand>
{
    public CreateTakeawayOrderCommandValidator()
    {
        RuleFor(x => x.BranchId).NotEmpty().WithMessage("Chi nhánh không được để trống.");
        RuleFor(x => x.CustomerPhone)
            .NotEmpty().WithMessage("Số điện thoại khách hàng không được để trống.")
            .Matches(@"^[0-9]{10}$").WithMessage("Số điện thoại phải đúng định dạng 10 chữ số.");
        RuleFor(x => x.Items).NotEmpty().WithMessage("Giỏ hàng phải có ít nhất 1 món.");
    }
}
