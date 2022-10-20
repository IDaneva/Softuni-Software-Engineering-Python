def coordinates_validator(row, col):
    if 0 <= row < SIZE_OF_BOARD and 0 <= col < SIZE_OF_BOARD:
        return True
    else:
        return False


def move_queen(position):
    success = False

    for direction in directions:
        r = position[0]
        c = position[1]
        while True:
            new_row = r + directions[direction][0]
            new_col = c + directions[direction][1]
            if not coordinates_validator(new_row, new_col):
                break
            if board[new_row][new_col] == "Q":
                break
            if board[new_row][new_col] == "K":
                success = True
                break
            else:
                r = new_row
                c = new_col
        if success:
            break
    if success:
        return True


directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
    "left_up_diagonal": [-1, -1],
    "right_up_diagonal": [-1, 1],
    "left_down_diagonal": [1, -1],
    "right_down_diagonal": [1, 1]
}


SIZE_OF_BOARD = 8

queen_positions = []
king_position = []

board = []

winning_queens = []

for r in range(SIZE_OF_BOARD):
    row = input().split()
    if "K" in row:
        king_position = [r, row.index("K")]

    if "Q" in row:
        for n, j in enumerate(row):
            if j == "Q":
                queen_positions.append([r, n])

    board.append(row)

safe_king = True
for current_position in queen_positions:
    if move_queen(current_position):
        winning_queens.append(current_position)
        safe_king = False

if not safe_king:
    for wins in winning_queens:
        print(wins)
else:
    print("The king is safe!")
