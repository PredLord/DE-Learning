# 21 Remove duplicates, keep order Medium • ~12 min
# Write `unique_in_order(items)` that returns a new list with only the first occurrence of each value.
# Assume all values are hashable. Do not mutate the input.
# SAMPLE INPUT / OUTPUT
# unique_in_order([3, 1, 3, 2, 1]) -> [3, 1, 2]
# unique_in_order([]) -> []


def unique_in_order(items):
    l1= items
    l2=[]
    for i in l1:
        if i not in l2:
            l2.append(i)

    return l2

print(unique_in_order([3, 1, 3, 2, 1]))
