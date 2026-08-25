using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using SmartFB.Domain.Entities;

namespace SmartFB.Infrastructure.Persistence.Configurations;

public class CustomerConfiguration : IEntityTypeConfiguration<Customer>
{
    public void Configure(EntityTypeBuilder<Customer> builder)
    {
        builder.ToTable("customers");

        builder.HasKey(c => c.Id);
        builder.Property(c => c.Id).HasColumnName("customer_id").HasDefaultValueSql("gen_random_uuid()");
        builder.Property(c => c.PhoneNumber).HasColumnName("phone_number").HasMaxLength(20).IsRequired();
        builder.HasIndex(c => c.PhoneNumber).IsUnique();

        builder.Property(c => c.FullName).HasColumnName("full_name").HasMaxLength(150);
        builder.Property(c => c.Email).HasColumnName("email").HasMaxLength(150);
        builder.Property(c => c.BirthDate).HasColumnName("birth_date");
        builder.Property(c => c.MembershipTier).HasColumnName("membership_tier").HasMaxLength(50).HasDefaultValue("Standard");
        builder.Property(c => c.CupBalance).HasColumnName("cup_balance").HasDefaultValue(0);
        builder.Property(c => c.TotalPoints).HasColumnName("total_points").HasDefaultValue(0);
        builder.Property(c => c.LastVisitedAt).HasColumnName("last_visited_at").HasDefaultValueSql("CURRENT_TIMESTAMP");
        builder.Property(c => c.CreatedAt).HasColumnName("created_at").HasDefaultValueSql("CURRENT_TIMESTAMP");
        builder.Property(c => c.IsDeleted).HasColumnName("is_deleted").HasDefaultValue(false);

        builder.Ignore(c => c.TakeawayCupCount);
        builder.Ignore(c => c.TotalLoyaltyPoints);

        builder.HasQueryFilter(c => !c.IsDeleted);
    }
}

public class LoyaltyCupTransactionConfiguration : IEntityTypeConfiguration<LoyaltyCupTransaction>
{
    public void Configure(EntityTypeBuilder<LoyaltyCupTransaction> builder)
    {
        builder.ToTable("loyalty_cup_transactions");

        builder.HasKey(l => l.TransId);
        builder.Property(l => l.TransId).HasColumnName("trans_id").HasDefaultValueSql("gen_random_uuid()");
        builder.Property(l => l.CustomerId).HasColumnName("customer_id").IsRequired();
        builder.Property(l => l.OrderId).HasColumnName("order_id");
        builder.Property(l => l.CupsEarned).HasColumnName("cups_earned").HasDefaultValue(0);
        builder.Property(l => l.CupsRedeemed).HasColumnName("cups_redeemed").HasDefaultValue(0);
        builder.Property(l => l.TransactionType).HasColumnName("transaction_type").HasConversion<string>().IsRequired();
        builder.Property(l => l.Notes).HasColumnName("notes").HasMaxLength(255);
        builder.Property(l => l.CreatedAt).HasColumnName("created_at").HasDefaultValueSql("CURRENT_TIMESTAMP");

        builder.HasIndex(l => new { l.CustomerId, l.CreatedAt });

        builder.HasOne(l => l.Customer)
            .WithMany(c => c.LoyaltyCupTransactions)
            .HasForeignKey(l => l.CustomerId)
            .OnDelete(DeleteBehavior.Cascade);

        builder.HasOne(l => l.Order)
            .WithMany(o => o.LoyaltyCupTransactions)
            .HasForeignKey(l => l.OrderId)
            .OnDelete(DeleteBehavior.SetNull);
    }
}

public class VoucherConfiguration : IEntityTypeConfiguration<Voucher>
{
    public void Configure(EntityTypeBuilder<Voucher> builder)
    {
        builder.ToTable("vouchers");

        builder.HasKey(v => v.Id);
        builder.Property(v => v.Id).HasColumnName("voucher_id").HasDefaultValueSql("gen_random_uuid()");
        builder.Property(v => v.Code).HasColumnName("code").HasMaxLength(50).IsRequired();
        builder.HasIndex(v => v.Code).IsUnique();

        builder.Property(v => v.DiscountType).HasColumnName("discount_type").HasConversion<string>().IsRequired();
        builder.Property(v => v.DiscountValue).HasColumnName("discount_value").HasPrecision(12, 2).IsRequired();
        builder.Property(v => v.MinOrderValue).HasColumnName("min_order_value").HasPrecision(12, 0).HasDefaultValue(0);
        builder.Property(v => v.MaxDiscountAmount).HasColumnName("max_discount_amount").HasPrecision(12, 0);
        builder.Property(v => v.StartDate).HasColumnName("start_date").IsRequired();
        builder.Property(v => v.EndDate).HasColumnName("end_date").IsRequired();
        builder.Property(v => v.UsageLimit).HasColumnName("usage_limit").HasDefaultValue(1000);
        builder.Property(v => v.UsedCount).HasColumnName("used_count").HasDefaultValue(0);
        builder.Property(v => v.IsActive).HasColumnName("is_active").HasDefaultValue(true);
        builder.Property(v => v.CreatedAt).HasColumnName("created_at").HasDefaultValueSql("CURRENT_TIMESTAMP");
        builder.Property(v => v.IsDeleted).HasColumnName("is_deleted").HasDefaultValue(false);

        builder.HasQueryFilter(v => !v.IsDeleted);
    }
}
