using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using SmartFB.Domain.Entities;

namespace SmartFB.Infrastructure.Persistence.Configurations;

public class BranchConfiguration : IEntityTypeConfiguration<Branch>
{
    public void Configure(EntityTypeBuilder<Branch> builder)
    {
        builder.ToTable("branches");

        builder.HasKey(b => b.Id);
        builder.Property(b => b.Id).HasColumnName("branch_id").HasDefaultValueSql("gen_random_uuid()");
        builder.Property(b => b.Code).HasColumnName("code").HasMaxLength(50).IsRequired();
        builder.HasIndex(b => b.Code).IsUnique();

        builder.Property(b => b.Name).HasColumnName("name").HasMaxLength(150).IsRequired();
        builder.Property(b => b.Address).HasColumnName("address").HasMaxLength(300).IsRequired();
        builder.Property(b => b.Phone).HasColumnName("phone").HasMaxLength(20).IsRequired();
        builder.Property(b => b.OperatingHours).HasColumnName("operating_hours").HasMaxLength(100).HasDefaultValue("07:00 - 22:30");
        builder.Property(b => b.IsActive).HasColumnName("is_active").HasDefaultValue(true);
        builder.Property(b => b.CreatedAt).HasColumnName("created_at").HasDefaultValueSql("CURRENT_TIMESTAMP");
        builder.Property(b => b.UpdatedAt).HasColumnName("updated_at");
        builder.Property(b => b.IsDeleted).HasColumnName("is_deleted").HasDefaultValue(false);

        builder.HasQueryFilter(b => !b.IsDeleted);
    }
}

public class BranchWifiConfigConfiguration : IEntityTypeConfiguration<BranchWifiConfig>
{
    public void Configure(EntityTypeBuilder<BranchWifiConfig> builder)
    {
        builder.ToTable("branch_wifi_configs");

        builder.HasKey(w => w.Id);
        builder.Property(w => w.Id).HasColumnName("wifi_config_id").HasDefaultValueSql("gen_random_uuid()");
        builder.Property(w => w.BranchId).HasColumnName("branch_id").IsRequired();
        builder.Property(w => w.SsidName).HasColumnName("ssid_name").HasMaxLength(100).IsRequired();
        builder.Property(w => w.BssidList).HasColumnName("bssid_list").IsRequired();
        builder.Property(w => w.AllowedIpSubnets).HasColumnName("allowed_ip_subnets").IsRequired();
        builder.Property(w => w.IsActive).HasColumnName("is_active").HasDefaultValue(true);
        builder.Property(w => w.CreatedAt).HasColumnName("created_at").HasDefaultValueSql("CURRENT_TIMESTAMP");

        builder.HasIndex(w => w.BranchId);

        builder.HasOne(w => w.Branch)
            .WithMany(b => b.WifiConfigs)
            .HasForeignKey(w => w.BranchId)
            .OnDelete(DeleteBehavior.Cascade);

        builder.HasQueryFilter(w => !w.IsDeleted);
    }
}

public class TableConfiguration : IEntityTypeConfiguration<Table>
{
    public void Configure(EntityTypeBuilder<Table> builder)
    {
        builder.ToTable("tables");

        builder.HasKey(t => t.Id);
        builder.Property(t => t.Id).HasColumnName("table_id").HasDefaultValueSql("gen_random_uuid()");
        builder.Property(t => t.BranchId).HasColumnName("branch_id").IsRequired();
        builder.Property(t => t.TableNumber).HasColumnName("table_number").HasMaxLength(50).IsRequired();
        builder.Property(t => t.Zone).HasColumnName("zone").HasMaxLength(50).HasDefaultValue("Tầng 1");
        builder.Property(t => t.Capacity).HasColumnName("capacity").HasDefaultValue(4);
        builder.Property(t => t.QrCodeUrl).HasColumnName("qr_code_url").HasMaxLength(500);
        builder.Property(t => t.Status).HasColumnName("status").HasConversion<string>().IsRequired();
        builder.Property(t => t.IsActive).HasColumnName("is_active").HasDefaultValue(true);
        builder.Property(t => t.CreatedAt).HasColumnName("created_at").HasDefaultValueSql("CURRENT_TIMESTAMP");

        builder.HasIndex(t => new { t.BranchId, t.TableNumber }).IsUnique();

        builder.HasOne(t => t.Branch)
            .WithMany(b => b.Tables)
            .HasForeignKey(t => t.BranchId)
            .OnDelete(DeleteBehavior.Cascade);

        builder.HasQueryFilter(t => !t.IsDeleted);
    }
}
