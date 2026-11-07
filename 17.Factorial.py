# 17 Factorial with a loop Easy • ~8 min
# Write `factorial(n)` returning n! for a non-negative integer n. Remember that 0! = 1.
# SAMPLE INPUT / OUTPUT
# factorial(5) -> 120
# factorial(0) -> 1


def factorial(n):
    
    if n==1:
        return 1
    else:
        counter =1
        for i in range(1,n+1):
            counter =counter*i

        return counter

print(factorial(5))
print(factorial(0))
