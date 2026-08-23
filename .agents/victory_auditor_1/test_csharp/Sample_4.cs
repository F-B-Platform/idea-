// ============================================================================
// File: src/SmartFB.Application/Features/Orders/Commands/CreateDineInOrder/CreateDineInOrderCommandHandler.cs
// Project: Smart F&B Operating System (v2.5.0-Production-Ready)
// Description: Handler thực thi logic khởi tạo đơn Dine-In, kiểm tra tính khả dụng,
// tạo liên kết PayOS VietQR (Nhánh A) hoặc thông báo SignalR KDS ngay lập tức (Nhánh B).
// ============================================================================

using MediatR;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Logging;
using SmartFB.Application.Common.Interfaces;
using SmartFB.Application.Common.Models;
using SmartFB.Domain.Entities;
using SmartFB.Domain.Enums;

namespace SmartFB.Application.Features.Orders.Commands.CreateDineInOrder;

public sealed class CreateDineInOrderCommandHandler : IRequestHandler<CreateDineInOrderCommand, Result<CreateOrderResponseDto>>
{
    private readonly IAppDbContext _dbContext;
    private readonly IPaymentService _paymentService;
    private readonly IKitchenRealtimeNotifier _kitchenNotifier;
    private readonly IDateTimeProvider _dateTimeProvider;
    private readonly ILogger<CreateDineInOrderCommandHandler> _logger;

    public CreateDineInOrderCommandHandler(
        IAppDbContext dbContext,
        IPaymentService paymentService,
        IKitchenRealtimeNotifier kitchenNotifier,
        IDateTimeProvider dateTimeProvider,
        ILogger<CreateDineInOrderCommandHandler> logger)
    {
        _dbContext = dbContext;
        _paymentService = paymentService;
        _kitchenNotifier = kitchenNotifier;
        _dateTimeProvider = dateTimeProvider;
        _logger = logger;
    }

    public async Task<Result<CreateOrderResponseDto>> Handle(
        CreateDineInOrderCommand request,
        CancellationToken cancellationToken)
    {
        _logger.LogInformation("Đang khởi tạo đơn hàng Dine-In cho Chi nhánh {BranchId} - Bàn {TableId}", request.BranchId, request.TableId);

        // 1. Kiểm tra sự tồn tại và tính khả dụng của Chi nhánh & Bàn
        var table = await _dbContext.Tables
            .AsNoTracking()
            .FirstOrDefaultAsync(t => t.Id == request.TableId && t.BranchId == request.BranchId, cancellationToken);

        if (table is null)
        {
            return Result<CreateOrderResponseDto>.Failure($"Không tìm thấy bàn {request.TableId} tại chi nhánh chỉ định.");
        }

        if (!table.IsActive)
        {
            return Result<CreateOrderResponseDto>.Failure("Bàn này hiện đang tạm ngưng phục vụ.");
        }

        // 2. Sinh mã đơn hàng chuẩn format: DIN-YYMMDD-XXXX
        DateTime nowUtc = _dateTimeProvider.UtcNow;
        string orderCode = $"DIN-{nowUtc:yyMMdd}-{Random.Shared.Next(1000, 9999)}";

        var order = Order.CreateDineInOrder(
            request.BranchId,
            request.TableId,
            orderCode,
            request.PaymentMethod,
            request.Note,
            nowUtc
        );

        // 3. Thêm chi tiết món và toppings kèm kiểm tra dữ liệu giá thực tế từ Database
        foreach (var itemDto in request.Items)
        {
            var menuItem = await _dbContext.MenuItems
                .AsNoTracking()
                .FirstOrDefaultAsync(m => m.Id == itemDto.MenuItemId && m.IsActive, cancellationToken);

            if (menuItem is null)
            {
                return Result<CreateOrderResponseDto>.Failure($"Món {itemDto.MenuItemId} không tồn tại hoặc đã ngưng bán.");
            }

            var itemSize = await _dbContext.ItemSizes
                .AsNoTracking()
                .FirstOrDefaultAsync(s => s.Id == itemDto.ItemSizeId && s.MenuItemId == itemDto.MenuItemId, cancellationToken);

            if (itemSize is null)
            {
                return Result<CreateOrderResponseDto>.Failure($"Kích cỡ {itemDto.ItemSizeId} không hợp lệ cho món {menuItem.Name}.");
            }

            List<OrderItemTopping>? toppings = null;
            if (itemDto.Toppings != null && itemDto.Toppings.Count > 0)
            {
                toppings = itemDto.Toppings
                    .Select(t => new OrderItemTopping(t.ToppingId, t.ToppingName, t.Price))
                    .ToList();
            }

            order.AddItem(
                menuItem.Id,
                itemSize.Id,
                menuItem.Name,
                itemSize.Name,
                itemSize.Price,
                itemDto.Quantity,
                itemDto.Note,
                toppings
            );
        }

        // 4. Lưu đơn hàng vào PostgreSQL
        await _dbContext.Orders.AddAsync(order, cancellationToken);
        await _dbContext.SaveChangesAsync(cancellationToken);

        string? paymentQrUrl = null;

        // 5. Xử lý phân nhánh thanh toán theo Master Spec v2.5.0
        if (request.PaymentMethod == PaymentMethod.VietQr)
        {
            // Nhánh A (VietQR Thanh toán trước): Sinh link thanh toán PayOS
            var paymentResult = await _paymentService.CreateVietQrPaymentLinkAsync(
                order.Id,
                order.OrderCode,
                order.TotalAmount.Amount,
                cancellationToken);

            if (!paymentResult.IsSuccess)
            {
                _logger.LogError("Không thể tạo liên kết PayOS VietQR cho đơn {OrderCode}: {Error}", order.OrderCode, paymentResult.ErrorMessage);
                return Result<CreateOrderResponseDto>.Failure($"Lỗi tích hợp cổng thanh toán: {paymentResult.ErrorMessage}");
            }

            paymentQrUrl = paymentResult.QrCodeUrl;
        }
        else
        {
            // Nhánh B (Tiền mặt Thanh toán sau): Phát vé ngay lập tức cho màn hình Bếp KDS qua SignalR
            await _kitchenNotifier.BroadcastNewTicketAsync(order.BranchId, order.Id, cancellationToken);
        }

        _logger.LogInformation("Khởi tạo đơn hàng thành công: {OrderCode} | Tổng tiền: {TotalAmount:N0} VND", order.OrderCode, order.TotalAmount.Amount);

        return Result<CreateOrderResponseDto>.Success(new CreateOrderResponseDto(
            order.Id,
            order.OrderCode,
            order.Status,
            order.PaymentStatus,
            order.TotalAmount.Amount,
            paymentQrUrl,
            order.CreatedAtUtc
        ));
    }
}