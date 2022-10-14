numbers = tuple(map(float, input().split()))

num_dict = {}

for number in numbers:
    if number not in num_dict:
        num_dict[number] = 0
    num_dict[number] += 1

for key, value in num_dict.items():
    print(f"{key} - {value} times")
