# 08 Check a relaxed palindrome Easy • ~8 min
# Write `is_palindrome(text)` that ignores case and all non-alphanumeric characters, then checks
# whether the cleaned text reads the same backward.
# SAMPLE INPUT / OUTPUT
# is_palindrome('A man, a plan, a canal: Panama!') -> True
# is_palindrome('Python') -> False


def is_palindrome(text):
    alnum = "".join(filter(str.isalnum,text)).lower()
    reversed_alnum= alnum[::-1]
    if alnum == reversed_alnum:
        return True
    else:
        return False



print(is_palindrome('A man, a plan, a canal: Panama!'))
# print(alnum)
