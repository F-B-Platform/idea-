#!/bin/bash
# ==============================================================================
# SMART F&B OS - QUICK START LOCAL DATABASE & REDIS (BASH)
# ==============================================================================
echo "🚀 Đang khởi động PostgreSQL 16 và Redis 7 cho môi trường Local Development..."

docker compose -f docker-compose.dev.yml up -d

if [ $? -eq 0 ]; then
    echo "✅ Hạ tầng Local Database & Redis đã sẵn sàng!"
    echo "   • PostgreSQL: localhost:5432 (Database: smart_fb_db, User: postgres)"
    echo "   • Redis:      localhost:6379"
    echo "   • pgAdmin:    http://localhost:5050 (User: admin@smartfb.vn, Pass: admin123)"
else
    echo "❌ Khởi động thất bại. Vui lòng kiểm tra Docker daemon đã bật chưa!"
fi
