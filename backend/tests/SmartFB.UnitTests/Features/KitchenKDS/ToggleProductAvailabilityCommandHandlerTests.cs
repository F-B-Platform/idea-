using FluentAssertions;
using Moq;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Domain.Entities;
using SmartFB.UnitTests.Common;
using Xunit;

namespace SmartFB.UnitTests.Features.KitchenKDS;

public record ToggleProductAvailabilityCommand(Guid BranchId, Guid ProductId, bool IsAvailable);

public class ToggleProductAvailabilityCommandHandler
{
    private readonly IApplicationDbContext _context;
    private readonly IRedisCacheService _redisCache;

    public ToggleProductAvailabilityCommandHandler(IApplicationDbContext context, IRedisCacheService redisCache)
    {
        _context = context;
        _redisCache = redisCache;
    }

    public async Task<ApiResponse<object>> Handle(
        ToggleProductAvailabilityCommand command, CancellationToken cancellationToken = default)
    {
        var product = _context.Products.FirstOrDefault(p => p.Id == command.ProductId);
        if (product == null)
        {
            throw new NotFoundException(nameof(Product), command.ProductId);
        }

        product.IsAvailable = command.IsAvailable;
        await _context.SaveChangesAsync(cancellationToken);

        // Invalidate menu cache for branch
        await _redisCache.RemoveAsync($"menu:branch:{command.BranchId}", cancellationToken);

        string actionText = command.IsAvailable ? "Mở bán lại" : "Khóa hết món (86-out)";
        return ApiResponse<object>.SuccessResult(new
        {
            ProductId = product.Id,
            IsAvailable = product.IsAvailable
        }, $"{actionText} thành công trên toàn hệ thống.");
    }
}

public class ToggleProductAvailabilityCommandHandlerTests : TestBase
{
    private readonly List<Product> _products;
    private readonly ToggleProductAvailabilityCommandHandler _handler;

    public ToggleProductAvailabilityCommandHandlerTests()
    {
        _products = new List<Product>();
        var mockProducts = MockDbSetHelper.CreateMockDbSet(_products);
        MockDbContext.Setup(c => c.Products).Returns(mockProducts.Object);
        MockDbContext.Setup(c => c.SaveChangesAsync(It.IsAny<CancellationToken>())).ReturnsAsync(1);

        MockRedisCacheService.Setup(r => r.RemoveAsync(It.IsAny<string>(), It.IsAny<CancellationToken>()))
            .Returns(Task.CompletedTask);

        _handler = new ToggleProductAvailabilityCommandHandler(MockDbContext.Object, MockRedisCacheService.Object);
    }

    [Fact]
    public async Task Handle_ToggleOutOfStock_ShouldSetIsAvailableFalseAndEvictCache()
    {
        // Arrange
        var branchId = Guid.NewGuid();
        var productId = Guid.NewGuid();
        var product = new Product
        {
            Id = productId,
            Name = "Tra Dao Cam Sa",
            IsAvailable = true
        };
        _products.Add(product);

        var command = new ToggleProductAvailabilityCommand(branchId, productId, false);

        // Act
        var result = await _handler.Handle(command);

        // Assert
        result.Should().NotBeNull();
        result.Success.Should().BeTrue();
        product.IsAvailable.Should().BeFalse();

        MockDbContext.Verify(c => c.SaveChangesAsync(It.IsAny<CancellationToken>()), Times.Once);
        MockRedisCacheService.Verify(r => r.RemoveAsync($"menu:branch:{branchId}", It.IsAny<CancellationToken>()), Times.Once);
    }
}
