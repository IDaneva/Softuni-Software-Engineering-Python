def coordinate_validator(r, c):
    if 0 <= r < SIZE and 0 <= c < SIZE:
        return True
    else:
        return False


initial_string = input()
SIZE = int(input())

player_position = []

directions = {
    "left": (0, -1),
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0)
}

matrix = []
for r in range(SIZE):
    row = list(input())
    if "P" in row:
        player_position = [r, row.index("P")]
    matrix.append(row)

matrix[player_position[0]][player_position[1]] = "-"
num = int(input())

for _ in range(num):
    command = input()
    new_row = player_position[0] + directions[command][0]
    new_col = player_position[1] + directions[command][1]

    if not coordinate_validator(new_row, new_col):
        initial_string = initial_string[:-1]
    else:
        if matrix[new_row][new_col].isalpha():
            initial_string += f"{matrix[new_row][new_col]}"
            matrix[new_row][new_col] = "-"
        player_position = [new_row, new_col]

matrix[player_position[0]][player_position[1]] = "P"
print(initial_string)
for row in matrix:
    print("".join(row))