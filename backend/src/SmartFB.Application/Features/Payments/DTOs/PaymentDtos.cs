using SmartFB.Domain.Enums;

namespace SmartFB.Application.Features.Payments.DTOs;

public record PaymentDto(
    Guid Id,
    Guid OrderId,
    PaymentMethod PaymentMethod,
    decimal Amount,
    string? TransactionCode,
    PaymentStatus Status,
    string? PayosPaymentLinkId,
    DateTime? PaidAt,
    DateTime CreatedAt
);

public record VietQrDto(
    Guid OrderId,
    string OrderCode,
    decimal Amount,
    string QrCodeUrl,
    string DeepLinkUrl,
    DateTime ExpiresAt
);

public record PayOSWebhookDataDto(
    long OrderCode,
    decimal Amount,
    string Description,
    string AccountNumber,
    string Reference,
    string TransactionDateTime,
    string PaymentLinkId,
    string Code,
    string Desc
);

public record CashConfirmationResultDto(
    Guid OrderId,
    string OrderCode,
    decimal TotalAmount,
    decimal ReceivedAmount,
    decimal ChangeAmount,
    OrderStatus OrderStatus,
    PaymentStatus PaymentStatus
);

public record PaymentStatusDto(
    Guid OrderId,
    string OrderCode,
    bool IsPaid,
    PaymentStatus Status,
    DateTime? PaidAt
);
