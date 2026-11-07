# 13 Shipping fee bands Easy • ~8 min
# Write `shipping_fee(order_total)` using: free for orders 1500; 80 for orders 500 but < 1500; 150 for ≥ ≥
# orders < 500. Assume non-negative order totals.
# SAMPLE INPUT / OUTPUT
# shipping_fee(2000) -> 0
# shipping_fee(500) -> 80
# shipping_fee(499) -> 150

def shipping_fee(order_total):
    if order_total <500:
        return 150
    elif order_total >=1500:
        return 0
    else:
        return 80

print(shipping_fee(2000))
print(shipping_fee(500))
print(shipping_fee(150))