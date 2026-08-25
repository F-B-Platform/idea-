using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Tables.DTOs;
using SmartFB.Domain.Enums;

namespace SmartFB.Application.Features.Tables.Commands.UpdateTableStatus;

public record UpdateTableStatusCommand(Guid TableId, TableStatus Status) : IRequest<ApiResponse<TableDto>>;

public class UpdateTableStatusCommandHandler : IRequestHandler<UpdateTableStatusCommand, ApiResponse<TableDto>>
{
    private readonly IApplicationDbContext _context;

    public UpdateTableStatusCommandHandler(IApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<ApiResponse<TableDto>> Handle(UpdateTableStatusCommand request, CancellationToken cancellationToken)
    {
        var table = await _context.Tables
            .FirstOrDefaultAsync(t => t.Id == request.TableId && !t.IsDeleted, cancellationToken);

        if (table == null)
        {
            throw new NotFoundException("Table", request.TableId);
        }

        table.Status = request.Status;
        await _context.SaveChangesAsync(cancellationToken);

        var dto = new TableDto(
            table.Id,
            table.BranchId,
            table.TableNumber,
            table.Zone,
            table.Capacity,
            table.QrCodeUrl,
            table.Status,
            table.IsActive
        );

        return ApiResponse<TableDto>.SuccessResult(dto, "Cập nhật trạng thái bàn thành công.");
    }
}
