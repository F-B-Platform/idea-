using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using SmartFB.Domain.Entities;

namespace SmartFB.Infrastructure.Persistence.Configurations;

public class ModifierConfiguration : IEntityTypeConfiguration<Modifier>
{
    public void Configure(EntityTypeBuilder<Modifier> builder)
    {
        builder.ToTable("modifiers");

        builder.HasKey(m => m.Id);
        builder.Property(m => m.Id).HasColumnName("modifier_id").HasDefaultValueSql("gen_random_uuid()");
        builder.Property(m => m.Name).HasColumnName("name").HasMaxLength(100).IsRequired();
        builder.Property(m => m.Type).HasColumnName("type").HasConversion<string>().IsRequired();
        builder.Property(m => m.ExtraPrice).HasColumnName("extra_price").HasPrecision(12, 0).HasDefaultValue(0);
        builder.Property(m => m.IsAvailable).HasColumnName("is_available").HasDefaultValue(true);
        builder.Property(m => m.CreatedAt).HasColumnName("created_at").HasDefaultValueSql("CURRENT_TIMESTAMP");

        builder.HasQueryFilter(m => !m.IsDeleted);
    }
}

public class ProductModifierConfiguration : IEntityTypeConfiguration<ProductModifier>
{
    public void Configure(EntityTypeBuilder<ProductModifier> builder)
    {
        builder.ToTable("product_modifiers");

        builder.HasKey(pm => new { pm.ProductId, pm.ModifierId });
        builder.Property(pm => pm.ProductId).HasColumnName("product_id");
        builder.Property(pm => pm.ModifierId).HasColumnName("modifier_id");
        builder.Property(pm => pm.IsDefault).HasColumnName("is_default").HasDefaultValue(false);
        builder.Property(pm => pm.MaxQuantity).HasColumnName("max_quantity").HasDefaultValue(1);

        builder.HasOne(pm => pm.Product)
            .WithMany(p => p.ProductModifiers)
            .HasForeignKey(pm => pm.ProductId)
            .OnDelete(DeleteBehavior.Cascade);

        builder.HasOne(pm => pm.Modifier)
            .WithMany(m => m.ProductModifiers)
            .HasForeignKey(pm => pm.ModifierId)
            .OnDelete(DeleteBehavior.Cascade);
    }
}

public class IngredientConfiguration : IEntityTypeConfiguration<Ingredient>
{
    public void Configure(EntityTypeBuilder<Ingredient> builder)
    {
        builder.ToTable("ingredients");

        builder.HasKey(i => i.Id);
        builder.Property(i => i.Id).HasColumnName("ingredient_id").HasDefaultValueSql("gen_random_uuid()");
        builder.Property(i => i.Code).HasColumnName("code").HasMaxLength(50).IsRequired();
        builder.HasIndex(i => i.Code).IsUnique();

        builder.Property(i => i.Name).HasColumnName("name").HasMaxLength(150).IsRequired();
        builder.Property(i => i.Unit).HasColumnName("unit").HasMaxLength(20).IsRequired();
        builder.Property(i => i.CurrentStock).HasColumnName("current_stock").HasPrecision(10, 3).HasDefaultValue(0);
        builder.Property(i => i.MinStockThreshold).HasColumnName("min_stock_threshold").HasPrecision(10, 3).HasDefaultValue(0);
        builder.Property(i => i.UnitCost).HasColumnName("unit_cost").HasPrecision(12, 0).HasDefaultValue(0);
        builder.Property(i => i.CreatedAt).HasColumnName("created_at").HasDefaultValueSql("CURRENT_TIMESTAMP");
        builder.Property(i => i.IsDeleted).HasColumnName("is_deleted").HasDefaultValue(false);

        builder.HasQueryFilter(i => !i.IsDeleted);
    }
}

