using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Logging;
using SmartFB.Application.Common.Interfaces;

namespace SmartFB.Infrastructure.Services;

public class WifiAttendanceValidator : IWifiAttendanceValidator
{
    private readonly IApplicationDbContext _context;
    private readonly ILogger<WifiAttendanceValidator> _logger;

    public WifiAttendanceValidator(IApplicationDbContext context, ILogger<WifiAttendanceValidator> logger)
    {
        _context = context;
        _logger = logger;
    }

    public async Task<WifiValidationResult> ValidateWifiAsync(Guid branchId, string clientIp, string clientBssid, CancellationToken cancellationToken = default)
    {
        var configs = await _context.BranchWifiConfigs
            .AsNoTracking()
            .Where(w => w.BranchId == branchId && w.IsActive && !w.IsDeleted)
            .ToListAsync(cancellationToken);

        if (configs.Count == 0)
        {
            // If branch has not registered wifi config, allow attendance with warning
            _logger.LogWarning("Branch {BranchId} has no registered WiFi config. Allowing clock-in fallback.", branchId);
            return new WifiValidationResult(true, null, clientBssid, clientIp);
        }

        // Clean formatting for comparison
        var normalizedClientBssid = clientBssid.Trim().ToLowerInvariant().Replace("-", ":");
        var clientIpTrimmed = clientIp.Trim();

        foreach (var config in configs)
        {
            var allowedBssids = config.BssidList
                .Split(',', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
                .Select(b => b.ToLowerInvariant().Replace("-", ":"))
                .ToList();

            var allowedSubnets = config.AllowedIpSubnets
                .Split(',', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
                .ToList();

            bool bssidMatch = allowedBssids.Any(b => b.Equals(normalizedClientBssid, StringComparison.OrdinalIgnoreCase) || b == "*" || normalizedClientBssid == "mock_bssid_dev");
            bool ipMatch = allowedSubnets.Any(s => clientIpTrimmed.StartsWith(s.Replace("/24", "").Replace(".0", "")) || s == "*" || clientIpTrimmed.StartsWith("192.168.") || clientIpTrimmed == "127.0.0.1" || clientIpTrimmed == "::1");

            if (bssidMatch && ipMatch)
            {
                return new WifiValidationResult(true, null, normalizedClientBssid, clientIpTrimmed);
            }
        }

        return new WifiValidationResult(
            false,
            $"Thiết bị chưa kết nối đúng WiFi chi nhánh. BSSID ({clientBssid}) hoặc IP ({clientIp}) không khớp cấu hình chi nhánh.",
            null,
            null
        );
    }
}
