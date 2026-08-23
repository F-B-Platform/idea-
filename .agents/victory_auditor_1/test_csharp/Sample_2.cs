// ============================================================================
// File: src/SmartFB.Domain/Entities/Order.cs
// Project: Smart F&B Operating System (v2.5.0-Production-Ready)
// Description: Entity gốc (Aggregate Root) quản lý toàn bộ vòng đời đơn hàng.
// Đóng gói 100% logic nghiệp vụ 3 kênh: DineIn (2 nhánh), Delivery (20k ship), TakeAway.
// ============================================================================

using SmartFB.Domain.Common;
using SmartFB.Domain.Enums;
using SmartFB.Domain.Events;
using SmartFB.Domain.Exceptions;
using SmartFB.Domain.ValueObjects;

namespace SmartFB.Domain.Entities;

public sealed class Order : BaseAuditableEntity
{
    public Guid BranchId { get; private set; }
    public Guid? TableId { get; private set; }
    public Guid? CustomerId { get; private set; }
    public string OrderCode { get; private set; }
    public OrderChannel Channel { get; private set; }
    public OrderStatus Status { get; private set; }
    public PaymentMethod PaymentMethod { get; private set; }
    public PaymentStatus PaymentStatus { get; private set; }
    public Money SubTotal { get; private set; }
    public Money ShippingFee { get; private set; }
    public Money DiscountAmount { get; private set; }
    public Money TotalAmount { get; private set; }
    public string? CustomerPhone { get; private set; }
    public string? DeliveryAddress { get; private set; }
    public string? Note { get; private set; }
    public DateTime CreatedAtUtc { get; private set; }
    public DateTime? PaidAtUtc { get; private set; }
    public DateTime? CompletedAtUtc { get; private set; }
    public DateTime? CancelledAtUtc { get; private set; }
    public string? CancelReason { get; private set; }

    private readonly List<OrderItem> _items = new();
    public IReadOnlyCollection<OrderItem> Items => _items.AsReadOnly();

    private Order() // Bắt buộc cho EF Core ORM Mapping
    {
        OrderCode = string.Empty;
        SubTotal = Money.Zero;
        ShippingFee = Money.Zero;
        DiscountAmount = Money.Zero;
        TotalAmount = Money.Zero;
    }

    /// <summary>
    /// Khởi tạo đơn dùng tại bàn (Dine-In)
    /// Nhánh A (VietQR): Trạng thái PendingPayment, đợi Webhook xác nhận mới vào Bếp.
    /// Nhánh B (Tiền mặt): Trạng thái Confirmed, vào Bếp ngay lập tức.
    /// </summary>
    public static Order CreateDineInOrder(
        Guid branchId,
        Guid tableId,
        string orderCode,
        PaymentMethod paymentMethod,
        string? note,
        DateTime utcNow)
    {
        if (branchId == Guid.Empty) throw new DomainException("Chi nhánh (BranchId) không được để trống.");
        if (tableId == Guid.Empty) throw new DomainException("Mã bàn (TableId) bắt buộc đối với đơn phục vụ tại chỗ.");
        if (string.IsNullOrWhiteSpace(orderCode)) throw new DomainException("Mã đơn hàng (OrderCode) không hợp lệ.");

        var order = new Order
        {
            Id = Guid.NewGuid(),
            BranchId = branchId,
            TableId = tableId,
            OrderCode = orderCode,
            Channel = OrderChannel.DineIn,
            PaymentMethod = paymentMethod,
            Status = paymentMethod == PaymentMethod.VietQr ? OrderStatus.PendingPayment : OrderStatus.Confirmed,
            PaymentStatus = PaymentStatus.Unpaid,
            SubTotal = Money.Zero,
            ShippingFee = Money.Zero,
            DiscountAmount = Money.Zero,
            TotalAmount = Money.Zero,
            Note = note?.Trim(),
            CreatedAtUtc = utcNow
        };

        order.AddDomainEvent(new OrderCreatedDomainEvent(order.Id, order.OrderCode, order.BranchId, order.Channel, order.Status));
        return order;
    }

    /// <summary>
    /// Khởi tạo đơn giao hàng tận nơi (Delivery) - Phí vận chuyển cố định 20.000 VNĐ
    /// </summary>
    public static Order CreateDeliveryOrder(
        Guid branchId,
        string customerPhone,
        string deliveryAddress,
        string orderCode,
        PaymentMethod paymentMethod,
        string? note,
        DateTime utcNow)
    {
        if (branchId == Guid.Empty) throw new DomainException("Chi nhánh (BranchId) không được để trống.");
        if (string.IsNullOrWhiteSpace(customerPhone)) throw new DomainException("Số điện thoại khách hàng là bắt buộc đối với đơn Delivery.");
        if (string.IsNullOrWhiteSpace(deliveryAddress)) throw new DomainException("Địa chỉ nhận hàng là bắt buộc đối với đơn Delivery.");

        var order = new Order
        {
            Id = Guid.NewGuid(),
            BranchId = branchId,
            TableId = null,
            CustomerPhone = customerPhone.Trim(),
            DeliveryAddress = deliveryAddress.Trim(),
            OrderCode = orderCode,
            Channel = OrderChannel.Delivery,
            PaymentMethod = paymentMethod,
            Status = paymentMethod == PaymentMethod.VietQr ? OrderStatus.PendingPayment : OrderStatus.Confirmed,
            PaymentStatus = PaymentStatus.Unpaid,
            SubTotal = Money.Zero,
            ShippingFee = Money.FromVnd(20000m), // Cố định 20.000 VNĐ theo spec v2.5.0
            DiscountAmount = Money.Zero,
            TotalAmount = Money.FromVnd(20000m),
            Note = note?.Trim(),
            CreatedAtUtc = utcNow
        };

        order.AddDomainEvent(new OrderCreatedDomainEvent(order.Id, order.OrderCode, order.BranchId, order.Channel, order.Status));
        return order;
    }

