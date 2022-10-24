directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

SIZE = int(input())

racing_number = input()

matrix = []
finish_line = []
tunnel_coordinates = []

player_position = [0, 0]

for r in range(SIZE):
    row = input().split()

    if "F" in row:
        finish_line = [r, row.index("F")]

    if "T" in row:
        for i, d in enumerate(row):
            if d == "T":
                tunnel_coordinates.append([r, i])

    matrix.append(row)

finished = False
total_km = 0

while True:
    command = input()
    if command == "End":
        matrix[player_position[0]][player_position[1]] = "C"
        if not finished:
            print(f"Racing car {racing_number} DNF.")
        else:
            pass
        break

    current_row = player_position[0] + directions[command][0]
    current_col = player_position[1] + directions[command][1]

    if matrix[current_row][current_col] == ".":
        total_km += 10
        player_position = [current_row, current_col]
        continue
    elif matrix[current_row][current_col] == "T":
        total_km += 30
        matrix[current_row][current_col] = "."
        if [current_row, current_col] == tunnel_coordinates[0]:
            player_position = tunnel_coordinates[1]
            matrix[player_position[0]][player_position[1]] = "."
            continue
        elif [current_row, current_col] == tunnel_coordinates[1]:
            player_position = tunnel_coordinates[0]
            matrix[player_position[0]][player_position[1]] = "."
            continue
    elif matrix[current_row][current_col] == "F":
        total_km += 10
        print(f"Racing car {racing_number} finished the stage!")
        finished = True
        matrix[current_row][current_col] = "C"
        break

print(f"Distance covered {total_km} km.")

for r in matrix:
    print(''.join(r))
