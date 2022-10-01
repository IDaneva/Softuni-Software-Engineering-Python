divisor = int(input())
boundary = int(input())

for current_num in range(boundary, divisor - 1, -1):
    if current_num % divisor == 0:
        print(current_num)
        break
