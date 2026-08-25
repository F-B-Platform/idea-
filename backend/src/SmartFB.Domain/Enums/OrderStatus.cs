namespace SmartFB.Domain.Enums;

public enum OrderStatus
{
    PendingPayment = 1,
    Paid = 2,
    Confirmed = 3,
    Preparing = 4,
    Ready = 5,
    Served = 6,
    Completed = 7,
    Cancelled = 8
}
