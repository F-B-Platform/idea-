using System.Net;
using System.Net.Http.Json;
using System.Text.Json;
using FluentAssertions;
using SmartFB.Application.Features.KitchenKDS.Commands.Toggle86Product;
using SmartFB.Application.Features.KitchenKDS.DTOs;
using SmartFB.Application.Features.Orders.Commands.CreateDineInPostpaidOrder;
using SmartFB.Application.Features.Orders.DTOs;
using SmartFB.IntegrationTests.Fixtures;
using Xunit;

namespace SmartFB.IntegrationTests.Endpoints;

public class KitchenKdsFlowTests : IClassFixture<CustomWebApplicationFactory>
{
    private readonly HttpClient _client;

    public KitchenKdsFlowTests(CustomWebApplicationFactory factory)
    {
        _client = factory.CreateClient();
    }

    [Fact]
    public async Task UAT_KDS_GetTickets_ShouldReturnActiveTickets()
    {
        // Act (TC-KDS-01): Query active kitchen tickets for Branch Q1
        var response = await _client.GetAsync($"/api/v1/kitchen/tickets?branchId={SeedDataConstants.BranchQ1Id}");

        // Assert
        response.StatusCode.Should().Be(HttpStatusCode.OK);
        var result = await response.Content.ReadFromJsonAsync<JsonElement>();
        result.GetProperty("success").GetBoolean().Should().BeTrue();
    }

    [Fact]
    public async Task UAT_KDS_86ToggleEmergencyOutOfStock_ShouldUpdateAvailability()
    {
        // Act (TC-KDS-03): Toggle 86-out for Trà Đào
        var toggleReq = new Toggle86ProductCommand(SeedDataConstants.BranchQ1Id, SeedDataConstants.ProductTraDaoId, false);
        var response = await _client.PostAsJsonAsync("/api/v1/kitchen/toggle-86", toggleReq);

        // Assert
        response.StatusCode.Should().Be(HttpStatusCode.OK);
        var result = await response.Content.ReadFromJsonAsync<JsonElement>();
        result.GetProperty("data").GetBoolean().Should().BeTrue();

        // Restore availability
        var restoreReq = new Toggle86ProductCommand(SeedDataConstants.BranchQ1Id, SeedDataConstants.ProductTraDaoId, true);
        await _client.PostAsJsonAsync("/api/v1/kitchen/toggle-86", restoreReq);
    }
}
