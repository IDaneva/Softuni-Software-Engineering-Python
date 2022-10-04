def sum_numbers(a, b):
    return a + b


def subtract(sum, c):
    return sum - c


def add_and_subtract(a, b, c):
    sum_of_1_2 = sum_numbers(a, b)
    subtraction = subtract(sum_of_1_2, c)
    return subtraction


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(add_and_subtract(num1, num2, num3))