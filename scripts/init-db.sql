-- ==============================================================================
-- SMART F&B OS - INITIAL DATABASE CONFIGURATION SCRIPT
-- ==============================================================================

-- Enable UUID extension for unique primary keys
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Enable pg_trgm for full-text search on product names and descriptions
CREATE EXTENSION IF NOT EXISTS "pg_trgm";

-- Grant basic privileges
GRANT ALL PRIVILEGES ON DATABASE smart_fb_db TO postgres;
