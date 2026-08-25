using FluentAssertions;
using Moq;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Domain.Entities;
using SmartFB.Domain.Enums;
using SmartFB.UnitTests.Common;
using Xunit;

namespace SmartFB.UnitTests.Features.Orders;

public record CreateDineInPostpaidOrderCommand(
    Guid BranchId,
    Guid TableId,
    List<OrderItemRequestDto> Items,
    string? CustomerNote = null
);

public record DineInPostpaidOrderResultDto(
    Guid OrderId,
    string OrderCode,
    decimal TotalAmount,
    OrderStatus Status,
    string Message
);

public interface ISignalRNotificationService
{
    Task NotifyKitchenNewOrderAsync(Guid branchId, Order order);
}

public class CreateDineInPostpaidOrderCommandHandler
{
    private readonly IApplicationDbContext _context;
    private readonly IDateTimeService _dateTimeService;
    private readonly ISignalRNotificationService _signalRService;

    public CreateDineInPostpaidOrderCommandHandler(
        IApplicationDbContext context,
        IDateTimeService dateTimeService,
        ISignalRNotificationService signalRService)
    {
        _context = context;
        _dateTimeService = dateTimeService;
        _signalRService = signalRService;
    }

    public async Task<ApiResponse<DineInPostpaidOrderResultDto>> Handle(
        CreateDineInPostpaidOrderCommand command, CancellationToken cancellationToken = default)
    {
        decimal subTotal = command.Items.Sum(i => i.Quantity * i.UnitPrice);
        var orderId = Guid.NewGuid();
        var orderCode = $"ORD-{_dateTimeService.UtcNow:yyyyMMdd}-{Random.Shared.Next(1000, 9999)}";

        var order = new Order
        {
            Id = orderId,
            OrderCode = orderCode,
            BranchId = command.BranchId,
            TableId = command.TableId,
            OrderType = OrderType.DineIn,
            Status = OrderStatus.Confirmed, // Enters Kitchen IMMEDIATELY
            SubTotal = subTotal,
            DiscountAmount = 0,
            DeliveryFee = 0,
            TotalAmount = subTotal,
            Note = command.CustomerNote,
            Items = command.Items.Select(i => new OrderItem
            {
                OrderId = orderId,
                ProductId = i.ProductId,
                SizeId = Guid.NewGuid(),
                Quantity = i.Quantity,
                UnitPrice = i.UnitPrice,
                SubtotalPrice = i.Quantity * i.UnitPrice,
                Note = $"{i.ProductName} ({i.Size})"
            }).ToList()
        };

        _context.Orders.Add(order);
        await _context.SaveChangesAsync(cancellationToken);

        // Notify KDS immediately
        await _signalRService.NotifyKitchenNewOrderAsync(command.BranchId, order);

        var result = new DineInPostpaidOrderResultDto(
            OrderId: order.Id,
            OrderCode: order.OrderCode,
            TotalAmount: order.TotalAmount,
            Status: order.Status,
            Message: "Bếp đã tiếp nhận đơn và đang pha chế. Nhân viên sẽ mang đồ uống kèm hóa đơn ra bàn."
        );

        return ApiResponse<DineInPostpaidOrderResultDto>.SuccessResult(result, "Đơn hàng đã được chuyển xuống bếp pha chế.");
    }
}

public class CreateDineInPostpaidOrderCommandHandlerTests : TestBase
{
    private readonly Mock<ISignalRNotificationService> _mockSignalR;
    private readonly CreateDineInPostpaidOrderCommandHandler _handler;

    public CreateDineInPostpaidOrderCommandHandlerTests()
    {
        _mockSignalR = new Mock<ISignalRNotificationService>();
        _mockSignalR.Setup(s => s.NotifyKitchenNewOrderAsync(It.IsAny<Guid>(), It.IsAny<Order>()))
            .Returns(Task.CompletedTask);

        var orders = new List<Order>();
        var mockOrdersDbSet = MockDbSetHelper.CreateMockDbSet(orders);
        mockOrdersDbSet.Setup(m => m.Add(It.IsAny<Order>())).Callback<Order>(orders.Add);

        MockDbContext.Setup(c => c.Orders).Returns(mockOrdersDbSet.Object);
        MockDbContext.Setup(c => c.SaveChangesAsync(It.IsAny<CancellationToken>())).ReturnsAsync(1);

        _handler = new CreateDineInPostpaidOrderCommandHandler(
            MockDbContext.Object,
            MockDateTimeService.Object,
            _mockSignalR.Object);
    }

    [Fact]
    public async Task Handle_PostpaidDineIn_ShouldCreateConfirmedOrderAndNotifyKitchen()
    {
        // Arrange
        var branchId = Guid.NewGuid();
        var tableId = Guid.NewGuid();
        var items = new List<OrderItemRequestDto>
        {
            new(Guid.NewGuid(), "Bac Xiu", "M", 1, 35000m)
        };

        var command = new CreateDineInPostpaidOrderCommand(branchId, tableId, items);

        // Act
        var result = await _handler.Handle(command);

        // Assert
        result.Should().NotBeNull();
        result.Success.Should().BeTrue();
        result.Data!.Status.Should().Be(OrderStatus.Confirmed);
        result.Data.TotalAmount.Should().Be(35000m);

        MockDbContext.Verify(c => c.Orders.Add(It.Is<Order>(o =>
            o.Status == OrderStatus.Confirmed &&
            o.OrderType == OrderType.DineIn
        )), Times.Once);

        _mockSignalR.Verify(s => s.NotifyKitchenNewOrderAsync(branchId, It.Is<Order>(o =>
            o.Status == OrderStatus.Confirmed
        )), Times.Once);
    }
}
