# 15 Grade a score Easy • ~8 min
# Write `grade(score)` returning `'A'` for 90–100, `'B'` for 80–89, `'C'` for 70–79, `'D'` for 60–69, `'F'` for 0–59.
# Return `'Invalid'` for scores outside 0–100.
# SAMPLE INPUT / OUTPUT
# grade(89) -> 'B'
# grade(105) -> 'Invalid'

def grade(score):
    if score >  100 or score < 0:
        return 'Invalid'
    elif score >=90 and score <=100:
        return 'A'
    elif score >= 80 and score <= 89:
        return 'B'
    elif score >= 70 and score <= 79:
        return 'C' 
    elif score >= 60 and score <= 69:
        return 'D'
    elif score >= 0 and score <= 59:
        return 'F'    

print(grade(89))
print(grade(100))
print(grade(79))
print(grade(65))
print(grade(4))
print(grade(106))