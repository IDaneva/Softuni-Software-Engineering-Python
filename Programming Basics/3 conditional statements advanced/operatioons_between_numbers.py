n1 = int(input())
n2 = int(input())
operator = input()
r1 = ""
if operator == "+":
    result = n1 + n2
    if result % 2 == 0:
        r1 = "even"
        print(f"{n1} + {n2} = {result} - {r1}")
    else:
        r1 = "odd"
        print(f"{n1} + {n2} = {result} - {r1}")
elif operator == "-":
    result = n1 - n2
    if result % 2 == 0:
        r1 = "even"
        print(f"{n1} - {n2} = {result} - {r1}")
    else:
        r1 = "odd"
        print(f"{n1} - {n2} = {result} - {r1}")
elif operator == "*":
    result = n1 * n2
    if result % 2 == 0:
        r1 = "even"
        print(f"{n1} * {n2} = {result} - {r1}")
    else:
        r1 = "odd"
        print(f"{n1} * {n2} = {result} - {r1}")
elif operator == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 / n2
        print(f"{n1} / {n2} = {result:.2f}")

elif operator == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 % n2
        print(f"{n1} % {n2} = {result}")
