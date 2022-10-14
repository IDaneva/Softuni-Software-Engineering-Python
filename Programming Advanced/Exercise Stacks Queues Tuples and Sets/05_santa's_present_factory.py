from collections import deque

materials_for_toys = list(map(int, input().split()))
magic_level = deque(map(int, input().split()))

info_dict = {
    "Doll": {"magic": 150, "crafted": 0},
    "Wooden train": {"magic": 250, "crafted": 0},
    "Teddy bear": {"magic": 300, "crafted": 0},
    "Bicycle": {"magic": 400, "crafted": 0}
}

while materials_for_toys and magic_level:
    last_box = materials_for_toys[-1]
    first_magic = magic_level[0]
    flag = False

    if last_box == 0:
        materials_for_toys.pop()
        flag = True
    if first_magic == 0:
        magic_level.popleft()
        flag = True

    if flag:
        continue

    multiplication = last_box * first_magic

    if multiplication == info_dict["Doll"]["magic"]:
        info_dict["Doll"]["crafted"] += 1
        materials_for_toys.pop()
        magic_level.popleft()
        continue
    elif multiplication == info_dict["Wooden train"]["magic"]:
        info_dict["Wooden train"]["crafted"] += 1
        materials_for_toys.pop()
        magic_level.popleft()
        continue
    elif multiplication == info_dict["Teddy bear"]["magic"]:
        info_dict["Teddy bear"]["crafted"] += 1
        materials_for_toys.pop()
        magic_level.popleft()
        continue
    elif multiplication == info_dict["Bicycle"]["magic"]:
        info_dict["Bicycle"]["crafted"] += 1
        materials_for_toys.pop()
        magic_level.popleft()
        continue

    if multiplication < 0:
        value = last_box + first_magic
        materials_for_toys.pop()
        magic_level.popleft()
        materials_for_toys.append(value)

    elif multiplication > 0:
        magic_level.popleft()
        materials_for_toys[-1] += 15

if info_dict["Doll"]["crafted"] >= 1 and info_dict["Wooden train"]["crafted"] >= 1 or \
        info_dict["Teddy bear"]["crafted"] >= 1 and info_dict["Bicycle"]["crafted"] >= 1:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials_for_toys:
    print(f"Materials left: {', '.join(reversed([str(mat) for mat in materials_for_toys]))}")
if magic_level:
    print(f"Magic left: {', '.join([str(mag) for mag in magic_level])}")

for current_toy in sorted(info_dict):
    if info_dict[current_toy]['crafted'] != 0:
        print(f"{current_toy}: {info_dict[current_toy]['crafted']}")
