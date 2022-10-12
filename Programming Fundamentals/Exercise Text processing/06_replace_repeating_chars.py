text = input()
new_string = ""


for ch in text:
    if len(new_string) > 0 and new_string[-1] == ch:
        continue
    else:
        new_string += ch
print(new_string)