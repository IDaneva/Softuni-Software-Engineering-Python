row, col = [int(x) for x in input().split(", ")]
matrix = []
total = 0
for _ in range(row):
    current = [int(x) for x in input().split(", ")]
    matrix.append(current)
    total += sum(current)

print(total)
print(matrix)
