const fs = require('fs');
const path = require('path');

const dir = 'd:/Idea_DoAn/03_Quy_Trinh_Trien_Khai';
const files = [
  '01_Phan_Tich_Yeu_Cau.md',
  '02_Thiet_Ke_Database.md',
  '03_Thiet_Ke_API_Contract.md',
  '04_Thiet_Ke_UI_UX.md',
  '05_Quy_Trinh_Backend.md',
  '06_Quy_Trinh_Frontend.md',
  '07_Ke_Hoach_Kiem_Thu.md',
  '08_Trien_Khai_He_Thong.md',
  'README.md'
];

console.log('=== VERIFYING 4 CORE BUSINESS ENGINES ACROSS ALL 9 FILES ===\n');

const engineVerifications = {
  'Engine 1: Dine-In (Branch A Prepay vs Branch B Postpay + Bill QR)': {
    keywords: ['Branch A', 'Branch B', 'Dine-In', 'Bill QR', 'Trả trước', 'Trả sau'],
    checkFile: (content) => {
      const c = content.toLowerCase();
      const hasDineIn = c.includes('dine-in') || c.includes('dinein') || c.includes('tại bàn');
      const hasBranchA = c.includes('chi nhánh a') || c.includes('nhánh a') || c.includes('prepay') || c.includes('trả trước');
      const hasBranchB = c.includes('chi nhánh b') || c.includes('nhánh b') || c.includes('postpay') || c.includes('bill qr') || c.includes('trả sau');
      return hasDineIn && (hasBranchA || hasBranchB);
    }
  },
  'Engine 2: Delivery (20,000 VND fee, 100% VietQR, No COD, Phone+Address)': {
    keywords: ['20.000', '20000', 'Delivery', 'VietQR', 'COD', 'delivery_address', 'delivery_fee'],
    checkFile: (content) => {
      const c = content.toLowerCase();
      const hasDelivery = c.includes('delivery') || c.includes('giao hàng');
      const hasFeeOrQR = c.includes('20.000') || c.includes('20000') || c.includes('delivery_fee') || c.includes('vietqr');
      return hasDelivery && hasFeeOrQR;
    }
  },
  'Engine 3: Takeaway POS (Quầy, Phone CRM, 10 Cups Loyalty, Postpay)': {
    keywords: ['Takeaway', 'Quầy', '10 ly', 'CRM', 'loyalty_cup_transactions', 'cups_earned', 'cups_redeemed'],
    checkFile: (content) => {
      const c = content.toLowerCase();
      const hasTakeaway = c.includes('takeaway') || c.includes('mang đi') || c.includes('pos');
      const hasLoyalty = c.includes('10 ly') || c.includes('loyalty') || c.includes('tích ly') || c.includes('crm');
      return hasTakeaway && hasLoyalty;
    }
  },
  'Engine 4: WiFi Attendance (BSSID + IP Subnet + PIN, No GPS/30s QR)': {
    keywords: ['BSSID', 'IP Subnet', 'Chấm công', 'branch_wifi_configs', 'attendances', 'Mã NV'],
    checkFile: (content) => {
      const c = content.toLowerCase();
      const hasWifi = c.includes('bssid') || c.includes('branch_wifi_configs') || c.includes('ip subnet') || c.includes('chấm công');
      const hasAttendance = c.includes('attendance') || c.includes('chấm công');
      return hasWifi && hasAttendance;
    }
  }
};

files.forEach(f => {
  const content = fs.readFileSync(path.join(dir, f), 'utf8');
  console.log(`\n📄 [${f}]`);
  Object.keys(engineVerifications).forEach(engName => {
    const passed = engineVerifications[engName].checkFile(content);
    console.log(`   ${passed ? '✅' : '⚠️'} ${engName}`);
  });
});
