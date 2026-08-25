using Microsoft.EntityFrameworkCore;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Domain.Common;
using SmartFB.Domain.Entities;

namespace SmartFB.Infrastructure.Persistence;

public class ApplicationDbContext : DbContext, IApplicationDbContext, IAppDbContext
{
    public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : base(options)
    {
    }

    public DbSet<Branch> Branches => Set<Branch>();
    public DbSet<BranchWifiConfig> BranchWifiConfigs => Set<BranchWifiConfig>();
    public DbSet<Table> Tables => Set<Table>();
    public DbSet<User> Users => Set<User>();
    public DbSet<Role> Roles => Set<Role>();
    public DbSet<UserRoleMapping> UserRoles => Set<UserRoleMapping>();
    public DbSet<AuditLog> AuditLogs => Set<AuditLog>();
    public DbSet<Category> Categories => Set<Category>();
    public DbSet<Product> Products => Set<Product>();
    public DbSet<ProductSize> ProductSizes => Set<ProductSize>();
    public DbSet<ProductBranchPrice> ProductBranchPrices => Set<ProductBranchPrice>();
    public DbSet<Modifier> Modifiers => Set<Modifier>();
    public DbSet<ProductModifier> ProductModifiers => Set<ProductModifier>();
    public DbSet<Ingredient> Ingredients => Set<Ingredient>();
    public DbSet<RecipeBom> RecipeBoms => Set<RecipeBom>();
    public DbSet<InventoryTransaction> InventoryTransactions => Set<InventoryTransaction>();
    public DbSet<Customer> Customers => Set<Customer>();
    public DbSet<Order> Orders => Set<Order>();
    public DbSet<OrderItem> OrderItems => Set<OrderItem>();
    public DbSet<OrderItemModifier> OrderItemModifiers => Set<OrderItemModifier>();
    public DbSet<Payment> Payments => Set<Payment>();
    public DbSet<PayOSTransaction> PayOSTransactions => Set<PayOSTransaction>();
    public DbSet<Voucher> Vouchers => Set<Voucher>();
    public DbSet<CustomerReview> CustomerReviews => Set<CustomerReview>();
    public DbSet<ReviewImage> ReviewImages => Set<ReviewImage>();
    public DbSet<Shift> Shifts => Set<Shift>();
    public DbSet<ZReport> ZReports => Set<ZReport>();
    public DbSet<Attendance> Attendances => Set<Attendance>();
    public DbSet<LoyaltyCupTransaction> LoyaltyCupTransactions => Set<LoyaltyCupTransaction>();

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        base.OnModelCreating(modelBuilder);
        modelBuilder.ApplyConfigurationsFromAssembly(typeof(ApplicationDbContext).Assembly);
    }

    public override Task<int> SaveChangesAsync(CancellationToken cancellationToken = default)
    {
        foreach (var entry in ChangeTracker.Entries<BaseEntity>())
        {
            switch (entry.State)
            {
                case EntityState.Added:
                    if (entry.Entity.CreatedAt == default)
                    {
                        entry.Entity.CreatedAt = DateTime.UtcNow;
                    }
                    break;

                case EntityState.Modified:
                    entry.Entity.UpdatedAt = DateTime.UtcNow;
                    break;

                case EntityState.Deleted:
                    entry.State = EntityState.Modified;
                    entry.Entity.IsDeleted = true;
                    entry.Entity.DeletedAt = DateTime.UtcNow;
                    entry.Entity.UpdatedAt = DateTime.UtcNow;
                    break;
            }
        }

        return base.SaveChangesAsync(cancellationToken);
    }
}
