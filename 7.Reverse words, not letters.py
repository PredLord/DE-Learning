# 07 Reverse words, not letters Easy • ~8 min
# Write `reverse_words(sentence)` that returns the words in reverse order, separated by single spaces.
# Treat any whitespace as a separator.
# SAMPLE INPUT / OUTPUT
# reverse_words('Python is fun') -> 'fun is Python'
# reverse_words(' a b ') -> 'b a'



def reverse_words(sentence):
    lists = sentence.title().split()
    reversed_words= " ".join(lists[::-1])
    return reversed_words

reversed_words= reverse_words('Python is fun')
print (reversed_words)

# print('Python is fun'.title().split())