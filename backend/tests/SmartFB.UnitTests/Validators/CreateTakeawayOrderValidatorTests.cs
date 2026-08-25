using FluentAssertions;
using FluentValidation;
using SmartFB.UnitTests.Features.Orders;
using Xunit;

namespace SmartFB.UnitTests.Validators;

public class CreateTakeawayOrderValidator : AbstractValidator<CreateTakeawayOrderCommand>
{
    public CreateTakeawayOrderValidator()
    {
        RuleFor(x => x.BranchId).NotEmpty().WithMessage("Chi nhánh không được để trống.");
        RuleFor(x => x.CustomerPhone)
            .Matches(@"^((03|05|07|08|09)\d{8})?$")
            .When(x => !string.IsNullOrEmpty(x.CustomerPhone))
            .WithMessage("Số điện thoại không đúng định dạng Việt Nam.");
        RuleFor(x => x.Items)
            .NotEmpty().WithMessage("Đơn hàng phải có ít nhất 1 món.");
        RuleFor(x => x.CashGiven)
            .GreaterThanOrEqualTo(0).WithMessage("Tiền khách đưa không được là số âm.");
    }
}

public class CreateTakeawayOrderValidatorTests
{
    private readonly CreateTakeawayOrderValidator _validator = new();

    [Fact]
    public void Validate_ValidTakeawayCommand_ShouldPass()
    {
        var command = new CreateTakeawayOrderCommand(
            BranchId: Guid.NewGuid(),
            CustomerPhone: "0909123456",
            CustomerName: "Nguyen Van A",
            RedeemFreeCup: false,
            FreeProductId: null,
            PaymentMethod: SmartFB.Domain.Enums.PaymentMethod.Cash,
            CashGiven: 100000m,
            Items: new List<OrderItemRequestDto> { new(Guid.NewGuid(), "Ca Phe", "M", 1, 35000m) }
        );

        var result = _validator.Validate(command);
        result.IsValid.Should().BeTrue();
    }

    [Fact]
    public void Validate_EmptyItems_ShouldFail()
    {
        var command = new CreateTakeawayOrderCommand(
            BranchId: Guid.NewGuid(),
            CustomerPhone: "0909123456",
            CustomerName: "Nguyen Van A",
            RedeemFreeCup: false,
            FreeProductId: null,
            PaymentMethod: SmartFB.Domain.Enums.PaymentMethod.Cash,
            CashGiven: 100000m,
            Items: new List<OrderItemRequestDto>()
        );

        var result = _validator.Validate(command);
        result.IsValid.Should().BeFalse();
        result.Errors.Should().Contain(e => e.PropertyName == nameof(CreateTakeawayOrderCommand.Items));
    }
}
