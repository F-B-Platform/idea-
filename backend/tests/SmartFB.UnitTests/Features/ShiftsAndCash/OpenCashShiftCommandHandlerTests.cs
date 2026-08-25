using FluentAssertions;
using FluentValidation.Results;
using SmartFB.Application.Common.Exceptions;
using SmartFB.Application.Common.Models;
using SmartFB.UnitTests.Common;
using Xunit;

namespace SmartFB.UnitTests.Features.ShiftsAndCash;

public record OpenCashShiftCommand(Guid BranchId, Guid StaffId, decimal InitialCash);
public record OpenShiftResultDto(Guid ShiftId, Guid BranchId, decimal InitialCash, DateTime OpenedAt);

public class OpenCashShiftCommandHandler
{
    public Task<ApiResponse<OpenShiftResultDto>> Handle(OpenCashShiftCommand command, CancellationToken cancellationToken = default)
    {
        if (command.InitialCash < 0)
        {
            throw new ValidationException(new List<ValidationFailure>
            {
                new("InitialCash", "Tiền đầu ca không thể là số âm.")
            });
        }

        var shiftId = Guid.NewGuid();
        var result = new OpenShiftResultDto(shiftId, command.BranchId, command.InitialCash, DateTime.UtcNow);
        return Task.FromResult(ApiResponse<OpenShiftResultDto>.SuccessResult(result, "Mở ca két tiền thành công."));
    }
}

public class OpenCashShiftCommandHandlerTests : TestBase
{
    private readonly OpenCashShiftCommandHandler _handler;

    public OpenCashShiftCommandHandlerTests()
    {
        _handler = new OpenCashShiftCommandHandler();
    }

    [Fact]
    public async Task Handle_ValidInitialCash_ShouldOpenShiftSuccessfully()
    {
        // Arrange
        var branchId = Guid.NewGuid();
        var staffId = Guid.NewGuid();
        var command = new OpenCashShiftCommand(branchId, staffId, 1500000m);

        // Act
        var result = await _handler.Handle(command);

        // Assert
        result.Should().NotBeNull();
        result.Success.Should().BeTrue();
        result.Data!.InitialCash.Should().Be(1500000m);
    }

    [Fact]
    public async Task Handle_NegativeCash_ShouldThrowValidationException()
    {
        // Arrange
        var command = new OpenCashShiftCommand(Guid.NewGuid(), Guid.NewGuid(), -50000m);

        // Act & Assert
        var act = () => _handler.Handle(command);
        await act.Should().ThrowAsync<ValidationException>();
    }
}
