using FluentAssertions;
using SmartFB.Domain.Common;
using SmartFB.Domain.Entities;
using SmartFB.Domain.Enums;
using Xunit;

namespace SmartFB.UnitTests;

public class DomainEntitiesTests
{
    [Fact]
    public void NewOrder_ShouldHaveDefaultPendingPaymentStatus_AndActiveId()
    {
        // Arrange & Act
        var order = new Order
        {
            OrderCode = "ORD-TEST-001",
            BranchId = Guid.NewGuid(),
            OrderType = OrderType.DineIn,
            SubTotal = 50000,
            TotalAmount = 50000
        };

        // Assert
        order.Id.Should().NotBeEmpty();
        order.Status.Should().Be(OrderStatus.PendingPayment);
        order.IsDeleted.Should().BeFalse();
        order.CreatedAt.Should().BeCloseTo(DateTime.UtcNow, TimeSpan.FromSeconds(5));
    }

    [Fact]
    public void Customer_TakeawayCupCount_ShouldTrackAccurately()
    {
        // Arrange
        var customer = new Customer
        {
            PhoneNumber = "0901234567",
            FullName = "Nguyen Van A",
            TakeawayCupCount = 9
        };

        // Act
        customer.TakeawayCupCount += 1;

        // Assert
        customer.TakeawayCupCount.Should().Be(10);
        (customer.TakeawayCupCount % 10 == 0).Should().BeTrue("Customer should be eligible for 1 free cup reward on takeaway");
    }
}
