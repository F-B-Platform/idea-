using MediatR;
using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Branches.DTOs;
using SmartFB.Domain.Entities;

namespace SmartFB.Application.Features.Branches.Commands.CreateBranch;

public record CreateBranchCommand(
    string Code,
    string Name,
    string Address,
    string Phone,
    string OperatingHours
) : IRequest<ApiResponse<BranchDto>>;

public class CreateBranchCommandHandler : IRequestHandler<CreateBranchCommand, ApiResponse<BranchDto>>
{
    private readonly IApplicationDbContext _context;

    public CreateBranchCommandHandler(IApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<ApiResponse<BranchDto>> Handle(CreateBranchCommand request, CancellationToken cancellationToken)
    {
        var existing = await _context.Branches
            .AnyAsync(b => b.Code == request.Code && !b.IsDeleted, cancellationToken);

        if (existing)
        {
            throw new AppException($"Mã chi nhánh \"{request.Code}\" đã tồn tại.");
        }

        var branch = new Branch
        {
            Code = request.Code,
            Name = request.Name,
            Address = request.Address,
            Phone = request.Phone,
            OperatingHours = request.OperatingHours,
            IsActive = true
        };

        _context.Branches.Add(branch);
        await _context.SaveChangesAsync(cancellationToken);

        var dto = new BranchDto(
            branch.Id,
            branch.Code,
            branch.Name,
            branch.Address,
            branch.Phone,
            branch.OperatingHours,
            branch.IsActive,
            new List<BranchWifiConfigDto>()
        );

        return ApiResponse<BranchDto>.SuccessResult(dto, "Tạo mới chi nhánh thành công.");
    }
}
