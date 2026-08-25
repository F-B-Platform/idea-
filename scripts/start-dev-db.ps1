# ==============================================================================
# SMART F&B OS - QUICK START LOCAL DATABASE & REDIS (POWERSHELL)
# ==============================================================================
Write-Host "🚀 Đang khởi động PostgreSQL 16 và Redis 7 cho môi trường Local Development..." -ForegroundColor Cyan

docker compose -f docker-compose.dev.yml up -d

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Hạ tầng Local Database & Redis đã sẵn sàng!" -ForegroundColor Green
    Write-Host "   • PostgreSQL: localhost:5432 (Database: smart_fb_db, User: postgres)" -ForegroundColor Yellow
    Write-Host "   • Redis:      localhost:6379" -ForegroundColor Yellow
    Write-Host "   • pgAdmin:    http://localhost:5050 (User: admin@smartfb.vn, Pass: admin123)" -ForegroundColor Yellow
} else {
    Write-Host "❌ Khởi động thất bại. Vui lòng kiểm tra Docker Desktop đã bật chưa!" -ForegroundColor Red
}
