# 16 Sum multiples of 3 or 5 Easy • ~8 min
# Write `sum_multiples(limit)` summing integers from 1 up to but excluding `limit` that are divisible by 3
# or 5. Assume `limit >= 0`.
# SAMPLE INPUT / OUTPUT
# sum_multiples(10) -> 23
# sum_multiples(1) -> 0

def sum_multiples(limit):
    counter =0
    for i in range(1,limit):
        if i%3 ==0 or i %5 ==0:
            counter = counter+ i
            # continue
        else:
            continue
    return counter

print(sum_multiples(10))
print(sum_multiples(1))