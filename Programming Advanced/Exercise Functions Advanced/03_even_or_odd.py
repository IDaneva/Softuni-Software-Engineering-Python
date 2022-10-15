def even_odd(*args):
    command = args[-1]
    numbers = [int(x) for x in args[:-1]]
    if command == "even":
        return [i for i in numbers if i % 2 == 0]
    elif command == "odd":
        return [i for i in numbers if i % 2 != 0]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
