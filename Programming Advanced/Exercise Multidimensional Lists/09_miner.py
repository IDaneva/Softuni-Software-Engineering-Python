size = int(input())
commands = input().split()
field = [input().split() for row in range(size)]

start_point = []
end_point = []
number_of_coals = 0

for row in range(size):
    for col in range(size):
        if field[row][col] == "s":
            start_point = [row, col]
        elif field[row][col] == "e":
            end_point = [row, col]
        elif field[row][col] == "c":
            number_of_coals += 1

current_move = start_point
collected_coal = 0

stopped = False
for move in commands:
    if move == "left":
        if False in [0 <= current_move[0] < size, 0 <= current_move[1] - 1 < size]:
            pass
        else:
            current_move = [current_move[0], current_move[1] - 1]
            if field[current_move[0]][current_move[1]] == "c":
                collected_coal += 1
                field[current_move[0]][current_move[1]] = "*"
                if collected_coal == number_of_coals:
                    print(f"You collected all coal! ({current_move[0]}, {current_move[1]})")
                    stopped = True
                    break

            elif field[current_move[0]][current_move[1]] == "e":
                print(f"Game over! ({current_move[0]}, {current_move[1]})")
                stopped = True
                break
            elif field[current_move[0]][current_move[1]] == "*":
                pass

    elif move == "right":
        if False in [0 <= current_move[0] < size, 0 <= current_move[1] + 1 < size]:
            pass
        else:
            current_move = [current_move[0], current_move[1] + 1]
            if field[current_move[0]][current_move[1]] == "c":
                collected_coal += 1
                field[current_move[0]][current_move[1]] = "*"
                if collected_coal == number_of_coals:
                    print(f"You collected all coal! ({current_move[0]}, {current_move[1]})")
                    stopped = True
                    break

            elif field[current_move[0]][current_move[1]] == "e":
                print(f"Game over! ({current_move[0]}, {current_move[1]})")
                stopped = True
                break
            elif field[current_move[0]][current_move[1]] == "*":
                pass

    elif move == "up":
        if False in [0 <= current_move[0] - 1 < size, 0 <= current_move[1] < size]:
            pass
        else:
            current_move = [current_move[0] - 1, current_move[1]]
            if field[current_move[0]][current_move[1]] == "c":
                collected_coal += 1
                field[current_move[0]][current_move[1]] = "*"
                if collected_coal == number_of_coals:
                    print(f"You collected all coal! ({current_move[0]}, {current_move[1]})")
                    stopped = True
                    break

            elif field[current_move[0]][current_move[1]] == "e":
                print(f"Game over! ({current_move[0]}, {current_move[1]})")
                stopped = True
                break
            elif field[current_move[0]][current_move[1]] == "*":
                pass
    elif move == "down":
        if False in [0 <= current_move[0] + 1 < size, 0 <= current_move[1] < size]:
            pass
        else:
            current_move = [current_move[0] + 1, current_move[1]]
            if field[current_move[0]][current_move[1]] == "c":
                collected_coal += 1
                field[current_move[0]][current_move[1]] = "*"
                if collected_coal == number_of_coals:
                    print(f"You collected all coal! ({current_move[0]}, {current_move[1]})")
                    stopped = True
                    break

            elif field[current_move[0]][current_move[1]] == "e":
                print(f"Game over! ({current_move[0]}, {current_move[1]})")
                stopped = True
                break
            elif field[current_move[0]][current_move[1]] == "*":
                pass

if not stopped:
    print(f"{number_of_coals - collected_coal} pieces of coal left. ({current_move[0]}, {current_move[1]})")
