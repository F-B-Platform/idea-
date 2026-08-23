// ============================================================================
// File: src/SmartFB.Application/Features/Orders/Commands/CreateDineInOrder/CreateDineInOrderCommandValidator.cs
// Project: Smart F&B Operating System (v2.5.0-Production-Ready)
// Description: Validator kiểm tra tính hợp lệ của Command khởi tạo đơn Dine-In.
// ============================================================================

using FluentValidation;

namespace SmartFB.Application.Features.Orders.Commands.CreateDineInOrder;

public sealed class CreateDineInOrderCommandValidator : AbstractValidator<CreateDineInOrderCommand>
{
    public CreateDineInOrderCommandValidator()
    {
        RuleFor(x => x.BranchId)
            .NotEmpty().WithMessage("Mã chi nhánh (BranchId) không được để trống.");

        RuleFor(x => x.TableId)
            .NotEmpty().WithMessage("Mã bàn (TableId) bắt buộc đối với đơn dùng tại bàn.");

        RuleFor(x => x.PaymentMethod)
            .IsInEnum().WithMessage("Phương thức thanh toán không hợp lệ (Hỗ trợ: VietQr, Cash).");

        RuleFor(x => x.Note)
            .MaximumLength(500).WithMessage("Ghi chú đơn hàng không được vượt quá 500 ký tự.");

        RuleFor(x => x.Items)
            .NotEmpty().WithMessage("Đơn hàng phải có ít nhất 01 món.")
            .Must(items => items.Count <= 50).WithMessage("Đơn hàng không được vượt quá 50 loại món khác nhau.");

        RuleForEach(x => x.Items).ChildRules(item =>
        {
            item.RuleFor(i => i.MenuItemId)
                .NotEmpty().WithMessage("Mã món (MenuItemId) không được để trống.");

            item.RuleFor(i => i.ItemSizeId)
                .NotEmpty().WithMessage("Mã kích cỡ (ItemSizeId) không được để trống.");

            item.RuleFor(i => i.Quantity)
                .GreaterThan(0).WithMessage("Số lượng từng món phải lớn hơn 0.")
                .LessThanOrEqualTo(20).WithMessage("Số lượng tối đa cho mỗi dòng món là 20 phần.");

            item.RuleFor(i => i.Note)
                .MaximumLength(200).WithMessage("Ghi chú món không được vượt quá 200 ký tự.");

            item.RuleForEach(i => i.Toppings).ChildRules(topping =>
            {
                topping.RuleFor(t => t.ToppingId)
                    .NotEmpty().WithMessage("Mã topping không được để trống.");

                topping.RuleFor(t => t.ToppingName)
                    .NotEmpty().WithMessage("Tên topping không được để trống.")
                    .MaximumLength(100).WithMessage("Tên topping tối đa 100 ký tự.");

                topping.RuleFor(t => t.Price)
                    .GreaterThanOrEqualTo(0).WithMessage("Đơn giá topping không thể là số âm.");
            });
        });
    }
}
