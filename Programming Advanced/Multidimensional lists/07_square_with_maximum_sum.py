import sys

rows, columns = [int(x) for x in input().split(", ")]

matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

max_square = []
max_sum = -sys.maxsize
for row in range(rows):
    if row == rows - 1:
        break
    for column in range(columns):
        if column == columns - 1:
            break
        current_square = [matrix[row][column], matrix[row][column+1], matrix[row+1][column], matrix[row+1][column+1]]
        if sum(current_square) > max_sum:
            max_sum = sum(current_square)
            max_square =[[matrix[row][column], matrix[row][column+1]], [matrix[row+1][column], matrix[row+1][column+1]]]

for r in max_square:
    print(' '.join(list(map(str, r))))
print(max_sum)
