// ============================================================================
// File: src/SmartFB.Domain/ValueObjects/Money.cs
// Project: Smart F&B Operating System (v2.5.0-Production-Ready)
// Description: Immutable Value Object đại diện cho số tiền trong hệ thống.
// Tuân thủ nghiêm ngặt chuẩn tiền tệ VND, không hỗ trợ số âm và đảm bảo an toàn phép tính.
// ============================================================================

namespace SmartFB.Domain.ValueObjects;

public sealed record Money : IComparable<Money>
{
    public decimal Amount { get; }
    public string Currency { get; }

    public static readonly Money Zero = new(0m, "VND");

    private Money(decimal amount, string currency)
    {
        if (amount < 0)
        {
            throw new ArgumentOutOfRangeException(nameof(amount), "Số tiền trong hệ thống F&B không thể là số âm.");
        }

        // Chuẩn hóa làm tròn tiền tệ VND: không có chữ số thập phân
        Amount = decimal.Round(amount, 0, MidpointRounding.AwayFromZero);
        Currency = string.IsNullOrWhiteSpace(currency) ? "VND" : currency.Trim().ToUpperInvariant();

        if (Currency != "VND")
        {
            throw new InvalidOperationException($"Hệ thống Smart F&B OS hiện chỉ hỗ trợ đơn vị tiền tệ VND, không chấp nhận: {currency}");
        }
    }

    public static Money FromVnd(decimal amount) => new(amount, "VND");

    public static Money operator +(Money left, Money right)
    {
        EnsureSameCurrency(left, right);
        return new Money(left.Amount + right.Amount, left.Currency);
    }

    public static Money operator -(Money left, Money right)
    {
        EnsureSameCurrency(left, right);
        if (left.Amount < right.Amount)
        {
            throw new InvalidOperationException($"Không thể trừ số tiền {right.Amount:N0} {right.Currency} từ {left.Amount:N0} {left.Currency} vì kết quả sẽ bị âm.");
        }
        return new Money(left.Amount - right.Amount, left.Currency);
    }

    public static Money operator *(Money money, decimal multiplier)
    {
        if (multiplier < 0)
        {
            throw new ArgumentOutOfRangeException(nameof(multiplier), "Hệ số nhân tiền tệ không thể là số âm.");
        }
        return new Money(money.Amount * multiplier, money.Currency);
    }

    public static Money operator *(decimal multiplier, Money money) => money * multiplier;

    public static bool operator >(Money left, Money right)
    {
        EnsureSameCurrency(left, right);
        return left.Amount > right.Amount;
    }

    public static bool operator <(Money left, Money right)
    {
        EnsureSameCurrency(left, right);
        return left.Amount < right.Amount;
    }

    public static bool operator >=(Money left, Money right)
    {
        EnsureSameCurrency(left, right);
        return left.Amount >= right.Amount;
    }

    public static bool operator <=(Money left, Money right)
    {
        EnsureSameCurrency(left, right);
        return left.Amount <= right.Amount;
    }

    public int CompareTo(Money? other)
    {
        if (other is null) return 1;
        EnsureSameCurrency(this, other);
        return Amount.CompareTo(other.Amount);
    }

    public override string ToString() => $"{Amount:N0} ₫";

    private static void EnsureSameCurrency(Money left, Money right)
    {
        if (left.Currency != right.Currency)
        {
            throw new InvalidOperationException($"Không thể thực hiện phép tính giữa 2 đơn vị tiền tệ khác nhau: {left.Currency} và {right.Currency}");
        }
    }
}
