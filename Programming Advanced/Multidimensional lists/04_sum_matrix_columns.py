rows, cols = list(map(int, input().split(", ")))

matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for column in range(cols):
    value = 0
    for row in range(rows):
        value += matrix[row][column]
    print(value)
