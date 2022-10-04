import math


def factorial(a):
    fact = math.factorial(a)
    return fact


# def factorial(a):
#     fact = 1
#     for i in range(1, a + 1):
#         fact = fact * i
#     return fact


num1 = int(input())
num2 = int(input())

result = factorial(num1) / factorial(num2)
print(f"{result:.2f}")
