from collections import deque


def list_manipulator(numbers: list, *args):
    numbers = deque(numbers)
    args = deque(args)
    if "add" in args and "beginning" in args:
        args.popleft()
        args.popleft()
        while args:
            numbers.appendleft(args.pop())

    elif "add" in args and "end" in args:
        args.popleft()
        args.popleft()
        for x in args:
            numbers.append(x)

    elif "remove" in args and "beginning" in args:
        args.popleft()
        args.popleft()
        if not args:
            numbers.popleft()
        else:
            nums_to_remove = args.popleft()
            for _ in range(nums_to_remove):
                numbers.popleft()

    elif "remove" in args and "end" in args:
        args.popleft()
        args.popleft()
        if not args:
            numbers.pop()
        else:
            nums_to_remove = args.popleft()
            for _ in range(nums_to_remove):
                numbers.pop()

    return list(numbers)


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
