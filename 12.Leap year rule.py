# 12 Leap year rule Easy • ~8 min
# Write `is_leap_year(year)` using Gregorian calendar rules: divisible by 4, except centuries must also be
# divisible by 400.
# SAMPLE INPUT / OUTPUT
# is_leap_year(2000) -> True
# is_leap_year(1900) -> False
# is_leap_year(2024) -> True

def is_leap_year(year):
    if str(year)[-2:] == '00' and year%400 != 0:
        return False
    elif str(year)[-2:] != '00' and year%4 != 0:
            return False
    else:
         return True

print(is_leap_year(2000))
print(is_leap_year(1900))
print(is_leap_year(2024))
print(is_leap_year(100))