using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using SmartFB.Domain.Entities;

namespace SmartFB.Infrastructure.Persistence.Configurations;

public class OrderConfiguration : IEntityTypeConfiguration<Order>
{
    public void Configure(EntityTypeBuilder<Order> builder)
    {
        builder.ToTable("orders");

        builder.HasKey(o => o.Id);
        builder.Property(o => o.Id).HasColumnName("order_id").HasDefaultValueSql("gen_random_uuid()");
        builder.Property(o => o.BranchId).HasColumnName("branch_id").IsRequired();
        builder.Property(o => o.TableId).HasColumnName("table_id");
        builder.Property(o => o.CustomerId).HasColumnName("customer_id");
        builder.Property(o => o.OrderCode).HasColumnName("order_code").HasMaxLength(50).IsRequired();
        builder.HasIndex(o => o.OrderCode).IsUnique();

        builder.Property(o => o.OrderType).HasColumnName("order_type").HasConversion<string>().IsRequired();
        builder.Property(o => o.Status).HasColumnName("status").HasConversion<string>().IsRequired();
        builder.Property(o => o.SubTotal).HasColumnName("sub_total").HasPrecision(12, 0).IsRequired();
        builder.Property(o => o.DiscountAmount).HasColumnName("discount_amount").HasPrecision(12, 0).HasDefaultValue(0);
        builder.Property(o => o.DeliveryFee).HasColumnName("delivery_fee").HasPrecision(12, 0).HasDefaultValue(0);
        builder.Property(o => o.TotalAmount).HasColumnName("total_amount").HasPrecision(12, 0).IsRequired();
        builder.Property(o => o.CustomerName).HasColumnName("customer_name").HasMaxLength(150);
        builder.Property(o => o.CustomerPhone).HasColumnName("customer_phone").HasMaxLength(20);
        builder.Property(o => o.DeliveryAddress).HasColumnName("delivery_address").HasMaxLength(500);
        builder.Property(o => o.Note).HasColumnName("note");
        builder.Property(o => o.ExpiresAt).HasColumnName("expires_at");
        builder.Property(o => o.PaidAt).HasColumnName("paid_at");
        builder.Property(o => o.CompletedAt).HasColumnName("completed_at");
        builder.Property(o => o.CreatedAt).HasColumnName("created_at").HasDefaultValueSql("CURRENT_TIMESTAMP");
        builder.Property(o => o.IsDeleted).HasColumnName("is_deleted").HasDefaultValue(false);

        builder.Ignore(o => o.RecipientName);
        builder.Ignore(o => o.RecipientPhone);
        builder.Ignore(o => o.DeliveryNotes);
        builder.Ignore(o => o.OrderItems);

        builder.HasIndex(o => new { o.BranchId, o.Status, o.CreatedAt });
        builder.HasIndex(o => new { o.CustomerId, o.CreatedAt });

        builder.HasOne(o => o.Branch)
            .WithMany(b => b.Orders)
            .HasForeignKey(o => o.BranchId)
            .OnDelete(DeleteBehavior.Restrict);

        builder.HasOne(o => o.Table)
            .WithMany(t => t.Orders)
            .HasForeignKey(o => o.TableId)
            .OnDelete(DeleteBehavior.SetNull);

        builder.HasOne(o => o.Customer)
            .WithMany(c => c.Orders)
            .HasForeignKey(o => o.CustomerId)
            .OnDelete(DeleteBehavior.SetNull);

        builder.HasQueryFilter(o => !o.IsDeleted);
    }
}

public class OrderItemConfiguration : IEntityTypeConfiguration<OrderItem>
{
    public void Configure(EntityTypeBuilder<OrderItem> builder)
    {
        builder.ToTable("order_items");

        builder.HasKey(oi => oi.Id);
        builder.Property(oi => oi.Id).HasColumnName("order_item_id").HasDefaultValueSql("gen_random_uuid()");
        builder.Property(oi => oi.OrderId).HasColumnName("order_id").IsRequired();
        builder.Property(oi => oi.ProductId).HasColumnName("product_id").IsRequired();
        builder.Property(oi => oi.SizeId).HasColumnName("size_id").IsRequired();
        builder.Property(oi => oi.Quantity).HasColumnName("quantity").HasDefaultValue(1);
        builder.Property(oi => oi.UnitPrice).HasColumnName("unit_price").HasPrecision(12, 0).IsRequired();
        builder.Property(oi => oi.SubtotalPrice).HasColumnName("subtotal_price").HasPrecision(12, 0).IsRequired();
        builder.Property(oi => oi.Note).HasColumnName("note").HasMaxLength(255);
        builder.Property(oi => oi.ItemStatus).HasColumnName("item_status").HasMaxLength(50).HasDefaultValue("Pending");
        builder.Property(oi => oi.CreatedAt).HasColumnName("created_at").HasDefaultValueSql("CURRENT_TIMESTAMP");

        builder.Ignore(oi => oi.TotalPrice);
        builder.Ignore(oi => oi.OrderItemModifiers);

        builder.HasIndex(oi => new { oi.OrderId, oi.ItemStatus });

        builder.HasOne(oi => oi.Order)
            .WithMany(o => o.Items)
            .HasForeignKey(oi => oi.OrderId)
            .OnDelete(DeleteBehavior.Cascade);

        builder.HasOne(oi => oi.Product)
            .WithMany(p => p.OrderItems)
            .HasForeignKey(oi => oi.ProductId)
            .OnDelete(DeleteBehavior.Restrict);

        builder.HasOne(oi => oi.ProductSize)
            .WithMany(s => s.OrderItems)
            .HasForeignKey(oi => oi.SizeId)
            .OnDelete(DeleteBehavior.Restrict);

        builder.HasQueryFilter(oi => !oi.IsDeleted);
    }
}

