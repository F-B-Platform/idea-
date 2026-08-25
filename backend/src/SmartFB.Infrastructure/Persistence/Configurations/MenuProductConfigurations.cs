using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using SmartFB.Domain.Entities;

namespace SmartFB.Infrastructure.Persistence.Configurations;

public class CategoryConfiguration : IEntityTypeConfiguration<Category>
{
    public void Configure(EntityTypeBuilder<Category> builder)
    {
        builder.ToTable("categories");

        builder.HasKey(c => c.Id);
        builder.Property(c => c.Id).HasColumnName("category_id").HasDefaultValueSql("gen_random_uuid()");
        builder.Property(c => c.Name).HasColumnName("name").HasMaxLength(100).IsRequired();
        builder.Property(c => c.Description).HasColumnName("description");
        builder.Property(c => c.DisplayOrder).HasColumnName("display_order").HasDefaultValue(0);
        builder.Property(c => c.ImageUrl).HasColumnName("image_url").HasMaxLength(500);
        builder.Property(c => c.IsActive).HasColumnName("is_active").HasDefaultValue(true);
        builder.Property(c => c.CreatedAt).HasColumnName("created_at").HasDefaultValueSql("CURRENT_TIMESTAMP");
        builder.Property(c => c.IsDeleted).HasColumnName("is_deleted").HasDefaultValue(false);

        builder.HasQueryFilter(c => !c.IsDeleted);
    }
}

public class ProductConfiguration : IEntityTypeConfiguration<Product>
{
    public void Configure(EntityTypeBuilder<Product> builder)
    {
        builder.ToTable("products");

        builder.HasKey(p => p.Id);
        builder.Property(p => p.Id).HasColumnName("product_id").HasDefaultValueSql("gen_random_uuid()");
        builder.Property(p => p.CategoryId).HasColumnName("category_id").IsRequired();
        builder.Property(p => p.Sku).HasColumnName("sku").HasMaxLength(50).IsRequired();
        builder.HasIndex(p => p.Sku).IsUnique();

        builder.Property(p => p.Name).HasColumnName("name").HasMaxLength(150).IsRequired();
        builder.Property(p => p.Description).HasColumnName("description");
        builder.Property(p => p.BasePrice).HasColumnName("base_price").HasPrecision(12, 0).IsRequired();
        builder.Property(p => p.ImageUrl).HasColumnName("image_url").HasMaxLength(500);
        builder.Property(p => p.IsAvailable).HasColumnName("is_available").HasDefaultValue(true);
        builder.Property(p => p.IsBestSeller).HasColumnName("is_best_seller").HasDefaultValue(false);
        builder.Property(p => p.CaloriesApprox).HasColumnName("calories_approx").HasDefaultValue(0);
        builder.Property(p => p.AllergenInfo).HasColumnName("allergen_info");
        builder.Property(p => p.CreatedAt).HasColumnName("created_at").HasDefaultValueSql("CURRENT_TIMESTAMP");
        builder.Property(p => p.IsDeleted).HasColumnName("is_deleted").HasDefaultValue(false);

        builder.HasIndex(p => new { p.CategoryId, p.IsAvailable });

        builder.HasOne(p => p.Category)
            .WithMany(c => c.Products)
            .HasForeignKey(p => p.CategoryId)
            .OnDelete(DeleteBehavior.Restrict);

        builder.HasQueryFilter(p => !p.IsDeleted);
    }
}

public class ProductSizeConfiguration : IEntityTypeConfiguration<ProductSize>
{
    public void Configure(EntityTypeBuilder<ProductSize> builder)
    {
        builder.ToTable("product_sizes");

        builder.HasKey(s => s.Id);
        builder.Property(s => s.Id).HasColumnName("size_id").HasDefaultValueSql("gen_random_uuid()");
        builder.Property(s => s.ProductId).HasColumnName("product_id").IsRequired();
        builder.Property(s => s.SizeName).HasColumnName("size_name").HasMaxLength(50).IsRequired();
        builder.Property(s => s.PriceAdjustment).HasColumnName("price_adjustment").HasPrecision(12, 0).HasDefaultValue(0);
        builder.Property(s => s.DisplayOrder).HasColumnName("display_order").HasDefaultValue(0);
        builder.Property(s => s.CreatedAt).HasColumnName("created_at").HasDefaultValueSql("CURRENT_TIMESTAMP");

        builder.HasIndex(s => new { s.ProductId, s.SizeName }).IsUnique();

        builder.HasOne(s => s.Product)
            .WithMany(p => p.ProductSizes)
            .HasForeignKey(s => s.ProductId)
            .OnDelete(DeleteBehavior.Cascade);

        builder.HasQueryFilter(s => !s.IsDeleted);
    }
}

public class ProductBranchPriceConfiguration : IEntityTypeConfiguration<ProductBranchPrice>
{
    public void Configure(EntityTypeBuilder<ProductBranchPrice> builder)
    {
        builder.ToTable("product_branch_prices");

        builder.HasKey(bp => bp.Id);
        builder.Property(bp => bp.Id).HasColumnName("branch_price_id").HasDefaultValueSql("gen_random_uuid()");
        builder.Property(bp => bp.ProductId).HasColumnName("product_id").IsRequired();
        builder.Property(bp => bp.BranchId).HasColumnName("branch_id").IsRequired();
        builder.Property(bp => bp.PriceOverride).HasColumnName("price_override").HasPrecision(12, 0).IsRequired();
        builder.Property(bp => bp.IsAvailable86).HasColumnName("is_available_86").HasDefaultValue(true);
        builder.Property(bp => bp.UpdatedAt).HasColumnName("updated_at");

        builder.HasIndex(bp => new { bp.BranchId, bp.ProductId }).IsUnique();

        builder.HasOne(bp => bp.Product)
            .WithMany(p => p.BranchPrices)
            .HasForeignKey(bp => bp.ProductId)
            .OnDelete(DeleteBehavior.Cascade);

        builder.HasOne(bp => bp.Branch)
            .WithMany(b => b.ProductBranchPrices)
            .HasForeignKey(bp => bp.BranchId)
            .OnDelete(DeleteBehavior.Cascade);

        builder.HasQueryFilter(bp => !bp.IsDeleted);
    }
}
