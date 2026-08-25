using Microsoft.AspNetCore.Mvc;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.KitchenKDS.Commands.Toggle86Product;
using SmartFB.Application.Features.KitchenKDS.Commands.UpdateKdsItemStatus;
using SmartFB.Application.Features.KitchenKDS.DTOs;
using SmartFB.Application.Features.KitchenKDS.Queries.GetKdsTickets;

namespace SmartFB.API.Controllers;

public class KitchenController : BaseApiController
{
    [HttpGet("tickets")]
    public async Task<ActionResult<ApiResponse<List<KdsTicketDto>>>> GetKdsTickets([FromQuery] Guid branchId)
    {
        var result = await Mediator.Send(new GetKdsTicketsQuery(branchId));
        return Ok(result);
    }

    [HttpPatch("items/{orderItemId:guid}/status")]
    public async Task<ActionResult<ApiResponse<bool>>> UpdateItemStatus(Guid orderItemId, [FromBody] UpdateKdsItemStatusRequestDto request)
    {
        var result = await Mediator.Send(new UpdateKdsItemStatusCommand(orderItemId, request.NewStatus));
        return Ok(result);
    }

    [HttpPost("toggle-86")]
    public async Task<ActionResult<ApiResponse<bool>>> Toggle86([FromBody] Toggle86ProductCommand command)
    {
        var result = await Mediator.Send(command);
        return Ok(result);
    }
}
