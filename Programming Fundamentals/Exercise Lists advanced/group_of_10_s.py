import math

numbers = list(map(int, input().split(", ")))

max_value = max(numbers) + 9
boundary = int(math.ceil(max_value) / 10)

for current_group in range(1, boundary+1):
    group = []
    for current_number in numbers.copy():
        if current_group * 10 >= current_number >= 0:
            group.append(current_number)
            numbers.remove(current_number)

    print(f"Group of {current_group * 10}'s: {group}")