public class OrderItemModifierConfiguration : IEntityTypeConfiguration<OrderItemModifier>
{
    public void Configure(EntityTypeBuilder<OrderItemModifier> builder)
    {
        builder.ToTable("order_item_modifiers");

        builder.HasKey(oim => oim.ItemModId);
        builder.Property(oim => oim.ItemModId).HasColumnName("item_mod_id").HasDefaultValueSql("gen_random_uuid()");
        builder.Property(oim => oim.OrderItemId).HasColumnName("order_item_id").IsRequired();
        builder.Property(oim => oim.ModifierId).HasColumnName("modifier_id").IsRequired();
        builder.Property(oim => oim.Quantity).HasColumnName("quantity").HasDefaultValue(1);
        builder.Property(oim => oim.ExtraPrice).HasColumnName("extra_price").HasPrecision(12, 0).HasDefaultValue(0);
        builder.Property(oim => oim.CreatedAt).HasColumnName("created_at").HasDefaultValueSql("CURRENT_TIMESTAMP");

        builder.HasOne(oim => oim.OrderItem)
            .WithMany(oi => oi.Modifiers)
            .HasForeignKey(oim => oim.OrderItemId)
            .OnDelete(DeleteBehavior.Cascade);

        builder.HasOne(oim => oim.Modifier)
            .WithMany(m => m.OrderItemModifiers)
            .HasForeignKey(oim => oim.ModifierId)
            .OnDelete(DeleteBehavior.Restrict);
    }
}

public class PaymentConfiguration : IEntityTypeConfiguration<Payment>
{
    public void Configure(EntityTypeBuilder<Payment> builder)
    {
        builder.ToTable("payments");

        builder.HasKey(p => p.Id);
        builder.Property(p => p.Id).HasColumnName("payment_id").HasDefaultValueSql("gen_random_uuid()");
        builder.Property(p => p.OrderId).HasColumnName("order_id").IsRequired();
        builder.Property(p => p.PaymentMethod).HasColumnName("payment_method").HasConversion<string>().IsRequired();
        builder.Property(p => p.Amount).HasColumnName("amount").HasPrecision(12, 0).IsRequired();
        builder.Property(p => p.TransactionCode).HasColumnName("transaction_code").HasMaxLength(100);
        builder.HasIndex(p => p.TransactionCode).IsUnique();

        builder.Property(p => p.Status).HasColumnName("status").HasConversion<string>().IsRequired();
        builder.Property(p => p.PayosPaymentLinkId).HasColumnName("payos_payment_link_id").HasMaxLength(100);
        builder.Property(p => p.PaidAt).HasColumnName("paid_at");
        builder.Property(p => p.CreatedAt).HasColumnName("created_at").HasDefaultValueSql("CURRENT_TIMESTAMP");

        builder.HasIndex(p => new { p.OrderId, p.Status });

        builder.HasOne(p => p.Order)
            .WithMany(o => o.Payments)
            .HasForeignKey(p => p.OrderId)
            .OnDelete(DeleteBehavior.Cascade);

        builder.HasQueryFilter(p => !p.IsDeleted);
    }
}

public class PayOSTransactionConfiguration : IEntityTypeConfiguration<PayOSTransaction>
{
    public void Configure(EntityTypeBuilder<PayOSTransaction> builder)
    {
        builder.ToTable("payos_transactions");

        builder.HasKey(pt => pt.Id);
        builder.Property(pt => pt.Id).HasColumnName("id").HasDefaultValueSql("gen_random_uuid()");
        builder.Property(pt => pt.OrderId).HasColumnName("order_id").IsRequired();
        builder.Property(pt => pt.PaymentId).HasColumnName("payment_id");
        builder.Property(pt => pt.PaymentLinkId).HasColumnName("payment_link_id").HasMaxLength(100).IsRequired();
        builder.Property(pt => pt.OrderCode).HasColumnName("order_code").IsRequired();
        builder.Property(pt => pt.Amount).HasColumnName("amount").HasPrecision(12, 0).IsRequired();
        builder.Property(pt => pt.Currency).HasColumnName("currency").HasMaxLength(10).HasDefaultValue("VND");
        builder.Property(pt => pt.Description).HasColumnName("description");
        builder.Property(pt => pt.Status).HasColumnName("status").HasMaxLength(50).HasDefaultValue("PENDING");
        builder.Property(pt => pt.WebhookData).HasColumnName("webhook_data").HasColumnType("text");
        builder.Property(pt => pt.ProcessedAt).HasColumnName("processed_at");
        builder.Property(pt => pt.CreatedAt).HasColumnName("created_at").HasDefaultValueSql("CURRENT_TIMESTAMP");

        builder.HasIndex(pt => pt.PaymentLinkId);
        builder.HasIndex(pt => pt.OrderCode);

        builder.HasOne(pt => pt.Order)
            .WithMany(o => o.PayOSTransactions)
            .HasForeignKey(pt => pt.OrderId)
            .OnDelete(DeleteBehavior.Cascade);

        builder.HasOne(pt => pt.Payment)
            .WithMany()
            .HasForeignKey(pt => pt.PaymentId)
            .OnDelete(DeleteBehavior.SetNull);

        builder.HasQueryFilter(pt => !pt.IsDeleted);
    }
}
