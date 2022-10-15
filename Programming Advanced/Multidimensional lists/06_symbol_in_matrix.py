size = int(input())
matrix = []

for _ in range(size):
    matrix.append(list(input()))
target_symbol = input()

found = False
for row in range(size):
    for column in range(size):
        if matrix[row][column] == target_symbol:
            print(f"({row}, {column})")
            found = True
            break
    if found:
        break
if not found:
    print(f"{target_symbol} does not occur in the matrix")
