using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Domain.Entities;

namespace SmartFB.Application.Features.KitchenKDS.Commands.Toggle86Product;

public record Toggle86ProductCommand(
    Guid BranchId,
    Guid ProductId,
    bool IsAvailable
) : IRequest<ApiResponse<bool>>;

public class Toggle86ProductCommandHandler : IRequestHandler<Toggle86ProductCommand, ApiResponse<bool>>
{
    private readonly IApplicationDbContext _context;
    private readonly ISignalRHubService _signalRService;

    public Toggle86ProductCommandHandler(IApplicationDbContext context, ISignalRHubService signalRService)
    {
        _context = context;
        _signalRService = signalRService;
    }

    public async Task<ApiResponse<bool>> Handle(Toggle86ProductCommand request, CancellationToken cancellationToken)
    {
        var product = await _context.Products
            .FirstOrDefaultAsync(p => p.Id == request.ProductId && !p.IsDeleted, cancellationToken);

        if (product == null)
        {
            throw new NotFoundException("Product", request.ProductId);
        }

        var branchPrice = await _context.ProductBranchPrices
            .FirstOrDefaultAsync(bp => bp.BranchId == request.BranchId && bp.ProductId == request.ProductId && !bp.IsDeleted, cancellationToken);

        if (branchPrice == null)
        {
            branchPrice = new ProductBranchPrice
            {
                BranchId = request.BranchId,
                ProductId = request.ProductId,
                PriceOverride = product.BasePrice,
                IsAvailable86 = request.IsAvailable
            };
            _context.ProductBranchPrices.Add(branchPrice);
        }
        else
        {
            branchPrice.IsAvailable86 = request.IsAvailable;
        }

        await _context.SaveChangesAsync(cancellationToken);

        // Broadcast 86-toggle status event via SignalR to KitchenHub and POS/Menu
        await _signalRService.Notify86ToggledAsync(request.BranchId, request.ProductId, request.IsAvailable);

        var statusText = request.IsAvailable ? "Đang phục vụ" : "Tạm hết hàng (86-Out)";
        return ApiResponse<bool>.SuccessResult(true, $"Đã cập nhật công tắc 86 món \"{product.Name}\": {statusText}.");
    }
}
