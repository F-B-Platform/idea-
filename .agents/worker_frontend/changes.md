# Smart F&B Operating System — Frontend Implementation Changes Log

**Agent**: `worker_frontend` (Lead Frontend Engineer)  
**Date**: 2026-08-25  
**Scope**: 100% Zero-Placeholder Next.js 14 App Router Frontend Scaffolding across all 5 Core Pillars  
**Verification Result**: `npm --prefix frontend run typecheck` & `npm --prefix frontend run build` passed with Exit Code 0 (30/30 routes compiled).

---

## 1. Domain Types & Contract Definitions (`frontend/src/types/index.ts`)
- Complete TypeScript enums: `OrderType`, `OrderStatus`, `PaymentMethod`, `PaymentStatus`, `UserRole`, `TableStatus`, `SugarLevel`, `IceLevel`.
- Standard RFC 7807 problem details (`ProblemDetails`, `ApiResponse<T>`, `PagedResponse<T>`).
- Domain interfaces: `AuthUser`, `LoginRequestDto`, `LoginResponseDto`, `ProductDto`, `ProductSizeDto`, `ProductModifierDto`, `ProductBOMItemDto`, `CategoryDto`, `SeasonalMenuDto`, `PriceGroupDto`, `OrderItemDto`, `OrderDto`, `CustomerDto`, `KdsTicketDto`, `Product86ToggleDto`, `TableDto`, `CashDenominationCount`, `ShiftDto`, `ZReportDto`, `StockAuditItemDto`, `WifiConfigDto`, `AttendanceRecordDto`, `ReviewDto`, `ComboCandidateDto`, `PlSummaryDto`, `BcgMatrixItemDto`, `AuditLogDto`.

---

## 2. Core Libraries & Utilities (`frontend/src/lib/`)
- `utils.ts`:
  - `cn(...)`: Tailwind class merger.
  - `formatCurrencyVND(...)`: Formats integer currency to Vietnamese Dong (`xx.xxx ₫`).
  - `formatDateTime(...)`: Formats ISO timestamps to `DD/MM/YYYY HH:mm`.
  - `calculateSlaStatus(...)`: Computes SLA color coding (<3m Green, 3-5m Amber, >5m Red pulsing).
  - `validateVietnamesePhone(...)`: 10-digit Vietnamese carrier prefix regex.
  - `generateEscPosReceipt(...)`: Generates ASCII 80mm thermal receipt structure.
  - `compressImageToWebP(...)`: Client-side Canvas image compressor (max 1024px, 80% quality WebP).
- `api-client.ts`: Typed fetch wrapper with JWT bearer token auto-injection and RFC 7807 error parsing.
- `signalr.ts`: SignalR HubConnection factory with automatic retry backoff for `/hubs/orders`, `/hubs/kitchen`, `/hubs/payments`, `/hubs/notifications`.

---

## 3. Zustand Global State Stores (`frontend/src/stores/`)
- `useAuthStore.ts`: Authentication state, user role permissions, localStorage sync.
- `useCartStore.ts`: Multi-size, sugar/ice level & modifier cart calculations, Dine-in vs Delivery branching (auto +20,000₫ shipping fee & 100% VietQR payment lock).
- `usePosStore.ts`: Takeaway POS cashier state, CRM phone lookup, 10-cup loyalty stamp progress, free drink redemption (-35,000₫), cash tender & change calculator.
- `useShiftStore.ts`: 6-denomination cash counter (500k to 10k), theoretical vs physical cash variance calculation, mandatory justification reason if variance != 0.
- `useKdsStore.ts`: KDS tickets stream, station filtering (`ALL`, `BAR`, `KITCHEN`), batching aggregation, live 1-second elapsed timer ticker.
- `useTableStore.ts`: Floor partitioning, table status state machine (`Available`, `Occupied_Paid`, `Occupied_PendingPayment`, `ServiceRequested`), service bell alert counter & sound dismissal.

---

## 4. Custom React Hooks (`frontend/src/hooks/`)
- `useSignalR.ts`: Dynamic WebSocket hub group joining and real-time event listener binding.
- `useWebAudio.ts`: Real Web Audio API synthesizer for 880-1174Hz sine (new ticket chime), 440Hz square 3-pulse (overdue >5m alert), and 587Hz chime (service bell).
- `useAttendanceWifi.ts`: Router BSSID & subnet IP verification probe for dual-lock attendance clock-in/out.
- `useApiQuery.ts`: Reactive data fetching and mutation wrapper hooks.

---

## 5. UI Components System (`frontend/src/components/`)
- **Atomic UI Atoms (`components/ui/`)**:
  - `Button.tsx`: Variants (`primary`, `secondary`, `outline`, `ghost`, `danger`, `amber`, `dark`), sizes (`sm`, `md`, `lg`), loading spinner, touch targets >= 44px.
  - `Input.tsx`: Floating label, error state, helper text.
  - `SearchInput.tsx`: Search icon with 1-click clear button.
  - `Textarea.tsx`: Multiline input with error state.
  - `Badge.tsx`: Semantic variants (`success`, `warning`, `danger`, `info`, `neutral`, `amber`).
  - `Switch.tsx`: Accessible toggle switch.
  - `Slider.tsx`: Range slider with value display.
  - `Modal.tsx`: Accessible dialog with backdrop blur and escape dismissal.
  - `Drawer.tsx`: Bottom sliding sheet for mobile customizations.
  - `Table.tsx`: Full table sub-components.
  - `Toast.tsx`: Notification alert banner.
