# 14 Validate a triangle Easy • ~8 min
# Write `triangle_type(a, b, c)`. Return `'invalid'` unless all sides are positive and satisfy the strict triangle
# inequality. Otherwise return `'equilateral'`, `'isosceles'`, or `'scalene'`.
# SAMPLE INPUT / OUTPUT
# triangle_type(3, 3, 3) -> 'equilateral'
# triangle_type(3, 4, 5) -> 'scalene'
# triangle_type(1, 2, 3) -> 'invalid'

def triangle_type(a, b, c):
    if a==b==c:
        return 'equilateral'
    elif ((a>c) and (a >b) and (b+c >a))  or ((b>c) and (b >c) and (a+c >b)) or ((c>a) and (c >b) and (b+a >c)):
        return 'scalene'
    else:
        return 'invalid'

print(triangle_type(3, 3, 3))
print(triangle_type(3, 4, 5))
print(triangle_type(1, 2, 3))