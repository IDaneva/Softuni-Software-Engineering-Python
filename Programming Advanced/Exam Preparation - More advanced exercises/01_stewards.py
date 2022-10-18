from collections import deque

seats = [x for x in input().split(", ")]

first_sequence = deque([int(x) for x in input().split(", ")])
second_sequence = deque([int(x) for x in input().split(", ")])

taken_seats = []
rotations = -1

while True:
    rotations += 1
    if len(taken_seats) == 3 or rotations == 10:
        break
    first_number = first_sequence.popleft()
    second_number = second_sequence.pop()

    found_character = chr(first_number + second_number)

    first_possible = f"{first_number}{found_character}"
    second_possible = f"{second_number}{found_character}"
    if first_possible in seats:
        if first_possible not in taken_seats:
            taken_seats.append(first_possible)
        continue
    elif second_possible in seats:
        if second_possible not in taken_seats:
            taken_seats.append(second_possible)
        continue
    else:
        first_sequence.append(first_number)
        second_sequence.appendleft(second_number)

print(f"Seat matches: {', '.join(taken_seats)}")
print(f"Rotations count: {rotations}")
