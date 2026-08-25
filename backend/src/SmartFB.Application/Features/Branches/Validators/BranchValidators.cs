using FluentValidation;
using SmartFB.Application.Features.Branches.Commands.ConfigureBranchWifi;
using SmartFB.Application.Features.Branches.Commands.CreateBranch;

namespace SmartFB.Application.Features.Branches.Validators;

public class CreateBranchCommandValidator : AbstractValidator<CreateBranchCommand>
{
    public CreateBranchCommandValidator()
    {
        RuleFor(x => x.Code)
            .NotEmpty().WithMessage("Mã chi nhánh không được để trống.")
            .MaximumLength(50).WithMessage("Mã chi nhánh không quá 50 ký tự.");

        RuleFor(x => x.Name)
            .NotEmpty().WithMessage("Tên chi nhánh không được để trống.")
            .MaximumLength(150).WithMessage("Tên chi nhánh không quá 150 ký tự.");

        RuleFor(x => x.Address)
            .NotEmpty().WithMessage("Địa chỉ chi nhánh không được để trống.");
    }
}

public class ConfigureBranchWifiCommandValidator : AbstractValidator<ConfigureBranchWifiCommand>
{
    public ConfigureBranchWifiCommandValidator()
    {
        RuleFor(x => x.BranchId)
            .NotEmpty().WithMessage("ID chi nhánh không hợp lệ.");

        RuleFor(x => x.SsidName)
            .NotEmpty().WithMessage("Tên SSID WiFi không được để trống.");

        RuleFor(x => x.BssidList)
            .NotEmpty().WithMessage("Danh sách MAC BSSID không được để trống.");

        RuleFor(x => x.AllowedIpSubnets)
            .NotEmpty().WithMessage("Dải IP Subnet không được để trống.");
    }
}
