number_of_lines = int(input())
first_list = []
filtered_list = []
for _ in range(number_of_lines):
    current_number = int(input())
    first_list.append(current_number)

command = input()

for item in first_list:
    if command == "even":
        if item % 2 == 0:
            filtered_list.append(item)
    elif command == "odd":
        if item % 2 != 0:
            filtered_list.append(item)
    elif command == "negative":
        if item < 0:
            filtered_list.append(item)
    elif command == "positive":
        if item >= 0:
            filtered_list.append(item)

print(filtered_list)