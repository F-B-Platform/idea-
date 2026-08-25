using Microsoft.AspNetCore.Mvc;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.ShiftsAndCash.Commands.CloseCashShift;
using SmartFB.Application.Features.ShiftsAndCash.Commands.OpenCashShift;
using SmartFB.Application.Features.ShiftsAndCash.DTOs;
using SmartFB.Application.Features.ShiftsAndCash.Queries.GetActiveShift;

namespace SmartFB.API.Controllers;

public class ShiftsController : BaseApiController
{
    [HttpGet("active")]
    public async Task<ActionResult<ApiResponse<ShiftDto?>>> GetActiveShift([FromQuery] Guid branchId)
    {
        var result = await Mediator.Send(new GetActiveShiftQuery(branchId));
        return Ok(result);
    }

    [HttpPost("open")]
    public async Task<ActionResult<ApiResponse<ShiftDto>>> OpenShift([FromBody] OpenCashShiftCommand command)
    {
        var result = await Mediator.Send(command);
        return Ok(result);
    }

    [HttpPost("close")]
    public async Task<ActionResult<ApiResponse<ZReportDto>>> CloseShift([FromBody] CloseCashShiftCommand command)
    {
        var result = await Mediator.Send(command);
        return Ok(result);
    }
}
