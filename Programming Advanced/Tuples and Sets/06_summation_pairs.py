sequence = list(map(int, input().split()))
used_indexes = set()
target = int(input())

for index in range(len(sequence)):
    n1 = sequence[index]
    for idx2 in range(index + 1, len(sequence)):
        n2 = sequence[idx2]
        if n1 + n2 == target and index not in used_indexes and idx2 not in used_indexes:
            used_indexes.add(index)
            used_indexes.add(idx2)
            print(f"{sequence[index]} + {sequence[idx2]} = {target}")