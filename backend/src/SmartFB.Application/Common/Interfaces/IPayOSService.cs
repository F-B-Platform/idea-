namespace SmartFB.Application.Common.Interfaces;

public record CreatePayOSPaymentRequest(
    long OrderCode,
    decimal Amount,
    string Description,
    string ReturnUrl,
    string CancelUrl,
    string? BuyerName = null,
    string? BuyerPhone = null
);

public record PayOSPaymentLinkResult(
    string PaymentLinkId,
    string CheckoutUrl,
    string QrCode,
    long OrderCode,
    decimal Amount,
    string Status
);

public interface IPayOSService
{
    Task<PayOSPaymentLinkResult> CreatePaymentLinkAsync(CreatePayOSPaymentRequest request, CancellationToken cancellationToken = default);
    bool VerifyWebhookSignature(string webhookBody, string signature);
    Task<PayOSPaymentLinkResult?> GetPaymentLinkInformationAsync(string paymentLinkId, CancellationToken cancellationToken = default);
}
