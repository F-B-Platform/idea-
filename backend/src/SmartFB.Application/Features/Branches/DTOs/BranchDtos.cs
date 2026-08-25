namespace SmartFB.Application.Features.Branches.DTOs;

public record BranchDto(
    Guid Id,
    string Code,
    string Name,
    string Address,
    string Phone,
    string OperatingHours,
    bool IsActive,
    List<BranchWifiConfigDto> WifiConfigs
);

public record BranchWifiConfigDto(
    Guid Id,
    Guid BranchId,
    string SsidName,
    string BssidList,
    string AllowedIpSubnets,
    bool IsActive
);

public record CreateBranchRequestDto(
    string Code,
    string Name,
    string Address,
    string Phone,
    string OperatingHours
);

public record UpdateBranchRequestDto(
    string Name,
    string Address,
    string Phone,
    string OperatingHours,
    bool IsActive
);

public record ConfigureWifiRequestDto(
    string SsidName,
    string BssidList,
    string AllowedIpSubnets,
    bool IsActive
);
