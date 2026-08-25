using Microsoft.AspNetCore.Mvc;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Tables.Commands.CreateTable;
using SmartFB.Application.Features.Tables.Commands.GenerateTableQr;
using SmartFB.Application.Features.Tables.Commands.UpdateTableStatus;
using SmartFB.Application.Features.Tables.DTOs;
using SmartFB.Application.Features.Tables.Queries.GetTables;

namespace SmartFB.API.Controllers;

public class TablesController : BaseApiController
{
    [HttpGet]
    public async Task<ActionResult<ApiResponse<List<TableDto>>>> GetTables([FromQuery] Guid branchId)
    {
        var result = await Mediator.Send(new GetTablesQuery(branchId));
        return Ok(result);
    }

    [HttpPost]
    public async Task<ActionResult<ApiResponse<TableDto>>> CreateTable([FromBody] CreateTableCommand command)
    {
        var result = await Mediator.Send(command);
        return Ok(result);
    }

    [HttpPatch("{tableId:guid}/status")]
    public async Task<ActionResult<ApiResponse<TableDto>>> UpdateStatus(Guid tableId, [FromBody] UpdateTableStatusRequestDto request)
    {
        var result = await Mediator.Send(new UpdateTableStatusCommand(tableId, request.Status));
        return Ok(result);
    }

    [HttpPost("{tableId:guid}/qr")]
    public async Task<ActionResult<ApiResponse<TableQrDto>>> GenerateQr(Guid tableId)
    {
        var result = await Mediator.Send(new GenerateTableQrCommand(tableId));
        return Ok(result);
    }
}
