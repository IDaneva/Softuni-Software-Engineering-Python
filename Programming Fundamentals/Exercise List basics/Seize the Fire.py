type_of_fire_and_their_cells = input().split("#")
water = int(input())
put_out_cells = []
effort = 0

for element in type_of_fire_and_their_cells:
    splited_info = element.split("=")
    if splited_info[0] == "High ":
        if int(splited_info[1]) > 125 or int(splited_info[1]) < 81:
            continue
        else:
            if water >= int(splited_info[1]):
                water -= int(splited_info[1])
                put_out_cells.append(splited_info[1])
                effort += 0.25 * int(splited_info[1])
    elif splited_info[0] == "Medium ":
        if int(splited_info[1]) > 80 or int(splited_info[1]) < 51:
            continue
        else:
            if water >= int(splited_info[1]):
                water -= int(splited_info[1])
                put_out_cells.append(splited_info[1])
                effort += 0.25 * int(splited_info[1])
    elif splited_info[0] == "Low ":
        if int(splited_info[1]) > 50 or int(splited_info[1]) < 1:
            continue
        else:
            if water >= int(splited_info[1]):
                water -= int(splited_info[1])
                put_out_cells.append(splited_info[1])
                effort += 0.25 * int(splited_info[1])

print("Cells:")
for cells in put_out_cells:
    print(f" -{cells}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum([int(x) for x in put_out_cells])}")
