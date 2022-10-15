field_size = 5
directions = {
    "left": (0, -1),
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0)
}


def move(instructions, directions, position):
    way = instructions[1]
    steps = int(instructions[2])
    new_row = position[0] + directions[way][0] * steps
    new_col = position[1] + directions[way][1] * steps
    if 0 <= new_row < field_size and 0 <= new_col < field_size:
        if actual_field[new_row][new_col] == ".":
            position = [new_row, new_col]
    return position


def shoot(instructions, directions, position):
    way = instructions[1]
    shooting_position = position
    shots_pos = []
    while True:
        new_row = shooting_position[0] + directions[way][0]
        new_col = shooting_position[1] + directions[way][1]
        if 0 <= new_row < field_size and 0 <= new_col < field_size:
            if actual_field[new_row][new_col] == "x":
                shots_pos.append([new_row, new_col])
                return shots_pos
            else:
                shooting_position = [new_row, new_col]
        else:
            return False


actual_field = []
my_pos = []
all_targets = 0

for r in range(field_size):
    row = input().split()
    if "A" in row:
        my_pos=[r, row.index("A")]
    all_targets += row.count("x")
    actual_field.append(row)
shot_targets = []

success = False
current_position = my_pos

for _ in range(int(input())):
    command = input().split()
    if command[0] == "move":
        current_position = move(command, directions, current_position)

    elif command[0] == "shoot":
        if shoot(command, directions, current_position):
            shot_targets.append(shoot(command, directions, current_position))
            if len(shot_targets) == all_targets:
                success = True
                break
        else:
            continue

if not success:
    print(f"Training completed! All {all_targets} targets hit.")
else:
    print(f"Training not completed! {all_targets - len(shot_targets)} targets left.")

print(shot_targets)
