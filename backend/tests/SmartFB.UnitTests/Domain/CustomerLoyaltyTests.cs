using FluentAssertions;
using SmartFB.Domain.Entities;
using SmartFB.Domain.Enums;
using Xunit;

namespace SmartFB.UnitTests.Domain;

public class CustomerLoyaltyTests
{
    [Fact]
    public void Customer_InitialCupCount_ShouldBeZero()
    {
        // Arrange & Act
        var customer = new Customer
        {
            PhoneNumber = "0909123456",
            FullName = "Nguyen Van A"
        };

        // Assert
        customer.TakeawayCupCount.Should().Be(0);
        customer.TotalLoyaltyPoints.Should().Be(0);
    }

    [Theory]
    [InlineData(1, 1, false)]
    [InlineData(5, 5, false)]
    [InlineData(9, 9, false)]
    [InlineData(10, 10, true)]
    [InlineData(12, 12, true)]
    public void Customer_AccumulateTakeawayCups_ShouldAccuratelyTrackAndFlagFreeRewardEligibility(
        int cupsToAdd, int expectedTotal, bool expectedEligibility)
    {
        // Arrange
        var customer = new Customer
        {
            PhoneNumber = "0909123456",
            FullName = "Nguyen Van A",
            TakeawayCupCount = 0
        };

        // Act
        customer.TakeawayCupCount += cupsToAdd;
        bool isEligibleForFreeReward = customer.TakeawayCupCount >= 10;

        // Assert
        customer.TakeawayCupCount.Should().Be(expectedTotal);
        isEligibleForFreeReward.Should().Be(expectedEligibility);
    }

    [Fact]
    public void Customer_Redeem10Cups_WhenPurchasing2NewCups_ShouldResetCorrectlyTo2()
    {
        // Arrange: Customer has exactly 10 accumulated takeaway cups
        var customer = new Customer
        {
            PhoneNumber = "0909123456",
            FullName = "Nguyen Hoang Nam",
            TakeawayCupCount = 10
        };

        int freeCupsToRedeem = 1;
        int newTakeawayCupsPurchased = 2;

        // Act: Formula: TakeawayCupCount = (CurrentCups - (freeCups * 10)) + newCupsPurchased
        int cupsToDeduct = freeCupsToRedeem * 10;
        customer.TakeawayCupCount.Should().BeGreaterThanOrEqualTo(cupsToDeduct, "Must have at least 10 cups to redeem");
        
        customer.TakeawayCupCount = (customer.TakeawayCupCount - cupsToDeduct) + newTakeawayCupsPurchased;

        // Assert: 10 - 10 + 2 = 2
        customer.TakeawayCupCount.Should().Be(2);
    }

    [Fact]
    public void Customer_Redeem10Cups_WhenPurchasingNoAdditionalPaidCups_ShouldResetToZero()
    {
        // Arrange
        var customer = new Customer
        {
            PhoneNumber = "0909123456",
            FullName = "Le Van Hung",
            TakeawayCupCount = 10
        };

        // Act
        customer.TakeawayCupCount -= 10;

        // Assert
        customer.TakeawayCupCount.Should().Be(0);
    }

    [Theory]
    [InlineData(OrderType.DineIn, false)]
    [InlineData(OrderType.Delivery, false)]
    [InlineData(OrderType.TakeAway, true)]
    public void CustomerLoyalty_ShouldOnlyApplyToTakeawayOrders(OrderType orderType, bool allowed)
    {
        // Arrange & Act
        bool isLoyaltyAllowed = orderType == OrderType.TakeAway;

        // Assert
        isLoyaltyAllowed.Should().Be(allowed, "Loyalty 10-cup rule is exclusively designed for Takeaway channel POS");
    }

    [Fact]
    public void Customer_RedeemWithoutSufficientCups_ShouldBeIdentifiedAsInvalid()
    {
        // Arrange
        var customer = new Customer
        {
            PhoneNumber = "0909123456",
            TakeawayCupCount = 7 // Less than 10
        };

        // Act
        bool canRedeem = customer.TakeawayCupCount >= 10;

        // Assert
        canRedeem.Should().BeFalse("Customer has only 7 cups, requires 10 cups to redeem");
    }
}
