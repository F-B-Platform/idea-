namespace SmartFB.Application.Common.Interfaces;

public interface IDateTimeService
{
    DateTime UtcNow { get; }
    DateTime VietnamNow { get; }
}
