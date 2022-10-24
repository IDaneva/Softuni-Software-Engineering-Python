from collections import deque
caffeine_miligrams = [int(x) for x in input().split(", ")]
energy_drinks = deque(int(x) for x in input().split(", "))

max_caffeine = 300

total_caffeine = 0

while True:
    if not caffeine_miligrams or not energy_drinks:
        break

    last_miligram = caffeine_miligrams.pop()
    first_energy_drink = energy_drinks.popleft()
    multiplication = last_miligram * first_energy_drink

    if multiplication + total_caffeine <= max_caffeine:
        total_caffeine += multiplication
        continue
    else:
        energy_drinks.append(first_energy_drink)
        if total_caffeine - 30 <= 0:
            total_caffeine = 0
        else:
            total_caffeine -= 30


if not energy_drinks:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
else:
    print(f"Drinks left: {', '.join(list(map(str, energy_drinks)))}")

print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")
