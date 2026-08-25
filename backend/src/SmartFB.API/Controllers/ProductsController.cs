using Microsoft.AspNetCore.Mvc;
using SmartFB.Application.Common.Models;
using SmartFB.Application.Features.Products.Commands.CreateProduct;
using SmartFB.Application.Features.Products.Commands.SetRegionalPrice;
using SmartFB.Application.Features.Products.DTOs;
using SmartFB.Application.Features.Products.Queries.GetProducts;

namespace SmartFB.API.Controllers;

public class ProductsController : BaseApiController
{
    [HttpGet]
    public async Task<ActionResult<ApiResponse<List<ProductDto>>>> GetProducts(
        [FromQuery] Guid? branchId = null,
        [FromQuery] Guid? categoryId = null,
        [FromQuery] bool? onlyAvailable = null)
    {
        var result = await Mediator.Send(new GetProductsQuery(branchId, categoryId, onlyAvailable));
        return Ok(result);
    }

    [HttpPost]
    public async Task<ActionResult<ApiResponse<ProductDto>>> CreateProduct([FromBody] CreateProductCommand command)
    {
        var result = await Mediator.Send(command);
        return Ok(result);
    }

    [HttpPost("regional-price")]
    public async Task<ActionResult<ApiResponse<bool>>> SetRegionalPrice([FromBody] SetRegionalPriceCommand command)
    {
        var result = await Mediator.Send(command);
        return Ok(result);
    }
}
