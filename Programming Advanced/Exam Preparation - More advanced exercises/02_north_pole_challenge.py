def found_item_validator(items_dict):
    if items["decorations"]["all"] == items["decorations"]["found"] \
            and items["gifts"]["all"] == items["gifts"]["found"] \
            and items["cookies"]["all"] == items["cookies"]["found"]:
        print("Merry Christmas!")
        return True


rows, cols = [int(x) for x in input().split(", ")]

items = {
    'decorations': {"all": 0, "found": 0},
    'gifts': {"all": 0, "found": 0},
    'cookies': {"all": 0, "found": 0}
}

santa_position = []
workshop = []

directions = {
    "left": (0, -1),
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0)
}

for r in range(rows):
    row = input().split()
    if "Y" in row:
        santa_position = [r, row.index("Y")]
    items["decorations"]["all"] += row.count("D")
    items["gifts"]["all"] += row.count("G")
    items["cookies"]["all"] += row.count("C")
    workshop.append(row)

workshop[santa_position[0]][santa_position[1]] = "x"
found = False
while True:
    command = input()
    if command == "End":
        workshop[santa_position[0]][santa_position[1]] = "Y"
        break
    if found_item_validator(items):
        print("Merry Christmas!")
        workshop[santa_position[0]][santa_position[1]] = "Y"
        break
    way_to_go, steps = command.split("-")
    for _ in range(int(steps)):
        new_row = santa_position[0] + directions[way_to_go][0]
        new_col = santa_position[1] + directions[way_to_go][1]
        if new_row == -1:
            new_row = rows - 1
        elif new_row == rows:
            new_row = 0
        if new_col == -1:
            new_col = cols - 1
        elif new_col == cols:
            new_col = 0

        santa_position = [new_row, new_col]
        if workshop[santa_position[0]][santa_position[1]] == "D":
            items["decorations"]["found"] += 1
        elif workshop[santa_position[0]][santa_position[1]] == "G":
            items["gifts"]["found"] += 1
        elif workshop[santa_position[0]][santa_position[1]] == "C":
            items["cookies"]["found"] += 1
        if found_item_validator(items):
            workshop[santa_position[0]][santa_position[1]] = "Y"
            found = True
            break
        workshop[santa_position[0]][santa_position[1]] = "x"
    if found:
        break

print("You've collected:")
print(f"- {items['decorations']['found']} Christmas decorations")
print(f"- {items['gifts']['found']} Gifts")
print(f"- {items['cookies']['found']} Cookies")


for r in workshop:
    print(' '.join(r))
