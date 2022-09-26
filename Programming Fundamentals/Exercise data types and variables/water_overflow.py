number_of_lines = int(input())
capacity = 255
used_capacity = 0

for litres in range(number_of_lines):
    water_used = int(input())
    used_capacity += water_used

    if used_capacity > capacity:
        used_capacity -= water_used
        print("Insufficient capacity!")
        continue
print(used_capacity)
