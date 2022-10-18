def coordinates_validator(row, col):
    if 0 <= row < SIZE and 0 <= col < SIZE:
        return True
    else:
        return False


def bomb_finder(position):
    found_bombs = 0
    r = position[0]
    c = position[1]
    for direction in directions:
        new_row = r + directions[direction][0]
        new_col = c + directions[direction][1]
        if not coordinates_validator(new_row, new_col):
            continue
        if matrix[new_row][new_col] == "*":
            found_bombs += 1
    matrix[r][c] = found_bombs
    return matrix


SIZE = int(input())
number_of_bombs = int(input())

all_bomb_coordinates = []
matrix = [["-"] * SIZE for _ in range(SIZE)]
for r in range(number_of_bombs):
    position = [int(x) for x in input().strip("()").split(", ")]
    all_bomb_coordinates.append(position)
    matrix[position[0]][position[1]] = "*"

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
    "left_up_diagonal": [-1, -1],
    "right_up_diagonal": [-1, 1],
    "left_down_diagonal": [1, -1],
    "right_down_diagonal": [1, 1]
}

for row in range(SIZE):
    for col in range(SIZE):
        if matrix[row][col] == "*":
            continue
        else:
            current_pos = [row, col]
            bomb_finder(current_pos)

for printing_row in matrix:
    print(' '.join(list(map(str, printing_row))))
