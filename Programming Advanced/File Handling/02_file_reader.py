result = 0

with open("numbers.txt") as file:
    result = [int(x.strip()) for x in file.readlines()]

print(sum(result))
