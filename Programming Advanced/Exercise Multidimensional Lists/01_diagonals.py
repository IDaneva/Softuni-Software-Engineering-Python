rows = int(input())

matrix = [input().split(", ") for _ in range(rows)]
primary = []
secondary = []
for index in range(rows):
    primary.append(matrix[index][index])
    secondary.append(matrix[index][len(matrix) - index - 1])

print(f'Primary diagonal: {", ".join(primary)}. Sum: {sum(list(map(int, primary)))}')
print(f'Secondary diagonal: {", ".join(secondary)}. Sum: {sum(list(map(int, secondary)))}')
