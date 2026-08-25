using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Orders.DTOs;
using SmartFB.Domain.Entities;
using SmartFB.Domain.Enums;

namespace SmartFB.Application.Features.Orders.Commands.CreateDeliveryOrder;

public record CreateDeliveryOrderCommand(
    Guid BranchId,
    string RecipientName,
    string RecipientPhone,
    string DeliveryAddress,
    string? DeliveryNotes,
    List<CreateOrderItemRequestDto> Items
) : IRequest<ApiResponse<DeliveryOrderResultDto>>;

public class CreateDeliveryOrderCommandHandler : IRequestHandler<CreateDeliveryOrderCommand, ApiResponse<DeliveryOrderResultDto>>
{
    private readonly IApplicationDbContext _context;
    private readonly IPayOSService _payOSService;

    public CreateDeliveryOrderCommandHandler(IApplicationDbContext context, IPayOSService payOSService)
    {
        _context = context;
        _payOSService = payOSService;
    }

    public async Task<ApiResponse<DeliveryOrderResultDto>> Handle(CreateDeliveryOrderCommand request, CancellationToken cancellationToken)
    {
        if (request.Items == null || request.Items.Count == 0)
        {
            throw new AppException("Giỏ hàng không được để trống.");
        }

        var branch = await _context.Branches
            .FirstOrDefaultAsync(b => b.Id == request.BranchId && !b.IsDeleted, cancellationToken);

        if (branch == null)
        {
            throw new NotFoundException("Branch", request.BranchId);
        }

        var orderCode = $"DEL-{DateTime.UtcNow:yyMMddHHmmss}-{Random.Shared.Next(100, 999)}";
        const decimal fixedDeliveryFee = 20000; // Pillar 2: Delivery 20,000 VND Fixed Fee

        var order = new Order
        {
            BranchId = request.BranchId,
            OrderCode = orderCode,
            OrderType = OrderType.Delivery,
            Status = OrderStatus.PendingPayment, // 100% VietQR Prepaid required!
            CustomerName = request.RecipientName,
            CustomerPhone = request.RecipientPhone,
            DeliveryAddress = request.DeliveryAddress,
            Note = request.DeliveryNotes,
            DeliveryFee = fixedDeliveryFee,
            ExpiresAt = DateTime.UtcNow.AddMinutes(15)
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
        order.TotalAmount = subTotal + fixedDeliveryFee;

        _context.Orders.Add(order);
        await _context.SaveChangesAsync(cancellationToken);

        // Generate VietQR payment via PayOS
        var payosResult = await _payOSService.CreatePaymentLinkAsync(new CreatePayOSPaymentRequest(
            OrderCode: long.Parse(DateTime.UtcNow.ToString("yyMMddHHmmss") + Random.Shared.Next(10, 99)),
            Amount: order.TotalAmount,
            Description: $"Giao hang {order.OrderCode}",
            ReturnUrl: $"https://app.smartfb.vn/delivery/success?orderId={order.Id}",
            CancelUrl: $"https://app.smartfb.vn/delivery/cancel?orderId={order.Id}",
            BuyerName: order.CustomerName,
            BuyerPhone: order.CustomerPhone
        ), cancellationToken);

        var result = new DeliveryOrderResultDto(
            order.Id,
            order.OrderCode,
            order.SubTotal,
            order.DeliveryFee,
            order.TotalAmount,
            order.ExpiresAt.Value,
            payosResult.QrCode
        );

        return ApiResponse<DeliveryOrderResultDto>.SuccessResult(result, "Tạo đơn giao hàng thành công. Vui lòng thanh toán VietQR.");
    }
}
