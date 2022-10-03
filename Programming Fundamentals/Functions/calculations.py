def calculator_function(a, b, command):
    if command == "multiply":
        return a * b
    elif command == "divide":
        return int(a/b)
    elif command == "add":
        return a + b
    elif command == "subtract":
        return a - b


operator = input()
first_num = int(input())
second_num = int(input())
print(calculator_function(first_num, second_num, operator))
