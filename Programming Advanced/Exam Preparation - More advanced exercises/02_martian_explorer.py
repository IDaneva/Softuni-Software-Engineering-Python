rows, cols = 6, 6
matrix = []
rover_position = []
for row in range(rows):
    current_row_info = input().split()
    matrix.append(current_row_info)
    if "E" in current_row_info:
        rover_position.append(row)
        rover_position.append(current_row_info.index("E"))

directions = {
    "left": (0, -1),
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0)
}

commands = input().split(", ")
deposits = {}
broken = False

for command in commands:
    new_row = rover_position[0] + directions[command][0]
    new_col = rover_position[1] + directions[command][1]

    if new_row == -1:
        new_row = 5
    elif new_row == 6:
        new_row = 0

    if new_col == -1:
        new_col = 5
    elif new_col == 6:
        new_col = 0

    if matrix[new_row][new_col] == "W":
        if "W" not in deposits:
            deposits["W"] = 0
        deposits["W"] += 1
        print(f"Water deposit found at ({new_row}, {new_col})")
    elif matrix[new_row][new_col] == "M":
        if "M" not in deposits:
            deposits["M"] = 0
        deposits["M"] += 1
        print(f"Metal deposit found at ({new_row}, {new_col})")
    elif matrix[new_row][new_col] == "C":
        if "C" not in deposits:
            deposits["C"] = 0
        deposits["C"] += 1
        print(f"Concrete deposit found at ({new_row}, {new_col})")
    elif matrix[new_row][new_col] == "R":
        broken = True
        print(f"Rover got broken at ({new_row}, {new_col})")
        break

    rover_position = [new_row, new_col]

if "W" in deposits and "M" in deposits and "C" in deposits:
    print("Area suitable to start the colony.")

else:
    print("Area not suitable to start the colony.")
