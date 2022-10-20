from collections import deque
SIZE = 8

white_position = []
black_position = []

board = []

for r in range(SIZE):
    row = input().split()
    board.append(row)
    if "w" in row:
        white_position = [r, row.index("w")]
    if "b" in row:
        black_position = [r, row.index("b")]

players = deque(["white", "black"])

while True:
    current_player = players.popleft()

    if current_player == "white":
        if white_position[0] == 0:
            print(f"Game over! White pawn is promoted to a queen at {chr(97 + white_position[1])}8.")
            break

        if board[white_position[0] - 1][white_position[1] - 1] == "b":
            print(f"Game over! White win, capture on {chr(97 + (white_position[1] - 1))}{SIZE - (white_position[0] - 1)}.")
            break
        elif board[white_position[0] - 1][white_position[1] + 1] == "b":
            print(f"Game over! White win, capture on {chr(97 + (white_position[1] + 1))}{SIZE - (white_position[0] - 1)}.")
            break

        new_row_white = white_position[0] - 1
        new_col_white = white_position[1]

        if new_row_white == 0:
            print(f"Game over! White pawn is promoted to a queen at {chr(97 + new_col_white)}8.")
            break

        board[white_position[0]][white_position[1]] = "-"
        white_position = [new_row_white, new_col_white]
        board[white_position[0]][white_position[1]] = "w"
        players.append(current_player)
        continue

    elif current_player == "black":

        if black_position[0] == SIZE - 1:
            print(f"Game over! Black pawn is promoted to a queen at {chr(97 + black_position[1])}1.")
            break

        if board[black_position[0] + 1][black_position[1] - 1] == "w":
            print(f"Game over! Black win, capture on {chr(97 + (black_position[1] - 1))}{SIZE - (black_position[0] + 1)}.")
            break
        elif board[black_position[0] + 1][black_position[1] + 1] == "w":
            print(f"Game over! Black win, capture on {chr(97 + (black_position[1] + 1))}{SIZE - (black_position[0] + 1)}.")
            break

        new_row_black = black_position[0] + 1
        new_col_black = black_position[1]

        if new_row_black == SIZE - 1:
            print(f"Game over! Black pawn is promoted to a queen at {chr(97 + new_col_black)}1.")
            break

        board[black_position[0]][black_position[1]] = "-"
        black_position = [new_row_black, new_col_black]
        board[black_position[0]][black_position[1]] = "b"
        players.append(current_player)
        continue

