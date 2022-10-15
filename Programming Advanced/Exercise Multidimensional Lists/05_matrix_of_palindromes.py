rows, columns = [int(x) for x in input().split()]
matrix = []
first_char = 97

for row in range(rows):
    current_row = []
    for column in range(columns):
        current_row.append(f'{chr(first_char + row)}{chr(first_char + row + column)}{chr(first_char + row)}')
    matrix.append(current_row)
    print(" ".join(current_row))
