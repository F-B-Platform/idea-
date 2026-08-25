using FluentAssertions;
using FluentValidation;
using SmartFB.UnitTests.Features.Payments;
using Xunit;

namespace SmartFB.UnitTests.Validators;

public class PayOSWebhookValidator : AbstractValidator<PayOSWebhookPayload>
{
    public PayOSWebhookValidator()
    {
        RuleFor(x => x.Code).NotEmpty().WithMessage("Mã kết quả webhook không được để trống.");
        RuleFor(x => x.Signature).NotEmpty().WithMessage("Chữ ký webhook HMAC-SHA256 không được để trống.");
        RuleFor(x => x.Data).NotNull().WithMessage("Dữ liệu webhook không được null.");
        When(x => x.Data != null, () =>
        {
            RuleFor(x => x.Data.OrderCode).GreaterThan(0).WithMessage("Mã đơn hàng phải lớn hơn 0.");
            RuleFor(x => x.Data.Amount).GreaterThan(0).WithMessage("Số tiền thanh toán phải lớn hơn 0.");
            RuleFor(x => x.Data.PaymentLinkId).NotEmpty().WithMessage("Mã liên kết thanh toán không được để trống.");
        });
    }
}

public class PayOSWebhookValidatorTests
{
    private readonly PayOSWebhookValidator _validator = new();

    [Fact]
    public void Validate_ValidWebhookPayload_ShouldPass()
    {
        var data = new PayOSWebhookData(
            OrderCode: 10042,
            Amount: 53000m,
            Description: "ORD10042",
            Reference: "FT2408239912",
            TransactionDateTime: "2026-08-25T14:40:00Z",
            PaymentLinkId: "pay-link-10042"
        );

        var payload = new PayOSWebhookPayload("00", "success", data, "valid_signature_hash");
        var result = _validator.Validate(payload);

        result.IsValid.Should().BeTrue();
    }

    [Fact]
    public void Validate_EmptySignature_ShouldFail()
    {
        var data = new PayOSWebhookData(
            OrderCode: 10042,
            Amount: 53000m,
            Description: "ORD10042",
            Reference: "FT2408239912",
            TransactionDateTime: "2026-08-25T14:40:00Z",
            PaymentLinkId: "pay-link-10042"
        );

        var payload = new PayOSWebhookPayload("00", "success", data, "");
        var result = _validator.Validate(payload);

        result.IsValid.Should().BeFalse();
        result.Errors.Should().Contain(e => e.PropertyName == nameof(PayOSWebhookPayload.Signature));
    }
}
