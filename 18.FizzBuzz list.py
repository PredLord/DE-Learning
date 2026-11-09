# 18 FizzBuzz list Easy • ~8 min
# Write `fizzbuzz(n)` returning a list for 1 through n. Replace multiples of 3 with `'Fizz'`, of 5 with `'Buzz'`,
# and of both with `'FizzBuzz'`. Keep all other values as integers.
# SAMPLE INPUT / OUTPUT
# fizzbuzz(5) -> [1, 2, 'Fizz', 4, 'Buzz']
# fizzbuzz(0) -> []

l1=[]
def fizzbuzz(n):
    for i in range (1,n+1):
        if i ==3:
            l1.append('Fizz')
        elif i==5:
            l1.append('Buzz')
        else:
            l1.append(i)
    return l1
# print(fizzbuzz(5))
print(fizzbuzz(0))