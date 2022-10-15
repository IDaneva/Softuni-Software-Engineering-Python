rows, columns = [int(x) for x in input().split()]
matrix = [input().split() for i in range(rows)]

while True:
    command = input()
    if command == "END":
        break
    command = command.split()
    if command[0] != "swap" or len(command) != 5:
        print("Invalid input!")
        continue
    row1 = int(command[1])
    col1 = int(command[2])
    row2 = int(command[3])
    col2 = int(command[4])
    if False in [0 <= row1 < rows, 0 <= col1 < columns, 0 <= row2 < rows, 0 <= col2 < columns]:
        print("Invalid input!")
        continue
    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
    for s in matrix:
        print(' '.join(s))
