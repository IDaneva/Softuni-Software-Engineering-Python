text = input()

try:
    times = int(input())
    print(times * text)
except ValueError:
    print("Variable times must be an integer")
