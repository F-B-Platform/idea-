using FluentAssertions;
using Moq;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Domain.Entities;
using SmartFB.Domain.Enums;
using SmartFB.UnitTests.Common;
using Xunit;

namespace SmartFB.UnitTests.Features.KitchenKDS;

public record UpdateKdsOrderStatusCommand(Guid OrderId, OrderStatus NewStatus);

public interface IBomInventoryService
{
    Task DeductBomForOrderAsync(Guid orderId);
}

public class UpdateKdsOrderStatusCommandHandler
{
    private readonly IApplicationDbContext _context;
    private readonly IBomInventoryService _bomService;

    public UpdateKdsOrderStatusCommandHandler(IApplicationDbContext context, IBomInventoryService bomService)
    {
        _context = context;
        _bomService = bomService;
    }

    public async Task<ApiResponse<object>> Handle(
        UpdateKdsOrderStatusCommand command, CancellationToken cancellationToken = default)
    {
        var order = _context.Orders.FirstOrDefault(o => o.Id == command.OrderId);
        if (order == null)
        {
            throw new NotFoundException(nameof(Order), command.OrderId);
        }

        order.Status = command.NewStatus;

        // Auto BOM Deduction when Ready
        if (command.NewStatus == OrderStatus.Ready)
        {
            await _bomService.DeductBomForOrderAsync(order.Id);
        }

        await _context.SaveChangesAsync(cancellationToken);

        return ApiResponse<object>.SuccessResult(new
        {
            OrderId = order.Id,
            Status = order.Status.ToString()
        }, "Cập nhật trạng thái chế biến KDS thành công.");
    }
}

public class UpdateKdsOrderStatusCommandHandlerTests : TestBase
{
    private readonly List<Order> _orders;
    private readonly Mock<IBomInventoryService> _mockBomService;
    private readonly UpdateKdsOrderStatusCommandHandler _handler;

    public UpdateKdsOrderStatusCommandHandlerTests()
    {
        _orders = new List<Order>();
        _mockBomService = new Mock<IBomInventoryService>();
        _mockBomService.Setup(b => b.DeductBomForOrderAsync(It.IsAny<Guid>()))
            .Returns(Task.CompletedTask);

        var mockOrders = MockDbSetHelper.CreateMockDbSet(_orders);
        MockDbContext.Setup(c => c.Orders).Returns(mockOrders.Object);
        MockDbContext.Setup(c => c.SaveChangesAsync(It.IsAny<CancellationToken>())).ReturnsAsync(1);

        _handler = new UpdateKdsOrderStatusCommandHandler(MockDbContext.Object, _mockBomService.Object);
    }

    [Fact]
    public async Task Handle_StatusChangeToReady_ShouldTriggerBomDeduction()
    {
        // Arrange
        var orderId = Guid.NewGuid();
        var order = new Order
        {
            Id = orderId,
            OrderCode = "ORD-KDS-001",
            Status = OrderStatus.Preparing
        };
        _orders.Add(order);

        var command = new UpdateKdsOrderStatusCommand(orderId, OrderStatus.Ready);

        // Act
        var result = await _handler.Handle(command);

        // Assert
        result.Should().NotBeNull();
        result.Success.Should().BeTrue();
        order.Status.Should().Be(OrderStatus.Ready);

        _mockBomService.Verify(b => b.DeductBomForOrderAsync(orderId), Times.Once);
        MockDbContext.Verify(c => c.SaveChangesAsync(It.IsAny<CancellationToken>()), Times.Once);
    }

    [Fact]
    public async Task Handle_StatusChangeToPreparing_ShouldNotTriggerBomDeduction()
    {
        // Arrange
        var orderId = Guid.NewGuid();
        var order = new Order
        {
            Id = orderId,
            OrderCode = "ORD-KDS-002",
            Status = OrderStatus.Confirmed
        };
        _orders.Add(order);

        var command = new UpdateKdsOrderStatusCommand(orderId, OrderStatus.Preparing);

        // Act
        var result = await _handler.Handle(command);

        // Assert
        order.Status.Should().Be(OrderStatus.Preparing);
        _mockBomService.Verify(b => b.DeductBomForOrderAsync(It.IsAny<Guid>()), Times.Never);
    }
}
