rows = int(input())

matrix = [input().split(" ") for _ in range(rows)]
primary = []
secondary = []

for index in range(rows):
    primary.append(int(matrix[index][index]))
    secondary.append(int(matrix[index][len(matrix) - index - 1]))

print(abs(sum(primary) - sum(secondary)))
