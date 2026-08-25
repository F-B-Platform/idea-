using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Domain.Entities;
using SmartFB.Domain.Enums;

namespace SmartFB.Application.Features.KitchenKDS.Commands.UpdateKdsItemStatus;

public record UpdateKdsItemStatusCommand(
    Guid OrderItemId,
    string NewStatus
) : IRequest<ApiResponse<bool>>;

public class UpdateKdsItemStatusCommandHandler : IRequestHandler<UpdateKdsItemStatusCommand, ApiResponse<bool>>
{
    private readonly IApplicationDbContext _context;
    private readonly ISignalRHubService _signalRService;

    public UpdateKdsItemStatusCommandHandler(IApplicationDbContext context, ISignalRHubService signalRService)
    {
        _context = context;
        _signalRService = signalRService;
    }

    public async Task<ApiResponse<bool>> Handle(UpdateKdsItemStatusCommand request, CancellationToken cancellationToken)
    {
        var item = await _context.OrderItems
            .Include(i => i.Order)
            .Include(i => i.Product)
            .FirstOrDefaultAsync(i => i.Id == request.OrderItemId && !i.IsDeleted, cancellationToken);

        if (item == null)
        {
            throw new NotFoundException("OrderItem", request.OrderItemId);
        }

        var oldStatus = item.ItemStatus;
        item.ItemStatus = request.NewStatus;

        // Pillar 5: Automatic BOM inventory deduction when item transition to "Ready"
        if (request.NewStatus.Equals("Ready", StringComparison.OrdinalIgnoreCase) && !oldStatus.Equals("Ready", StringComparison.OrdinalIgnoreCase))
        {
            var recipeBoms = await _context.RecipeBoms
                .Include(r => r.Ingredient)
                .Where(r => r.ProductId == item.ProductId && r.SizeId == item.SizeId && !r.IsDeleted)
                .ToListAsync(cancellationToken);

            foreach (var bom in recipeBoms)
            {
                decimal totalDeductQuantity = (bom.StandardQuantity * (1 + (bom.WastagePercentage / 100))) * item.Quantity;
                bom.Ingredient.CurrentStock = Math.Max(0, bom.Ingredient.CurrentStock - totalDeductQuantity);

                _context.InventoryTransactions.Add(new InventoryTransaction
                {
                    IngredientId = bom.IngredientId,
                    BranchId = item.Order.BranchId,
                    TransactionType = InventoryTransactionType.Export,
                    Quantity = totalDeductQuantity,
                    UnitPrice = bom.Ingredient.UnitCost,
                    TotalCost = totalDeductQuantity * bom.Ingredient.UnitCost,
                    Notes = $"Tự động trừ định mức BOM cho món {item.Product.Name} x{item.Quantity} (Đơn {item.Order.OrderCode})"
                });
            }
        }

        // Check if all items in order are ready/served -> update whole order status
        var allItemsInOrder = await _context.OrderItems
            .Where(i => i.OrderId == item.OrderId && !i.IsDeleted)
            .ToListAsync(cancellationToken);

        if (allItemsInOrder.All(i => i.ItemStatus.Equals("Ready", StringComparison.OrdinalIgnoreCase) || i.ItemStatus.Equals("Served", StringComparison.OrdinalIgnoreCase)))
        {
            item.Order.Status = OrderStatus.Ready;
            await _signalRService.NotifyOrderStatusChangedAsync(item.OrderId, item.Order.OrderCode, "Ready");
        }
        else if (request.NewStatus.Equals("Preparing", StringComparison.OrdinalIgnoreCase))
        {
            item.Order.Status = OrderStatus.Preparing;
            await _signalRService.NotifyOrderStatusChangedAsync(item.OrderId, item.Order.OrderCode, "Preparing");
        }

        await _context.SaveChangesAsync(cancellationToken);
        return ApiResponse<bool>.SuccessResult(true, $"Cập nhật trạng thái món sang \"{request.NewStatus}\" thành công.");
    }
}
