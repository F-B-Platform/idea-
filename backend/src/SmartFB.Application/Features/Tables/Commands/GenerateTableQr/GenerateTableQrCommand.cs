using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Tables.DTOs;

namespace SmartFB.Application.Features.Tables.Commands.GenerateTableQr;

public record GenerateTableQrCommand(Guid TableId) : IRequest<ApiResponse<TableQrDto>>;

public class GenerateTableQrCommandHandler : IRequestHandler<GenerateTableQrCommand, ApiResponse<TableQrDto>>
{
    private readonly IApplicationDbContext _context;

    public GenerateTableQrCommandHandler(IApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<ApiResponse<TableQrDto>> Handle(GenerateTableQrCommand request, CancellationToken cancellationToken)
    {
        var table = await _context.Tables
            .FirstOrDefaultAsync(t => t.Id == request.TableId && !t.IsDeleted, cancellationToken);

        if (table == null)
        {
            throw new NotFoundException("Table", request.TableId);
        }

        var deepLink = $"https://app.smartfb.vn/order?branchId={table.BranchId}&tableId={table.Id}&tableNumber={Uri.EscapeDataString(table.TableNumber)}";
        table.QrCodeUrl = deepLink;
        await _context.SaveChangesAsync(cancellationToken);

        var result = new TableQrDto(
            table.Id,
            table.TableNumber,
            deepLink,
            deepLink
        );

        return ApiResponse<TableQrDto>.SuccessResult(result, "Sinh mã QR bàn thành công.");
    }
}
