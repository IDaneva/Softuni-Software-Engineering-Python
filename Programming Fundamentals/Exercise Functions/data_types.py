def processes(operation, numbers):
    if operation == "int":
        return int(numbers) * 2
    elif operation == "real":
        return f"{(float(numbers) * 1.5):.2f}"
    elif operation == "string":
        return f"${numbers}$"


operand = input()
number = input()
print(processes(operand, number))
