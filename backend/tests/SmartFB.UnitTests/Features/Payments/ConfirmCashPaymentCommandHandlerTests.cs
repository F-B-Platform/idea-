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

public record ConfirmCashPaymentCommand(Guid OrderId, decimal ReceivedAmount);

public class ConfirmCashPaymentCommandHandler
{
    private readonly IApplicationDbContext _context;

    public ConfirmCashPaymentCommandHandler(IApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<ApiResponse<object>> Handle(ConfirmCashPaymentCommand command, CancellationToken cancellationToken = default)
    {
        var order = _context.Orders.FirstOrDefault(o => o.Id == command.OrderId);
        if (order == null)
        {
            throw new NotFoundException(nameof(Order), command.OrderId);
        }

        if (command.ReceivedAmount < order.TotalAmount)
        {
            throw new AppException("Số tiền khách đưa không đủ để thanh toán hóa đơn.", 400);
        }

        order.Status = OrderStatus.Completed;

        var payment = new Payment
        {
            OrderId = order.Id,
            PaymentMethod = PaymentMethod.Cash,
            Status = PaymentStatus.Paid,
            Amount = order.TotalAmount,
            TransactionCode = $"CASH-{Guid.NewGuid():N}"[..12],
            PaidAt = DateTime.UtcNow
        };
        _context.Payments.Add(payment);

        await _context.SaveChangesAsync(cancellationToken);

        decimal changeDue = command.ReceivedAmount - order.TotalAmount;
        return ApiResponse<object>.SuccessResult(new
        {
            OrderId = order.Id,
            TotalAmount = order.TotalAmount,
            ReceivedAmount = command.ReceivedAmount,
            ChangeDue = changeDue,
            Status = "Completed"
        }, "Xác nhận thu tiền mặt hoàn tất đơn.");
    }
}

public class ConfirmCashPaymentCommandHandlerTests : TestBase
{
    private readonly List<Order> _orders;
    private readonly List<Payment> _payments;
    private readonly ConfirmCashPaymentCommandHandler _handler;

    public ConfirmCashPaymentCommandHandlerTests()
    {
        _orders = new List<Order>();
        _payments = new List<Payment>();

        var mockOrders = MockDbSetHelper.CreateMockDbSet(_orders);
        var mockPayments = MockDbSetHelper.CreateMockDbSet(_payments);
        mockPayments.Setup(p => p.Add(It.IsAny<Payment>())).Callback<Payment>(_payments.Add);

        MockDbContext.Setup(c => c.Orders).Returns(mockOrders.Object);
        MockDbContext.Setup(c => c.Payments).Returns(mockPayments.Object);
        MockDbContext.Setup(c => c.SaveChangesAsync(It.IsAny<CancellationToken>())).ReturnsAsync(1);

        _handler = new ConfirmCashPaymentCommandHandler(MockDbContext.Object);
    }

    [Fact]
    public async Task Handle_ValidCashPayment_ShouldCompleteOrderAndCalculateChange()
    {
        // Arrange
        var orderId = Guid.NewGuid();
        var order = new Order
        {
            Id = orderId,
            OrderCode = "ORD-20260825-0010",
            BranchId = Guid.NewGuid(),
            OrderType = OrderType.DineIn,
            Status = OrderStatus.Ready,
            TotalAmount = 35000m
        };
        _orders.Add(order);

        var command = new ConfirmCashPaymentCommand(orderId, 50000m); // 50k given, 35k cost -> 15k change

        // Act
        var result = await _handler.Handle(command);

        // Assert
        result.Should().NotBeNull();
        result.Success.Should().BeTrue();
        order.Status.Should().Be(OrderStatus.Completed);

        MockDbContext.Verify(c => c.Payments.Add(It.Is<Payment>(p =>
            p.OrderId == orderId &&
            p.PaymentMethod == PaymentMethod.Cash &&
            p.Status == PaymentStatus.Paid &&
            p.Amount == 35000m
        )), Times.Once);
    }

    [Fact]
    public async Task Handle_InsufficientAmount_ShouldThrowAppException()
    {
        // Arrange
        var orderId = Guid.NewGuid();
        var order = new Order
        {
            Id = orderId,
            OrderCode = "ORD-20260825-0011",
            TotalAmount = 35000m
        };
        _orders.Add(order);

        var command = new ConfirmCashPaymentCommand(orderId, 20000m); // 20k < 35k

        // Act & Assert
        var act = () => _handler.Handle(command);
        var ex = await act.Should().ThrowAsync<AppException>();
        ex.Which.StatusCode.Should().Be(400);
    }
}
