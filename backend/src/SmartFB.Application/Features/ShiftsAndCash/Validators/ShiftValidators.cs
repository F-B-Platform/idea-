using FluentValidation;
using SmartFB.Application.Features.ShiftsAndCash.Commands.CloseCashShift;
using SmartFB.Application.Features.ShiftsAndCash.Commands.OpenCashShift;

namespace SmartFB.Application.Features.ShiftsAndCash.Validators;

public class OpenCashShiftCommandValidator : AbstractValidator<OpenCashShiftCommand>
{
    public OpenCashShiftCommandValidator()
    {
        RuleFor(x => x.BranchId).NotEmpty().WithMessage("Chi nhánh không được để trống.");
        RuleFor(x => x.CashierId).NotEmpty().WithMessage("Thu ngân không được để trống.");
        RuleFor(x => x.InitialCash).GreaterThanOrEqualTo(0).WithMessage("Số tiền lẻ bàn giao đầu ca không được âm.");
    }
}

public class CloseCashShiftCommandValidator : AbstractValidator<CloseCashShiftCommand>
{
    public CloseCashShiftCommandValidator()
    {
        RuleFor(x => x.ShiftId).NotEmpty().WithMessage("ID ca làm việc không hợp lệ.");
        RuleFor(x => x.ActualCashCounted).GreaterThanOrEqualTo(0).WithMessage("Số tiền mặt kiểm đếm không được âm.");
    }
}
