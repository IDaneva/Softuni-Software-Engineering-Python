starting_index = int(input())
ending_index = int(input())

for current_index in range(starting_index, ending_index + 1):
    print(chr(current_index), end=" ")
