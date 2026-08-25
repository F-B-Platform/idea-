using FluentAssertions;
using FluentValidation;
using SmartFB.UnitTests.Features.Orders;
using Xunit;

namespace SmartFB.UnitTests.Validators;

public class CreateDeliveryOrderValidator : AbstractValidator<CreateDeliveryOrderCommand>
{
    public CreateDeliveryOrderValidator()
    {
        RuleFor(x => x.BranchId).NotEmpty().WithMessage("Chi nhánh không được để trống.");
        RuleFor(x => x.RecipientName).NotEmpty().WithMessage("Tên người nhận không được để trống.");
        RuleFor(x => x.RecipientPhone)
            .NotEmpty().WithMessage("Số điện thoại người nhận không được để trống.")
            .Matches(@"^(03|05|07|08|09)\d{8}$").WithMessage("Số điện thoại phải gồm 10 chữ số đúng định dạng Việt Nam.");
        RuleFor(x => x.DeliveryAddress)
            .NotEmpty().WithMessage("Địa chỉ giao hàng không được để trống.")
            .MinimumLength(10).WithMessage("Địa chỉ giao hàng phải có độ dài tối thiểu 10 ký tự.");
        RuleFor(x => x.Items)
            .NotEmpty().WithMessage("Đơn hàng phải có ít nhất 1 món.");
    }
}

public class CreateDeliveryOrderValidatorTests
{
    private readonly CreateDeliveryOrderValidator _validator = new();

    [Fact]
    public void Validate_ValidCommand_ShouldNotHaveAnyErrors()
    {
        // Arrange
        var command = new CreateDeliveryOrderCommand(
            BranchId: Guid.NewGuid(),
            RecipientName: "Nguyen Van A",
            RecipientPhone: "0909123456",
            DeliveryAddress: "123 Le Loi, Quan 1, TP Ho Chi Minh",
            Items: new List<OrderItemRequestDto> { new(Guid.NewGuid(), "Tra Dao", "M", 1, 35000m) }
        );

        // Act
        var result = _validator.Validate(command);

        // Assert
        result.IsValid.Should().BeTrue();
    }

    [Theory]
    [InlineData("123456")] // Too short
    [InlineData("0123456789")] // Invalid prefix
    [InlineData("09091234567")] // 11 digits
    [InlineData("abc0909123")] // Alphabets
    public void Validate_InvalidPhoneFormat_ShouldHaveValidationError(string phone)
    {
        // Arrange
        var command = new CreateDeliveryOrderCommand(
            BranchId: Guid.NewGuid(),
            RecipientName: "Nguyen Van A",
            RecipientPhone: phone,
            DeliveryAddress: "123 Le Loi, Quan 1, TP Ho Chi Minh",
            Items: new List<OrderItemRequestDto> { new(Guid.NewGuid(), "Tra Dao", "M", 1, 35000m) }
        );

        // Act
        var result = _validator.Validate(command);

        // Assert
        result.IsValid.Should().BeFalse();
        result.Errors.Should().Contain(e => e.PropertyName == nameof(CreateDeliveryOrderCommand.RecipientPhone));
    }

    [Theory]
    [InlineData("")]
    [InlineData("Short")]
    public void Validate_ShortOrEmptyAddress_ShouldHaveValidationError(string address)
    {
        // Arrange
        var command = new CreateDeliveryOrderCommand(
            BranchId: Guid.NewGuid(),
            RecipientName: "Nguyen Van A",
            RecipientPhone: "0909123456",
            DeliveryAddress: address,
            Items: new List<OrderItemRequestDto> { new(Guid.NewGuid(), "Tra Dao", "M", 1, 35000m) }
        );

        // Act
        var result = _validator.Validate(command);

        // Assert
        result.IsValid.Should().BeFalse();
        result.Errors.Should().Contain(e => e.PropertyName == nameof(CreateDeliveryOrderCommand.DeliveryAddress));
    }

    [Fact]
    public void Validate_EmptyItemsList_ShouldHaveValidationError()
    {
        // Arrange
        var command = new CreateDeliveryOrderCommand(
            BranchId: Guid.NewGuid(),
            RecipientName: "Nguyen Van A",
            RecipientPhone: "0909123456",
            DeliveryAddress: "123 Le Loi, Quan 1, TP Ho Chi Minh",
            Items: new List<OrderItemRequestDto>()
        );

        // Act
        var result = _validator.Validate(command);

        // Assert
        result.IsValid.Should().BeFalse();
        result.Errors.Should().Contain(e => e.PropertyName == nameof(CreateDeliveryOrderCommand.Items));
    }
}
