def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    result = ""
    for el in args:
        fun_name = el[0]
        nums = el[1]
        result += f"{fun_name.__name__} - {fun_name(*nums)}" + "\n"

    return result


print(func_executor(

(sum_numbers, (1, 2)),
(multiply_numbers, (2, 4))))

