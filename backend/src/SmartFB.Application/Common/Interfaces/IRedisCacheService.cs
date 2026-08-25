namespace SmartFB.Application.Common.Interfaces;

public interface IRedisCacheService
{
    Task<T?> GetAsync<T>(string key, CancellationToken cancellationToken = default);
    Task SetAsync<T>(string key, T value, TimeSpan? expiry = null, CancellationToken cancellationToken = default);
    Task RemoveAsync(string key, CancellationToken cancellationToken = default);
    Task<bool> AcquireLockAsync(string lockKey, string lockValue, TimeSpan expiry);
    Task<bool> ReleaseLockAsync(string lockKey, string lockValue);
}
