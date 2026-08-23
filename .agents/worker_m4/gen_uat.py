# -*- coding: utf-8 -*-
import os

target = 'd4Idea_DoAn/05_Quy_Chuan_&_Test_Cases/UAT_Test_Cases.md'
os.makedirs(os.path.dirname(target), exist_ok=True)

with open(target, 'w', encoding='utf-8') as f:
    f.write('''---
# üìñ T√Ä Li·ªÜU B√ÇPN B·∫†N DEMO & B·ªô TEST CASES NGHI·ªÜ] THU UAT (USER ACCEPTANCE-TESTING)
## H·ªô TH·ªêNG QU·∫†N L√Ω V√Ä V·∫¨N H√ÇM QU√ÅN C√Ä PH√™ TH√ëNG MINH SMART F&B OS

> **Ph√™√™n b·∫£n:** v2.0.0 (Production Grade & Formal Capstone Defense)  
> **D·ª± √°n:** Smart F&B Operating System (AI-Powered QR Order & Management Platform)  
> **T√†i li·ªáu tham chi·∫øu:** `PROJECT.md`, `Smart_FBGOS_Revised_4members.docx`, `technical_contracts.md`  
> **M·ª•c ti√™u:** Cung c·∫•p k·ªãch b·∫£n Demo ho√†n ch·ªânh 5 ph√∫t k·∫•t n·ªëi li√™n h√†n c√°c ph√¢n h·ªá v√† b·ªô h∆°n 30 k·ªãch b·∫£n ki·ªÉm th·ª≠ nghi·ªám thu ng∆∞·ªùi d√πng (UAT Test Cases) bao ph·ªß 100% √°c lu·ªìng nghi·ªáp v·ª• c·ªët l√µi v√† c√°c t√¨nh hu·ªëng bi√™n (Edge Cases).

---

## üìó M·ªåC L·ªåC

1. [T·ªîNG QUAN PH·∫†M VI NGHI·ªÜM THU UAT](#1-t·ªïng-quan-ph·∫°m-vi-nghi·ªám-thu-uat)
2. [K·ªãCH B·∫£N DEMO H·ªòI ƒê·ªÇNG B·∫¢O V·ªÜ CAPSTONE (5 PH√öT END-TO-END)](#2-k·ªãch-b·∫£n-demo-h·ªôi-ƒë·ªìng-b·∫£o-v·ªá-capstone-5-phut-end-to-end)
3. [MA TR·ªÜN KI·ªÇM TH·ª¨ NGHI·ªÜ] THU (UAT TEST MATRIX)](#3-ma-tr·ªán-ki·ªÇm-th·ª≠-nghi·ªám-thu-uat-test-matrix)
4. [B·ªô TEST CASES UAT CHI TI·∫æT THEO PH√äSH H·ªÜ](#4-b·ªô-test-cases-uat-chi-ti·∫øt-theo-ph√¢n-h·ªá)
   - [4.1 Ph√¢n h·ªá X√°c th·ª±c & Ph√¢n quy·ªÅn (Auth & RBAC)](#41-ph√¢n-h·ªá-x√°c-th·ª±c---ph√¢n-quy·ªÅn-auth---rbac)
   - [4.2 Ph√¢n h·ªá Th·ª±c ƒë∆°n & T√πy bi·∫øn m√≥n (Menu & Modifiers)](#42-ph√¢n-h·ªáth·ª±c-ƒë∆°n---t√πy-bi·∫øn-m√≥n-menu--modifiers)
   - [4.3 Ph√¢n h·ªá ƒê·∫∑t m√≥n T·∫°i b√†n (Dine-in Pre-Payment Flow)](#43-ph√¢n-h·ªá-ƒê·∫∑t-m√≥n-t·∫°i-b√†n-dine-in-pre-payment-flow)
   - [4.4 Ph√¢n h·ªá ƒê·∫∑t h√†ng Giao t·∫≠n n∆°i (QR Delivery Flow)](#44-ph√¢n-h·ªá-ƒê·∫∑t-h√†ng-giao-t·∫≠n-n∆°i-qr-delivery-flow)
   - [4.5 Ph√¢n h·ªá B√°n h√†ng Mang v·ªÅ t·∫°i Qu·∫ßy & T√≠ch Ly (Takeaway POS & Loyalty 10 Cups)](#45-ph√¢n-h·ªá-b√°n-h√†ng-mang-v·ªã-t·∫°i-qu·∫ßy---t√≠ch-ly-takeaway-pos---loyalty-10-cups)
   - [4.6 Ph√¢n h·ªá Ch·∫•m c√¥ng Kh√°a m·∫°ng WiFi (WiFi-Locked Attendance)](#46-ph√¢n-h·ªá-ch·∫•m-c√¥ng-kh√°a-m·∫°ng-wifi-wifi-locked-attendance)
   - [4.7 Ph√¢n h·ªá ƒêi·ªÅu ph·ªëi B·∫øp (Web KDS Real-time Flow)](#47-ph√¢n-h·ªá- ƒëi·ªÅu-ph·ªëi-b·∫øp-web-kds-real-time-flow)
   - [4.8 Ph√¢n h·ªá Qu·∫£n l√Ω Ca & ƒê·ªëi so√°t K√©t ti·ªÅn (Shift & Cash Drawer Reconciliation)](#48-ph√¢n-h·ªá-qu·∫£n-l√Ω-ca---ƒê·ªëi-so√°t-k√©t-ti·ªÉn-shift---cash-drawer-reconciliation)
   - [4.9 Ph√¢n h·ªá ƒê√°nh gi√° & Ph·∫£n h·ªìi Kh√°ch h√†ng (Reviews & Feedback Moderation)](#49-ph√¢n-h·ªá-ƒê√°nh-gi√°---ph·∫£n-h·ªìi-kh√°ch-h√†nw-reviews---feedback-moderation)
   - [4.10 Ph√¢n h·ªá Tr√≠ tu·ªá Nh√¢n t·∫°o (AI-1 Chatbot & AI-2 Combo Engine)](#410-ph√¢n-h·ªá-tr√≠-tu·ªá-nh√¢n-t·∫°o-ai-1-chatbot---ai-2-combo-engine)
   - [4.11 Ph√¢n h·ªá T√¨nh hu·ªëng Bi√™n & An ninh Ngo·∫°i l·ªá (Edge Cases & Resilience)](#411-ph√¢n-h·ªát√≠ng-hu·ªëng-bi√™n---an-ninh-ngo·∫°i-l·ªá-Âdge-cases---resilience)
5. [TI√äU CH√ç ƒê«6NH GI√Å NGHI·ªÜ] THU & B√ÇM8Å%<Ä°AQ9Å	I%QI%•t†å‘µ—ß©‘µç£¥∑GÖπ†µùßÑµπù°ßÜÓ¥µ—°‘¥¥µãÅ∏µù•ÖºµÖççï¡—Öπçîµç…•—ï…•Ñ§4(4(¥¥¥4(4(ååÄƒ∏ÅSÜÓU9ÅEU8ÅA#ÜÍ4ÅY$Å9!'ÜÓ4ÅQ!TÅUP4(4)-ßÜÓ¥Å—£ÜÓ¥Åπù°ßÜÓ¥Å—°‘Åπü√ÜÓu§ÅìÂπúÄ°UP§ÅèÜÓùÑÅMµÖ…–Åô	=LÉG√ÜÓçåÅ—°ßÜÍ˝–ÅØÜÍ¸Åπ£ÜÍ≈¥Å„ÖåÅµ•π†Å”µπ†ÉGÈπúÉGÜÍΩ∏ÅèÜÓùÑÅ—øÅ∏ÅãÜÓdÅ≈’‰Å—À±π†Å€ÜÍµ∏Å£Åπ†Åç°◊ÜÓ]§ÅôÅìÜÓ≈ÑÅ—À©∏Ä‘Å—°Ö‰ÉGÜÓU§Åπù°ßÜÓ¿Å€ÜÓîÅªÜÓ∏Å”ÜÍçπúË4(¥Ä®©•πîµ•∏ÅA…îµAÖÂµïπ–®®ËÅ-£Öç†Å≈◊•–ÅEHÅãÅ∏Ä¥¯Åë’ÁÜÓ–Åµïπ‘Å”Â‰ÅâßÜÍ˝∏Å∑Õ∏Ä¥¯Å—°Öπ†Å—øÖ∏ÅY•ï—EHÅ—À√ÜÓmåÄ¥¯Å]ïâ°ΩΩ¨ΩAΩ±±•πúÅ„ÖåÅπ£ÜÍµ∏Å—ßÜÓ∏Å€ÜÓÄ¥¯Å-LÅÜÍ˝¿Å∑ÜÓm§Åπ£ÜÍµ∏ÉGÖ∏Å≈’ÑÅM•ùπÖ±HÄ°±øÜÍÖ§ÅãÜÓ<Å°øÅ∏Å—øÅ∏Å±◊ÜÓMπúÅÁÖ‘ÅèÜÍù‘Åâ•±∞Å€ÄÅ—°Öπ†Å—øÖ∏ÅÕÖ‘§π∏4(¥Ä®©EHÅï±•Ÿï…‰®®ËÅ-£Öç†Å≈◊•–Å∑åÅEHÅï±•Ÿï…‰Ä°¡ΩÕ—ï»ΩôÖπ¡ÖùîΩÕ—Öπëïî§Ä¥¯ÅA]Å∑ÜÓ|Åç£ÜÍÅìÜÓdÅù•ÖºÅ”ÜÍµ∏ÅªÖ§Ä¥¯ÅãÜÍΩ–Åâ◊ÜÓeåÅπ£ÜÍµ¿ÅOAPÅ€ÄÉCÜÓ-ÑÅç£ÜÓ$Åù•ÖºÅ£ÅπúÅç°§Å—ßÜÍ˝–Ä¥¯Å”ÜÓƒÉGÜÓeπúÅèÜÓeπúÅ¡£¥ÅÕ°•¿ÅèÜÓDÅÉÕπ†Ä®®»¿∏¿¿¿ÅY;@®®Ä¥¯Å—°Öπ†Å—øÖ∏Äƒ¿¿îÅY•ï—EHÅ—ÀÜÍåÅ—À√ÜÓmåÄ°-£—πúÅ=§∏4(¥Ä®©QÖ≠ïÖ›Ö‰ÅM—ÖôòÅA=LÄòÅ1ΩÂÖ±—‰Äƒ¿Å1‰®®ËÅQ°ÖºÅ”ÖåÅ°øÅ∏Å—øÅ∏Å—À©∏Åù•ÖºÅëßÜÓ∏Å]ïàÅA=LÅ—°‘Åπüâ∏Ä°±øÜÍÖ§ÅãÜÓ<ÅEHÅQÖ≠ïÖ›Ö‰Åè®§∞Å—…ÑÅèÜÓ•‘ÅOAPÅI4∞ÉÖ¿ÅìÜÓïπúèÑÅç£ÜÍ¸ÉGÜÓU§ÄƒÅ±‰ÅµßÜÓ∏Å¡£¥Å≠°§Å”µç†ÉGÜÓúÄƒ¿Å±‰Ä°Å’¡Ω’π–ÄîÄƒ¿ÄÙÙÄ¡Ä§∞Å—°Öπ†Å—øÖ∏Å±•π†Å°øÜÍÖ–ÅÕÖ‘Å≠°§Åπù£ÜÍµ∏Å∑Õ∏Ä°QßÜÓ∏Å∑ÜÍ›–ÅèÃÅ”µπ†Å—ßÜÓ∏Å—£≈§Å°øÜÍ›åÅY•ï—EHÅ≈◊ÜÍù‰§∏4(¥Ä®©]•§µ1Ωç≠ïêÅ——ïπëÖπçî®®ËÅcÖåÅ—£ÜÓ≈åÅç£ÜÍV‘Åè—πúÄ»Å≥ÜÓm¿ÅãÜÍ≈πúÅ	MM%ÄºÅM’âπï–Å%@ÅèÜÓùÑÅ∑ÜÍÖπúÅ]•§Åç°§Åπ£Öπ†Å€ÄÅ7åÅœÜÓDÅπ£â∏ÅŸß©∏Ä°±øÜÍÖ§ÅãÜÓ<Å°øÅ∏Å—øÅ∏ÅALÄ‘¡¥Å€ÄÅEHÅ·ΩÖ‰ÄÃ¿Åùßâ‰§∏4(¥Ä®©#ÜÓç¿Åπ£ÜÍï–Å]ïàÅM—Öç¨®®ËÅQøÅ∏ÅãÜÓdÅπù°ßÜÓ¿Å€ÜÓîÅπ£â∏ÅŸß©∏Å¡£ÜÓïåÅ€ÜÓî∞Å—°‘Åπüâ∏∞ÅâÖ…•Õ—ÑÅ€ÄÅ≈◊ÜÍç∏Å≥ÙÅ”µç†Å£ÜÓç¿Å—…ΩπúÅèÖåÅ]ïàÅAΩ…—Ö±ÃÅIïÕ¡ΩπÕ•ŸîÅ9ï·–π©ÃÄƒ–Ä°±øÜÍÖ§ÅãÜÓ<Å°øÅ∏Å—øÅ∏ÅM—ÖôòÅ5Ωâ•±îÅ¡¿Å…ß©πúÅâßÜÓ–§∏4(ààú§4(