public class RecipeBomConfiguration : IEntityTypeConfiguration<RecipeBom>
{
    public void Configure(EntityTypeBuilder<RecipeBom> builder)
    {
        builder.ToTable("recipes_bom");

        builder.HasKey(r => r.Id);
        builder.Property(r => r.Id).HasColumnName("recipe_id").HasDefaultValueSql("gen_random_uuid()");
        builder.Property(r => r.ProductId).HasColumnName("product_id").IsRequired();
        builder.Property(r => r.SizeId).HasColumnName("size_id").IsRequired();
        builder.Property(r => r.IngredientId).HasColumnName("ingredient_id").IsRequired();
        builder.Property(r => r.StandardQuantity).HasColumnName("standard_quantity").HasPrecision(10, 3).IsRequired();
        builder.Property(r => r.WastagePercentage).HasColumnName("wastage_percentage").HasPrecision(5, 2).HasDefaultValue(0);
        builder.Property(r => r.CreatedAt).HasColumnName("created_at").HasDefaultValueSql("CURRENT_TIMESTAMP");
        builder.Property(r => r.IsDeleted).HasColumnName("is_deleted").HasDefaultValue(false);

        builder.HasIndex(r => new { r.ProductId, r.SizeId, r.IngredientId }).IsUnique();

        builder.HasOne(r => r.Product)
            .WithMany(p => p.RecipeBoms)
            .HasForeignKey(r => r.ProductId)
            .OnDelete(DeleteBehavior.Cascade);

        builder.HasOne(r => r.ProductSize)
            .WithMany(s => s.RecipeBoms)
            .HasForeignKey(r => r.SizeId)
            .OnDelete(DeleteBehavior.Cascade);

        builder.HasOne(r => r.Ingredient)
            .WithMany(i => i.RecipeBoms)
            .HasForeignKey(r => r.IngredientId)
            .OnDelete(DeleteBehavior.Restrict);

        builder.HasQueryFilter(r => !r.IsDeleted);
    }
}

public class InventoryTransactionConfiguration : IEntityTypeConfiguration<InventoryTransaction>
{
    public void Configure(EntityTypeBuilder<InventoryTransaction> builder)
    {
        builder.ToTable("inventory_transactions");

        builder.HasKey(it => it.Id);
        builder.Property(it => it.Id).HasColumnName("trans_id").HasDefaultValueSql("gen_random_uuid()");
        builder.Property(it => it.IngredientId).HasColumnName("ingredient_id").IsRequired();
        builder.Property(it => it.BranchId).HasColumnName("branch_id").IsRequired();
        builder.Property(it => it.TransactionType).HasColumnName("transaction_type").HasConversion<string>().IsRequired();
        builder.Property(it => it.Quantity).HasColumnName("quantity").HasPrecision(10, 3).IsRequired();
        builder.Property(it => it.UnitPrice).HasColumnName("unit_price").HasPrecision(12, 0).HasDefaultValue(0);
        builder.Property(it => it.TotalCost).HasColumnName("total_cost").HasPrecision(12, 0).HasDefaultValue(0);
        builder.Property(it => it.SupplierName).HasColumnName("supplier_name").HasMaxLength(150);
        builder.Property(it => it.InvoiceImageUrl).HasColumnName("invoice_image_url").HasMaxLength(500);
        builder.Property(it => it.Notes).HasColumnName("notes");
        builder.Property(it => it.CreatedAt).HasColumnName("created_at").HasDefaultValueSql("CURRENT_TIMESTAMP");

        builder.HasIndex(it => new { it.BranchId, it.IngredientId, it.CreatedAt });

        builder.HasOne(it => it.Ingredient)
            .WithMany(i => i.InventoryTransactions)
            .HasForeignKey(it => it.IngredientId)
            .OnDelete(DeleteBehavior.Restrict);

        builder.HasOne(it => it.Branch)
            .WithMany(b => b.InventoryTransactions)
            .HasForeignKey(it => it.BranchId)
            .OnDelete(DeleteBehavior.Restrict);

        builder.HasQueryFilter(it => !it.IsDeleted);
    }
}
