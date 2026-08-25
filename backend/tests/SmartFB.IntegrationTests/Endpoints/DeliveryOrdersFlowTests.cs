using System.Net;
using System.Net.Http.Json;
using System.Text.Json;
using FluentAssertions;
using SmartFB.Application.Features.Orders.Commands.CreateDeliveryOrder;
using SmartFB.Application.Features.Orders.DTOs;
using SmartFB.IntegrationTests.Fixtures;
using Xunit;

namespace SmartFB.IntegrationTests.Endpoints;

public class DeliveryOrdersFlowTests : IClassFixture<CustomWebApplicationFactory>
{
    private readonly HttpClient _client;

    public DeliveryOrdersFlowTests(CustomWebApplicationFactory factory)
    {
        _client = factory.CreateClient();
    }

    [Fact]
    public async Task UAT_DeliveryOrder_ShouldAdd20kFixedShippingFee_AndGenerateVietQR()
    {
        // Arrange (TC-DEL-01): 2 Trà Đào M (90,000 VND) + 20,000 VND shipping fee = 110,000 VND
        var deliveryReq = new CreateDeliveryOrderCommand(
            BranchId: SeedDataConstants.BranchQ1Id,
            RecipientName: "Mai Huong",
            RecipientPhone: "0987654321",
            DeliveryAddress: "Bitexco Tower, Quan 1, TP.HCM",
            DeliveryNotes: "Giao sanh le tan",
            Items: new List<CreateOrderItemRequestDto>
            {
                new(SeedDataConstants.ProductTraDaoId, SeedDataConstants.SizeMId, 2, "It da")
            }
        );

        // Act
        var response = await _client.PostAsJsonAsync("/api/v1/orders/delivery", deliveryReq);

        // Assert
        response.StatusCode.Should().Be(HttpStatusCode.OK);
        var result = await response.Content.ReadFromJsonAsync<JsonElement>();
        var data = result.GetProperty("data");

        data.GetProperty("subTotal").GetDecimal().Should().Be(90000m);
        data.GetProperty("deliveryFee").GetDecimal().Should().Be(20000m);
        data.GetProperty("totalAmount").GetDecimal().Should().Be(110000m);
        data.GetProperty("vietQrCodeUrl").GetString().Should().Contain("110000");
    }

    [Fact]
    public async Task UAT_DeliveryOrder_EmptyItems_ShouldReturnBadRequest()
    {
        // Arrange (TC-DEL-02): Empty items basket
        var deliveryReq = new CreateDeliveryOrderCommand(
            BranchId: SeedDataConstants.BranchQ1Id,
            RecipientName: "Mai Huong",
            RecipientPhone: "0987654321",
            DeliveryAddress: "Bitexco Tower",
            DeliveryNotes: null,
            Items: new List<CreateOrderItemRequestDto>()
        );

        // Act
        var response = await _client.PostAsJsonAsync("/api/v1/orders/delivery", deliveryReq);

        // Assert
        response.StatusCode.Should().Be(HttpStatusCode.BadRequest);
    }
}
