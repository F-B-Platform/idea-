using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using SmartFB.Domain.Entities;

namespace SmartFB.Infrastructure.Persistence.Configurations;

public class CustomerReviewConfiguration : IEntityTypeConfiguration<CustomerReview>
{
    public void Configure(EntityTypeBuilder<CustomerReview> builder)
    {
        builder.ToTable("customer_reviews");

        builder.HasKey(r => r.Id);
        builder.Property(r => r.Id).HasColumnName("review_id").HasDefaultValueSql("gen_random_uuid()");
        builder.Property(r => r.OrderId).HasColumnName("order_id").IsRequired();
        builder.Property(r => r.ProductId).HasColumnName("product_id");
        builder.Property(r => r.CustomerId).HasColumnName("customer_id");
        builder.Property(r => r.RatingStars).HasColumnName("rating_stars").IsRequired();
        builder.Property(r => r.Comment).HasColumnName("comment");
        builder.Property(r => r.PhotoUrls).HasColumnName("photo_urls").HasColumnType("jsonb");
        builder.Property(r => r.IsAnonymous).HasColumnName("is_anonymous").HasDefaultValue(false);
        builder.Property(r => r.IsApproved).HasColumnName("is_approved").HasDefaultValue(false);
        builder.Property(r => r.IsUrgentAlert).HasColumnName("is_urgent_alert").HasDefaultValue(false);
        builder.Property(r => r.CreatedAt).HasColumnName("created_at").HasDefaultValueSql("CURRENT_TIMESTAMP");

        builder.HasIndex(r => r.OrderId);
        builder.HasIndex(r => r.RatingStars);

        builder.HasOne(r => r.Order)
            .WithMany(o => o.CustomerReviews)
            .HasForeignKey(r => r.OrderId)
            .OnDelete(DeleteBehavior.Restrict);

        builder.HasOne(r => r.Product)
            .WithMany(p => p.CustomerReviews)
            .HasForeignKey(r => r.ProductId)
            .OnDelete(DeleteBehavior.SetNull);

        builder.HasOne(r => r.Customer)
            .WithMany(c => c.CustomerReviews)
            .HasForeignKey(r => r.CustomerId)
            .OnDelete(DeleteBehavior.SetNull);

        builder.HasQueryFilter(r => !r.IsDeleted);
    }
}

public class ReviewImageConfiguration : IEntityTypeConfiguration<ReviewImage>
{
    public void Configure(EntityTypeBuilder<ReviewImage> builder)
    {
        builder.ToTable("review_images");

        builder.HasKey(ri => ri.Id);
        builder.Property(ri => ri.Id).HasColumnName("image_id").HasDefaultValueSql("gen_random_uuid()");
        builder.Property(ri => ri.ReviewId).HasColumnName("review_id").IsRequired();
        builder.Property(ri => ri.ImageUrl).HasColumnName("image_url").HasMaxLength(500).IsRequired();
        builder.Property(ri => ri.IsApproved).HasColumnName("is_approved").HasDefaultValue(false);
        builder.Property(ri => ri.CreatedAt).HasColumnName("created_at").HasDefaultValueSql("CURRENT_TIMESTAMP");

        builder.HasOne(ri => ri.Review)
            .WithMany(r => r.ReviewImages)
            .HasForeignKey(ri => ri.ReviewId)
            .OnDelete(DeleteBehavior.Cascade);

        builder.HasQueryFilter(ri => !ri.IsDeleted);
    }
}

public class ShiftConfiguration : IEntityTypeConfiguration<Shift>
{
    public void Configure(EntityTypeBuilder<Shift> builder)
    {
        builder.ToTable("shifts");

        builder.HasKey(s => s.Id);
        builder.Property(s => s.Id).HasColumnName("shift_id").HasDefaultValueSql("gen_random_uuid()");
        builder.Property(s => s.BranchId).HasColumnName("branch_id").IsRequired();
        builder.Property(s => s.CashierId).HasColumnName("cashier_id").IsRequired();
        builder.Property(s => s.OpeningTime).HasColumnName("opening_time").HasDefaultValueSql("CURRENT_TIMESTAMP");
        builder.Property(s => s.ClosingTime).HasColumnName("closing_time");
        builder.Property(s => s.InitialCash).HasColumnName("initial_cash").HasPrecision(12, 0).IsRequired();
        builder.Property(s => s.ActualCashCounted).HasColumnName("actual_cash_counted").HasPrecision(12, 0);
        builder.Property(s => s.SystemCashCalculated).HasColumnName("system_cash_calculated").HasPrecision(12, 0).HasDefaultValue(0);
        builder.Property(s => s.CashDifference).HasColumnName("cash_difference").HasPrecision(12, 0).HasDefaultValue(0);
        builder.Property(s => s.ShiftNotes).HasColumnName("shift_notes");
        builder.Property(s => s.Status).HasColumnName("status").HasConversion<string>().IsRequired();
        builder.Property(s => s.CreatedAt).HasColumnName("created_at").HasDefaultValueSql("CURRENT_TIMESTAMP");

        builder.HasIndex(s => new { s.BranchId, s.Status, s.OpeningTime });

        builder.HasOne(s => s.Branch)
            .WithMany(b => b.Shifts)
            .HasForeignKey(s => s.BranchId)
            .OnDelete(DeleteBehavior.Restrict);

        builder.HasOne(s => s.Cashier)
            .WithMany(u => u.Shifts)
            .HasForeignKey(s => s.CashierId)
            .OnDelete(DeleteBehavior.Restrict);

        builder.HasQueryFilter(s => !s.IsDeleted);
    }
}

