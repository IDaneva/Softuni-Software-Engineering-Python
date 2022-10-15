from collections import deque

rows, columns = [int(x) for x in input().split()]
snake = input()
snake_deque = deque(snake)
matrix = []

for row in range(rows):
    current_row = []
    for col in range(columns):
        current_row.append(snake_deque.popleft())

        if not snake_deque:
            snake_deque = deque(snake)

    matrix.append(current_row)
    if row % 2 == 0:
        print("".join(current_row))
    else:
        print("".join(current_row[::-1]))
