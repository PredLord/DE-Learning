# 04 Calculate compound growth Easy • ~8 min
# Write `future_value(principal, annual_rate_percent, years)` for annual compounding. Return the future
# amount rounded to 2 decimals. Assume non-negative years.
# SAMPLE INPUT / OUTPUT
# future_value(1000, 10, 2) -> 1210.0
# future_value(500, 0, 4) -> 500.0

def future_value(principal, annual_rate_percent, years):
    interest= principal * ((1+(annual_rate_percent)/100))**years
    final = interest
    return final

print(future_value(1000, 10, 2))