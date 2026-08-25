using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Infrastructure.Persistence;
using SmartFB.Infrastructure.Services;
using StackExchange.Redis;

namespace SmartFB.Infrastructure;

public static class DependencyInjection
{
    public static IServiceCollection AddInfrastructureServices(this IServiceCollection services, IConfiguration configuration)
    {
        // 1. PostgreSQL DbContext
        var connectionString = configuration.GetConnectionString("DefaultConnection") 
            ?? "Host=localhost;Port=5432;Database=smart_fb_db;Username=postgres;Password=postgres_password_dev_2026";

        services.AddDbContext<ApplicationDbContext>(options =>
            options.UseNpgsql(connectionString, b => b.MigrationsAssembly(typeof(ApplicationDbContext).Assembly.FullName)));

        services.AddScoped<IApplicationDbContext>(provider => provider.GetRequiredService<ApplicationDbContext>());
        services.AddScoped<IAppDbContext>(provider => provider.GetRequiredService<ApplicationDbContext>());

        // 2. Redis Connection & Cache Service (Safe fallback if Redis instance is not available)
        var redisConnectionString = configuration.GetValue<string>("Redis:ConnectionString") ?? "localhost:6379,abortConnect=false";
        try
        {
            services.AddSingleton<IConnectionMultiplexer>(sp => ConnectionMultiplexer.Connect(redisConnectionString));
            services.AddScoped<IRedisCacheService, RedisCacheService>();
        }
        catch
        {
            // Logging / handled gracefully in RedisCacheService
        }

        // 3. Infrastructure & External Services
        services.AddHttpContextAccessor();
        services.AddSingleton<IDateTimeService, DateTimeService>();
        services.AddScoped<ICurrentUserService, CurrentUserService>();
        services.AddScoped<IJwtTokenProvider, JwtTokenProvider>();
        services.AddScoped<IPayOSService, PayOSService>();
        services.AddScoped<IWifiAttendanceValidator, WifiAttendanceValidator>();
        services.AddScoped<ISignalRHubService, SignalRHubService>();

        return services;
    }
}
