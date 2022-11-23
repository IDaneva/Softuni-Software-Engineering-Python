def tags(tag_name):
    def decorator(func):
        def wrapper(*args):
            return f"<{tag_name}>{func(*args)}</{tag_name}>"
        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))

