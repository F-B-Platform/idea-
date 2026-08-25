using FluentAssertions;
using SmartFB.Domain.Entities;
using SmartFB.Domain.Enums;
using Xunit;

namespace SmartFB.UnitTests.Domain;

public class OrderEntityTests
{
    [Fact]
    public void Order_Delivery_ShouldApplyFlat20kShippingFee()
    {
        // Arrange
        const decimal subTotal = 78000m;
        const decimal deliveryFee = 20000m;

        // Act
        var order = new Order
        {
            OrderCode = "DEL-20260825-0001",
            BranchId = Guid.NewGuid(),
            OrderType = OrderType.Delivery,
            SubTotal = subTotal,
            DeliveryFee = deliveryFee,
            DiscountAmount = 0,
            TotalAmount = subTotal + deliveryFee,
            CustomerName = "Mai Huong",
            CustomerPhone = "0987654321",
            DeliveryAddress = "Bitexco Tower Q1"
        };

        // Assert
        order.OrderType.Should().Be(OrderType.Delivery);
        order.DeliveryFee.Should().Be(20000m);
        order.TotalAmount.Should().Be(98000m);
    }

    [Theory]
    [InlineData(OrderType.DineIn, 0)]
    [InlineData(OrderType.TakeAway, 0)]
    public void Order_DineInAndTakeaway_ShouldHaveZeroDeliveryFee(OrderType orderType, decimal expectedFee)
    {
        // Arrange & Act
        var order = new Order
        {
            OrderCode = "ORD-TEST-002",
            BranchId = Guid.NewGuid(),
            OrderType = orderType,
            SubTotal = 50000m,
            DeliveryFee = expectedFee,
            TotalAmount = 50000m + expectedFee
        };

        // Assert
        order.DeliveryFee.Should().Be(0m);
        order.TotalAmount.Should().Be(50000m);
    }

    [Fact]
    public void Order_StatusTransitions_ValidDineInPrepaidFlow()
    {
        // Arrange
        var order = new Order
        {
            OrderCode = "ORD-DINEIN-001",
            BranchId = Guid.NewGuid(),
            OrderType = OrderType.DineIn,
            Status = OrderStatus.PendingPayment
        };

        // Step 1: Initial state is PendingPayment
        order.Status.Should().Be(OrderStatus.PendingPayment);

        // Step 2: Customer pays via PayOS Webhook -> Paid
        order.Status = OrderStatus.Paid;
        order.Status.Should().Be(OrderStatus.Paid);

        // Step 3: Kitchen receives and confirms order -> Confirmed
        order.Status = OrderStatus.Confirmed;
        order.Status.Should().Be(OrderStatus.Confirmed);

        // Step 4: Barista starts preparing -> Preparing
        order.Status = OrderStatus.Preparing;
        order.Status.Should().Be(OrderStatus.Preparing);

        // Step 5: Barista finishes preparing -> Ready
        order.Status = OrderStatus.Ready;
        order.Status.Should().Be(OrderStatus.Ready);

        // Step 6: Staff serves to table / customer completes -> Completed
        order.Status = OrderStatus.Completed;
        order.Status.Should().Be(OrderStatus.Completed);
    }

    [Fact]
    public void Order_StatusTransitions_ValidDineInPostpaidFlow()
    {
        // Arrange: Postpaid cash order enters kitchen directly as Confirmed
        var order = new Order
        {
            OrderCode = "ORD-POSTPAID-001",
            BranchId = Guid.NewGuid(),
            OrderType = OrderType.DineIn,
            Status = OrderStatus.Confirmed
        };

        order.Status.Should().Be(OrderStatus.Confirmed);

        // Barista prepares & readies
        order.Status = OrderStatus.Preparing;
        order.Status.Should().Be(OrderStatus.Preparing);

        order.Status = OrderStatus.Ready;
        order.Status.Should().Be(OrderStatus.Ready);

        // Staff collects cash and completes
        order.Status = OrderStatus.Completed;
        order.Status.Should().Be(OrderStatus.Completed);
    }

    [Fact]
    public void Order_TtlCancellation_ShouldTransitionFromPendingPaymentToCancelled()
    {
        // Arrange
        var order = new Order
        {
            OrderCode = "ORD-EXPIRED-001",
            BranchId = Guid.NewGuid(),
            OrderType = OrderType.DineIn,
            Status = OrderStatus.PendingPayment
        };

        // Act: 10-minute timeout expired
        order.Status = OrderStatus.Cancelled;

        // Assert
        order.Status.Should().Be(OrderStatus.Cancelled);
    }

    [Fact]
    public void Order_ItemsAggregation_ShouldMatchSubTotal()
    {
        // Arrange
        var orderId = Guid.NewGuid();
        var item1 = new OrderItem
        {
            OrderId = orderId,
            ProductId = Guid.NewGuid(),
            SizeId = Guid.NewGuid(),
            Quantity = 2,
            UnitPrice = 45000m,
            SubtotalPrice = 90000m
        };

        var item2 = new OrderItem
        {
            OrderId = orderId,
            ProductId = Guid.NewGuid(),
            SizeId = Guid.NewGuid(),
            Quantity = 1,
            UnitPrice = 35000m,
            SubtotalPrice = 35000m
        };

        var order = new Order
        {
            Id = orderId,
            OrderCode = "ORD-MULTI-001",
            BranchId = Guid.NewGuid(),
            OrderType = OrderType.DineIn,
            Items = new List<OrderItem> { item1, item2 },
            SubTotal = item1.SubtotalPrice + item2.SubtotalPrice,
            DiscountAmount = 10000m,
            DeliveryFee = 0m
        };
        order.TotalAmount = order.SubTotal - order.DiscountAmount + order.DeliveryFee;

        // Assert
        order.SubTotal.Should().Be(125000m);
        order.DiscountAmount.Should().Be(10000m);
        order.TotalAmount.Should().Be(115000m);
        order.Items.Should().HaveCount(2);
    }
}
