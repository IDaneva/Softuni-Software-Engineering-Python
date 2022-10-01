string1 = input()
string2 = input()
last_string = string1

for i in range(len(string1)):
    left_part = string2[:i+1]
    right_part = string1[i+1:]
    current_string = left_part + right_part

    if current_string == last_string:
        continue
    else:
        print(current_string)
        last_string = current_string

