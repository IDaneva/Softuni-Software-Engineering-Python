n = int(input())
# main logic that is used
# for r in range(1, n + 1):
#     print(f"{' '* (n - r)}{'* ' * r}")
#
# for r1 in range(n-1, 0, -1):
#     print(f"{' ' * (n- r1)}{'* ' * r1}")


def create_line(r):
    line = f"{' ' * (n - r)}{'* ' * r}\n"
    return line


def create_rhombus(n):
    result = ""
    for r in range(1, n + 1):
        result += create_line(r)
    for r in range(n - 1, 0, -1):
        result += create_line(r)
    return result


print(create_rhombus(n))
