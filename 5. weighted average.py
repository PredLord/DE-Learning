# 05 Calculate a weighted average Easy • ~8 min
# Write `weighted_average(scores, weights)` that returns the weighted average rounded to 2 decimals.
# Lists have the same positive length, and the weights add to a positive number.
# SAMPLE INPUT / OUTPUT
# weighted_average([80, 90], [1, 3]) -> 87.5
# weighted_average([10, 20, 30], [1, 1, 2]) -> 22.5


# a =[1,2]
# b= 3* a
# c=[2,4]
# print(b)
# counter =0
# sum=0
# for i,j in a,c:
#     counter += i*j
#     sum+=j
# print(counter)
# print(sum)
# print(counter/sum)

def weighted_average(scores, weights):
    counter =0
    sums=0
    for i,j in scores, weights:
        counter += i*j
        sums+=j
    return counter, sums

counter, sums = weighted_average([80, 90], [1, 3])

average = round(counter / sums, 2)
print(average)

