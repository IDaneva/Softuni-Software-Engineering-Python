number_of_lines = int(input())
elements = set()

for _ in range(number_of_lines):
    els = input().split()
    for e in els:
        elements.add(e)

print(*elements, sep="\n")
