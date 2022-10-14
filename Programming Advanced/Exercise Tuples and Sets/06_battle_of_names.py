n = int(input())
even_set = set()
odd_set = set()

for row in range(1, n+1):
    value = int((sum([ord(ch) for ch in input()]))/row)
    if value % 2 == 0:
        even_set.add(value)
    else:
        odd_set.add(value)

sum_even = sum(list(even_set))
sum_odd = sum(list(odd_set))

if sum_even == sum_odd:
    result = odd_set.union(even_set)
elif sum_odd > sum_even:
    result = odd_set.difference(even_set)
elif sum_even > sum_odd:
    result = odd_set.symmetric_difference(even_set)

print(", ".join(map(str, result)))
