rows, columns = [int(x) for x in input().split()]
found = 0
matrix = [input().split() for i in range(rows)]

for row in range(rows):
    if row == rows - 1:
        break
    for column in range(columns):
        if column == columns - 1:
            break
        if matrix[row][column] == matrix[row][column+1] == matrix[row+1][column] == matrix[row+1][column+1]:
            found += 1

print(found)
