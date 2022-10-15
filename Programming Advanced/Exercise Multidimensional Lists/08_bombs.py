size = int(input())
matrix = []
for _ in range(size):
    matrix.append([int(x) for x in input().split()])

bombed_cells = 0
coordinates = input().split()

for current in coordinates:
    row, col = list(map(int, current.split(",")))

    current_bomb = matrix[row][col]

    if matrix[row][col] <= 0:
        pass
    else:
        matrix[row][col] = 0
        bombed_cells += 1

    if False in [0 <= row - 1 < size, 0 <= col - 1 < size] or matrix[row - 1][col - 1] <= 0:
        pass
    else:
        matrix[row - 1][col - 1] -= current_bomb
        bombed_cells += 1

    if False in [0 <= row < size, 0 <= col - 1 < size] or matrix[row][col - 1] <= 0:
        pass
    else:
        matrix[row][col - 1] -= current_bomb
        bombed_cells += 1

    if False in [0 <= row + 1 < size, 0 <= col - 1 < size] or matrix[row + 1][col - 1] <= 0:
        pass
    else:
        matrix[row + 1][col - 1] -= current_bomb
        bombed_cells += 1

    if False in [0 <= row - 1 < size, 0 <= col < size] or matrix[row - 1][col] <= 0:
        pass
    else:
        matrix[row - 1][col] -= current_bomb
        bombed_cells += 1

    if False in [0 <= row + 1 < size, 0 <= col < size] or matrix[row + 1][col] <= 0:
        pass
    else:
        matrix[row + 1][col] -= current_bomb
        bombed_cells += 1

    if False in [0 <= row - 1 < size, 0 <= col + 1 < size] or matrix[row - 1][col + 1] <= 0:
        pass
    else:
        matrix[row - 1][col + 1] -= current_bomb
        bombed_cells += 1

    if False in [0 <= row < size, 0 <= col + 1 < size] or matrix[row][col + 1] <= 0:
        pass
    else:
        matrix[row][col + 1] -= current_bomb
        bombed_cells += 1

    if False in [0 <= row + 1 < size, 0 <= col + 1 < size] or matrix[row + 1][col + 1] <= 0:
        pass
    else:
        matrix[row + 1][col + 1] -= current_bomb
        bombed_cells += 1

print(f"Alive cells: {abs((size * size) - bombed_cells)}")
print(size*size)
print(bombed_cells)

total = 0
for r in matrix:
    for c in r:
        if c > 0:
            total += c
print(f"Sum: {total}")
for i in matrix:
    print(*i, sep=" ")

