number = int(input())
current_number = 0

for row in range(number):
    for column in range(row + 1):
        current_number += 1
        if current_number > number:
            break
        else:
            print(current_number, end=" ")
    print()