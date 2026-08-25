using Moq;
using SmartFB.Application.Common.Interfaces;

namespace SmartFB.UnitTests.Common;

public abstract class TestBase
{
    protected readonly Mock<IApplicationDbContext> MockDbContext;
    protected readonly Mock<IDateTimeService> MockDateTimeService;
    protected readonly Mock<IRedisCacheService> MockRedisCacheService;

    protected TestBase()
    {
        MockDbContext = new Mock<IApplicationDbContext>();
        MockDateTimeService = new Mock<IDateTimeService>();
        MockRedisCacheService = new Mock<IRedisCacheService>();

        var fixedUtc = new DateTime(2026, 8, 25, 8, 0, 0, DateTimeKind.Utc);
        MockDateTimeService.Setup(d => d.UtcNow).Returns(fixedUtc);
        MockDateTimeService.Setup(d => d.VietnamNow).Returns(fixedUtc.AddHours(7));
    }
}
