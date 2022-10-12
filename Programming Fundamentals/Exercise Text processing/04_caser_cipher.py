text_to_encrypt = input()

encypted_version = ""

for ch in text_to_encrypt:
    encypted_version += chr(ord(ch) + 3)


print(encypted_version)
