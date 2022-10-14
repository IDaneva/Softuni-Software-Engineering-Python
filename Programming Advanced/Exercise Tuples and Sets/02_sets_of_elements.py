n, m = map(int, input().split())

set1 = set()
set2 = set()
for _ in range(n):
    set1.add(input())

for _ in range(m):
    set2.add(input())

print("\n".join(map(str, set1.intersection(set2))))
