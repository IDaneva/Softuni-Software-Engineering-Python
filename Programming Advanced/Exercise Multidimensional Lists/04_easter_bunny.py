size = int(input())
egg_field = []
bunny_position = []

for r in range(size):
    row = [int(x) if x[-1].isdigit() else x for x in input().split()]
    if "B" in row:
        bunny_position = [r, row.index("B")]
    egg_field.append(row)

max_path_value = 0
max_path = []
direction = []

directions = {
    "left": (0, -1),
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0)
}

current_position = bunny_position

for way, coordinates in directions.items():
    current_path = []
    current_path_value = 0

    while True:
        row_pos = current_position[0] + coordinates[0]
        col_pos = current_position[1] + coordinates[1]

        if 0 <= row_pos < size and 0 <= col_pos < size:
            if egg_field[row_pos][col_pos] == "X" or egg_field[row_pos][col_pos] <= 0:
                break
            else:
                current_path_value += egg_field[row_pos][col_pos]
                current_path.append([row_pos, col_pos])
                current_position = [row_pos, col_pos]
        else:
            break

    if current_path_value >= max_path_value:
        max_path_value = current_path_value
        max_path = current_path
        direction = way

    current_position = bunny_position

print(direction)
[print(c) for c in max_path]
print(max_path_value)
