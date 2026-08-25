using Microsoft.AspNetCore.Mvc;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;

namespace SmartFB.API.Controllers;

public class HealthController : BaseApiController
{
    private readonly IDateTimeService _dateTimeService;

    public HealthController(IDateTimeService dateTimeService)
    {
        _dateTimeService = dateTimeService;
    }

    [HttpGet]
    public ActionResult<ApiResponse<object>> GetHealth()
    {
        var healthData = new
        {
            Status = "Healthy",
            Service = "Smart F&B OS API",
            Version = "2.5.0",
            ServerTimeUtc = _dateTimeService.UtcNow,
            ServerTimeVietnam = _dateTimeService.VietnamNow,
            Environment = Environment.GetEnvironmentVariable("ASPNETCORE_ENVIRONMENT") ?? "Development"
        };

        return Ok(ApiResponse<object>.SuccessResult(healthData, "Smart F&B OS API is up and running."));
    }
}
