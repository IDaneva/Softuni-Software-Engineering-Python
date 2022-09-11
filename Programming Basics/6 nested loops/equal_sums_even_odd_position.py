number1 = int(input())

number2 = int(input())



for current_number in range(number1, number2 + 1):
    string_current_number = str(current_number)
    even_sum = 0
    odd_sum = 0
    for index, digit in enumerate(string_current_number):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    if odd_sum == even_sum:
        print(string_current_number, end=" ")
