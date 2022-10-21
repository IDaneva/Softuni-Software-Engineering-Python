from collections import deque

elves_energy = deque([int(x) for x in input().split()])
number_of_materials_in_box = [int(x) for x in input().split()]

made_toys = 0
total_energy_used = 0
attempt = 1

while True:
    if not elves_energy or not number_of_materials_in_box:
        break

    first_elf = elves_energy.popleft()
    if first_elf < 5:
        continue
    last_material = number_of_materials_in_box.pop()

    if attempt % 3 == 0:
        if attempt % 5 == 0:
            if first_elf >= last_material:
                made_toys += 0
                first_elf -= last_material
                total_energy_used += last_material
                elves_energy.append(first_elf)
            else:
                number_of_materials_in_box.append(last_material)
                first_elf *= 2
                elves_energy.append(first_elf)
        else:
            if first_elf >= last_material * 2:
                made_toys += 2
                first_elf -= last_material * 2
                total_energy_used += last_material * 2
                first_elf += 1
                elves_energy.append(first_elf)
            else:
                number_of_materials_in_box.append(last_material)
                first_elf *= 2
                elves_energy.append(first_elf)

    elif attempt % 5 == 0:
        if first_elf >= last_material:
            made_toys += 0
            first_elf -= last_material
            total_energy_used += last_material
            elves_energy.append(first_elf)
        else:
            number_of_materials_in_box.append(last_material)
            first_elf *= 2
            elves_energy.append(first_elf)
    else:
        if first_elf >= last_material:
            made_toys += 1
            first_elf -= last_material
            total_energy_used += last_material
            first_elf += 1
            elves_energy.append(first_elf)
        else:
            number_of_materials_in_box.append(last_material)
            first_elf *= 2
            elves_energy.append(first_elf)

    attempt += 1

print(f"Toys: {made_toys}")
print(f"Energy: {total_energy_used}")

if elves_energy:
    print(f"Elves left: {', '.join(list(map(str, elves_energy)))}")
if number_of_materials_in_box:
    print(f"Boxes left: {', '.join(list(map(str, number_of_materials_in_box)))}")