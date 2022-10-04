is_even = lambda x: x % 2 == 0


sequence = [int(s) for s in input().split()]

result = list(filter(is_even, sequence))
print(result)
