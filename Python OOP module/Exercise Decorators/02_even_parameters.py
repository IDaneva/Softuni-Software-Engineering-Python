def even_parameters(func):
    def wrapper(*args):
        for x in args:
            if isinstance(x, int):
                if x % 2 == 0:
                    continue
            return f"Please use only even numbers!"

        return func(*args)

    return wrapper


@even_parameters
def add(a, b):

    return a + b


print(add(2.0, 4.0))
print(add(3, 4))

print(add("Peter", 1))
