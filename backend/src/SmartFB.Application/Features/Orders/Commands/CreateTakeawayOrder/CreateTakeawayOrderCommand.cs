using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Orders.DTOs;
using SmartFB.Domain.Entities;
using SmartFB.Domain.Enums;

namespace SmartFB.Application.Features.Orders.Commands.CreateTakeawayOrder;

public record CreateTakeawayOrderCommand(
    Guid BranchId,
    string CustomerPhone,
    string? CustomerName,
    bool RedeemFreeCup,
    List<CreateOrderItemRequestDto> Items,
    PaymentMethod PaymentMethod = PaymentMethod.Cash
) : IRequest<ApiResponse<TakeawayOrderResultDto>>;

public class CreateTakeawayOrderCommandHandler : IRequestHandler<CreateTakeawayOrderCommand, ApiResponse<TakeawayOrderResultDto>>
{
    private readonly IApplicationDbContext _context;

    public CreateTakeawayOrderCommandHandler(IApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<ApiResponse<TakeawayOrderResultDto>> Handle(CreateTakeawayOrderCommand request, CancellationToken cancellationToken)
    {
        if (request.Items == null || request.Items.Count == 0)
        {
            throw new AppException("Danh sách món mang về không được để trống.");
        }

        // Find or create customer by phone for Takeaway CRM
        var customer = await _context.Customers
            .FirstOrDefaultAsync(c => c.PhoneNumber == request.CustomerPhone && !c.IsDeleted, cancellationToken);

        if (customer == null)
        {
            customer = new Customer
            {
                PhoneNumber = request.CustomerPhone,
                FullName = request.CustomerName,
                CupBalance = 0,
                TotalPoints = 0,
                MembershipTier = "Standard",
                LastVisitedAt = DateTime.UtcNow
            };
            _context.Customers.Add(customer);
        }
        else
        {
            customer.LastVisitedAt = DateTime.UtcNow;
            if (!string.IsNullOrWhiteSpace(request.CustomerName))
            {
                customer.FullName = request.CustomerName;
            }
        }

        var orderCode = $"TAK-{DateTime.UtcNow:yyMMddHHmmss}-{Random.Shared.Next(100, 999)}";
        var order = new Order
        {
            BranchId = request.BranchId,
            CustomerId = customer.Id,
            OrderCode = orderCode,
            OrderType = OrderType.TakeAway,
            Status = OrderStatus.Confirmed,
            CustomerName = customer.FullName ?? request.CustomerName,
            CustomerPhone = customer.PhoneNumber,
            DeliveryFee = 0
        };

        decimal subTotal = 0;
        int totalCupsInOrder = 0;
        decimal highestItemPrice = 0;

        foreach (var itemReq in request.Items)
        {
            var product = await _context.Products
                .Include(p => p.ProductSizes)
                .FirstOrDefaultAsync(p => p.Id == itemReq.ProductId && !p.IsDeleted, cancellationToken);

            if (product == null)
            {
                throw new NotFoundException("Product", itemReq.ProductId);
            }

            var size = product.ProductSizes.FirstOrDefault(s => s.Id == itemReq.SizeId && !s.IsDeleted);
            decimal unitPrice = product.BasePrice + (size?.PriceAdjustment ?? 0);
            decimal itemSubtotal = unitPrice * itemReq.Quantity;

            if (unitPrice > highestItemPrice)
            {
                highestItemPrice = unitPrice;
            }

            totalCupsInOrder += itemReq.Quantity;

            var orderItem = new OrderItem
            {
                OrderId = order.Id,
                ProductId = product.Id,
                SizeId = size?.Id ?? Guid.Empty,
                Quantity = itemReq.Quantity,
                UnitPrice = unitPrice,
                SubtotalPrice = itemSubtotal,
                Note = itemReq.Note,
                ItemStatus = "Pending"
            };

            subTotal += itemSubtotal;
            order.Items.Add(orderItem);
        }

        decimal discountAmount = 0;

        // Pillar 3: Takeaway 10-Cup Loyalty Redemption (10 cups = 1 free standard drink)
        if (request.RedeemFreeCup)
        {
            if (customer.CupBalance < 10)
            {
                throw new BusinessRuleException($"Khách hàng hiện có {customer.CupBalance} ly, chưa đủ 10 ly để quy đổi quà tặng.", "LOYALTY_INSUFFICIENT_CUPS");
            }

            // Deduct 10 cups and discount the price of 1 drink
            customer.CupBalance -= 10;
            discountAmount = highestItemPrice;

            _context.LoyaltyCupTransactions.Add(new LoyaltyCupTransaction
            {
                CustomerId = customer.Id,
                OrderId = order.Id,
                CupsEarned = 0,
                CupsRedeemed = 10,
                TransactionType = LoyaltyTransactionType.TakeawayRedeem10Free,
                Notes = $"Đổi 10 ly nhận 1 ly miễn phí cho đơn {order.OrderCode}"
            });
        }

        // Accumulate new paid cups for takeaway
        int paidCups = Math.Max(0, totalCupsInOrder - (request.RedeemFreeCup ? 1 : 0));
        if (paidCups > 0)
        {
            customer.CupBalance += paidCups;
            customer.TotalPoints += (int)(subTotal / 1000);

            _context.LoyaltyCupTransactions.Add(new LoyaltyCupTransaction
            {
                CustomerId = customer.Id,
                OrderId = order.Id,
                CupsEarned = paidCups,
                CupsRedeemed = 0,
                TransactionType = LoyaltyTransactionType.TakeawayAccumulate,
                Notes = $"Tích {paidCups} ly mang về cho đơn {order.OrderCode}"
            });
        }

        order.SubTotal = subTotal;
        order.DiscountAmount = discountAmount;
        order.TotalAmount = Math.Max(0, subTotal - discountAmount);

        _context.Orders.Add(order);
        await _context.SaveChangesAsync(cancellationToken);

        var result = new TakeawayOrderResultDto(
            order.Id,
            order.OrderCode,
            order.SubTotal,
            order.DiscountAmount,
            order.TotalAmount,
            EarnedCups: paidCups,
            RemainingCupBalance: customer.CupBalance
        );

        return ApiResponse<TakeawayOrderResultDto>.SuccessResult(result, "Tạo đơn mang về POS thành công.");
    }
}
