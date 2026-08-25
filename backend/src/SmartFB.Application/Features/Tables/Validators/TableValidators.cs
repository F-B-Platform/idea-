using FluentValidation;
using SmartFB.Application.Features.Tables.Commands.CreateTable;
using SmartFB.Application.Features.Tables.Commands.UpdateTableStatus;

namespace SmartFB.Application.Features.Tables.Validators;

public class CreateTableCommandValidator : AbstractValidator<CreateTableCommand>
{
    public CreateTableCommandValidator()
    {
        RuleFor(x => x.BranchId).NotEmpty().WithMessage("Chi nhánh không được để trống.");
        RuleFor(x => x.TableNumber).NotEmpty().WithMessage("Số bàn không được để trống.");
        RuleFor(x => x.Capacity).GreaterThan(0).WithMessage("Sức chứa bàn phải lớn hơn 0.");
    }
}

public class UpdateTableStatusCommandValidator : AbstractValidator<UpdateTableStatusCommand>
{
    public UpdateTableStatusCommandValidator()
    {
        RuleFor(x => x.TableId).NotEmpty().WithMessage("ID bàn không hợp lệ.");
        RuleFor(x => x.Status).IsInEnum().WithMessage("Trạng thái bàn không hợp lệ.");
    }
}
