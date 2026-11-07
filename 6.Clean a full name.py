# 06 Clean a full name Easy • ~8 min
# Write `clean_name(name)` that strips extra spaces from the ends, reduces multiple internal spaces to
# one, and capitalizes the first letter of each word.
# SAMPLE INPUT / OUTPUT
# clean_name(' aLIce jONES ') -> 'Alice Jones'
# clean_name('MARY jane') -> 'Mary Jane'



# print(("  ghfdb   fdf  fggf    ".strip().title()))


def clean_name(name):
    name_new= " ".join(name.strip().split()).title()
    return name_new


a = clean_name('   Akilesh     Anantha    Krishnan')
print(a)


