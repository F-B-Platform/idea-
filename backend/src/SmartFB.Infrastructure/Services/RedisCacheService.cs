using System.Text.Json;
using Microsoft.Extensions.Logging;
using SmartFB.Application.Common.Interfaces;
using StackExchange.Redis;

namespace SmartFB.Infrastructure.Services;

public class RedisCacheService : IRedisCacheService
{
    private readonly IConnectionMultiplexer? _redis;
    private readonly IDatabase? _database;
    private readonly ILogger<RedisCacheService> _logger;

    public RedisCacheService(ILogger<RedisCacheService> logger, IConnectionMultiplexer? redis = null)
    {
        _logger = logger;
        _redis = redis;
        try
        {
            _database = redis?.GetDatabase();
        }
        catch
        {
            _database = null;
        }
    }

    public async Task<T?> GetAsync<T>(string key, CancellationToken cancellationToken = default)
    {
        if (_database == null) return default;
        try
        {
            var value = await _database.StringGetAsync(key);
            if (!value.HasValue) return default;
            return JsonSerializer.Deserialize<T>(value!);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error getting cache key: {Key}", key);
            return default;
        }
    }

    public async Task SetAsync<T>(string key, T value, TimeSpan? expiry = null, CancellationToken cancellationToken = default)
    {
        if (_database == null) return;
        try
        {
            var serialized = JsonSerializer.Serialize(value);
            await _database.StringSetAsync(key, serialized, expiry);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error setting cache key: {Key}", key);
        }
    }

    public Task RemoveAsync(string key)
    {
        return RemoveAsync(key, CancellationToken.None);
    }

    public async Task RemoveAsync(string key, CancellationToken cancellationToken)
    {
        if (_database == null) return;
        try
        {
            await _database.KeyDeleteAsync(key);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error deleting cache key: {Key}", key);
        }
    }

    public Task<bool> AcquireLockAsync(string lockKey, string lockValue)
    {
        return AcquireLockAsync(lockKey, lockValue, TimeSpan.FromSeconds(30));
    }

    public async Task<bool> AcquireLockAsync(string lockKey, string lockValue, TimeSpan expiry)
    {
        if (_database == null) return true; // In absence of Redis, grant lock for dev/test
        try
        {
            return await _database.LockTakeAsync(lockKey, lockValue, expiry);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error acquiring distributed lock for key: {Key}", lockKey);
            return true;
        }
    }

    public async Task<bool> ReleaseLockAsync(string lockKey, string lockValue)
    {
        if (_database == null) return true;
        try
        {
            return await _database.LockReleaseAsync(lockKey, lockValue);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error releasing distributed lock for key: {Key}", lockKey);
            return false;
        }
    }
}
