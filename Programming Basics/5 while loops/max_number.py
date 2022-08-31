import sys

max_number = - sys.maxsize

while True:
    number = input()
    if number == "Stop":
        break
    number = float(number)

    if number > max_number:
        max_number = number

print(int(max_number))
