const fs = require('fs');
const path = require('path');
const dir = 'd:/Idea_DoAn/03_Quy_Trinh_Trien_Khai';

console.log('=== ADVERSARIAL CRITIC VERIFICATION ===\n');

const scenarios = [
  {
    name: '1. Concurrency Race on Inventory / RedLock',
    files: ['05_Quy_Trinh_Backend.md'],
    pattern: /RedLock|Distributed.*Lock|lock:ingredient|lock:order/i
  },
  {
    name: '2. PayOS Webhook HMAC SHA256 Signature & Idempotency',
    files: ['03_Thiet_Ke_API_Contract.md', '05_Quy_Trinh_Backend.md'],
    pattern: /HMAC|SHA256|webhook|signature|Idempotent/i
  },
  {
    name: '3. WiFi Dual-Check Anti-Spoofing (BSSID + IP Subnet + PIN)',
    files: ['01_Phan_Tich_Yeu_Cau.md', '03_Thiet_Ke_API_Contract.md', '05_Quy_Trinh_Backend.md'],
    pattern: /BSSID.*IP\s*Subnet|RemoteIpAddress|Dual-Check/i
  },
  {
    name: '4. Order TTL Expiration Worker & Table Release',
    files: ['05_Quy_Trinh_Backend.md'],
    pattern: /OrderTtlExpirationWorker|BackgroundService|TTL.*10\s*phút|Cancelled/i
  },
  {
    name: '5. Takeaway-Only Loyalty Cup Atomic Balance Check',
    files: ['01_Phan_Tich_Yeu_Cau.md', '02_Thiet_Ke_Database.md', '05_Quy_Trinh_Backend.md'],
    pattern: /LoyaltyCup|10\s*ly.*đổi\s*1|cups_earned|cups_redeemed/i
  },
  {
    name: '6. Delivery Strict 20k Fee & COD Lock Validation',
    files: ['01_Phan_Tich_Yeu_Cau.md', '03_Thiet_Ke_API_Contract.md', '05_Quy_Trinh_Backend.md'],
    pattern: /delivery_fee.*20\.?000|khóa\s*COD|prepaid.*delivery/i
  }
];

scenarios.forEach(sc => {
  console.log(`Checking Scenario [${sc.name}]:`);
  sc.files.forEach(f => {
    const content = fs.readFileSync(path.join(dir, f), 'utf8');
    const matched = sc.pattern.test(content);
    console.log(`  - File ${f}: ${matched ? '✓ DEFENSE VERIFIED' : '✗ DEFENSE GAP'}`);
  });
});
