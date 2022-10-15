def operate(operator, *args):
    def suming():
        return sum(args)
    def subtract():
        result = args[0]
        for el in args[1::]:
            result -= el
        return result

    def multiplicate():
        result = 1
        for el in args:
            result *= el
        return result

    def division():
        result = args[0]
        for el in args[1::]:
            result /= el
        return result
    if operator == "+":
        return suming()
    elif operator == "-":
        return subtract()
    elif operator == "*":
        return multiplicate()
    elif operator == "/":
        return division()


print(operate("/", 1, 2, 0))
print(operate("*", 3, 4))
