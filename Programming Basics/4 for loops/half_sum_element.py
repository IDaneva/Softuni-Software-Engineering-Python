import sys

number = int(input())

max_number = -sys.maxsize
total = 0

for i in range(number):
    current_number = int(input())
    total += current_number
    if current_number > max_number:
        max_number = current_number

diff = abs(max_number - (total - max_number))

if total - max_number == max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    print(f"Diff = {diff}")

