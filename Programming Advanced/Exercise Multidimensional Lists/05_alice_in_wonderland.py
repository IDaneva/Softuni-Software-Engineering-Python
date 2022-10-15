def index_validator(r, c):
    if 0 <= r < size_of_territory and 0 <= c < size_of_territory:
        return True
    else:
        print("Alice didn't make it to the tea party.")
        return False


def rabit_hole(field):
    if field[current_position[0]][current_position[1]] == "R":
        field[current_position[0]][current_position[1]] = "*"
        print("Alice didn't make it to the tea party.")
        return True


size_of_territory = int(input())
field = []
alice_position = []

for r in range(size_of_territory):
    row = [int(x) if x[-1].isdigit() else x for x in input().split()]
    if "A" in row:
        alice_position = [r, row.index("A")]
    field.append(row)

found_tea_bags = 0

directions = {
    "left": (0, -1),
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0)
}
current_position = alice_position
field[alice_position[0]][alice_position[1]] = "*"

while True:
    command = input()

    if command == "up":
        new_row = current_position[0] + directions["up"][0]
        new_col = current_position[1] + directions["up"][1]
        if not index_validator(new_row, new_col):
            break
        else:
            current_position = [new_row, new_col]
            if not rabit_hole(field):
                if field[current_position[0]][current_position[1]] not in [".", "*"]:
                    found_tea_bags += field[current_position[0]][current_position[1]]
                field[current_position[0]][current_position[1]] = "*"
            else:
                break

    elif command == "down":
        new_row = current_position[0] + directions["down"][0]
        new_col = current_position[1] + directions["down"][1]
        if not index_validator(new_row, new_col):
            break
        else:
            current_position = [new_row, new_col]
            if not rabit_hole(field):
                if field[current_position[0]][current_position[1]] not in [".", "*"]:
                    found_tea_bags += field[current_position[0]][current_position[1]]
                field[current_position[0]][current_position[1]] = "*"
            else:
                break

    elif command == "left":
        new_row = current_position[0] + directions["left"][0]
        new_col = current_position[1] + directions["left"][1]
        if not index_validator(new_row, new_col):
            break
        else:
            current_position = [new_row, new_col]
            if not rabit_hole(field):
                if field[current_position[0]][current_position[1]] not in [".", "*"]:
                    found_tea_bags += field[current_position[0]][current_position[1]]
                field[current_position[0]][current_position[1]] = "*"
            else:
                break

    elif command == "right":
        new_row = current_position[0] + directions["right"][0]
        new_col = current_position[1] + directions["right"][1]
        if not index_validator(new_row, new_col):
            break
        else:
            current_position = [new_row, new_col]
            if not rabit_hole(field):
                if field[current_position[0]][current_position[1]] not in [".", "*"]:
                    found_tea_bags += field[current_position[0]][current_position[1]]
                field[current_position[0]][current_position[1]] = "*"
            else:
                break

    if found_tea_bags >= 10:
        print(f"She did it! She went to the party.")
        break

[print(*row) for row in field]
