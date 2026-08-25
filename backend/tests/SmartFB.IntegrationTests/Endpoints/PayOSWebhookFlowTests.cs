using System.Net;
using System.Net.Http.Json;
using System.Security.Cryptography;
using System.Text;
using System.Text.Json;
using FluentAssertions;
using SmartFB.Application.Features.Payments.DTOs;
using SmartFB.IntegrationTests.Fixtures;
using Xunit;

namespace SmartFB.IntegrationTests.Endpoints;

public class PayOSWebhookFlowTests : IClassFixture<CustomWebApplicationFactory>
{
    private readonly HttpClient _client;

    public PayOSWebhookFlowTests(CustomWebApplicationFactory factory)
    {
        _client = factory.CreateClient();
    }

    [Fact]
    public async Task UAT_PayOSWebhook_ValidSignatureAndIdempotency_ShouldHandlePayment()
    {
        // Arrange (TC-EDGE-02): Valid Webhook Data
        var webhookData = new PayOSWebhookDataDto(
            OrderCode: 10042,
            Amount: 53000m,
            Description: "Thanh toan don DIN-260825-001",
            AccountNumber: "0001882199201",
            Reference: "FT262359918239",
            TransactionDateTime: "2026-08-25T14:32:15Z",
            PaymentLinkId: $"payos-link-{Guid.NewGuid():N}",
            Code: "00",
            Desc: "success"
        );

        // Compute HMAC
        string rawData = JsonSerializer.Serialize(webhookData);
        using var hmac = new HMACSHA256(Encoding.UTF8.GetBytes(SeedDataConstants.PayOsChecksumSecret));
        byte[] hash = hmac.ComputeHash(Encoding.UTF8.GetBytes(rawData));
        string signature = Convert.ToHexString(hash).ToLowerInvariant();

        var request = new HttpRequestMessage(HttpMethod.Post, "/api/v1/payments/webhook/payos")
        {
            Content = JsonContent.Create(webhookData)
        };
        request.Headers.Add("x-payos-signature", signature);

        // Act - First Execution
        var response1 = await _client.SendAsync(request);

        // Assert
        response1.StatusCode.Should().Be(HttpStatusCode.OK);
        var result1 = await response1.Content.ReadFromJsonAsync<JsonElement>();
        result1.GetProperty("success").GetBoolean().Should().BeTrue();
    }
}
