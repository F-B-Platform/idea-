using System.Collections.Concurrent;
using System.Security.Cryptography;
using System.Text;
using Microsoft.AspNetCore.Authentication;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Mvc.Testing;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Domain.Common;
using SmartFB.Domain.Entities;
using SmartFB.Domain.Enums;
using SmartFB.Infrastructure.Persistence;

namespace SmartFB.IntegrationTests.Fixtures;

public class TestApplicationDbContext : ApplicationDbContext
{
    private readonly string _databaseName;

    public TestApplicationDbContext(string databaseName)
        : base(new DbContextOptionsBuilder<ApplicationDbContext>().UseInMemoryDatabase(databaseName).Options)
    {
        _databaseName = databaseName;
    }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        if (!optionsBuilder.IsConfigured)
        {
            optionsBuilder.UseInMemoryDatabase(_databaseName);
        }
    }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        base.OnModelCreating(modelBuilder);
        modelBuilder.Ignore<DomainEvent>();
    }
}

public class InMemoryTestRedisCacheService : IRedisCacheService
{
    private readonly ConcurrentDictionary<string, object> _cache = new();
    private readonly ConcurrentDictionary<string, string> _locks = new();

    public Task<T?> GetAsync<T>(string key, CancellationToken cancellationToken = default)
    {
        if (_cache.TryGetValue(key, out var val) && val is T typedVal)
        {
            return Task.FromResult<T?>(typedVal);
        }
        return Task.FromResult<T?>(default);
    }

    public Task SetAsync<T>(string key, T value, TimeSpan? expiry = null, CancellationToken cancellationToken = default)
    {
        if (value != null)
        {
            _cache[key] = value;
        }
        return Task.CompletedTask;
    }

    public Task RemoveAsync(string key)
    {
        _cache.TryRemove(key, out _);
        return Task.CompletedTask;
    }

    public Task RemoveAsync(string key, CancellationToken cancellationToken)
    {
        _cache.TryRemove(key, out _);
        return Task.CompletedTask;
    }

    public Task<bool> AcquireLockAsync(string lockKey, string lockValue)
    {
        bool added = _locks.TryAdd(lockKey, lockValue);
        return Task.FromResult(added);
    }

    public Task<bool> AcquireLockAsync(string lockKey, string lockValue, TimeSpan expiry)
    {
        bool added = _locks.TryAdd(lockKey, lockValue);
        return Task.FromResult(added);
    }

    public Task<bool> ReleaseLockAsync(string lockKey, string lockValue)
    {
        if (_locks.TryGetValue(lockKey, out var current) && current == lockValue)
        {
            return Task.FromResult(_locks.TryRemove(lockKey, out _));
        }
        return Task.FromResult(false);
    }
}

public class TestPayOSService : IPayOSService
{
    public Task<PayOSPaymentLinkResult> CreatePaymentLinkAsync(CreatePayOSPaymentRequest request, CancellationToken cancellationToken = default)
    {
        var qrUrl = $"https://img.vietqr.io/image/ICB-0001882199201-compact2.png?amount={request.Amount}&addInfo={request.OrderCode}";
        return Task.FromResult(new PayOSPaymentLinkResult(
            PaymentLinkId: $"payos-link-{request.OrderCode}",
            CheckoutUrl: $"https://pay.payos.vn/web/{request.OrderCode}",
            QrCode: qrUrl,
            OrderCode: request.OrderCode,
            Amount: request.Amount,
            Status: "PENDING"
        ));
    }

    public bool VerifyWebhookSignature(string webhookBody, string signature)
    {
        return true;
    }

    public Task<PayOSPaymentLinkResult?> GetPaymentLinkInformationAsync(string paymentLinkId, CancellationToken cancellationToken = default)
    {
        return Task.FromResult<PayOSPaymentLinkResult?>(new PayOSPaymentLinkResult(
            PaymentLinkId: paymentLinkId,
            CheckoutUrl: "https://pay.payos.vn",
            QrCode: "https://img.vietqr.io",
            OrderCode: 10042,
            Amount: 50000,
            Status: "PAID"
        ));
    }
}

public class TestSignalRHubService : ISignalRHubService
{
    public Task NotifyOrderCreatedAsync(Guid branchId, object orderData) => Task.CompletedTask;
    public Task NotifyOrderStatusChangedAsync(Guid orderId, string orderCode, string status) => Task.CompletedTask;
    public Task NotifyKitchenTicketAsync(Guid branchId, object ticketData) => Task.CompletedTask;
    public Task Notify86ToggledAsync(Guid branchId, Guid productId, bool isAvailable) => Task.CompletedTask;
    public Task NotifyPaymentSuccessAsync(Guid orderId, string transactionCode, decimal amount) => Task.CompletedTask;
    public Task NotifyUrgentAlertAsync(Guid branchId, string title, string message, object? payload = null) => Task.CompletedTask;
    public Task NotifyServiceCallAsync(Guid branchId, Guid tableId, string tableNumber, string reason) => Task.CompletedTask;
}

