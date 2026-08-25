using Microsoft.AspNetCore.Mvc;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Branches.Commands.ConfigureBranchWifi;
using SmartFB.Application.Features.Branches.Commands.CreateBranch;
using SmartFB.Application.Features.Branches.DTOs;
using SmartFB.Application.Features.Branches.Queries.GetBranches;

namespace SmartFB.API.Controllers;

public class BranchesController : BaseApiController
{
    [HttpGet]
    public async Task<ActionResult<ApiResponse<List<BranchDto>>>> GetBranches([FromQuery] bool? onlyActive = null)
    {
        var result = await Mediator.Send(new GetBranchesQuery(onlyActive));
        return Ok(result);
    }

    [HttpPost]
    public async Task<ActionResult<ApiResponse<BranchDto>>> CreateBranch([FromBody] CreateBranchCommand command)
    {
        var result = await Mediator.Send(command);
        return Ok(result);
    }

    [HttpPut("{branchId:guid}/wifi")]
    public async Task<ActionResult<ApiResponse<BranchWifiConfigDto>>> ConfigureWifi(Guid branchId, [FromBody] ConfigureWifiRequestDto request)
    {
        var command = new ConfigureBranchWifiCommand(branchId, request.SsidName, request.BssidList, request.AllowedIpSubnets, request.IsActive);
        var result = await Mediator.Send(command);
        return Ok(result);
    }
}
