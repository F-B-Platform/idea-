using Microsoft.AspNetCore.Mvc;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.AdminAndAnalytics.Commands.MineAprioriCombos;
using SmartFB.Application.Features.AdminAndAnalytics.DTOs;
using SmartFB.Application.Features.AdminAndAnalytics.Queries.GetPandLReport;

namespace SmartFB.API.Controllers;

public class AnalyticsController : BaseApiController
{
    [HttpGet("pnl")]
    public async Task<ActionResult<ApiResponse<PandLReportDto>>> GetPandLReport(
        [FromQuery] DateTime fromDate,
        [FromQuery] DateTime toDate,
        [FromQuery] Guid? branchId = null)
    {
        var result = await Mediator.Send(new GetPandLReportQuery(fromDate, toDate, branchId));
        return Ok(result);
    }

    [HttpPost("combos/mine")]
    public async Task<ActionResult<ApiResponse<List<AiComboCandidateDto>>>> MineAprioriCombos([FromBody] MineAprioriCombosCommand command)
    {
        var result = await Mediator.Send(command);
        return Ok(result);
    }
}
