from collections import deque


def best_list_pureness(numbers: list, K):
    numbers = deque(numbers)
    highest_pureness = 0
    made_rotations = 0
    best_rotation_count = 0

    for rotation in range(K+1):
        current = 0
        for idx, value in enumerate(numbers):
            current += idx * value

        if current > highest_pureness:
            highest_pureness = current
            best_rotation_count = made_rotations
        numbers.appendleft(numbers.pop())
        made_rotations += 1

    return f"Best pureness {highest_pureness} after {best_rotation_count} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
