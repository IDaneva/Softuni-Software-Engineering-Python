start_of_interval = int(input())
end_of_interval = int(input())
magic_number = int(input())
combinations = 0
condition = False

for number1 in range(start_of_interval, end_of_interval + 1):
    for number2 in range(start_of_interval, end_of_interval + 1):
        combinations += 1
        if number1 + number2 == magic_number:
            condition = True
            print(f"Combination N:{combinations} ({number1} + {number2} = {magic_number})")
            break
    if condition:
        break

if not condition:
    print(f"{combinations} combinations - neither equals {magic_number}")