using FluentAssertions;
using FluentValidation.Results;
using Moq;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Domain.Entities;
using SmartFB.Domain.Enums;
using SmartFB.UnitTests.Common;
using Xunit;

namespace SmartFB.UnitTests.Features.Orders;

public record CreateDeliveryOrderCommand(
    Guid BranchId,
    string RecipientName,
    string RecipientPhone,
    string DeliveryAddress,
    List<OrderItemRequestDto> Items,
    string? CustomerNote = null
);

public record DeliveryOrderResultDto(
    Guid OrderId,
    string OrderCode,
    decimal SubtotalAmount,
    decimal DeliveryFee,
    decimal FinalAmount,
    OrderStatus Status,
    string VietQrUrl
);

public class CreateDeliveryOrderCommandHandler
{
    private readonly IApplicationDbContext _context;
    private readonly IDateTimeService _dateTimeService;
    public const decimal FixedDeliveryFee = 20000m;

    public CreateDeliveryOrderCommandHandler(IApplicationDbContext context, IDateTimeService dateTimeService)
    {
        _context = context;
        _dateTimeService = dateTimeService;
    }

    public async Task<ApiResponse<DeliveryOrderResultDto>> Handle(
        CreateDeliveryOrderCommand command, CancellationToken cancellationToken = default)
    {
        if (string.IsNullOrWhiteSpace(command.RecipientName) ||
            string.IsNullOrWhiteSpace(command.RecipientPhone) ||
            string.IsNullOrWhiteSpace(command.DeliveryAddress))
        {
            throw new ValidationException(new List<ValidationFailure>
            {
                new("DeliveryInfo", "Thông tin người nhận và địa chỉ giao hàng không được để trống.")
            });
        }

        if (command.Items == null || command.Items.Count == 0)
        {
            throw new ValidationException(new List<ValidationFailure>
            {
                new("Items", "Đơn hàng phải có ít nhất 1 món.")
            });
        }

        decimal subtotal = command.Items.Sum(i => i.Quantity * i.UnitPrice);
        decimal finalAmount = subtotal + FixedDeliveryFee;
        var orderId = Guid.NewGuid();
        var orderCode = $"DEL-{_dateTimeService.UtcNow:yyyyMMdd}-{Random.Shared.Next(1000, 9999)}";

        var order = new Order
        {
            Id = orderId,
            OrderCode = orderCode,
            BranchId = command.BranchId,
            OrderType = OrderType.Delivery,
            Status = OrderStatus.PendingPayment, // 100% VietQR prepaid
            SubTotal = subtotal,
            DeliveryFee = FixedDeliveryFee,
            DiscountAmount = 0,
            TotalAmount = finalAmount,
            CustomerName = command.RecipientName,
            CustomerPhone = command.RecipientPhone,
            DeliveryAddress = command.DeliveryAddress,
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

        var qrUrl = $"https://img.vietqr.io/image/ICB-0001882199201-compact2.png?amount={finalAmount}&addInfo={orderCode}";

        var result = new DeliveryOrderResultDto(
            OrderId: order.Id,
            OrderCode: order.OrderCode,
            SubtotalAmount: order.SubTotal,
            DeliveryFee: order.DeliveryFee,
            FinalAmount: order.TotalAmount,
            Status: order.Status,
            VietQrUrl: qrUrl
        );

        return ApiResponse<DeliveryOrderResultDto>.SuccessResult(result, "Tạo đơn giao hàng thành công. Vui lòng thanh toán VietQR.");
    }
}

public class CreateDeliveryOrderCommandHandlerTests : TestBase
{
    private readonly CreateDeliveryOrderCommandHandler _handler;

    public CreateDeliveryOrderCommandHandlerTests()
    {
        var orders = new List<Order>();
        var mockOrdersDbSet = MockDbSetHelper.CreateMockDbSet(orders);
        mockOrdersDbSet.Setup(m => m.Add(It.IsAny<Order>())).Callback<Order>(orders.Add);

        MockDbContext.Setup(c => c.Orders).Returns(mockOrdersDbSet.Object);
        MockDbContext.Setup(c => c.SaveChangesAsync(It.IsAny<CancellationToken>())).ReturnsAsync(1);

        _handler = new CreateDeliveryOrderCommandHandler(MockDbContext.Object, MockDateTimeService.Object);
    }

    [Fact]
    public async Task Handle_ValidDeliveryOrder_ShouldAdd20kDeliveryFeeAndReturnVietQR()
    {
        // Arrange
        var branchId = Guid.NewGuid();
        var items = new List<OrderItemRequestDto>
        {
            new(Guid.NewGuid(), "Tra Dao Cam Sa", "M", 2, 35000m) // 70,000 VND
        };

        var command = new CreateDeliveryOrderCommand(
            BranchId: branchId,
            RecipientName: "Mai Huong",
            RecipientPhone: "0987654321",
            DeliveryAddress: "Bitexco Q1",
            Items: items,
            CustomerNote: "Giao tang 12"
        );

        // Act
        var result = await _handler.Handle(command);

        // Assert: 70,000 + 20,000 delivery fee = 90,000 VND
        result.Should().NotBeNull();
        result.Success.Should().BeTrue();
        result.Data!.SubtotalAmount.Should().Be(70000m);
        result.Data.DeliveryFee.Should().Be(20000m);
        result.Data.FinalAmount.Should().Be(90000m);
        result.Data.Status.Should().Be(OrderStatus.PendingPayment);
        result.Data.VietQrUrl.Should().Contain("amount=90000");

        MockDbContext.Verify(c => c.Orders.Add(It.Is<Order>(o =>
            o.OrderType == OrderType.Delivery &&
            o.DeliveryFee == 20000m &&
            o.TotalAmount == 90000m &&
            o.CustomerPhone == "0987654321"
        )), Times.Once);
    }

    [Fact]
    public async Task Handle_MissingRecipientInfo_ShouldThrowValidationException()
    {
        // Arrange
        var command = new CreateDeliveryOrderCommand(
            BranchId: Guid.NewGuid(),
            RecipientName: "",
            RecipientPhone: "",
            DeliveryAddress: "",
            Items: new List<OrderItemRequestDto> { new(Guid.NewGuid(), "Product", "M", 1, 30000m) }
        );

        // Act & Assert
        var act = () => _handler.Handle(command);
        await act.Should().ThrowAsync<ValidationException>();
    }
}