public class TestWifiAttendanceValidator : IWifiAttendanceValidator
{
    public Task<WifiValidationResult> ValidateWifiAsync(Guid branchId, string clientIp, string clientBssid, CancellationToken cancellationToken = default)
    {
        string normRegistered = SeedDataConstants.ValidBssid.Replace("-", ":").ToUpperInvariant();
        string normClient = clientBssid.Replace("-", ":").ToUpperInvariant();
        bool bssidMatches = normRegistered.Equals(normClient, StringComparison.OrdinalIgnoreCase);

        bool ipInSubnet = CheckIpInSubnet(clientIp, SeedDataConstants.SubnetCidr);

        if (!bssidMatches || !ipInSubnet)
        {
            return Task.FromResult(new WifiValidationResult(
                IsValid: false,
                ErrorMessage: "Bạn đang dùng 4G hoặc mạng ngoài quán. Vui lòng kết nối đúng WiFi chi nhánh để chấm công.",
                MatchedBssid: null,
                MatchedSubnet: null
            ));
        }

        return Task.FromResult(new WifiValidationResult(
            IsValid: true,
            ErrorMessage: null,
            MatchedBssid: SeedDataConstants.ValidBssid,
            MatchedSubnet: SeedDataConstants.SubnetCidr
        ));
    }

    private static bool CheckIpInSubnet(string ipAddress, string cidr)
    {
        var parts = cidr.Split('/');
        if (parts.Length != 2) return false;
        var subnetPrefix = parts[0];
        int prefixLength = int.Parse(parts[1]);

        if (prefixLength == 24)
        {
            var subnetOctets = subnetPrefix.Split('.');
            var ipOctets = ipAddress.Split('.');
            if (subnetOctets.Length != 4 || ipOctets.Length != 4) return false;

            return subnetOctets[0] == ipOctets[0] &&
                   subnetOctets[1] == ipOctets[1] &&
                   subnetOctets[2] == ipOctets[2];
        }

        return false;
    }
}

public class CustomWebApplicationFactory : WebApplicationFactory<Program>
{
    private readonly string _dbName = "SmartFB_Integration_TestDb_" + Guid.NewGuid();

    protected override void ConfigureWebHost(IWebHostBuilder builder)
    {
        builder.UseEnvironment("Testing");

        builder.ConfigureServices(services =>
        {
            // Remove existing DbContext registrations
            var dbContextDescriptor = services.SingleOrDefault(d => d.ServiceType == typeof(DbContextOptions<ApplicationDbContext>));
            if (dbContextDescriptor != null) services.Remove(dbContextDescriptor);

            var appDbDescriptor = services.SingleOrDefault(d => d.ServiceType == typeof(ApplicationDbContext));
            if (appDbDescriptor != null) services.Remove(appDbDescriptor);

            var iAppDbDescriptor = services.SingleOrDefault(d => d.ServiceType == typeof(IApplicationDbContext));
            if (iAppDbDescriptor != null) services.Remove(iAppDbDescriptor);

            var iAppDbLegacyDescriptor = services.SingleOrDefault(d => d.ServiceType == typeof(IAppDbContext));
            if (iAppDbLegacyDescriptor != null) services.Remove(iAppDbLegacyDescriptor);

            // Register TestApplicationDbContext
            services.AddScoped<ApplicationDbContext>(sp => new TestApplicationDbContext(_dbName));
            services.AddScoped<IApplicationDbContext>(sp => sp.GetRequiredService<ApplicationDbContext>());
            services.AddScoped<IAppDbContext>(sp => sp.GetRequiredService<ApplicationDbContext>());

            // Replace Redis with In-Memory Test implementation
            var redisDescriptor = services.SingleOrDefault(d => d.ServiceType == typeof(IRedisCacheService));
            if (redisDescriptor != null) services.Remove(redisDescriptor);
            services.AddSingleton<IRedisCacheService, InMemoryTestRedisCacheService>();

            // Replace PayOS with Test implementation
            var payosDescriptor = services.SingleOrDefault(d => d.ServiceType == typeof(IPayOSService));
            if (payosDescriptor != null) services.Remove(payosDescriptor);
            services.AddSingleton<IPayOSService, TestPayOSService>();

            // Replace SignalR with Test implementation
            var signalRDescriptor = services.SingleOrDefault(d => d.ServiceType == typeof(ISignalRHubService));
            if (signalRDescriptor != null) services.Remove(signalRDescriptor);
            services.AddSingleton<ISignalRHubService, TestSignalRHubService>();

            // Replace WifiValidator with Test implementation
            var wifiDescriptor = services.SingleOrDefault(d => d.ServiceType == typeof(IWifiAttendanceValidator));
            if (wifiDescriptor != null) services.Remove(wifiDescriptor);
            services.AddSingleton<IWifiAttendanceValidator, TestWifiAttendanceValidator>();

            // Configure Test Authentication
            services.AddAuthentication(options =>
            {
                options.DefaultAuthenticateScheme = TestAuthHandler.AuthenticationScheme;
                options.DefaultChallengeScheme = TestAuthHandler.AuthenticationScheme;
            })
            .AddScheme<TestAuthHandlerOptions, TestAuthHandler>(TestAuthHandler.AuthenticationScheme, _ => { });
        });
    }

