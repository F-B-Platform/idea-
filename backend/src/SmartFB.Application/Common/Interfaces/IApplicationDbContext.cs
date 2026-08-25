using Microsoft.EntityFrameworkCore;
using SmartFB.Domain.Entities;

namespace SmartFB.Application.Common.Interfaces;

public interface IApplicationDbContext
{
    DbSet<Branch> Branches { get; }
    DbSet<BranchWifiConfig> BranchWifiConfigs { get; }
    DbSet<Table> Tables { get; }
    DbSet<User> Users { get; }
    DbSet<Role> Roles { get; }
    DbSet<UserRoleMapping> UserRoles { get; }
    DbSet<AuditLog> AuditLogs { get; }
    DbSet<Category> Categories { get; }
    DbSet<Product> Products { get; }
    DbSet<ProductSize> ProductSizes { get; }
    DbSet<ProductBranchPrice> ProductBranchPrices { get; }
    DbSet<Modifier> Modifiers { get; }
    DbSet<ProductModifier> ProductModifiers { get; }
    DbSet<Ingredient> Ingredients { get; }
    DbSet<RecipeBom> RecipeBoms { get; }
    DbSet<InventoryTransaction> InventoryTransactions { get; }
    DbSet<Customer> Customers { get; }
    DbSet<Order> Orders { get; }
    DbSet<OrderItem> OrderItems { get; }
    DbSet<OrderItemModifier> OrderItemModifiers { get; }
    DbSet<Payment> Payments { get; }
    DbSet<PayOSTransaction> PayOSTransactions { get; }
    DbSet<Voucher> Vouchers { get; }
    DbSet<CustomerReview> CustomerReviews { get; }
    DbSet<ReviewImage> ReviewImages { get; }
    DbSet<Shift> Shifts { get; }
    DbSet<ZReport> ZReports { get; }
    DbSet<Attendance> Attendances { get; }
    DbSet<LoyaltyCupTransaction> LoyaltyCupTransactions { get; }

    Task<int> SaveChangesAsync(CancellationToken cancellationToken = default);
}

// Alias interface matching alternative naming
public interface IAppDbContext : IApplicationDbContext { }
