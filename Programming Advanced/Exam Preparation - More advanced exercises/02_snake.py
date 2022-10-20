def coordinate_validator(r, c):
    if 0 <= r < SIZE and 0 <= c < SIZE:
        return True


def move_snake(current_position, direction):
    current_row = current_position[0]
    current_col = current_position[1]
    food = 0
    new_row = current_row + directions[direction][0]
    new_col = current_col + directions[direction][1]
    if not coordinate_validator(new_row, new_col):
        return False

    if matrix[new_row][new_col] == "*":
        food += 1
        if food == 10:
            stop = True
            print("You won! You fed the snake.")

    if matrix[new_row][new_col] == "B":
        matrix[new_row][new_col] = "."
        burrows.remove([new_row, new_col])
        current_position = burrows.pop()
        matrix[current_position[0]][current_position[1]] = "."
        return [current_position, food]

    matrix[new_row][new_col] = "."
    current_position = [new_row, new_col]
    return [current_position, food]


SIZE = int(input())

snake_position = []
matrix = []
burrows = []

for r in range(SIZE):
    row = list(input())
    if "S" in row:
        snake_position = [r, row.index("S")]
    matrix.append(row)
    if "B" in row:
        for i, d in enumerate(row):
            if d == "B":
                burrows.append([r, i])

matrix[snake_position[0]][snake_position[1]] = "."

directions = {
    "left": (0, -1),
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0)
}

found_food = 0

stopped = False

while True:
    command = input()
    a = move_snake(snake_position, command)
    if not a:
        print("Game over!")
        break
    snake_position = a[0]
    found_food += a[1]
    if found_food == 10:
        print("You won! You fed the snake.")
        matrix[snake_position[0]][snake_position[1]] = "S"
        break


print(f"Food eaten: {found_food}")
for k in matrix:
    print("".join(k))
