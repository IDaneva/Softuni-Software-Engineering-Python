def coordinate_validator(r, c):
    if 0 <= r < SIZE and 0 <= c < SIZE:
        return True


def corresponding_numbers_finder(r, c):
    num1 = board[r][0]
    num2 = board[0][c]
    num3 = board[r][SIZE - 1]
    num4 = board[SIZE - 1][c]
    total = num1 + num2 + num3 + num4
    return total


SIZE = 7

players = input().split(", ")

board = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(SIZE)]

score_info = {players[0]: [501, 0], players[1]: [501, 0]}
# Ivan: 501(points), 0(throws)

while True:
    row, col = [int(x) for x in input().strip("()").split(", ")]
    current_player = players.pop(0)
    score_info[current_player][1] += 1

    if not coordinate_validator(row, col):
        players.append(current_player)
        continue

    if board[row][col] == "B":
        print(f"{current_player} won the game with {score_info[current_player][1]} throws!")
        break

    if board[row][col] != "D" and board[row][col] != "T":
        score_info[current_player][0] -= board[row][col]

    elif board[row][col] == "D":
        score_info[current_player][0] -= 2 * corresponding_numbers_finder(row, col)

    elif board[row][col] == "T":
        score_info[current_player][0] -= 3 * corresponding_numbers_finder(row, col)

    if score_info[current_player][0] <= 0:
        print(f"{current_player} won the game with {score_info[current_player][1]} throws!")
        break

    players.append(current_player)
