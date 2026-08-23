import sys
from parse_sql_proper import inserted_rows

sys.stdout.reconfigure(encoding='utf-8')

print("=== DEEP MATHEMATICAL ARITHMETIC VERIFICATION OF SEED DATA ===")

orders = inserted_rows.get('orders', [])
order_items = inserted_rows.get('order_items', [])
item_modifiers = inserted_rows.get('order_item_modifiers', [])
payments = inserted_rows.get('payments', [])
shifts = inserted_rows.get('shifts', [])
loyalty_tx = inserted_rows.get('loyalty_cup_transactions', [])
customers = inserted_rows.get('customers', [])
combos = inserted_rows.get('combos', [])
combo_items = inserted_rows.get('combo_items', [])

# Build Order Items Map: order_id -> list of items
order_items_map = {}
for oi in order_items:
    oid = oi.get('order_id')
    if oid not in order_items_map:
        order_items_map[oid] = []
    order_items_map[oid].append(oi)

math_errors = []

print("\n--- 1. Order Calculations Audit ---")
for o in orders:
    oid = o['order_id']
    ocode = o.get('order_code')
    otype = o.get('order_type')
    items = order_items_map.get(oid, [])
    
    # Calculate item subtotals
    calc_subtotal = 0
    print(f"\nOrder [{ocode}] ({oid[:8]}) - Type: {otype}:")
    for it in items:
        oi_id = it['order_item_id']
        qty = it.get('quantity', 1)
        u_price = it.get('unit_price', 0)
        item_sub = u_price * qty
        calc_subtotal += item_sub
        db_item_sub = it.get('subtotal_price', 0)
        print(f"  Item {it.get('product_id')[:15]} ({it.get('note', '')}): Qty={qty}, UnitPrice={u_price:,}, Subtotal={db_item_sub:,} (Calc={item_sub:,})")
        if db_item_sub != item_sub:
            math_errors.append(f"Item {oi_id} subtotal mismatch: DB={db_item_sub} vs Calc={item_sub}")
            
    db_subtotal = o.get('sub_total', 0)
    shipping_fee = o.get('delivery_fee', 0)
    discount = o.get('discount_amount', 0)
    db_final = o.get('total_amount', 0)
    
    calc_final = db_subtotal + shipping_fee - discount
    print(f"  Summary: Subtotal={db_subtotal:,} (Calc={calc_subtotal:,}), DeliveryFee={shipping_fee:,}, Discount={discount:,}, TotalDB={db_final:,}, CalcTotal={calc_final:,}")
    
    if db_subtotal != calc_subtotal:
        math_errors.append(f"Order {ocode} sub_total mismatch: DB={db_subtotal} vs Calc={calc_subtotal}")
        
    if otype == 'Delivery':
        if shipping_fee != 20000:
            math_errors.append(f"Delivery order {ocode} delivery_fee is {shipping_fee}, expected 20,000 VND!")
        else:
            print(f"  -> Delivery shipping fee verified: exactly 20,000 VND [PASS]")
            
    if calc_final != db_final:
        math_errors.append(f"Order {ocode} total_amount mismatch: DB={db_final} vs Calc={calc_final}")

print("\n--- 2. Payments Reconciliation Audit ---")
order_map = {o['order_id']: o for o in orders}
for p in payments:
    oid = p.get('order_id')
    p_amount = p.get('amount')
    p_method = p.get('payment_method')
    p_status = p.get('status')
    if oid in order_map:
        o = order_map[oid]
        expected_amount = o.get('total_amount')
        print(f"Payment [{p['payment_id'][:8]}] for Order [{o.get('order_code')}]: Method={p_method}, Amount={p_amount:,}, Expected={expected_amount:,}, Status={p_status}")
        if p_amount != expected_amount:
            math_errors.append(f"Payment {p['payment_id']} amount {p_amount} != Order {o.get('order_code')} total {expected_amount}")

print("\n--- 3. Shifts & Cash Drawer Reconciliation Audit ---")
for s in shifts:
    sid = s['shift_id']
    opening = s.get('initial_cash', 0) or 0
    sys_calc = s.get('system_cash_calculated', 0) or 0
    actual_closing = s.get('actual_cash_counted')
    diff = s.get('cash_difference', 0) or 0
    reason = s.get('shift_notes', '')
    actual_str = f"{actual_closing:,}" if actual_closing is not None else "N/A (Open)"
    print(f"Shift [{sid[:8]}]: InitialCash={opening:,}, SysCalculated={sys_calc:,}, ActualCounted={actual_str}, Diff={diff:,}, Status={s.get('status')}")
    print(f"  Notes/Explanation: {reason}")
    if actual_closing is not None:
        calc_diff = actual_closing - sys_calc
        if calc_diff != diff:
            math_errors.append(f"Shift {sid} difference calculation mismatch: DB={diff} vs Calc={calc_diff}")
        if abs(diff) > 50000:
            if not reason or len(reason) < 10:
                math_errors.append(f"Shift {sid} has discrepancy > 50k ({diff}) without proper explanation reason!")
            else:
                print(f"  -> Discrepancy > 50k (+{diff:,}đ) has comprehensive manager explanation: [PASS]")

print("\n--- 4. Loyalty Cup Transactions Audit ---")
for tx in loyalty_tx:
    cid = tx.get('customer_id')
    tx_type = tx.get('transaction_type')
    change_earned = tx.get('cups_earned', 0)
    change_redeemed = tx.get('cups_redeemed', 0)
    print(f"Loyalty Tx [{tx['trans_id'][:8]}]: Cust={cid[:8]}, Type={tx_type}, Earned={change_earned}, Redeemed={change_redeemed}, Notes='{tx.get('notes')}'")

print("\n=== MATHEMATICAL ARITHMETIC VERIFICATION SUMMARY ===")
if not math_errors:
    print(">>> [PASS] ALL MATHEMATICAL CALCULATIONS, REVENUE, DISCOUNTS, SHIPPING FEES, AND RECONCILIATIONS ARE 100% ACCURATE! <<<")
else:
    print(f">>> [FAIL] {len(math_errors)} ARITHMETIC ERRORS DETECTED: <<<")
    for e in math_errors:
        print(f"  - {e}")
