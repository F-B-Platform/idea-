using System.Net;
using System.Net.Http.Json;
using System.Text.Json;
using FluentAssertions;
using SmartFB.Application.Features.Orders.Commands.CreateTakeawayOrder;
using SmartFB.Application.Features.Orders.DTOs;
using SmartFB.Domain.Enums;
using SmartFB.IntegrationTests.Fixtures;
using Xunit;

namespace SmartFB.IntegrationTests.Endpoints;

public class TakeawayPosLoyaltyFlowTests : IClassFixture<CustomWebApplicationFactory>
{
    private readonly HttpClient _client;

    public TakeawayPosLoyaltyFlowTests(CustomWebApplicationFactory factory)
    {
        _client = factory.CreateClient();
    }

    [Fact]
    public async Task UAT_TakeawayPOS_Redeem10Cups_ShouldApply100PercentDiscountOnFreeCup_AndResetBalance()
    {
        // Arrange (TC-TAKE-01): Customer has 10 cups, orders 2 Ca Phe Muoi (78,000 VND), redeems 1 free (-39,000 VND) -> final 39,000 VND.
        var takeawayReq = new CreateTakeawayOrderCommand(
            BranchId: SeedDataConstants.BranchQ1Id,
            CustomerPhone: "0909123456",
            CustomerName: "Nguyen Hoang Nam",
            RedeemFreeCup: true,
            Items: new List<CreateOrderItemRequestDto>
            {
                new(SeedDataConstants.ProductCaPheMuoiId, SeedDataConstants.SizeMId3, 2, "It da")
            },
            PaymentMethod: PaymentMethod.Cash
        );

        // Act
        var response = await _client.PostAsJsonAsync("/api/v1/orders/takeaway", takeawayReq);

        // Assert
        response.StatusCode.Should().Be(HttpStatusCode.OK);
        var result = await response.Content.ReadFromJsonAsync<JsonElement>();
        var data = result.GetProperty("data");

        data.GetProperty("subTotal").GetDecimal().Should().Be(78000m);
        data.GetProperty("loyaltyDiscount").GetDecimal().Should().Be(39000m);
        data.GetProperty("totalAmount").GetDecimal().Should().Be(39000m);
        data.GetProperty("remainingCupBalance").GetInt32().Should().Be(1); // 10 - 10 + 1 paid = 1 cup
    }

    [Fact]
    public async Task UAT_TakeawayPOS_NewCustomerRegistration_ShouldAccumulateCups()
    {
        // Arrange (TC-TAKE-03): Register new walk-in member with fresh phone
        var takeawayReq = new CreateTakeawayOrderCommand(
            BranchId: SeedDataConstants.BranchQ1Id,
            CustomerPhone: "0911223344",
            CustomerName: "Tran Van Moi",
            RedeemFreeCup: false,
            Items: new List<CreateOrderItemRequestDto>
            {
                new(SeedDataConstants.ProductBacXiuId, SeedDataConstants.SizeMId2, 2, "Mang ve")
            },
            PaymentMethod: PaymentMethod.Cash
        );

        // Act
        var response = await _client.PostAsJsonAsync("/api/v1/orders/takeaway", takeawayReq);

        // Assert
        response.StatusCode.Should().Be(HttpStatusCode.OK);
        var result = await response.Content.ReadFromJsonAsync<JsonElement>();
        var data = result.GetProperty("data");

        data.GetProperty("earnedCups").GetInt32().Should().Be(2);
        data.GetProperty("remainingCupBalance").GetInt32().Should().Be(2);
    }
}
