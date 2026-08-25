using FluentValidation;
using SmartFB.Application.Features.Payments.Commands.ConfirmCashPayment;
using SmartFB.Application.Features.Payments.Commands.ProcessPayOSWebhook;

namespace SmartFB.Application.Features.Payments.Validators;

public class ConfirmCashPaymentCommandValidator : AbstractValidator<ConfirmCashPaymentCommand>
{
    public ConfirmCashPaymentCommandValidator()
    {
        RuleFor(x => x.OrderId).NotEmpty().WithMessage("ID đơn hàng không hợp lệ.");
        RuleFor(x => x.ReceivedAmount).GreaterThan(0).WithMessage("Số tiền khách đưa phải lớn hơn 0.");
    }
}

public class ProcessPayOSWebhookCommandValidator : AbstractValidator<ProcessPayOSWebhookCommand>
{
    public ProcessPayOSWebhookCommandValidator()
    {
        RuleFor(x => x.Data).NotNull().WithMessage("Dữ liệu webhook không được null.");
        RuleFor(x => x.Signature).NotEmpty().WithMessage("Chữ ký signature không được để trống.");
    }
}
