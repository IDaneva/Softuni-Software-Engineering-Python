size = int(input())
matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

value = 0
for current in range(size):
    value += matrix[current][current]
print(value)