using System;
using System.Collections.Generic;

namespace SmartFB.Domain.Common
{
    public abstract class BaseEntity
    {
        public Guid Id { get; set; } = Guid.NewGuid();
    }

    public abstract class BaseAuditableEntity : BaseEntity
    {
        public string? CreatedBy { get; set; }
        public DateTime? LastModifiedAtUtc { get; set; }
        public string? LastModifiedBy { get; set; }
        
        private readonly List<object> _domainEvents = new();
        public IReadOnlyCollection<object> DomainEvents => _domainEvents.AsReadOnly();
        public void AddDomainEvent(object domainEvent) => _domainEvents.Add(domainEvent);
        public void ClearDomainEvents() => _domainEvents.Clear();
    }
}

namespace SmartFB.Domain.Enums
{
    public enum OrderChannel { DineIn, Takeaway, Delivery }
    public enum OrderStatus { PendingPayment, Confirmed, Preparing, Ready, Delivering, Completed, Cancelled }
    public enum PaymentMethod { VietQr, Cash }
    public enum PaymentStatus { Unpaid, Pending, Paid, Failed, Refunded }
}

namespace SmartFB.Domain.Events
{
    public record OrderCreatedDomainEvent(Guid OrderId, string OrderCode, Guid BranchId, Enums.OrderChannel Channel, Enums.OrderStatus Status);
    public record OrderPaidDomainEvent(Guid OrderId, string OrderCode, Guid BranchId, decimal Amount, Enums.OrderChannel Channel);
    public record OrderCancelledDomainEvent(Guid OrderId, string OrderCode, Guid BranchId, string CancelReason);
}

namespace SmartFB.Domain.Exceptions
{
    public class DomainException : Exception
    {
        public DomainException(string message) : base(message) { }
    }
}
