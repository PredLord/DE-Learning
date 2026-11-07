# 11 Classify a number Easy • ~8 min
# Write `classify_number(n)` returning one of `'positive even'`, `'positive odd'`, `'negative even'`, `'negative
# odd'`, or `'zero'`.
# SAMPLE INPUT / OUTPUT
# classify_number(-4) -> 'negative even'
# classify_number(0) -> 'zero'



def classify_number(n):
    if n ==0:
        return 'Zero'
    elif n>0 and n%2 ==0:
        return 'positive even'
    elif n>0 and n%2 !=0:
            return 'positive odd'
    elif n<0 and n%2 ==0:
        return 'negative even'
    elif n<0 and n%2 !=0:
            return 'negative odd'    

print(classify_number(-7))
print(classify_number(8))