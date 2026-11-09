# 20 Find all primes up to n Easy • ~8 min
# Write `primes_up_to(n)` returning all prime numbers n in ascending order. A prime is an integer ≤
# greater than 1 divisible only by 1 and itself.
# SAMPLE INPUT / OUTPUT
# primes_up_to(10) -> [2, 3, 5, 7]
# primes_up_to(1) -> []

def primes_up_to(n):
    l1 = []
    if n <=1:
        return l1
        for i in range (2,n+1):
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                l1.append(i)
            
        return l1
print(primes_up_to(10))