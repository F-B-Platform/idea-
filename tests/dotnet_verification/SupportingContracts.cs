using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Logging;
using SmartFB.Domain.Entities;
using SmartFB.Domain.Enums;
using SmartFB.Domain.ValueObjects;

namespace SmartFB.Domain.Common
{
    public interface IDomainEvent { }

    public abstract class BaseEntity
    {
        public Guid Id { get; protected set; }
        private readonly List<IDomainEvent> _domainEvents = new();
        public IReadOnlyCollection<IDomainEvent> DomainEvents => _domainEvents.AsReadOnly();
        public void AddDomainEvent(IDomainEvent domainEvent) => _domainEvents.Add(domainEvent);
        public void ClearDomainEvents() => _domainEvents.Clear();
    }

    public abstract class BaseAuditableEntity : BaseEntity
    {
        public string? CreatedBy { get; set; }
        public DateTime? LastModifiedAtUtc { get; set; }
        public string? LastModifiedBy { get; set; }
    }
}

namespace SmartFB.Domain.Enums
{
    public enum OrderChannel { DineIn, TakeAway, Delivery }
    public enum OrderStatus { PendingPayment, Confirmed, Preparing, Ready, Served, Completed, Cancelled }
    public enum PaymentMethod { Cash, VietQr, CreditCard, InternalWallet }
    public enum PaymentStatus { Unpaid, Pending, Paid, Failed, Refunded }
}

namespace SmartFB.Domain.Events
{
    using SmartFB.Domain.Common;
    using SmartFB.Domain.Enums;
    public sealed record OrderCreatedDomainEvent(Guid OrderId, string OrderCode, Guid BranchId, OrderChannel Channel, OrderStatus Status) : IDomainEvent;
    public sealed record OrderPaidDomainEvent(Guid OrderId, string OrderCode, Guid BranchId, decimal TotalAmount, OrderChannel Channel) : IDomainEvent;
    public sealed record OrderCancelledDomainEvent(Guid OrderId, string OrderCode, Guid BranchId, string CancelReason) : IDomainEvent;
    public sealed record OrderStatusChangedDomainEvent(Guid OrderId, OrderStatus OldStatus, OrderStatus NewStatus) : IDomainEvent;
}

namespace SmartFB.Domain.Exceptions
{
    public class DomainException : Exception
    {
        public DomainException(string message) : base(message) { }
    }
}

namespace SmartFB.Application.Common.Models
{
    public class Result<T>
    {
        public bool IsSuccess { get; }
        public T? Value { get; }
        public string? Error { get; }
        protected Result(bool isSuccess, T? value, string? error)
        {
            IsSuccess = isSuccess;
            Value = value;
            Error = error;
        }
        public static Result<T> Success(T value) => new(true, value, null);
        public static Result<T> Failure(string error) => new(false, default, error);
    }
}

namespace SmartFB.Application.Common.Interfaces
{
    public class TableEntity
    {
        public Guid Id { get; set; }
        public Guid BranchId { get; set; }
        public bool IsActive { get; set; }
    }

    public class MenuItemEntity
    {
        public Guid Id { get; set; }
        public string Name { get; set; } = string.Empty;
        public bool IsActive { get; set; }
    }

    public class ItemSizeEntity
    {
        public Guid Id { get; set; }
        public Guid MenuItemId { get; set; }
        public string Name { get; set; } = string.Empty;
        public decimal Price { get; set; }
    }

    public interface IAppDbContext
    {
        DbSet<TableEntity> Tables { get; }
        DbSet<MenuItemEntity> MenuItems { get; }
        DbSet<ItemSizeEntity> ItemSizes { get; }
        DbSet<Order> Orders { get; }
        Task<int> SaveChangesAsync(CancellationToken cancellationToken = default);
    }

    public record PaymentLinkResult(bool IsSuccess, string? QrCodeUrl, string? ErrorMessage);

    public interface IPaymentService
    {
        Task<PaymentLinkResult> CreateVietQrPaymentLinkAsync(Guid orderId, string orderCode, decimal amount, CancellationToken cancellationToken = default);
    }

    public interface IKitchenRealtimeNotifier
    {
        Task BroadcastNewTicketAsync(Guid branchId, Guid orderId, CancellationToken cancellationToken = default);
    }

    public interface IDateTimeProvider
    {
        DateTime UtcNow { get; }
    }
}
