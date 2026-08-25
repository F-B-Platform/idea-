using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Tables.DTOs;
using SmartFB.Domain.Entities;
using SmartFB.Domain.Enums;

namespace SmartFB.Application.Features.Tables.Commands.CreateTable;

public record CreateTableCommand(
    Guid BranchId,
    string TableNumber,
    string Zone,
    int Capacity
) : IRequest<ApiResponse<TableDto>>;

public class CreateTableCommandHandler : IRequestHandler<CreateTableCommand, ApiResponse<TableDto>>
{
    private readonly IApplicationDbContext _context;

    public CreateTableCommandHandler(IApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<ApiResponse<TableDto>> Handle(CreateTableCommand request, CancellationToken cancellationToken)
    {
        var branchExists = await _context.Branches
            .AnyAsync(b => b.Id == request.BranchId && !b.IsDeleted, cancellationToken);

        if (!branchExists)
        {
            throw new NotFoundException("Branch", request.BranchId);
        }

        var tableExists = await _context.Tables
            .AnyAsync(t => t.BranchId == request.BranchId && t.TableNumber == request.TableNumber && !t.IsDeleted, cancellationToken);

        if (tableExists)
        {
            throw new AppException($"Bàn \"{request.TableNumber}\" đã tồn tại tại chi nhánh.");
        }

        var tableId = Guid.NewGuid();
        var qrUrl = $"https://app.smartfb.vn/order?branchId={request.BranchId}&tableId={tableId}";

        var table = new Table
        {
            Id = tableId,
            BranchId = request.BranchId,
            TableNumber = request.TableNumber,
            Zone = string.IsNullOrWhiteSpace(request.Zone) ? "Tầng 1" : request.Zone,
            Capacity = request.Capacity <= 0 ? 4 : request.Capacity,
            QrCodeUrl = qrUrl,
            Status = TableStatus.Available,
            IsActive = true
        };

        _context.Tables.Add(table);
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

        return ApiResponse<TableDto>.SuccessResult(dto, "Tạo mới bàn thành công.");
    }
}