    protected override IHost CreateHost(IHostBuilder builder)
    {
        var host = base.CreateHost(builder);
        using var scope = host.Services.CreateScope();
        var db = scope.ServiceProvider.GetRequiredService<ApplicationDbContext>();
        db.Database.EnsureCreated();
        SeedTestData(db);
        return host;
    }

    private static void SeedTestData(ApplicationDbContext db)
    {
        if (db.Branches.Any()) return;

        var branchQ1 = new Branch
        {
            Id = SeedDataConstants.BranchQ1Id,
            Code = "BR-Q1",
            Name = "Smart Coffee Quan 1",
            Address = "123 Le Loi, Q1, TP.HCM",
            Phone = "02838123456",
            IsActive = true
        };
        db.Branches.Add(branchQ1);

        var table04 = new Table
        {
            Id = SeedDataConstants.Table04Id,
            BranchId = SeedDataConstants.BranchQ1Id,
            TableNumber = "B04",
            Capacity = 4,
            Status = TableStatus.Available,
            QrCodeUrl = "https://smartfb.vn/table/B04",
            IsActive = true
        };

        var table05 = new Table
        {
            Id = SeedDataConstants.Table05Id,
            BranchId = SeedDataConstants.BranchQ1Id,
            TableNumber = "B05",
            Capacity = 2,
            Status = TableStatus.Available,
            QrCodeUrl = "https://smartfb.vn/table/B05",
            IsActive = true
        };
        db.Tables.AddRange(table04, table05);

        var wifiConfig = new BranchWifiConfig
        {
            BranchId = SeedDataConstants.BranchQ1Id,
            SsidName = SeedDataConstants.Ssid,
            BssidList = SeedDataConstants.ValidBssid,
            AllowedIpSubnets = SeedDataConstants.SubnetCidr,
            IsActive = true
        };
        db.BranchWifiConfigs.Add(wifiConfig);

        var user = new User
        {
            Id = SeedDataConstants.CashierUserId,
            BranchId = SeedDataConstants.BranchQ1Id,
            Username = "NV-Q1-008",
            EmployeeCode = "NV-Q1-008",
            FullName = "Nguyen Van Thu Ngan",
            Email = "thungan@smartfb.vn",
            PasswordHash = "hash123",
            Role = UserRole.CashierStaff,
            Status = "Active"
        };
        db.Users.Add(user);

        var customerNam = new Customer
        {
            Id = SeedDataConstants.CustomerNamId,
            PhoneNumber = "0909123456",
            FullName = "Nguyen Hoang Nam",
            CupBalance = 10,
            TotalPoints = 250
        };
        db.Customers.Add(customerNam);

        var productTraDao = new Product
        {
            Id = SeedDataConstants.ProductTraDaoId,
            ProductCode = "TRA-DAO-01",
            Name = "Trà Đào Cam Sả",
            Description = "Trà đào thơm ngon kèm đào miếng",
            BasePrice = 45000m,
            IsAvailable = true
        };
        productTraDao.ProductSizes.Add(new ProductSize
        {
            Id = SeedDataConstants.SizeMId,
            ProductId = productTraDao.Id,
            SizeName = "M",
            PriceAdjustment = 0
        });
        productTraDao.ProductSizes.Add(new ProductSize
        {
            Id = SeedDataConstants.SizeLId,
            ProductId = productTraDao.Id,
            SizeName = "L",
            PriceAdjustment = 8000m
        });

        var productBacXiu = new Product
        {
            Id = SeedDataConstants.ProductBacXiuId,
            ProductCode = "CF-BAC-XIU",
            Name = "Bạc Xỉu Sài Gòn",
            Description = "Cà phê sữa nhiều sữa",
            BasePrice = 35000m,
            IsAvailable = true
        };
        productBacXiu.ProductSizes.Add(new ProductSize
        {
            Id = SeedDataConstants.SizeMId2,
            ProductId = productBacXiu.Id,
            SizeName = "M",
            PriceAdjustment = 0
        });

        var productCaPheMuoi = new Product
        {
            Id = SeedDataConstants.ProductCaPheMuoiId,
            ProductCode = "CF-MUOI",
            Name = "Cà Phê Muối",
            Description = "Cà phê muối béo ngậy",
            BasePrice = 39000m,
            IsAvailable = true
        };
        productCaPheMuoi.ProductSizes.Add(new ProductSize
        {
            Id = SeedDataConstants.SizeMId3,
            ProductId = productCaPheMuoi.Id,
            SizeName = "M",
            PriceAdjustment = 0
        });

        db.Products.AddRange(productTraDao, productBacXiu, productCaPheMuoi);
        db.SaveChanges();
    }
}
