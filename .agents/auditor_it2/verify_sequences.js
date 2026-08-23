const fs = require('fs');
const path = require('path');

const doc02Path = 'd:\\Idea_DoAn\\04_Thiet_Ke_Kien_Truc_Diagrams\\02_Sequence_Diagrams.md';
const content = fs.readFileSync(doc02Path, 'utf8');

const expectedSequences = [
  { id: 'Seq-01', name: 'Dine-In Nhánh A (VietQR trả trước -> PayOS Webhook -> KDS Bếp)' },
  { id: 'Seq-02', name: 'Dine-In Nhánh B (Tiền mặt trả sau / In Bill kèm VietQR -> Thu tiền sau)' },
  { id: 'Seq-03', name: 'QR Delivery (Form SĐT + Địa chỉ, Phí ship 20k, 100% VietQR trước)' },
  { id: 'Seq-04', name: 'Takeaway Web POS (NV thao tác tại quầy, CRM SĐT, Tích 10 ly đổi 1 ly)' },
  { id: 'Seq-05', name: 'Chấm công Khóa mạng WiFi (BSSID Router / IP Subnet + Mã NV)' },
  { id: 'Seq-06', name: 'Điều phối KDS Bếp, Trừ kho định mức BOM & Công tắc khẩn cấp 86-Toggle' },
  { id: 'Seq-07', name: 'Gọi phục vụ tại bàn & Tiếp nhận chuông báo trên Web Staff/KDS' },
  { id: 'Seq-08', name: 'Đánh giá món 1-5 sao, Tải ảnh & Kích hoạt Alert đỏ Quản lý khi <= 2 sao' },
  { id: 'Seq-09', name: 'Mở ca két tiền, Quản lý kho, Kết ca đối soát Z-Report (giải trình khi lệch > 50k)' },
  { id: 'Seq-10', name: 'Admin CRUD Menu, BOM từng size, Lên lịch Seasonal Menu & Phê duyệt AI Combo' }
];

console.log('=== VERIFYING 10 SEQUENCE DIAGRAMS IN 02_Sequence_Diagrams.md ===');

const foundSeqs = [];

expectedSequences.forEach(seq => {
  const hasSeq = content.includes(seq.id);
  // Check sequence diagram block
  const reg = new RegExp(`(?:#|##)\\s*\\d+\\.\\s*${seq.id}[\\s\\S]*?\`\`\`mermaid\\r?\\nsequenceDiagram([\\s\\S]*?)\`\`\``, 'i');
  const match = content.match(reg);
  
  const hasDiagram = !!match;
  const lineCount = match ? match[1].trim().split('\n').length : 0;
  
  console.log(`- ${seq.id}: ${seq.name}`);
  console.log(`  Found Header: ${hasSeq ? 'YES' : 'NO'}, Has SequenceDiagram Block: ${hasDiagram ? 'YES' : 'NO'} (${lineCount} lines)`);
  
  foundSeqs.push({
    id: seq.id,
    name: seq.name,
    hasHeader: hasSeq,
    hasDiagram,
    diagramLines: lineCount
  });
});

const all10Valid = foundSeqs.every(s => s.hasHeader && s.hasDiagram && s.diagramLines > 10);
console.log(`\nAll 10 Sequence Diagrams Fully Specified: ${all10Valid}`);

fs.writeFileSync('d:\\Idea_DoAn\\.agents\\auditor_it2\\sequence_audit_results.json', JSON.stringify({
  all10Valid,
  sequences: foundSeqs
}, null, 2), 'utf8');
