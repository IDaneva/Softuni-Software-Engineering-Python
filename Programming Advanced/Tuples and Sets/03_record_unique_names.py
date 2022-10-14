number_of_names = int(input())
unique_data = []

for _ in range(number_of_names):
    name = input()
    unique_data.append(name)

print("\n".join(set(unique_data)))
