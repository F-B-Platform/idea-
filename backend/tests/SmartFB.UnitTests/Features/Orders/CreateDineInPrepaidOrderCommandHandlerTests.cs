using FluentAssertions;
using Moq;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Domain.Entities;
using SmartFB.Domain.Enums;
using SmartFB.UnitTests.Common;
using Xunit;

namespace SmartFB.UnitTests.Features.Orders;

public record OrderItemRequestDto(Guid ProductId, string ProductName, string Size, int Quantity, decimal UnitPrice);

public record CreateDineInPrepaidOrderCommand(
    Guid BranchId,
    Guid TableId,
    List<OrderItemRequestDto> Items,
    string? CustomerNote = null
);

public record DineInPrepaidOrderResultDto(
    Guid OrderId,
    string OrderCode,
    decimal SubTotal,
    decimal TotalAmount,
    OrderStatus Status,
    string VietQrUrl
);

public class CreateDineInPrepaidOrderCommandHandler
{
    private readonly IApplicationDbContext _context;
    private readonly IDateTimeService _dateTimeService;

    public CreateDineInPrepaidOrderCommandHandler(IApplicationDbContext context, IDateTimeService dateTimeService)
    {
        _context = context;
        _dateTimeService = dateTimeService;
    }

    public async Task<ApiResponse<DineInPrepaidOrderResultDto>> Handle(
        CreateDineInPrepaidOrderCommand command, CancellationToken cancellationToken = default)
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
            Status = OrderStatus.PendingPayment,
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

        var qrUrl = $"https://img.vietqr.io/image/ICB-0001882199201-compact2.png?amount={subTotal}&addInfo={orderCode}";

        var result = new DineInPrepaidOrderResultDto(
            OrderId: order.Id,
            OrderCode: order.OrderCode,
            SubTotal: order.SubTotal,
            TotalAmount: order.TotalAmount,
            Status: order.Status,
            VietQrUrl: qrUrl
        );

        return ApiResponse<DineInPrepaidOrderResultDto>.SuccessResult(result, "Tạo đơn hàng trả trước thành công. Vui lòng quét mã VietQR.");
    }
}

public class CreateDineInPrepaidOrderCommandHandlerTests : TestBase
{
    private readonly CreateDineInPrepaidOrderCommandHandler _handler;

    public CreateDineInPrepaidOrderCommandHandlerTests()
    {
        var orders = new List<Order>();
        var mockOrdersDbSet = MockDbSetHelper.CreateMockDbSet(orders);
        mockOrdersDbSet.Setup(m => m.Add(It.IsAny<Order>())).Callback<Order>(orders.Add);

        MockDbContext.Setup(c => c.Orders).Returns(mockOrdersDbSet.Object);
        MockDbContext.Setup(c => c.SaveChangesAsync(It.IsAny<CancellationToken>())).ReturnsAsync(1);

        _handler = new CreateDineInPrepaidOrderCommandHandler(MockDbContext.Object, MockDateTimeService.Object);
    }

    [Fact]
    public async Task Handle_ValidRequest_ShouldCreateOrderWithPendingPaymentStatusAndVietQR()
    {
        // Arrange
        var branchId = Guid.NewGuid();
        var tableId = Guid.NewGuid();
        var items = new List<OrderItemRequestDto>
        {
            new(Guid.NewGuid(), "Tra Dao Cam Sa", "L", 2, 45000m),
            new(Guid.NewGuid(), "Ca Phe Muoi", "M", 1, 35000m)
        };

        var command = new CreateDineInPrepaidOrderCommand(branchId, tableId, items, "It duong");

        // Act
        var result = await _handler.Handle(command);

        // Assert
        result.Should().NotBeNull();
        result.Success.Should().BeTrue();
        result.Data!.Status.Should().Be(OrderStatus.PendingPayment);
        result.Data.SubTotal.Should().Be(125000m);
        result.Data.TotalAmount.Should().Be(125000m);
        result.Data.VietQrUrl.Should().Contain("amount=125000");

        MockDbContext.Verify(c => c.Orders.Add(It.Is<Order>(o =>
            o.OrderType == OrderType.DineIn &&
            o.Status == OrderStatus.PendingPayment &&
            o.TotalAmount == 125000m &&
            o.DeliveryFee == 0m
        )), Times.Once);

        MockDbContext.Verify(c => c.SaveChangesAsync(It.IsAny<CancellationToken>()), Times.Once);
    }
}
