def validator(passwort):
    result = []
    if 6 <= len(passwort) <= 10:
        result.append("True")
    else:
        result.append("False")
        print("Password must be between 6 and 10 characters")
    if passwort.isalnum():
        result.append("True")
    else:
        result.append("False")
        print("Password must consist only of letters and digits")
    nums = 0
    for x in passwort:
        if x.isdigit():
            nums += 1
    if nums >= 2:
        result.append("True")
    else:
        result.append("False")
        print("Password must have at least 2 digits")
    return result


password = input()
if "False" not in validator(password):
    print("Password is valid")
