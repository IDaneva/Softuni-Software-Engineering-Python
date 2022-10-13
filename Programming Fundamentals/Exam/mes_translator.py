import re

count_of_strings = int(input())

validation_pattern = r"!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]"

for _ in range(count_of_strings):
    current_command = input()
    result = re.findall(validation_pattern, current_command)
    if result:
        for match in result:
            print(f"{match[0]}: {' '.join([str(ord(ch)) for ch in match[1]])}")
    else:
        print("The message is invalid")
