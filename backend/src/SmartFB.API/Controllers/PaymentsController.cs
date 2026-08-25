using Microsoft.AspNetCore.Mvc;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Payments.Commands.ConfirmCashPayment;
using SmartFB.Application.Features.Payments.Commands.ProcessPayOSWebhook;
using SmartFB.Application.Features.Payments.DTOs;
using SmartFB.Application.Features.Payments.Queries.GetPaymentStatus;

namespace SmartFB.API.Controllers;

public class PaymentsController : BaseApiController
{
    [HttpPost("webhook/payos")]
    public async Task<ActionResult<ApiResponse<bool>>> ProcessPayOSWebhook(
        [FromBody] PayOSWebhookDataDto data,
        [FromHeader(Name = "x-payos-signature")] string? signature = null)
    {
        var result = await Mediator.Send(new ProcessPayOSWebhookCommand(data, signature ?? "mock_signature_dev"));
        return Ok(result);
    }

    [HttpPost("confirm-cash")]
    public async Task<ActionResult<ApiResponse<CashConfirmationResultDto>>> ConfirmCashPayment([FromBody] ConfirmCashPaymentCommand command)
    {
        var result = await Mediator.Send(command);
        return Ok(result);
    }

    [HttpGet("{orderId:guid}/status")]
    public async Task<ActionResult<ApiResponse<PaymentStatusDto>>> GetPaymentStatus(Guid orderId)
    {
        var result = await Mediator.Send(new GetPaymentStatusQuery(orderId));
        return Ok(result);
    }
}
