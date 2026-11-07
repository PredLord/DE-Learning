# 10 Mask an email username Easy • ~8 min
# Write `mask_email(email)` for a valid email with at least one character before `@`. Show the first
# character of the username and replace the remaining username characters with `*`. Preserve the
# domain.
# SAMPLE INPUT / OUTPUT
# mask_email('alice@example.com') -> 'a****@example.com'
# mask_email('a@x.io') -> 'a@x.io'

def mask_email(email):
    username, domain = email.split("@", 1)

    masked_username = username[0] + "*" * (len(username) - 1)

    return masked_username + "@" + domain


print(mask_email("alice@example.com"))
print(mask_email("a@x.io"))