public class ZReportConfiguration : IEntityTypeConfiguration<ZReport>
{
    public void Configure(EntityTypeBuilder<ZReport> builder)
    {
        builder.ToTable("z_reports");

        builder.HasKey(z => z.Id);
        builder.Property(z => z.Id).HasColumnName("report_id").HasDefaultValueSql("gen_random_uuid()");
        builder.Property(z => z.ShiftId).HasColumnName("shift_id").IsRequired();
        builder.Property(z => z.BranchId).HasColumnName("branch_id").IsRequired();
        builder.Property(z => z.ReportDate).HasColumnName("report_date").HasDefaultValueSql("CURRENT_TIMESTAMP");
        builder.Property(z => z.TotalOrders).HasColumnName("total_orders").HasDefaultValue(0);
        builder.Property(z => z.TotalGrossSales).HasColumnName("total_gross_sales").HasPrecision(12, 0).HasDefaultValue(0);
        builder.Property(z => z.TotalDiscounts).HasColumnName("total_discounts").HasPrecision(12, 0).HasDefaultValue(0);
        builder.Property(z => z.TotalNetSales).HasColumnName("total_net_sales").HasPrecision(12, 0).HasDefaultValue(0);
        builder.Property(z => z.TotalCashPayments).HasColumnName("total_cash_payments").HasPrecision(12, 0).HasDefaultValue(0);
        builder.Property(z => z.TotalVietQrPayments).HasColumnName("total_vietqr_payments").HasPrecision(12, 0).HasDefaultValue(0);
        builder.Property(z => z.SystemCash).HasColumnName("system_cash").HasPrecision(12, 0).HasDefaultValue(0);
        builder.Property(z => z.ActualCash).HasColumnName("actual_cash").HasPrecision(12, 0).HasDefaultValue(0);
        builder.Property(z => z.VarianceAmount).HasColumnName("variance_amount").HasPrecision(12, 0).HasDefaultValue(0);
        builder.Property(z => z.VarianceReason).HasColumnName("variance_reason");
        builder.Property(z => z.GeneratedByUserId).HasColumnName("generated_by_user_id").IsRequired();
        builder.Property(z => z.CreatedAt).HasColumnName("created_at").HasDefaultValueSql("CURRENT_TIMESTAMP");

        builder.HasOne(z => z.Shift)
            .WithOne(s => s.ZReport)
            .HasForeignKey<ZReport>(z => z.ShiftId)
            .OnDelete(DeleteBehavior.Cascade);

        builder.HasOne(z => z.Branch)
            .WithMany()
            .HasForeignKey(z => z.BranchId)
            .OnDelete(DeleteBehavior.Restrict);

        builder.HasOne(z => z.GeneratedByUser)
            .WithMany()
            .HasForeignKey(z => z.GeneratedByUserId)
            .OnDelete(DeleteBehavior.Restrict);

        builder.HasQueryFilter(z => !z.IsDeleted);
    }
}

public class AttendanceConfiguration : IEntityTypeConfiguration<Attendance>
{
    public void Configure(EntityTypeBuilder<Attendance> builder)
    {
        builder.ToTable("attendances");

        builder.HasKey(a => a.Id);
        builder.Property(a => a.Id).HasColumnName("attendance_id").HasDefaultValueSql("gen_random_uuid()");
        builder.Property(a => a.BranchId).HasColumnName("branch_id").IsRequired();
        builder.Property(a => a.UserId).HasColumnName("user_id").IsRequired();
        builder.Property(a => a.EmployeeCode).HasColumnName("employee_code").HasMaxLength(50).IsRequired();
        builder.Property(a => a.CheckInTime).HasColumnName("check_in_time").HasDefaultValueSql("CURRENT_TIMESTAMP");
        builder.Property(a => a.CheckOutTime).HasColumnName("check_out_time");
        builder.Property(a => a.VerifiedIp).HasColumnName("verified_ip").HasMaxLength(50).IsRequired();
        builder.Property(a => a.VerifiedBssid).HasColumnName("verified_bssid").HasMaxLength(50).IsRequired();
        builder.Property(a => a.Status).HasColumnName("status").HasConversion<string>().IsRequired();
        builder.Property(a => a.CreatedAt).HasColumnName("created_at").HasDefaultValueSql("CURRENT_TIMESTAMP");

        builder.HasIndex(a => new { a.BranchId, a.UserId, a.CheckInTime });

        builder.HasOne(a => a.Branch)
            .WithMany(b => b.Attendances)
            .HasForeignKey(a => a.BranchId)
            .OnDelete(DeleteBehavior.Restrict);

        builder.HasOne(a => a.User)
            .WithMany(u => u.Attendances)
            .HasForeignKey(a => a.UserId)
            .OnDelete(DeleteBehavior.Cascade);

        builder.HasQueryFilter(a => !a.IsDeleted);
    }
}
