using FluentValidation;
using SmartFB.Application.Features.AdminAndAnalytics.Commands.MineAprioriCombos;
using SmartFB.Application.Features.AdminAndAnalytics.Queries.GetPandLReport;

namespace SmartFB.Application.Features.AdminAndAnalytics.Validators;

public class GetPandLReportQueryValidator : AbstractValidator<GetPandLReportQuery>
{
    public GetPandLReportQueryValidator()
    {
        RuleFor(x => x.ToDate)
            .GreaterThanOrEqualTo(x => x.FromDate)
            .WithMessage("Ngày kết thúc phải lớn hơn hoặc bằng ngày bắt đầu.");
    }
}

public class MineAprioriCombosCommandValidator : AbstractValidator<MineAprioriCombosCommand>
{
    public MineAprioriCombosCommandValidator()
    {
        RuleFor(x => x.MinSupport).InclusiveBetween(0.001, 1.0).WithMessage("Min Support phải nằm trong khoảng (0, 1].");
        RuleFor(x => x.MinConfidence).InclusiveBetween(0.01, 1.0).WithMessage("Min Confidence phải nằm trong khoảng (0, 1].");
    }
}
