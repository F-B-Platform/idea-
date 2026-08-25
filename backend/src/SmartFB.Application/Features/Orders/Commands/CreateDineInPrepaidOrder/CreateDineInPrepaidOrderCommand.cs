using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Orders.DTOs;
using SmartFB.Domain.Entities;
using SmartFB.Domain.Enums;

namespace SmartFB.Application.Features.Orders.Commands.CreateDineInPrepaidOrder;

public record CreateDineInPrepaidOrderCommand(
    Guid BranchId,
    Guid TableId,
    string? CustomerPhone,
    string? CustomerName,
    string? Note,
    List<CreateOrderItemRequestDto> Items
) : IRequest<ApiResponse<PrepaidOrderResultDto>>;

public class CreateDineInPrepaidOrderCommandHandler : IRequestHandler<CreateDineInPrepaidOrderCommand, ApiResponse<PrepaidOrderResultDto>>
{
    private readonly IApplicationDbContext _context;
    private readonly IPayOSService _payOSService;

    public CreateDineInPrepaidOrderCommandHandler(IApplicationDbContext context, IPayOSService payOSService)
    {
        _context = context;
        _payOSService = payOSService;
    }

    public async Task<ApiResponse<PrepaidOrderResultDto>> Handle(CreateDineInPrepaidOrderCommand request, CancellationToken cancellationToken)
    {
        if (request.Items == null || request.Items.Count == 0)
        {
            throw new AppException("Giỏ hàng không được để trống.");
        }

        var table = await _context.Tables
            .FirstOrDefaultAsync(t => t.Id == request.TableId && t.BranchId == request.BranchId && !t.IsDeleted, cancellationToken);

        if (table == null)
        {
            throw new NotFoundException("Table", request.TableId);
        }

        var orderCode = $"DIN-{DateTime.UtcNow:yyMMddHHmmss}-{Random.Shared.Next(100, 999)}";
        var order = new Order
        {
            BranchId = request.BranchId,
            TableId = request.TableId,
            OrderCode = orderCode,
            OrderType = OrderType.DineIn,
            Status = OrderStatus.PendingPayment,
            CustomerName = request.CustomerName,
            CustomerPhone = request.CustomerPhone,
            Note = request.Note,
            ExpiresAt = DateTime.UtcNow.AddMinutes(10), // TTL 10m for VietQR
            DeliveryFee = 0
        };

        decimal subTotal = 0;
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

        order.SubTotal = subTotal;
        order.TotalAmount = subTotal;

        _context.Orders.Add(order);
        await _context.SaveChangesAsync(cancellationToken);

        // Generate PayOS payment link
        var payosResult = await _payOSService.CreatePaymentLinkAsync(new CreatePayOSPaymentRequest(
            OrderCode: long.Parse(DateTime.UtcNow.ToString("yyMMddHHmmss") + Random.Shared.Next(10, 99)),
            Amount: order.TotalAmount,
            Description: $"Thanh toan {order.OrderCode}",
            ReturnUrl: $"https://app.smartfb.vn/order/success?orderId={order.Id}",
            CancelUrl: $"https://app.smartfb.vn/order/cancel?orderId={order.Id}",
            BuyerName: order.CustomerName,
            BuyerPhone: order.CustomerPhone
        ), cancellationToken);

        var result = new PrepaidOrderResultDto(
            order.Id,
            order.OrderCode,
            order.TotalAmount,
            order.ExpiresAt.Value,
            payosResult.QrCode,
            payosResult.CheckoutUrl
        );

        return ApiResponse<PrepaidOrderResultDto>.SuccessResult(result, "Tạo đơn tại bàn trả trước thành công.");
    }
}
