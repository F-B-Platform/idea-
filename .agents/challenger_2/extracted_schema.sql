-- ============================================================================
-- SMART F&B OS - PRODUCTION DATABASE INITIALIZATION SCRIPT (POSTGRESQL 16)
-- File: 01_schema_ddl.sql
-- ============================================================================

-- 2.1 EXTENSIONS
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- 2.1 ENUMS
DO $$ BEGIN
    CREATE TYPE user_role_enum AS ENUM ('Admin', 'Manager', 'Cashier', 'Barista');
EXCEPTION WHEN duplicate_object THEN null; END $$;

DO $$ BEGIN
    CREATE TYPE order_type_enum AS ENUM ('DineIn', 'TakeAway', 'Delivery');
EXCEPTION WHEN duplicate_object THEN null; END $$;

DO $$ BEGIN
    CREATE TYPE order_status_enum AS ENUM (
        'PendingPayment',
        'Paid',
        'Confirmed',
        'Preparing',
        'Ready',
        'Completed',
        'Cancelled'
    );
EXCEPTION WHEN duplicate_object THEN null; END $$;

DO $$ BEGIN
    CREATE TYPE payment_method_enum AS ENUM ('VietQR', 'Cash');
EXCEPTION WHEN duplicate_object THEN null; END $$;

DO $$ BEGIN
    CREATE TYPE payment_status_enum AS ENUM ('Pending', 'Success', 'Failed', 'Refunded');
EXCEPTION WHEN duplicate_object THEN null; END $$;

DO $$ BEGIN
    CREATE TYPE attendance_status_enum AS ENUM ('Present', 'Late', 'Absent', 'EarlyLeave');
EXCEPTION WHEN duplicate_object THEN null; END $$;

DO $$ BEGIN
    CREATE TYPE shift_status_enum AS ENUM ('Open', 'Closed', 'Audited');
EXCEPTION WHEN duplicate_object THEN null; END $$;

DO $$ BEGIN
    CREATE TYPE loyalty_trans_type_enum AS ENUM ('Earn', 'Redeem', 'Adjust', 'Expire');
EXCEPTION WHEN duplicate_object THEN null; END $$;

-- ============================================================================
-- 2.2 BẢNG CHI NHÁNH, MẠNG WIFI & BÀN ĂN
-- ============================================================================

CREATE TABLE IF NOT EXISTS branches (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    code VARCHAR(30) UNIQUE NOT NULL,
    name VARCHAR(150) NOT NULL,
    address VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS branch_wifi_configs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    branch_id UUID NOT NULL REFERENCES branches(id) ON DELETE CASCADE,
    wifi_ssid VARCHAR(100) NOT NULL,
    wifi_bssid VARCHAR(50) NOT NULL,
    allowed_ip_subnet VARCHAR(50) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uq_branch_wifi UNIQUE (branch_id, wifi_bssid)
);

CREATE TABLE IF NOT EXISTS tables (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    branch_id UUID NOT NULL REFERENCES branches(id) ON DELETE CASCADE,
    table_number VARCHAR(20) NOT NULL,
    zone VARCHAR(50) NOT NULL DEFAULT 'Indoor',
    capacity INT NOT NULL DEFAULT 4,
    qr_token VARCHAR(100) UNIQUE NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uq_branch_table_number UNIQUE (branch_id, table_number)
);

-- ============================================================================
-- 2.3 BẢNG NGƯỜI DÙNG, CA LÀM VIỆC & CHẤM CÔNG WIFI
-- ============================================================================

CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    branch_id UUID REFERENCES branches(id) ON DELETE SET NULL,
    employee_code VARCHAR(30) UNIQUE NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role user_role_enum NOT NULL,
    phone VARCHAR(20),
    is_active BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS work_shifts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    branch_id UUID NOT NULL REFERENCES branches(id) ON DELETE RESTRICT,
    opened_by_user_id UUID NOT NULL REFERENCES users(id) ON DELETE RESTRICT,
    closed_by_user_id UUID REFERENCES users(id) ON DELETE RESTRICT,
    start_time TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    end_time TIMESTAMPTZ,
    initial_cash NUMERIC(12, 2) NOT NULL DEFAULT 0.00,
    ending_cash NUMERIC(12, 2),
    system_cash NUMERIC(12, 2),
    variance NUMERIC(12, 2),
    discrepancy_reason TEXT,
    status shift_status_enum NOT NULL DEFAULT 'Open',
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS attendances (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE RESTRICT,
    branch_id UUID NOT NULL REFERENCES branches(id) ON DELETE RESTRICT,
    work_shift_id UUID REFERENCES work_shifts(id) ON DELETE SET NULL,
    check_in_time TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    check_out_time TIMESTAMPTZ,
    client_ip VARCHAR(50) NOT NULL,
    client_bssid VARCHAR(50) NOT NULL,
    is_wifi_verified BOOLEAN NOT NULL DEFAULT false,
    status attendance_status_enum NOT NULL DEFAULT 'Present',
    notes TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- 2.4 BẢNG THỰC ĐƠN, BIẾN THỂ & ĐỊNH LƯỢNG MÓN (BOM)
-- ============================================================================

CREATE TABLE IF NOT EXISTS categories (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) NOT NULL,
    slug VARCHAR(100) UNIQUE NOT NULL,
    display_order INT NOT NULL DEFAULT 0,
    is_active BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS products (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    category_id UUID NOT NULL REFERENCES categories(id) ON DELETE RESTRICT,
    code VARCHAR(30) UNIQUE NOT NULL,
    name VARCHAR(150) NOT NULL,
    description TEXT,
    base_price NUMERIC(12, 2) NOT NULL DEFAULT 0.00,
    image_url VARCHAR(255),
    is_active BOOLEAN NOT NULL DEFAULT true,
    is_bestseller BOOLEAN NOT NULL DEFAULT false,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS product_variants (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    product_id UUID NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    name VARCHAR(50) NOT NULL, -- Size M, Size L
    sku VARCHAR(50) UNIQUE NOT NULL,
    price_adjustment NUMERIC(12, 2) NOT NULL DEFAULT 0.00,
    is_default BOOLEAN NOT NULL DEFAULT false,
    is_active BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS product_options (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    product_id UUID NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    name VARCHAR(50) NOT NULL, -- Mức Đường, Mức Đá, Topping
    is_required BOOLEAN NOT NULL DEFAULT false,
    min_selection INT NOT NULL DEFAULT 0,
    max_selection INT NOT NULL DEFAULT 1,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS product_option_items (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    product_option_id UUID NOT NULL REFERENCES product_options(id) ON DELETE CASCADE,
    name VARCHAR(50) NOT NULL, -- 0%, 50%, 100%, Thạch dừa
    price_adjustment NUMERIC(12, 2) NOT NULL DEFAULT 0.00,
    is_default BOOLEAN NOT NULL DEFAULT false,
    is_active BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ingredients (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    code VARCHAR(30) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    unit VARCHAR(20) NOT NULL, -- gram, ml, cai
    unit_cost NUMERIC(12, 2) NOT NULL DEFAULT 0.00,
    min_stock_level NUMERIC(12, 2) NOT NULL DEFAULT 10.00,
    is_active BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS recipes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    product_id UUID NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    variant_id UUID REFERENCES product_variants(id) ON DELETE CASCADE,
    name VARCHAR(150) NOT NULL,
    instructions TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS recipe_ingredients (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    recipe_id UUID NOT NULL REFERENCES recipes(id) ON DELETE CASCADE,
    ingredient_id UUID NOT NULL REFERENCES ingredients(id) ON DELETE RESTRICT,
    quantity_required NUMERIC(10, 2) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uq_recipe_ingredient UNIQUE (recipe_id, ingredient_id)
);

CREATE TABLE IF NOT EXISTS inventory_transactions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    branch_id UUID NOT NULL REFERENCES branches(id) ON DELETE RESTRICT,
    ingredient_id UUID NOT NULL REFERENCES ingredients(id) ON DELETE RESTRICT,
    transaction_type VARCHAR(30) NOT NULL, -- Import, Export, OrderDeduction, Wastage
    quantity NUMERIC(10, 2) NOT NULL,
    unit_cost NUMERIC(12, 2) NOT NULL,
    reference_order_id UUID,
    notes TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- 2.5 BẢNG KHÁCH HÀNG CRM & SỔ CÁI TÍCH LY (LOYALTY 10 CUPS)
-- ============================================================================

CREATE TABLE IF NOT EXISTS customers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    phone_number VARCHAR(20) UNIQUE NOT NULL,
    full_name VARCHAR(100),
    cup_balance INT NOT NULL DEFAULT 0,
    total_spent NUMERIC(14, 2) NOT NULL DEFAULT 0.00,
    last_order_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS loyalty_cup_transactions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_id UUID NOT NULL REFERENCES customers(id) ON DELETE CASCADE,
    order_id UUID,
    cups_changed INT NOT NULL, -- +2, -10
    balance_after INT NOT NULL,
    transaction_type loyalty_trans_type_enum NOT NULL,
    notes TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- 2.6 BẢNG ĐƠN HÀNG 3 LOẠI & CHI TIẾT MÓN (ORDERS & ITEMS)
-- ============================================================================

CREATE TABLE IF NOT EXISTS orders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    branch_id UUID NOT NULL REFERENCES branches(id) ON DELETE RESTRICT,
    table_id UUID REFERENCES tables(id) ON DELETE SET NULL,
    customer_id UUID REFERENCES customers(id) ON DELETE SET NULL,
    order_number VARCHAR(30) UNIQUE NOT NULL,
    order_type order_type_enum NOT NULL,
    status order_status_enum NOT NULL DEFAULT 'PendingPayment',
    recipient_name VARCHAR(100),
    recipient_phone VARCHAR(20),
    delivery_address TEXT,
    delivery_fee NUMERIC(12, 2) NOT NULL DEFAULT 0.00,
    subtotal NUMERIC(12, 2) NOT NULL DEFAULT 0.00,
    discount_amount NUMERIC(12, 2) NOT NULL DEFAULT 0.00,
    total_amount NUMERIC(12, 2) NOT NULL DEFAULT 0.00,
    paid_at TIMESTAMPTZ,
    notes TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS order_items (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    order_id UUID NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
    product_id UUID NOT NULL REFERENCES products(id) ON DELETE RESTRICT,
    variant_id UUID REFERENCES product_variants(id) ON DELETE SET NULL,
    quantity INT NOT NULL DEFAULT 1,
    unit_price NUMERIC(12, 2) NOT NULL,
    total_price NUMERIC(12, 2) NOT NULL,
    selected_options_json JSONB,
    notes TEXT,
    kds_status VARCHAR(30) NOT NULL DEFAULT 'Pending',
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- 2.7 BẢNG THANH TOÁN VIETQR / TIỀN MẶT
-- ============================================================================

CREATE TABLE IF NOT EXISTS payments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    order_id UUID NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
    payment_method payment_method_enum NOT NULL,
    payment_status payment_status_enum NOT NULL DEFAULT 'Pending',
    amount NUMERIC(12, 2) NOT NULL,
    transaction_ref VARCHAR(100) UNIQUE,
    qr_code_payload TEXT,
    paid_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- 2.8 BẢNG KHUYẾN MÃI, COMBO AI, ĐÁNH GIÁ & AUDIT LOGS
-- ============================================================================

CREATE TABLE IF NOT EXISTS combos (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(150) NOT NULL,
    code VARCHAR(30) UNIQUE NOT NULL,
    discount_percent NUMERIC(5, 2) NOT NULL DEFAULT 10.00,
    is_active BOOLEAN NOT NULL DEFAULT true,
    start_date TIMESTAMPTZ,
    end_date TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS combo_items (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    combo_id UUID NOT NULL REFERENCES combos(id) ON DELETE CASCADE,
    product_id UUID NOT NULL REFERENCES products(id) ON DELETE RESTRICT,
    quantity INT NOT NULL DEFAULT 1,
    CONSTRAINT uq_combo_product UNIQUE (combo_id, product_id)
);

CREATE TABLE IF NOT EXISTS customer_reviews (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    order_id UUID NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
    customer_id UUID REFERENCES customers(id) ON DELETE SET NULL,
    rating INT NOT NULL CHECK (rating >= 1 AND rating <= 5),
    comment TEXT,
    photo_urls JSONB,
    status VARCHAR(30) NOT NULL DEFAULT 'Approved',
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS audit_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE SET NULL,
    action VARCHAR(50) NOT NULL,
    entity_name VARCHAR(50) NOT NULL,
    entity_id VARCHAR(50) NOT NULL,
    old_values_json JSONB,
    new_values_json JSONB,
    ip_address VARCHAR(50),
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- INDEXES FOR PERFORMANCE OPTIMIZATION
CREATE INDEX IF NOT EXISTS idx_orders_branch_status ON orders(branch_id, status);
CREATE INDEX IF NOT EXISTS idx_orders_customer_id ON orders(customer_id);
CREATE INDEX IF NOT EXISTS idx_order_items_order_id ON order_items(order_id);
CREATE INDEX IF NOT EXISTS idx_attendances_user_checkin ON attendances(user_id, check_in_time);
CREATE INDEX IF NOT EXISTS idx_products_category ON products(category_id, is_active);
CREATE INDEX IF NOT EXISTS idx_customers_phone ON customers(phone_number);

-- ============================================================================
-- SMART F&B OS - REALISTIC SEED DATA SCRIPT (POSTGRESQL 16)
-- File: 02_seed_dml.sql
-- ============================================================================

-- 3.1 CHI NHÁNH & CẤU HÌNH WIFI BSSID / SUBNET IP
INSERT INTO branches (id, code, name, address, phone, is_active) VALUES
('b1000000-0000-0000-0000-000000000001', 'BR-Q1', 'Smart Coffee - Quận 1 Flagship', '72 Lê Thánh Tôn, P. Bến Nghé, Quận 1, TP.HCM', '02838221101', true),
('b1000000-0000-0000-0000-000000000002', 'BR-TD', 'Smart Coffee - Thủ Đức Campus', '01 Võ Văn Ngân, TP. Thủ Đức, TP.HCM', '02838992202', true),
('b1000000-0000-0000-0000-000000000003', 'BR-Q7', 'Smart Coffee - Phú Mỹ Hưng', '105 Tôn Dật Tiên, Tân Phong, Quận 7, TP.HCM', '02854113303', true)
ON CONFLICT (code) DO NOTHING;

INSERT INTO branch_wifi_configs (id, branch_id, wifi_ssid, wifi_bssid, allowed_ip_subnet, is_active) VALUES
('w1000000-0000-0000-0000-000000000001', 'b1000000-0000-0000-0000-000000000001', 'SmartCoffee_Q1', '00:14:22:01:23:45', '192.168.1.0/24', true),
('w1000000-0000-0000-0000-000000000002', 'b1000000-0000-0000-0000-000000000002', 'SmartCoffee_ThuDuc', '00:14:22:FE:DC:BA', '192.168.2.0/24', true),
('w1000000-0000-0000-0000-000000000003', 'b1000000-0000-0000-0000-000000000003', 'SmartCoffee_Q7', '00:14:22:AA:BB:CC', '192.168.3.0/24', true)
ON CONFLICT (branch_id, wifi_bssid) DO NOTHING;

-- BÀN ĂN CHO 3 CHI NHÁNH
INSERT INTO tables (id, branch_id, table_number, zone, capacity, qr_token, is_active) VALUES
-- Chi nhánh Q1 (10 Bàn)
('t1000000-0000-0000-0000-000000000001', 'b1000000-0000-0000-0000-000000000001', '01', 'Indoor', 2, 'QR-Q1-T01-TOKEN-A1B2C3D4', true),
('t1000000-0000-0000-0000-000000000002', 'b1000000-0000-0000-0000-000000000001', '02', 'Indoor', 4, 'QR-Q1-T02-TOKEN-E5F6G7H8', true),
('t1000000-0000-0000-0000-000000000003', 'b1000000-0000-0000-0000-000000000001', '03', 'Indoor', 4, 'QR-Q1-T03-TOKEN-I9J0K1L2', true),
('t1000000-0000-0000-0000-000000000004', 'b1000000-0000-0000-0000-000000000001', '04', 'Terrace', 4, 'QR-Q1-T04-TOKEN-M3N4O5P6', true),
('t1000000-0000-0000-0000-000000000005', 'b1000000-0000-0000-0000-000000000001', '05', 'Terrace', 6, 'QR-Q1-T05-TOKEN-Q7R8S9T0', true),
('t1000000-0000-0000-0000-000000000006', 'b1000000-0000-0000-0000-000000000001', '06', 'VIP Room', 8, 'QR-Q1-T06-TOKEN-U1V2W3X4', true),
('t1000000-0000-0000-0000-000000000007', 'b1000000-0000-0000-0000-000000000001', '07', 'Indoor', 2, 'QR-Q1-T07-TOKEN-Y5Z6A7B8', true),
('t1000000-0000-0000-0000-000000000008', 'b1000000-0000-0000-0000-000000000001', '08', 'Indoor', 4, 'QR-Q1-T08-TOKEN-C9D0E1F2', true),
('t1000000-0000-0000-0000-000000000009', 'b1000000-0000-0000-0000-000000000001', '09', 'Terrace', 4, 'QR-Q1-T09-TOKEN-G3H4I5J6', true),
('t1000000-0000-0000-0000-000000000010', 'b1000000-0000-0000-0000-000000000001', '10', 'Indoor', 2, 'QR-Q1-T10-TOKEN-K7L8M9N0', true)
ON CONFLICT (qr_token) DO NOTHING;

-- 3.2 TÀI KHOẢN NGƯỜI DÙNG (BCRYPT HASH: SmartFB@2026!)
-- Hash: $2a$11$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy
INSERT INTO users (id, branch_id, employee_code, full_name, email, password_hash, role, phone, is_active) VALUES
('u1000000-0000-0000-0000-000000000001', NULL, 'ADM-001', 'Tổng Giám Đốc (Admin)', 'admin@smartfb.vn', '$2a$11$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy', 'Admin', '0901000001', true),
('u1000000-0000-0000-0000-000000000002', 'b1000000-0000-0000-0000-000000000001', 'MGR-Q1', 'Trần Văn Quản Lý', 'manager.q1@smartfb.vn', '$2a$11$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy', 'Manager', '0901000002', true),
('u1000000-0000-0000-0000-000000000003', 'b1000000-0000-0000-0000-000000000001', 'CSH-Q1-01', 'Lê Thu Ngân', 'cashier.q1@smartfb.vn', '$2a$11$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy', 'Cashier', '0901000003', true),
('u1000000-0000-0000-0000-000000000004', 'b1000000-0000-0000-0000-000000000001', 'NV-Q1-008', 'Trần Thị Bích (Barista)', 'barista.q1@smartfb.vn', '$2a$11$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy', 'Barista', '0901000004', true)
ON CONFLICT (email) DO NOTHING;

-- 3.3 DANH MỤC & SẢN PHẨM
INSERT INTO categories (id, name, slug, display_order, is_active) VALUES
('c1000000-0000-0000-0000-000000000001', 'Cà Phê Truyền Thống', 'ca-phe-truyen-thong', 1, true),
('c1000000-0000-0000-0000-000000000002', 'Trà & Trà Trái Cây', 'tra-trai-cay', 2, true),
('c1000000-0000-0000-0000-000000000003', 'Bánh Ngọt & Tráng Miệng', 'banh-ngot', 3, true)
ON CONFLICT (slug) DO NOTHING;

INSERT INTO products (id, category_id, code, name, description, base_price, image_url, is_active, is_bestseller) VALUES
('p1000000-0000-0000-0000-000000000001', 'c1000000-0000-0000-0000-000000000001', 'CF-BACXIU', 'Bạc Xỉu Sài Gòn', 'Cà phê phin đậm đà kết hợp sữa tươi và sữa đặc béo ngậy.', 35000.00, 'https://cdn.smartfb.vn/images/bac-xiu.jpg', true, true),
('p1000000-0000-0000-0000-000000000002', 'c1000000-0000-0000-0000-000000000001', 'CF-MUOI', 'Cà Phê Muối Hoàng Gia', 'Cà phê nguyên chất phủ lớp kem béo mặn Himalaya.', 39000.00, 'https://cdn.smartfb.vn/images/cafe-muoi.jpg', true, true),
('p1000000-0000-0000-0000-000000000003', 'c1000000-0000-0000-0000-000000000002', 'TEA-DAOCAMSA', 'Trà Đào Cam Sả', 'Trà thanh mát kết hợp đào miếng giòn và sả thơm ngát.', 45000.00, 'https://cdn.smartfb.vn/images/tra-dao-cam-sa.jpg', true, true),
('p1000000-0000-0000-0000-000000000004', 'c1000000-0000-0000-0000-000000000003', 'CAKE-CROISSANT', 'Bánh Croissant Bơ Tỏi', 'Bánh sừng bò ngàn lớp thơm lừng bơ Pháp và tỏi phi.', 32000.00, 'https://cdn.smartfb.vn/images/croissant.jpg', true, false)
ON CONFLICT (code) DO NOTHING;

INSERT INTO product_variants (id, product_id, name, sku, price_adjustment, is_default, is_active) VALUES
('v1000000-0000-0000-0000-000000000001', 'p1000000-0000-0000-0000-000000000001', 'Size M (Chuẩn)', 'CF-BACXIU-M', 0.00, true, true),
('v1000000-0000-0000-0000-000000000002', 'p1000000-0000-0000-0000-000000000001', 'Size L (+10K)', 'CF-BACXIU-L', 10000.00, false, true),
('v1000000-0000-0000-0000-000000000003', 'p1000000-0000-0000-0000-000000000002', 'Size M (Chuẩn)', 'CF-MUOI-M', 0.00, true, true),
('v1000000-0000-0000-0000-000000000004', 'p1000000-0000-0000-0000-000000000003', 'Size M (Chuẩn)', 'TEA-DAOCAMSA-M', 0.00, true, true),
('v1000000-0000-0000-0000-000000000005', 'p1000000-0000-0000-0000-000000000003', 'Size L (+8K)', 'TEA-DAOCAMSA-L', 8000.00, false, true)
ON CONFLICT (sku) DO NOTHING;

-- NGUYÊN LIỆU & ĐỊNH LƯỢNG MÓN (BOM)
INSERT INTO ingredients (id, code, name, unit, unit_cost, min_stock_level, is_active) VALUES
('i1000000-0000-0000-0000-000000000001', 'ING-COFFEE-ROBUSTA', 'Hạt Cà Phê Robusta Đăk Lăk', 'gram', 0.25, 5000.00, true),
('i1000000-0000-0000-0000-000000000002', 'ING-CONDENSED-MILK', 'Sữa Đặc Larose Extra', 'ml', 0.08, 3000.00, true),
('i1000000-0000-0000-0000-000000000003', 'ING-FRESH-MILK', 'Sữa Tươi Thanh Trùng Dalat', 'ml', 0.05, 10000.00, true),
('i1000000-0000-0000-0000-000000000004', 'ING-RICH-CREAM', 'Kem Béo Thực Vật Richs', 'ml', 0.12, 2000.00, true),
('i1000000-0000-0000-0000-000000000005', 'ING-PINK-SALT', 'Muối Hồng Himalaya Tinh Khiết', 'gram', 0.15, 500.00, true)
ON CONFLICT (code) DO NOTHING;

INSERT INTO recipes (id, product_id, variant_id, name, instructions) VALUES
('r1000000-0000-0000-0000-000000000001', 'p1000000-0000-0000-0000-000000000002', 'v1000000-0000-0000-0000-000000000003', 'Công Thức Cà Phê Muối Size M', 'Chiết xuất 45ml cà phê phin. Khuấy 20ml sữa đặc. Rót 30ml kem béo muối lên bề mặt.')
ON CONFLICT DO NOTHING;

INSERT INTO recipe_ingredients (id, recipe_id, ingredient_id, quantity_required) VALUES
('ri000000-0000-0000-0000-000000000001', 'r1000000-0000-0000-0000-000000000001', 'i1000000-0000-0000-0000-000000000001', 25.00),
('ri000000-0000-0000-0000-000000000002', 'r1000000-0000-0000-0000-000000000001', 'i1000000-0000-0000-0000-000000000002', 20.00),
('ri000000-0000-0000-0000-000000000003', 'r1000000-0000-0000-0000-000000000001', 'i1000000-0000-0000-0000-000000000004', 30.00),
('ri000000-0000-0000-0000-000000000004', 'r1000000-0000-0000-0000-000000000001', 'i1000000-0000-0000-0000-000000000005', 1.50)
ON CONFLICT (recipe_id, ingredient_id) DO NOTHING;

-- 3.4 KHÁCH HÀNG CRM & SỔ CÁI TÍCH LY
INSERT INTO customers (id, phone_number, full_name, cup_balance, total_spent, last_order_at) VALUES
('cust0000-0000-0000-0000-000000000001', '0901234567', 'Trần Khách Mới', 0, 0.00, NULL),
('cust0000-0000-0000-0000-000000000002', '0909123456', 'Nguyễn Hoàng Nam', 9, 345000.00, CURRENT_TIMESTAMP - INTERVAL '2 days'),
('cust0000-0000-0000-0000-000000000003', '0908888999', 'Lê Văn Tâm (Đủ 10 Ly)', 10, 420000.00, CURRENT_TIMESTAMP - INTERVAL '1 day')
ON CONFLICT (phone_number) DO NOTHING;

-- 3.5 ĐƠN HÀNG MẪU ĐẦY ĐỦ 3 LOẠI (DINE-IN, TAKEAWAY, DELIVERY)

-- [1] ĐƠN TẠI BÀN (DINE-IN PRE-PAY) - BÀN 05 ĐÃ THANH TOÁN VIETQR
INSERT INTO orders (id, branch_id, table_id, customer_id, order_number, order_type, status, subtotal, discount_amount, delivery_fee, total_amount, paid_at, notes) VALUES
('ord00000-0000-0000-0000-000000000001', 'b1000000-0000-0000-0000-000000000001', 't1000000-0000-0000-0000-000000000005', 'cust0000-0000-0000-0000-000000000001', 'ORD-20260417-0042', 'DineIn', 'Completed', 35000.00, 0.00, 0.00, 35000.00, CURRENT_TIMESTAMP - INTERVAL '30 minutes', 'Uống tại quán, ít đá')
ON CONFLICT (order_number) DO NOTHING;

INSERT INTO order_items (id, order_id, product_id, variant_id, quantity, unit_price, total_price, selected_options_json, notes, kds_status) VALUES
('oi000000-0000-0000-0000-000000000001', 'ord00000-0000-0000-0000-000000000001', 'p1000000-0000-0000-0000-000000000001', 'v1000000-0000-0000-0000-000000000001', 1, 35000.00, 35000.00, '{"sugar": "50%", "ice": "50%"}', 'Ít đá', 'Completed')
ON CONFLICT DO NOTHING;

INSERT INTO payments (id, order_id, payment_method, payment_status, amount, transaction_ref, paid_at) VALUES
('pay00000-0000-0000-0000-000000000001', 'ord00000-0000-0000-0000-000000000001', 'VietQR', 'Success', 35000.00, 'PAYOS_TRANS_998811', CURRENT_TIMESTAMP - INTERVAL '30 minutes')
ON CONFLICT DO NOTHING;

-- [2] ĐƠN MANG VỀ TẠI QUẦY (TAKEAWAY STAFF POS) - ĐỔI 1 LY FREE + TIỀN MẶT
INSERT INTO orders (id, branch_id, table_id, customer_id, order_number, order_type, status, subtotal, discount_amount, delivery_fee, total_amount, paid_at, notes) VALUES
('ord00000-0000-0000-0000-000000000002', 'b1000000-0000-0000-0000-000000000001', NULL, 'cust0000-0000-0000-0000-000000000003', 'ORD-20260417-0089', 'TakeAway', 'Paid', 78000.00, 35000.00, 0.00, 43000.00, CURRENT_TIMESTAMP - INTERVAL '15 minutes', 'Khách đổi 10 ly lấy 1 ly free')
ON CONFLICT (order_number) DO NOTHING;

INSERT INTO order_items (id, order_id, product_id, variant_id, quantity, unit_price, total_price, selected_options_json, notes, kds_status) VALUES
('oi000000-0000-0000-0000-000000000002', 'ord00000-0000-0000-0000-000000000002', 'p1000000-0000-0000-0000-000000000002', 'v1000000-0000-0000-0000-000000000003', 2, 39000.00, 78000.00, '{"sugar": "100%", "ice": "100%"}', 'Mang về đóng nắp kín', 'Preparing')
ON CONFLICT DO NOTHING;

INSERT INTO payments (id, order_id, payment_method, payment_status, amount, transaction_ref, paid_at) VALUES
('pay00000-0000-0000-0000-000000000002', 'ord00000-0000-0000-0000-000000000002', 'Cash', 'Success', 43000.00, 'CASH_POS_Q1_0089', CURRENT_TIMESTAMP - INTERVAL '15 minutes')
ON CONFLICT DO NOTHING;

INSERT INTO loyalty_cup_transactions (id, customer_id, order_id, cups_changed, balance_after, transaction_type, notes) VALUES
('lt000000-0000-0000-0000-000000000001', 'cust0000-0000-0000-0000-000000000003', 'ord00000-0000-0000-0000-000000000002', -10, 0, 'Redeem', 'Đổi 10 ly nhận 1 ly miễn phí'),
('lt000000-0000-0000-0000-000000000002', 'cust0000-0000-0000-0000-000000000003', 'ord00000-0000-0000-0000-000000000002', 2, 2, 'Earn', 'Tích 2 ly từ đơn mang về')
ON CONFLICT DO NOTHING;

-- [3] ĐƠN GIAO TẬN NƠI (QR DELIVERY) - PHÍ SHIP 20K + VIETQR TRẢ TRƯỚC
INSERT INTO orders (id, branch_id, table_id, customer_id, order_number, order_type, status, recipient_name, recipient_phone, delivery_address, delivery_fee, subtotal, discount_amount, total_amount, paid_at, notes) VALUES
('ord00000-0000-0000-0000-000000000003', 'b1000000-0000-0000-0000-000000000001', NULL, NULL, 'ORD-20260417-DEL15', 'Delivery', 'Confirmed', 'Chị Mai Hương', '0987654321', 'Tòa nhà Bitexco, Số 2 Hải Triều, P. Bến Nghé, Quận 1, TP.HCM', 20000.00, 70000.00, 0.00, 90000.00, CURRENT_TIMESTAMP - INTERVAL '5 minutes', 'Giao lên lầu 12 gặp lễ tân')
ON CONFLICT (order_number) DO NOTHING;

INSERT INTO order_items (id, order_id, product_id, variant_id, quantity, unit_price, total_price, selected_options_json, notes, kds_status) VALUES
('oi000000-0000-0000-0000-000000000003', 'ord00000-0000-0000-0000-000000000003', 'p1000000-0000-0000-0000-000000000001', 'v1000000-0000-0000-0000-000000000001', 2, 35000.00, 70000.00, '{"sugar": "70%", "ice": "70%"}', 'Giao xa để đá riêng', 'Pending')
ON CONFLICT DO NOTHING;

INSERT INTO payments (id, order_id, payment_method, payment_status, amount, transaction_ref, paid_at) VALUES
('pay00000-0000-0000-0000-000000000003', 'ord00000-0000-0000-0000-000000000003', 'VietQR', 'Success', 90000.00, 'PAYOS_TRANS_776655', CURRENT_TIMESTAMP - INTERVAL '5 minutes')
ON CONFLICT DO NOTHING;

-- 3.6 CHẤM CÔNG WIFI & CA LÀM VIỆC ĐỐI SOÁT
INSERT INTO work_shifts (id, branch_id, opened_by_user_id, start_time, initial_cash, system_cash, status) VALUES
('s1000000-0000-0000-0000-000000000001', 'b1000000-0000-0000-0000-000000000001', 'u1000000-0000-0000-0000-000000000002', CURRENT_TIMESTAMP - INTERVAL '4 hours', 2000000.00, 43000.00, 'Open')
ON CONFLICT DO NOTHING;

INSERT INTO attendances (id, user_id, branch_id, work_shift_id, check_in_time, client_ip, client_bssid, is_wifi_verified, status, notes) VALUES
('att00000-0000-0000-0000-000000000001', 'u1000000-0000-0000-0000-000000000004', 'b1000000-0000-0000-0000-000000000001', 's1000000-0000-0000-0000-000000000001', CURRENT_TIMESTAMP - INTERVAL '4 hours', '192.168.1.45', '00:14:22:01:23:45', true, 'Present', 'Chấm công thành công qua WiFi chi nhánh Q1')
ON CONFLICT DO NOTHING;