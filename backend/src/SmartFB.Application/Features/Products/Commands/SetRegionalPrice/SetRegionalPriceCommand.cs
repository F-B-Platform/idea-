using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Products.DTOs;
using SmartFB.Domain.Entities;

namespace SmartFB.Application.Features.Products.Commands.SetRegionalPrice;

public record SetRegionalPriceCommand(
    Guid BranchId,
    Guid ProductId,
    decimal PriceOverride,
    bool IsAvailable86 = true
) : IRequest<ApiResponse<bool>>;

public class SetRegionalPriceCommandHandler : IRequestHandler<SetRegionalPriceCommand, ApiResponse<bool>>
{
    private readonly IApplicationDbContext _context;

    public SetRegionalPriceCommandHandler(IApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<ApiResponse<bool>> Handle(SetRegionalPriceCommand request, CancellationToken cancellationToken)
    {
        var product = await _context.Products
            .FirstOrDefaultAsync(p => p.Id == request.ProductId && !p.IsDeleted, cancellationToken);

        if (product == null)
        {
            throw new NotFoundException("Product", request.ProductId);
        }

        var branch = await _context.Branches
            .FirstOrDefaultAsync(b => b.Id == request.BranchId && !b.IsDeleted, cancellationToken);

        if (branch == null)
        {
            throw new NotFoundException("Branch", request.BranchId);
        }

        var regionalPrice = await _context.ProductBranchPrices
            .FirstOrDefaultAsync(rb => rb.BranchId == request.BranchId && rb.ProductId == request.ProductId && !rb.IsDeleted, cancellationToken);

        if (regionalPrice == null)
        {
            regionalPrice = new ProductBranchPrice
            {
                BranchId = request.BranchId,
                ProductId = request.ProductId,
                PriceOverride = request.PriceOverride,
                IsAvailable86 = request.IsAvailable86
            };
            _context.ProductBranchPrices.Add(regionalPrice);
        }
        else
        {
            regionalPrice.PriceOverride = request.PriceOverride;
            regionalPrice.IsAvailable86 = request.IsAvailable86;
        }

        await _context.SaveChangesAsync(cancellationToken);
        return ApiResponse<bool>.SuccessResult(true, "Thiết lập giá vùng chi nhánh thành công.");
    }
}
