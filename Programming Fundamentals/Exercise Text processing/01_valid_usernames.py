def length_validator(word):
    if 3 <= len(word) <= 16:
        return True
    return False


def symbol_validator(word):
    for ch in word:
        if not (ch.isalnum() or ch == '-' or ch == '_'):
            return False
    return True


def redundant_validator(word):
    if " " in word:
        return False
    return True


def username_validator(word):
    if length_validator(word) and symbol_validator(word) and redundant_validator(word):
        return True
    return False


usernames = input().split(", ")

for current_user in usernames:
    if username_validator(current_user):
        print(current_user)

