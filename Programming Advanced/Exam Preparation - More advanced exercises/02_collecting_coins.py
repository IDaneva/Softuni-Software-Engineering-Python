import math

SIZE = int(input())

player_position = []

field_matrix = []


directions = {
    "left": (0, -1),
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0)
}

for r in range(SIZE):
    row = [int(x) if x.isdigit() else x for x in input().split()]
    if "P" in row:
        player_position = [r, row.index("P")]
    field_matrix.append(row)


field_matrix[player_position[0]][player_position[1]] = "."

found_coins = 0
path_of_player = [player_position]

current_position = player_position

while True:
    command = input()

    if command not in ["up", "down", "left", "right"]:
        continue
    else:
        new_row = current_position[0] + directions[command][0]
        new_col = current_position[1] + directions[command][1]

        if new_row == -1:
            new_row = SIZE - 1
        elif new_row == SIZE:
            new_row = 0

        if new_col == -1:
            new_col = SIZE - 1
        elif new_col == SIZE:
            new_col = 0

        if field_matrix[new_row][new_col] == "X":
            path_of_player.append([new_row, new_col])
            found_coins = math.floor(found_coins/2)
            print(f"Game over! You've collected {found_coins} coins.")
            break
        if field_matrix[new_row][new_col] != "X" and field_matrix[new_row][new_col] != ".":
            found_coins += field_matrix[new_row][new_col]
            field_matrix[new_row][new_col] = "."

        path_of_player.append([new_row, new_col])
        current_position = [new_row, new_col]

        if found_coins >= 100:
            print(f"You won! You've collected {found_coins} coins.")
            break

print("Your path:")
for p in path_of_player:
    print(p)
