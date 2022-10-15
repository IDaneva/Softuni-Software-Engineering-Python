size = int(input())

matrix = [[int(n) for n in input().split()] for _ in range(size)]

while True:
    command = input().split()
    instructions = command[0]
    if instructions == "END":
        break
    row, col, num = list(map(int, command[1::]))
    if False in [0 <= row < size, 0 <= col < size]:
        print("Invalid coordinates")
        continue

    if instructions == "Add":
        matrix[row][col] += num
    elif instructions == "Subtract":
        matrix[row][col] -= num

[print(*row) for row in matrix]
