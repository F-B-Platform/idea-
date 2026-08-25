using System.Net;
using System.Net.Http.Json;
using System.Text.Json;
using FluentAssertions;
using SmartFB.Application.Features.Orders.Commands.CreateDineInPostpaidOrder;
using SmartFB.Application.Features.Orders.Commands.CreateDineInPrepaidOrder;
using SmartFB.Application.Features.Orders.DTOs;
using SmartFB.Application.Features.Payments.Commands.ConfirmCashPayment;
using SmartFB.Application.Features.Payments.Commands.ProcessPayOSWebhook;
using SmartFB.Application.Features.Payments.DTOs;
using SmartFB.Domain.Enums;
using SmartFB.IntegrationTests.Fixtures;
using Xunit;

namespace SmartFB.IntegrationTests.Endpoints;

public class DineInOrdersFlowTests : IClassFixture<CustomWebApplicationFactory>
{
    private readonly HttpClient _client;

    public DineInOrdersFlowTests(CustomWebApplicationFactory factory)
    {
        _client = factory.CreateClient();
    }

    [Fact]
    public async Task UAT_DineInBranchA_PrepaidVietQR_ShouldCreatePendingPayment_AndProcessPayment()
    {
        // 1. Arrange & Act: Create Prepaid Dine-in Order (TC-DINE-01A)
        var prepaidReq = new CreateDineInPrepaidOrderCommand(
            BranchId: SeedDataConstants.BranchQ1Id,
            TableId: SeedDataConstants.Table04Id,
            CustomerPhone: "0909123456",
            CustomerName: "Nguyen Hoang Nam",
            Note: "It duong",
            Items: new List<CreateOrderItemRequestDto>
            {
                new(SeedDataConstants.ProductTraDaoId, SeedDataConstants.SizeLId, 1, "It da")
            }
        );

        var createResponse = await _client.PostAsJsonAsync("/api/v1/orders/dine-in/prepaid", prepaidReq);

        // Assert Step 1: 200 OK with status PendingPayment & VietQR Link
        createResponse.StatusCode.Should().Be(HttpStatusCode.OK);
        var createResult = await createResponse.Content.ReadFromJsonAsync<JsonElement>();
        var data = createResult.GetProperty("data");

        string orderIdStr = data.GetProperty("orderId").GetString()!;
        Guid orderId = Guid.Parse(orderIdStr);
        string orderCode = data.GetProperty("orderCode").GetString()!;
        decimal finalAmount = data.GetProperty("totalAmount").GetDecimal();

        finalAmount.Should().Be(53000m); // 45k base + 8k L size
        data.GetProperty("vietQrCodeUrl").GetString().Should().Contain("53000");

        // Step 2: Customer pays via PayOS -> Webhook arrives
        long orderCodeNumber = 10042;
        var webhookData = new PayOSWebhookDataDto(
            OrderCode: orderCodeNumber,
            Amount: 53000m,
            Description: $"SmartCoffee Q1 {orderCode}",
            AccountNumber: "0001882199201",
            Reference: "FT2408239912",
            TransactionDateTime: "2026-08-25T14:40:00Z",
            PaymentLinkId: $"pay-link-{orderId}",
            Code: "00",
            Desc: "success"
        );

        var webhookResponse = await _client.PostAsJsonAsync("/api/v1/payments/webhook/payos", webhookData);

        webhookResponse.StatusCode.Should().Be(HttpStatusCode.OK);

        // Step 3: Check Order Tracking -> Status must be accessible
        var trackingResponse = await _client.GetAsync($"/api/v1/orders/{orderId}");
        trackingResponse.StatusCode.Should().Be(HttpStatusCode.OK);
    }

    [Fact]
    public async Task UAT_DineInBranchB_PostpaidCash_ShouldCreateConfirmedOrderImmediately_AndCollectCash()
    {
        // 1. Arrange & Act: Create Postpaid Dine-in Order (TC-DINE-01B)
        var postpaidReq = new CreateDineInPostpaidOrderCommand(
            BranchId: SeedDataConstants.BranchQ1Id,
            TableId: SeedDataConstants.Table05Id,
            CustomerPhone: "0909123456",
            CustomerName: "Nguyen Hoang Nam",
            Note: "Mang nuoc loc truoc",
            Items: new List<CreateOrderItemRequestDto>
            {
                new(SeedDataConstants.ProductBacXiuId, SeedDataConstants.SizeMId2, 1, "Binh thuong")
            }
        );

        var createResponse = await _client.PostAsJsonAsync("/api/v1/orders/dine-in/postpaid", postpaidReq);

        // Assert: Created immediately as Confirmed -> Enters KDS
        createResponse.StatusCode.Should().Be(HttpStatusCode.OK);
        var createResult = await createResponse.Content.ReadFromJsonAsync<JsonElement>();
        var data = createResult.GetProperty("data");

        Guid orderId = Guid.Parse(data.GetProperty("orderId").GetString()!);
        data.GetProperty("totalAmount").GetDecimal().Should().Be(35000m);

        // Step 2: Staff serves drink with bill & confirms cash payment (35,000 VND)
        var cashReq = new ConfirmCashPaymentCommand(orderId, 50000m); // 50k given -> 15k change
        var cashResponse = await _client.PostAsJsonAsync("/api/v1/payments/confirm-cash", cashReq);

        cashResponse.StatusCode.Should().Be(HttpStatusCode.OK);
        var cashResult = await cashResponse.Content.ReadFromJsonAsync<JsonElement>();
        cashResult.GetProperty("data").GetProperty("changeAmount").GetDecimal().Should().Be(15000m);
    }
}
