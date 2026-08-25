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

public record CreateTakeawayOrderCommand(
    Guid BranchId,
    string CustomerPhone,
    string? CustomerName,
    bool RedeemFreeCup,
    Guid? FreeProductId,
    PaymentMethod PaymentMethod,
    decimal CashGiven,
    List<OrderItemRequestDto> Items
);

public record TakeawayOrderResultDto(
    Guid OrderId,
    string OrderCode,
    decimal SubtotalAmount,
    decimal LoyaltyDiscount,
    decimal FinalAmount,
    decimal CashGiven,
    decimal CashChange,
    OrderStatus Status,
    int RemainingLoyaltyCups
);

public class CreateTakeawayOrderCommandHandler
{
    private readonly IApplicationDbContext _context;
    private readonly IDateTimeService _dateTimeService;

    public CreateTakeawayOrderCommandHandler(IApplicationDbContext context, IDateTimeService dateTimeService)
    {
        _context = context;
        _dateTimeService = dateTimeService;
    }

    public async Task<ApiResponse<TakeawayOrderResultDto>> Handle(
        CreateTakeawayOrderCommand command, CancellationToken cancellationToken = default)
    {
        if (command.Items == null || command.Items.Count == 0)
        {
            throw new ValidationException(new List<ValidationFailure>
            {
                new("Items", "Đơn hàng phải có ít nhất 1 món.")
            });
        }

        // Lookup CRM customer
        var customer = _context.Customers.FirstOrDefault(c => c.PhoneNumber == command.CustomerPhone);
        if (customer == null && !string.IsNullOrWhiteSpace(command.CustomerPhone))
        {
            customer = new Customer
            {
                PhoneNumber = command.CustomerPhone,
                FullName = command.CustomerName ?? "Khách Hàng",
                TakeawayCupCount = 0
            };
            _context.Customers.Add(customer);
        }

        decimal subtotal = command.Items.Sum(i => i.Quantity * i.UnitPrice);
        decimal loyaltyDiscount = 0;
        int totalCupsInOrder = command.Items.Sum(i => i.Quantity);

        if (command.RedeemFreeCup)
        {
            if (customer == null || customer.TakeawayCupCount < 10)
            {
                throw new AppException("Khách hàng chưa đủ 10 ly để đổi thưởng miễn phí.", 400);
            }

            // Discount 100% 1 cup (the cheapest item or freeProductId)
            var targetItem = command.Items.FirstOrDefault(i => i.ProductId == command.FreeProductId) ?? command.Items.First();
            loyaltyDiscount = targetItem.UnitPrice;

            // Deduct 10 cups and accumulate new purchased cups (totalCupsInOrder)
            customer.TakeawayCupCount = (customer.TakeawayCupCount - 10) + totalCupsInOrder;
        }
        else if (customer != null)
        {
            customer.TakeawayCupCount += totalCupsInOrder;
        }

        decimal finalAmount = Math.Max(0, subtotal - loyaltyDiscount);
        decimal cashChange = command.PaymentMethod == PaymentMethod.Cash ? Math.Max(0, command.CashGiven - finalAmount) : 0;

        var orderId = Guid.NewGuid();
        var orderCode = $"TK-{_dateTimeService.UtcNow:yyyyMMdd}-{Random.Shared.Next(1000, 9999)}";

        var order = new Order
        {
            Id = orderId,
            OrderCode = orderCode,
            BranchId = command.BranchId,
            CustomerId = customer?.Id,
            OrderType = OrderType.TakeAway,
            Status = OrderStatus.Confirmed, // Takeaway POS sends directly to Kitchen
            SubTotal = subtotal,
            DiscountAmount = loyaltyDiscount,
            DeliveryFee = 0,
            TotalAmount = finalAmount,
            CustomerName = customer?.FullName,
            CustomerPhone = customer?.PhoneNumber,
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

        var result = new TakeawayOrderResultDto(
            OrderId: order.Id,
            OrderCode: order.OrderCode,
            SubtotalAmount: order.SubTotal,
            LoyaltyDiscount: loyaltyDiscount,
            FinalAmount: order.TotalAmount,
            CashGiven: command.CashGiven,
            CashChange: cashChange,
            Status: order.Status,
            RemainingLoyaltyCups: customer?.TakeawayCupCount ?? 0
        );

        return ApiResponse<TakeawayOrderResultDto>.SuccessResult(result, "Tạo đơn mang về thành công.");
    }
}

public class CreateTakeawayOrderCommandHandlerTests : TestBase
{
    private readonly List<Customer> _customers;
    private readonly List<Order> _orders;
    private readonly CreateTakeawayOrderCommandHandler _handler;

