from itertools import permutations


def possible_permutations(sequence:list):
    perm = permutations(sequence)
    for x in perm:
        yield list(x)


[print(n) for n in possible_permutations([1, 2, 3])]