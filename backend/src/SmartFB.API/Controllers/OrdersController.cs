using Microsoft.AspNetCore.Mvc;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Orders.Commands.CreateDeliveryOrder;
using SmartFB.Application.Features.Orders.Commands.CreateDineInPostpaidOrder;
using SmartFB.Application.Features.Orders.Commands.CreateDineInPrepaidOrder;
using SmartFB.Application.Features.Orders.Commands.CreateTakeawayOrder;
using SmartFB.Application.Features.Orders.DTOs;
using SmartFB.Application.Features.Orders.Queries.GetOrderById;

namespace SmartFB.API.Controllers;

public class OrdersController : BaseApiController
{
    [HttpGet("{orderId:guid}")]
    public async Task<ActionResult<ApiResponse<OrderDto>>> GetOrderById(Guid orderId)
    {
        var result = await Mediator.Send(new GetOrderByIdQuery(orderId));
        return Ok(result);
    }

    [HttpPost("dine-in/prepaid")]
    public async Task<ActionResult<ApiResponse<PrepaidOrderResultDto>>> CreateDineInPrepaid([FromBody] CreateDineInPrepaidOrderCommand command)
    {
        var result = await Mediator.Send(command);
        return Ok(result);
    }

    [HttpPost("dine-in/postpaid")]
    public async Task<ActionResult<ApiResponse<PostpaidOrderResultDto>>> CreateDineInPostpaid([FromBody] CreateDineInPostpaidOrderCommand command)
    {
        var result = await Mediator.Send(command);
        return Ok(result);
    }

    [HttpPost("delivery")]
    public async Task<ActionResult<ApiResponse<DeliveryOrderResultDto>>> CreateDelivery([FromBody] CreateDeliveryOrderCommand command)
    {
        var result = await Mediator.Send(command);
        return Ok(result);
    }

    [HttpPost("takeaway")]
    public async Task<ActionResult<ApiResponse<TakeawayOrderResultDto>>> CreateTakeaway([FromBody] CreateTakeawayOrderCommand command)
    {
        var result = await Mediator.Send(command);
        return Ok(result);
    }
}