    public CreateTakeawayOrderCommandHandlerTests()
    {
        _customers = new List<Customer>();
        _orders = new List<Order>();

        var mockCustomerSet = MockDbSetHelper.CreateMockDbSet(_customers);
        mockCustomerSet.Setup(m => m.Add(It.IsAny<Customer>())).Callback<Customer>(_customers.Add);

        var mockOrderSet = MockDbSetHelper.CreateMockDbSet(_orders);
        mockOrderSet.Setup(m => m.Add(It.IsAny<Order>())).Callback<Order>(_orders.Add);

        MockDbContext.Setup(c => c.Customers).Returns(mockCustomerSet.Object);
        MockDbContext.Setup(c => c.Orders).Returns(mockOrderSet.Object);
        MockDbContext.Setup(c => c.SaveChangesAsync(It.IsAny<CancellationToken>())).ReturnsAsync(1);

        _handler = new CreateTakeawayOrderCommandHandler(MockDbContext.Object, MockDateTimeService.Object);
    }

    [Fact]
    public async Task Handle_TakeawayWith10CupLoyaltyRedemption_ShouldDeductDiscountAndResetCupsAccurately()
    {
        // Arrange: Existing CRM customer with 10 cups
        var customerId = Guid.NewGuid();
        var existingCustomer = new Customer
        {
            Id = customerId,
            PhoneNumber = "0909123456",
            FullName = "Nguyen Hoang Nam",
            TakeawayCupCount = 10
        };
        _customers.Add(existingCustomer);

        var productId = Guid.NewGuid();
        var items = new List<OrderItemRequestDto>
        {
            new(productId, "Ca Phe Muoi", "M", 2, 39000m) // 2 cups = 78,000 VND
        };

        var command = new CreateTakeawayOrderCommand(
            BranchId: Guid.NewGuid(),
            CustomerPhone: "0909123456",
            CustomerName: "Nguyen Hoang Nam",
            RedeemFreeCup: true,
            FreeProductId: productId,
            PaymentMethod: PaymentMethod.Cash,
            CashGiven: 100000m,
            Items: items
        );

        // Act
        var result = await _handler.Handle(command);

        // Assert
        result.Should().NotBeNull();
        result.Success.Should().BeTrue();
        result.Data!.SubtotalAmount.Should().Be(78000m);
        result.Data.LoyaltyDiscount.Should().Be(39000m); // 1 cup free (-39k)
        result.Data.FinalAmount.Should().Be(39000m);
        result.Data.CashGiven.Should().Be(100000m);
        result.Data.CashChange.Should().Be(61000m); // 100k - 39k = 61k change
        result.Data.RemainingLoyaltyCups.Should().Be(2); // 10 - 10 + 2 = 2 cups

        existingCustomer.TakeawayCupCount.Should().Be(2);
    }

    [Fact]
    public async Task Handle_RedeemFreeCup_WhenCustomerHasLessThan10Cups_ShouldThrowAppException()
    {
        // Arrange: Customer with only 5 cups
        var existingCustomer = new Customer
        {
            PhoneNumber = "0909123456",
            FullName = "Le Van Hung",
            TakeawayCupCount = 5
        };
        _customers.Add(existingCustomer);

        var command = new CreateTakeawayOrderCommand(
            BranchId: Guid.NewGuid(),
            CustomerPhone: "0909123456",
            CustomerName: "Le Van Hung",
            RedeemFreeCup: true,
            FreeProductId: Guid.NewGuid(),
            PaymentMethod: PaymentMethod.Cash,
            CashGiven: 50000m,
            Items: new List<OrderItemRequestDto> { new(Guid.NewGuid(), "Ca Phe", "M", 1, 35000m) }
        );

        // Act & Assert
        var act = () => _handler.Handle(command);
        var ex = await act.Should().ThrowAsync<AppException>();
        ex.Which.StatusCode.Should().Be(400);
    }
}
