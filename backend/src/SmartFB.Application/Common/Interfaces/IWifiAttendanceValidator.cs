namespace SmartFB.Application.Common.Interfaces;

public record WifiValidationResult(
    bool IsValid,
    string? ErrorMessage,
    string? MatchedBssid,
    string? MatchedSubnet
);

public interface IWifiAttendanceValidator
{
    Task<WifiValidationResult> ValidateWifiAsync(Guid branchId, string clientIp, string clientBssid, CancellationToken cancellationToken = default);
}