    public void AddItem(
        Guid menuItemId,
        Guid itemSizeId,
        string itemName,
        string sizeName,
        decimal unitPrice,
        int quantity,
        string? note,
        IReadOnlyList<OrderItemTopping>? toppings = null)
    {
        if (Status != OrderStatus.PendingPayment && Status != OrderStatus.Confirmed)
        {
            throw new DomainException($"Không thể thêm món vào đơn hàng đang ở trạng thái {Status}.");
        }

        if (quantity <= 0 || quantity > 50)
        {
            throw new DomainException("Số lượng từng món phải từ 1 đến tối đa 50 phần.");
        }

        var orderItem = new OrderItem(
            Id,
            menuItemId,
            itemSizeId,
            itemName,
            sizeName,
            unitPrice,
            quantity,
            note,
            toppings
        );

        _items.Add(orderItem);
        RecalculateTotals();
    }

    public void ApplyDiscount(Money discount)
    {
        if (discount > SubTotal)
        {
            throw new DomainException($"Số tiền giảm giá ({discount}) không thể vượt quá tổng tiền món ({SubTotal}).");
        }

        DiscountAmount = discount;
        RecalculateTotals();
    }

    public void MarkAsPaid(DateTime paidAtUtc)
    {
        if (PaymentStatus == PaymentStatus.Paid)
        {
            return; // Đảm bảo tính Idempotent nếu Webhook gọi lại
        }

        PaymentStatus = PaymentStatus.Paid;
        PaidAtUtc = paidAtUtc;

        if (Status == OrderStatus.PendingPayment)
        {
            Status = OrderStatus.Confirmed;
        }

        AddDomainEvent(new OrderPaidDomainEvent(Id, OrderCode, BranchId, TotalAmount.Amount, Channel));
    }

    public void CancelOrder(string reason, DateTime cancelledAtUtc)
    {
        if (Status == OrderStatus.Completed)
        {
            throw new DomainException("Không thể hủy đơn hàng đã hoàn tất phục vụ.");
        }

        if (Status == OrderStatus.Cancelled)
        {
            return;
        }

        Status = OrderStatus.Cancelled;
        CancelledAtUtc = cancelledAtUtc;
        CancelReason = string.IsNullOrWhiteSpace(reason) ? "Hủy theo yêu cầu khách hàng" : reason.Trim();

        AddDomainEvent(new OrderCancelledDomainEvent(Id, OrderCode, BranchId, CancelReason));
    }

    private void RecalculateTotals()
    {
        decimal itemsTotal = _items.Sum(item => item.TotalPrice.Amount);
        SubTotal = Money.FromVnd(itemsTotal);
        TotalAmount = Money.FromVnd(itemsTotal + ShippingFee.Amount - DiscountAmount.Amount);
    }
}

public sealed class OrderItem : BaseEntity
{
    public Guid OrderId { get; private set; }
    public Guid MenuItemId { get; private set; }
    public Guid ItemSizeId { get; private set; }
    public string ItemName { get; private set; }
    public string SizeName { get; private set; }
    public Money UnitPrice { get; private set; }
    public int Quantity { get; private set; }
    public Money TotalPrice { get; private set; }
    public string? Note { get; private set; }

    private readonly List<OrderItemTopping> _toppings = new();
    public IReadOnlyCollection<OrderItemTopping> Toppings => _toppings.AsReadOnly();

    private OrderItem()
    {
        ItemName = string.Empty;
        SizeName = string.Empty;
        UnitPrice = Money.Zero;
        TotalPrice = Money.Zero;
    }

    public OrderItem(
        Guid orderId,
        Guid menuItemId,
        Guid itemSizeId,
        string itemName,
        string sizeName,
        decimal unitPrice,
        int quantity,
        string? note,
        IReadOnlyList<OrderItemTopping>? toppings)
    {
        Id = Guid.NewGuid();
        OrderId = orderId;
        MenuItemId = menuItemId;
        ItemSizeId = itemSizeId;
        ItemName = itemName.Trim();
        SizeName = sizeName.Trim();
        UnitPrice = Money.FromVnd(unitPrice);
        Quantity = quantity;
        Note = note?.Trim();

        if (toppings != null && toppings.Count > 0)
        {
            _toppings.AddRange(toppings);
        }

        decimal toppingsUnitSum = _toppings.Sum(t => t.Price.Amount);
        TotalPrice = Money.FromVnd((unitPrice + toppingsUnitSum) * quantity);
    }
}

public sealed class OrderItemTopping : BaseEntity
{
    public Guid OrderItemId { get; private set; }
    public Guid ToppingId { get; private set; }
    public string ToppingName { get; private set; }
    public Money Price { get; private set; }

    private OrderItemTopping()
    {
        ToppingName = string.Empty;
        Price = Money.Zero;
    }

    public OrderItemTopping(Guid toppingId, string toppingName, decimal price)
    {
        Id = Guid.NewGuid();
        ToppingId = toppingId;
        ToppingName = toppingName.Trim();
        Price = Money.FromVnd(price);
    }
}