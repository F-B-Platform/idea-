// ============================================================================
// File: src/SmartFB.WebApi/Middlewares/GlobalExceptionHandler.cs
// Project: Smart F&B Operating System (v2.5.0-Production-Ready)
// Description: Middleware bắt ngoại lệ toàn cục chuyển đổi sang chuẩn RFC 7807 ProblemDetails.
// ============================================================================

using System.Diagnostics;
using FluentValidation;
using Microsoft.AspNetCore.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using SmartFB.Domain.Exceptions;

namespace SmartFB.WebApi.Middlewares;

public sealed class GlobalExceptionHandler : IExceptionHandler
{
    private readonly ILogger<GlobalExceptionHandler> _logger;

    public GlobalExceptionHandler(ILogger<GlobalExceptionHandler> logger)
    {
        _logger = logger;
    }

    public async ValueTask<bool> TryHandleAsync(
        HttpContext httpContext,
        Exception exception,
        CancellationToken cancellationToken)
    {
        var traceId = Activity.Current?.Id ?? httpContext.TraceIdentifier;
        _logger.LogError(exception, "Phát hiện ngoại lệ chưa được xử lý. TraceId: {TraceId} | Path: {Path}", traceId, httpContext.Request.Path);

        var (statusCode, title, detail, errorsDictionary) = exception switch
        {
            ValidationException validationEx => (
                StatusCodes.Status400BadRequest,
                "Lỗi Xác Thực Dữ Liệu (Validation Error)",
                "Một hoặc nhiều trường dữ liệu đầu vào không đáp ứng quy chuẩn nghiệp vụ.",
                validationEx.Errors
                    .GroupBy(e => e.PropertyName)
                    .ToDictionary(g => g.Key, g => (object)g.Select(e => e.ErrorMessage).ToArray())
            ),
            DomainException domainEx => (
                StatusCodes.Status422UnprocessableEntity,
                "Vi Phạm Quy Tắc Nghiệp Vụ (Business Rule Violation)",
                domainEx.Message,
                null
            ),
            KeyNotFoundException notFoundEx => (
                StatusCodes.Status404NotFound,
                "Không Tìm Thấy Tài Nguyên (Resource Not Found)",
                notFoundEx.Message,
                null
            ),
            UnauthorizedAccessException unauthorizedEx => (
                StatusCodes.Status401Unauthorized,
                "Không Có Quyền Truy Cập (Unauthorized)",
                unauthorizedEx.Message,
                null
            ),
            InvalidOperationException invalidOpEx => (
                StatusCodes.Status409Conflict,
                "Xung Đột Trạng Thái Hệ Thống (Conflict)",
                invalidOpEx.Message,
                null
            ),
            _ => (
                StatusCodes.Status500InternalServerError,
                "Lỗi Máy Chủ Nội Bộ (Internal Server Error)",
                "Đã xảy ra sự cố không mong muốn trên hệ thống. Vui lòng liên hệ kỹ thuật viên hỗ trợ.",
                null
            )
        };

        var problemDetails = new ProblemDetails
        {
            Status = statusCode,
            Title = title,
            Detail = detail,
            Instance = httpContext.Request.Path,
            Extensions =
            {
                ["traceId"] = traceId,
                ["timestamp"] = DateTime.UtcNow.ToString("o")
            }
        };

        if (errorsDictionary is not null)
        {
            problemDetails.Extensions["errors"] = errorsDictionary;
        }

        httpContext.Response.StatusCode = statusCode;
        httpContext.Response.ContentType = "application/problem+json";

        await httpContext.Response.WriteAsJsonAsync(problemDetails, cancellationToken);
        return true;
    }
}