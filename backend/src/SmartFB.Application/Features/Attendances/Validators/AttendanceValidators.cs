using FluentValidation;
using SmartFB.Application.Features.Attendances.Commands.WifiClockIn;
using SmartFB.Application.Features.Attendances.Commands.WifiClockOut;

namespace SmartFB.Application.Features.Attendances.Validators;

public class WifiClockInCommandValidator : AbstractValidator<WifiClockInCommand>
{
    public WifiClockInCommandValidator()
    {
        RuleFor(x => x.BranchId).NotEmpty().WithMessage("Chi nhánh không được để trống.");
        RuleFor(x => x.EmployeeCode).NotEmpty().WithMessage("Mã nhân viên không được để trống.");
        RuleFor(x => x.ClientIp).NotEmpty().WithMessage("Địa chỉ IP client không được để trống.");
        RuleFor(x => x.ClientBssid).NotEmpty().WithMessage("Địa chỉ BSSID WiFi không được để trống.");
    }
}

public class WifiClockOutCommandValidator : AbstractValidator<WifiClockOutCommand>
{
    public WifiClockOutCommandValidator()
    {
        RuleFor(x => x.AttendanceId).NotEmpty().WithMessage("ID lượt chấm công không hợp lệ.");
    }
}
