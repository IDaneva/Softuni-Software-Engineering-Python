rows, cols = 6, 6
matrix = [input().split() for _ in range(cols)]

first_position = input()
first_position = first_position.replace("(", "")
first_position = first_position.replace(")", "")
first_row, first_col = first_position.split(", ")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    command = input().split(", ")
    instructions = command[0]
    if instructions == "Stop":
        break
    direction = command[1]

    if instructions == "Create":
        value = command[2]
        r = int(first_row) + directions[direction][0]
        c = int(first_col) + directions[direction][1]
        if matrix[r][c] == ".":
            matrix[r][c] = value

    elif instructions == "Update":
        value = command[2]
        r = int(first_row) + directions[direction][0]
        c = int(first_col) + directions[direction][1]
        if matrix[r][c] != ".":
            matrix[r][c] = value

    elif instructions == "Delete":
        r = int(first_row) + directions[direction][0]
        c = int(first_col) + directions[direction][1]
        if matrix[r][c] != ".":
            matrix[r][c] = "."

    elif instructions == "Read":
        r = int(first_row) + directions[direction][0]
        c = int(first_col) + directions[direction][1]
        if matrix[r][c] != ".":
            print(matrix[r][c])

    first_row = r
    first_col = c

for row in matrix:
    print(" ".join(row))
