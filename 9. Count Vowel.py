# 09 Count vowels Easy • ~8 min
# Write `count_vowels(text)` that counts A, E, I, O, U in any case. Do not count Y.
# SAMPLE INPUT / OUTPUT
# count_vowels('Data Engineering') -> 7
# count_vowels('rhythm') -> 0

def count_vowels(text):
    counter =0
    vowel= ['a','e','i','o','u']
    for i in text:
        if i.lower() in vowel:
            counter+=1
        else:
            counter
    return counter

counter =count_vowels('Data Engineering') 
print(counter) 