- **Domain Specific Components**:
  - `order/`: `OrderCard.tsx`, `ModifierSelector.tsx`, `CustomizationDrawer.tsx`, `LiveStepper.tsx`.
  - `kds/`: `KdsTicketCard.tsx`, `BomRecipeModal.tsx`, `Emergency86Modal.tsx`, `BatchActionModal.tsx`.
  - `pos/`: `CrmLookupBar.tsx`, `LoyaltyProgress.tsx`, `CashTenderCalculator.tsx`, `ReceiptPrint.tsx`.
  - `manager/`: `DenominationCounter.tsx`, `ZReportPrint.tsx`, `StockAuditTable.tsx`, `WifiConfigModal.tsx`.
  - `admin/`: `ComboApprovalCard.tsx`, `SeasonalScheduler.tsx`, `PricingMatrixTable.tsx`, `PlSummaryCard.tsx`.
  - `layout/`: `CustomerNavbar.tsx`, `StaffSidebar.tsx`, `ManagerSidebar.tsx`, `AdminSidebar.tsx`, `Navbar.tsx`, `StatusBadge.tsx`.

---

## 6. Next.js 14 App Router Route Groups (`frontend/src/app/`)
- `page.tsx`: Central workspace directory portal linking to all 5 operational roles.
- `(customer)`:
  - `layout.tsx`: Mobile-first customer shell with `CustomerNavbar`.
  - `table/[tableId]/page.tsx`: Table QR Dine-in digital menu with category tabs, customization drawer, floating cart bar.
  - `menu/page.tsx`: Digital menu browsing page.
  - `cart/page.tsx`: Shopping cart with Dine-in payment branching (Prepaid VietQR vs Postpaid Cash) and vouchers.
  - `checkout/vietqr/page.tsx`: Dynamic VietQR with 10-minute countdown, bank transfer details, 1-tap copy, SignalR payment auto-redirect, wrapped in `<Suspense>`.
  - `delivery/page.tsx`: QR Delivery form with 10-digit VN phone validation, flat 20,000₫ delivery fee, and locked 100% VietQR payment.
  - `tracking/[orderId]/page.tsx`: Real-time order progress stepper, queue position, 60s debounced service call bell button, E-Receipt view.
  - `review/[orderId]/page.tsx`: 1-5 star review, WebP photo upload (max 3), <= 2 star Red Alert protocol.
  - `history/page.tsx`: Order history lookup by phone & 1-tap reorder.
  - `ai-chat/page.tsx`: AI-1 Gemini drink recommendation chatbot with direct cart integration.
- `(kds)`:
  - `layout.tsx`: Dark mode `#0F172A` layout for kitchen TV displays.
  - `kitchen/page.tsx`: Real-time Kanban board, SLA color timers, Web Audio synthesizer, station filters, BOM modal, 86-toggle modal trigger.
  - `86-toggle/page.tsx`: Emergency out-of-stock management screen.
  - `batch/page.tsx`: KDS batch preparation view.
- `(staff)`:
  - `layout.tsx`: Staff portal shell with `StaffSidebar`.
  - `pos/page.tsx`: Takeaway Web POS, CRM phone lookup, 10-cup loyalty stamp progress, free drink redemption, cash calculator, thermal receipt modal.
  - `tables/page.tsx`: Floor plan table map, service bell alert dismissal, 587Hz chime.
  - `attendance/page.tsx`: WiFi-locked attendance clock-in/out with BSSID and Subnet IP verification.
  - `shift-report/page.tsx`: End-of-shift handover report.
- `(manager)`:
  - `layout.tsx`: Manager portal shell with `ManagerSidebar`.
  - `branch-dashboard/page.tsx`: Branch KPI overview, payment breakdown, low stock alerts.
  - `shifts/page.tsx`: Cash shift open/close with 6-denomination counter, automated variance calculation, and Z-Report.
  - `inventory/page.tsx`: BOM inventory management, supplier goods receipt note with photo, internal bar stock transfer, theoretical vs physical audit table (>3% wastage alert).
  - `wifi-configs/page.tsx`: Branch router BSSID & subnet IP registration.
  - `reviews/page.tsx`: Urgent <= 2 star review inbox (Red Alert) & customer photo moderation.
- `(admin)`:
  - `layout.tsx`: Admin portal shell with `AdminSidebar`.
  - `admin-dashboard/page.tsx`: Consolidated multi-branch P&L dashboard with `PlSummaryCard`, BCG matrix analysis.
  - `menu/products/page.tsx`: Multi-size BOM & Product CRUD.
  - `menu/categories/page.tsx`: Category management with display order sorting.
  - `menu/seasonal/page.tsx`: Seasonal menu campaign scheduler with start/end dates.
  - `pricing/page.tsx`: Regional pricing matrix.
  - `ai/combos/page.tsx`: Apriori AI-2 combo mining runner, dynamic discount slider (5%-30%), real-time profit margin projection, human-in-the-loop approval.
  - `crm/page.tsx`: Customer CRM directory, RFM segmentation.
  - `audit-logs/page.tsx`: Immutable audit trail viewer.
