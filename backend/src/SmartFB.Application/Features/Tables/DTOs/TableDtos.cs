using SmartFB.Domain.Enums;

namespace SmartFB.Application.Features.Tables.DTOs;

public record TableDto(
    Guid Id,
    Guid BranchId,
    string TableNumber,
    string Zone,
    int Capacity,
    string? QrCodeUrl,
    TableStatus Status,
    bool IsActive
);

public record TableQrDto(
    Guid TableId,
    string TableNumber,
    string QrCodeUrl,
    string DeepLinkUrl
);

public record CreateTableRequestDto(
    Guid BranchId,
    string TableNumber,
    string Zone,
    int Capacity
);

public record UpdateTableStatusRequestDto(
    TableStatus Status
);
