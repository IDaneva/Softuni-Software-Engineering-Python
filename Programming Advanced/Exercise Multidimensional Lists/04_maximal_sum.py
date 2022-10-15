import sys

rows, columns = [int(x) for x in input().split()]
matrix = [list(map(int, input().split())) for i in range(rows)]
max_sum = -sys.maxsize
max_square = []

for row in range(rows):
    if row == rows - 2:
        break
    for column in range(columns):
        if column == columns - 2:
            break
        current_square = [
            [matrix[row][column], matrix[row][column+1], matrix[row][column+2]],
            [matrix[row+1][column], matrix[row+1][column+1], matrix[row+1][column+2]],
            [matrix[row+2][column], matrix[row+2][column+1], matrix[row+2][column+2]]
        ]
        total = 0
        for sq in current_square:
            total += sum(sq)
        if total > max_sum:
            max_sum = total
            max_square = current_square

print(f"Sum = {max_sum}")
for s in max_square:
    print(" ".join(list(map(str, s))))
