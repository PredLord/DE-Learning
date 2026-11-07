# 02 Split a restaurant bill Easy • ~8 min
# Write `split_bill(total, tip_percent, people)` returning the amount each person pays, rounded to 2
# decimals. Add a percentage tip to `total`. Assume `people > 0`.
# SAMPLE INPUT / OUTPUT
# split_bill(1200, 10, 3) -> 440.0
# split_bill(500, 0, 2) -> 250.0



def split_bill(total, tip_percent, people):
    actual_total = total + (total * tip_percent/100)
    split = actual_total/people
    return round(split,2)

print(split_bill(25005, 10, 10))