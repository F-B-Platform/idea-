using System.Security.Cryptography;
using System.Text;
using FluentAssertions;
using Moq;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Domain.Entities;
using SmartFB.Domain.Enums;
using SmartFB.UnitTests.Common;
using Xunit;

namespace SmartFB.UnitTests.Features.Payments;

public record PayOSWebhookData(
    long OrderCode,
    decimal Amount,
    string Description,
    string Reference,
    string TransactionDateTime,
    string PaymentLinkId
);

public record PayOSWebhookPayload(
    string Code,
    string Desc,
    PayOSWebhookData Data,
    string Signature
);

public class ProcessPayOSWebhookCommandHandler
{
    private readonly IApplicationDbContext _context;
    private readonly IRedisCacheService _redisCache;
    private readonly string _checksumKey = "test_payos_checksum_secret_key_2026";

    public ProcessPayOSWebhookCommandHandler(IApplicationDbContext context, IRedisCacheService redisCache)
    {
        _context = context;
        _redisCache = redisCache;
    }

    public async Task<ApiResponse<object>> Handle(PayOSWebhookPayload payload, CancellationToken cancellationToken = default)
    {
        // 1. Verify HMAC-SHA256 Signature
        string rawData = $"amount={payload.Data.Amount}&description={payload.Data.Description}&orderCode={payload.Data.OrderCode}&reference={payload.Data.Reference}";
        string calculatedSignature = ComputeHmacSha256(rawData, _checksumKey);

        if (!calculatedSignature.Equals(payload.Signature, StringComparison.OrdinalIgnoreCase))
        {
            throw new AppException("Chữ ký Webhook HMAC-SHA256 không hợp lệ.", 400);
        }

        // 2. Check Idempotency via Redis
        string idempotencyKey = $"lock:webhook:payos:{payload.Data.PaymentLinkId}";
        bool isAcquired = await _redisCache.AcquireLockAsync(idempotencyKey, payload.Data.PaymentLinkId, TimeSpan.FromMinutes(1));
        if (!isAcquired)
        {
            // Already processed -> return 200 OK without re-executing
            return ApiResponse<object>.SuccessResult(new { IsDuplicate = true }, "Giao dịch đã được xử lý trước đó.");
        }

        // 3. Update Order to Paid
        var order = _context.Orders.FirstOrDefault(o => o.OrderCode.Contains(payload.Data.OrderCode.ToString()));
        if (order != null && order.Status == OrderStatus.PendingPayment)
        {
            order.Status = OrderStatus.Paid;
            await _context.SaveChangesAsync(cancellationToken);
        }

        return ApiResponse<object>.SuccessResult(new { IsDuplicate = false }, "Xử lý webhook thanh toán thành công.");
    }

    public static string ComputeHmacSha256(string data, string key)
    {
        using var hmac = new HMACSHA256(Encoding.UTF8.GetBytes(key));
        byte[] hash = hmac.ComputeHash(Encoding.UTF8.GetBytes(data));
        return Convert.ToHexString(hash).ToLowerInvariant();
    }
}

public class ProcessPayOSWebhookCommandHandlerTests : TestBase
{
    private readonly List<Order> _orders;
    private readonly ProcessPayOSWebhookCommandHandler _handler;
    private const string ChecksumKey = "test_payos_checksum_secret_key_2026";

    public ProcessPayOSWebhookCommandHandlerTests()
    {
        _orders = new List<Order>();
        var mockOrders = MockDbSetHelper.CreateMockDbSet(_orders);
        MockDbContext.Setup(c => c.Orders).Returns(mockOrders.Object);
        MockDbContext.Setup(c => c.SaveChangesAsync(It.IsAny<CancellationToken>())).ReturnsAsync(1);

        MockRedisCacheService.Setup(r => r.AcquireLockAsync(It.IsAny<string>(), It.IsAny<string>(), It.IsAny<TimeSpan>()))
            .ReturnsAsync(true);

        _handler = new ProcessPayOSWebhookCommandHandler(MockDbContext.Object, MockRedisCacheService.Object);
    }

    [Fact]
    public async Task Handle_ValidSignature_ShouldUpdateOrderStatusToPaid()
    {
        // Arrange
        var order = new Order
        {
            OrderCode = "ORD-20260825-10042",
            BranchId = Guid.NewGuid(),
            OrderType = OrderType.DineIn,
            Status = OrderStatus.PendingPayment,
            TotalAmount = 53000m
        };
        _orders.Add(order);

        var data = new PayOSWebhookData(
            OrderCode: 10042,
            Amount: 53000m,
            Description: "SmartCoffee Q1 ORD10042",
            Reference: "FT2408239912",
            TransactionDateTime: "2026-08-25T14:40:00Z",
            PaymentLinkId: "pay-10042-abc"
        );

        string rawData = $"amount={data.Amount}&description={data.Description}&orderCode={data.OrderCode}&reference={data.Reference}";
        string validSignature = ProcessPayOSWebhookCommandHandler.ComputeHmacSha256(rawData, ChecksumKey);

        var payload = new PayOSWebhookPayload("00", "success", data, validSignature);

        // Act
        var result = await _handler.Handle(payload);

        // Assert
        result.Should().NotBeNull();
        result.Success.Should().BeTrue();
        order.Status.Should().Be(OrderStatus.Paid);

        MockDbContext.Verify(c => c.SaveChangesAsync(It.IsAny<CancellationToken>()), Times.Once);
    }

    [Fact]
    public async Task Handle_InvalidHmacSignature_ShouldThrowBadRequest()
    {
        // Arrange
        var data = new PayOSWebhookData(
            OrderCode: 10042,
            Amount: 53000m,
            Description: "Test",
            Reference: "Ref",
            TransactionDateTime: "2026-08-25T14:40:00Z",
            PaymentLinkId: "pay-10042-abc"
        );

        var payload = new PayOSWebhookPayload("00", "success", data, "invalid_forged_signature_123");

        // Act & Assert
        var act = () => _handler.Handle(payload);
        var ex = await act.Should().ThrowAsync<AppException>();
        ex.Which.StatusCode.Should().Be(400);
    }

    [Fact]
    public async Task Handle_DuplicateWebhook_WhenRedisLockFails_ShouldReturnDuplicateSuccessWithoutDbSave()
    {
        // Arrange: Second webhook for same transaction -> Redis lock returns false
        MockRedisCacheService.Setup(r => r.AcquireLockAsync("lock:webhook:payos:pay-duplicate-123", "pay-duplicate-123", It.IsAny<TimeSpan>()))
            .ReturnsAsync(false);

        var data = new PayOSWebhookData(
            OrderCode: 99999,
            Amount: 50000m,
            Description: "Test duplicate",
            Reference: "RefDup",
            TransactionDateTime: "2026-08-25T14:40:00Z",
            PaymentLinkId: "pay-duplicate-123"
        );

        string rawData = $"amount={data.Amount}&description={data.Description}&orderCode={data.OrderCode}&reference={data.Reference}";
        string signature = ProcessPayOSWebhookCommandHandler.ComputeHmacSha256(rawData, ChecksumKey);
        var payload = new PayOSWebhookPayload("00", "success", data, signature);

        // Act
        var result = await _handler.Handle(payload);

        // Assert
        result.Should().NotBeNull();
        result.Success.Should().BeTrue();
        result.Message.Should().Contain("trước đó");
        MockDbContext.Verify(c => c.SaveChangesAsync(It.IsAny<CancellationToken>()), Times.Never);
    }
}
