# 19 Count digits without strings Easy • ~8 min
# Write `digit_count(n)` returning the number of decimal digits of an integer, including negative values.
# Do not convert to a string. Zero has 1 digit.
# SAMPLE INPUT / OUTPUT
# digit_count(-12345) -> 5
# digit_count(0) -> 1




def digit_count(n):
    c=1
    if n!=0:
        while not((n/10 > 0 and n/10<1) or  (n/10 < 0 and n/10>-1)):
            n= n/10
            c=c+1
        return c
    else:
        return c
print(digit_count(-12345))
print(digit_count(0))