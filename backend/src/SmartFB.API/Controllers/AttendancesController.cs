using Microsoft.AspNetCore.Mvc;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Attendances.Commands.WifiClockIn;
using SmartFB.Application.Features.Attendances.Commands.WifiClockOut;
using SmartFB.Application.Features.Attendances.DTOs;
using SmartFB.Application.Features.Attendances.Queries.GetAttendances;

namespace SmartFB.API.Controllers;

public class AttendancesController : BaseApiController
{
    [HttpGet]
    public async Task<ActionResult<ApiResponse<List<AttendanceDto>>>> GetAttendances(
        [FromQuery] Guid? branchId = null,
        [FromQuery] Guid? userId = null,
        [FromQuery] DateTime? fromDate = null,
        [FromQuery] DateTime? toDate = null)
    {
        var result = await Mediator.Send(new GetAttendancesQuery(branchId, userId, fromDate, toDate));
        return Ok(result);
    }

    [HttpPost("clock-in")]
    public async Task<ActionResult<ApiResponse<AttendanceDto>>> ClockIn([FromBody] WifiClockInCommand command)
    {
        var result = await Mediator.Send(command);
        return Ok(result);
    }

    [HttpPost("clock-out")]
    public async Task<ActionResult<ApiResponse<AttendanceDto>>> ClockOut([FromBody] WifiClockOutCommand command)
    {
        var result = await Mediator.Send(command);
        return Ok(result);
    }
}
