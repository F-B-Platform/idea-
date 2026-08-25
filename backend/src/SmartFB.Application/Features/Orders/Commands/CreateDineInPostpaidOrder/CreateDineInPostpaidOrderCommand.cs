using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Orders.DTOs;
using SmartFB.Domain.Entities;
using SmartFB.Domain.Enums;

namespace SmartFB.Application.Features.Orders.Commands.CreateDineInPostpaidOrder;

public record CreateDineInPostpaidOrderCommand(
    Guid BranchId,
    Guid TableId,
    string? CustomerPhone,
    string? CustomerName,
    string? Note,
    List<CreateOrderItemRequestDto> Items
) : IRequest<ApiResponse<PostpaidOrderResultDto>>;

public class CreateDineInPostpaidOrderCommandHandler : IRequestHandler<CreateDineInPostpaidOrderCommand, ApiResponse<PostpaidOrderResultDto>>
{
    private readonly IApplicationDbContext _context;
    private readonly ISignalRHubService _signalRService;

    public CreateDineInPostpaidOrderCommandHandler(IApplicationDbContext context, ISignalRHubService signalRService)
    {
        _context = context;
        _signalRService = signalRService;
    }

    public async Task<ApiResponse<PostpaidOrderResultDto>> Handle(CreateDineInPostpaidOrderCommand request, CancellationToken cancellationToken)
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

        var orderCode = $"DIN-POST-{DateTime.UtcNow:yyMMddHHmmss}-{Random.Shared.Next(100, 999)}";
        var order = new Order
        {
            BranchId = request.BranchId,
            TableId = request.TableId,
            OrderCode = orderCode,
            OrderType = OrderType.DineIn,
            Status = OrderStatus.Confirmed, // In Branch B, order goes to KDS immediately!
            CustomerName = request.CustomerName,
            CustomerPhone = request.CustomerPhone,
            Note = request.Note,
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

        table.Status = TableStatus.Occupied;

        _context.Orders.Add(order);
        await _context.SaveChangesAsync(cancellationToken);

        // Notify KDS kitchen immediately via SignalR
        await _signalRService.NotifyKitchenTicketAsync(order.BranchId, new
        {
            order.Id,
            order.OrderCode,
            table.TableNumber,
            order.Status,
            ItemsCount = order.Items.Count
        });

        var result = new PostpaidOrderResultDto(
            order.Id,
            order.OrderCode,
            order.Status,
            order.TotalAmount,
            EstimatedPrepMinutes: 10
        );

        return ApiResponse<PostpaidOrderResultDto>.SuccessResult(result, "Tạo đơn tại bàn trả sau thành công. Bếp đã nhận đơn.");
    }
}
