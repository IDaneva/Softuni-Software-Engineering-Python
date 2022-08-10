number = int(input())
right_sum = 0
left_sum = 0

for i in range(0, number * 2):
    current_number = int(input("Number? "))
    if i >= number:
        right_sum += current_number
    else:
        left_sum += current_number

diff = abs(right_sum - left_sum)

if right_sum == left_sum:
    print(f"Yes, sum = {right_sum}")
else:
    print(f"No, diff = {diff}")
