def coordinate_validator(r, c):
    if 0 <= r < SIZE and 0 <= c < SIZE:
        return True


SIZE = 6
board = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(SIZE)]

throws = 3
won_points = 0
buckets_down = []

for throw in range(throws):
    row, col = [int(x) for x in input().strip("()").split(", ")]
    if coordinate_validator(row, col) and board[row][col] == "B" and [row, col] not in buckets_down:
        for current_row in range(SIZE):
            for current_col in range(SIZE):
                if current_col == col and current_row != row:
                    won_points += board[current_row][current_col]
        buckets_down.append([row, col])
    else:
        continue

if won_points >= 100:
    if 100 <= won_points <= 199:
        print(f"Good job! You scored {won_points} points, and you've won Football.")
    elif 200 <= won_points <= 299:
        print(f"Good job! You scored {won_points} points, and you've won Teddy Bear.")
    elif 300 <= won_points:
        print(f"Good job! You scored {won_points} points, and you've won Lego Construction Set.")


else:
    print(f"Sorry! You need {100 - won_points} points more to win a prize.")