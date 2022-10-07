message = input().split()

for word in message:
    current_message = []
    number = "".join([s for s in word if s.isnumeric()])
    current_message += chr(int(number))
    left_part = "".join(i for i in word if i.isalpha())
    if len(left_part) >= 2:
        current_message += left_part[-1] + left_part[1:-1] + left_part[0]
    else:
        current_message += left_part
    print("".join(current_message), end=" ")