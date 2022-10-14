n = int(input())
unique_names = []
for _ in range(n):
    unique_names.append(input())

print("\n".join(set(unique_names)))