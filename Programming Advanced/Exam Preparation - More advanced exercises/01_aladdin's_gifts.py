from collections import deque


def check_made_material(result_of_sum):
    if 100 <= result_of_sum <= 199:
        gifts["Gemstone"]["made"] += 1
    elif 200 <= result_of_sum <= 299:
        gifts["Porcelain Sculpture"]["made"] += 1
    elif 300 <= result_of_sum <= 399:
        gifts["Gold"]["made"] += 1
    elif 400 <= result_of_sum <= 499:
        gifts["Diamond Jewellery"]["made"] += 1
    else:
        return False


def success_in_crafting():
    if gifts["Gemstone"]["made"] > 0 and gifts["Porcelain Sculpture"]["made"] > 0:
        return True
    elif gifts["Gold"]["made"] > 0 and gifts["Diamond Jewellery"]["made"] > 0:
        return True
    else:
        return False


materials_for_presents = deque([int(x) for x in input().split()])
genie_magic_level = deque([int(x) for x in input().split()])

gifts = {
    "Gemstone": {"needed_magic": [100, 199], "made": 0},
    "Porcelain Sculpture": {"needed_magic": [200, 299], "made": 0},
    "Gold": {"needed_magic": [300, 399], "made": 0},
    "Diamond Jewellery": {"needed_magic": [400, 499], "made": 0}
}


while True:
    if not materials_for_presents or not genie_magic_level:
        break
    last_material = materials_for_presents.pop()
    first_magic_level = genie_magic_level.popleft()
    product_to_check = last_material + first_magic_level

    if not check_made_material(product_to_check):

        if product_to_check < 100:
            if product_to_check % 2 == 0:
                materials = last_material * 2
                magic = first_magic_level * 3
                num_to_check = materials + magic
                check_made_material(num_to_check)

            elif product_to_check % 2 != 0:
                num_to_check = product_to_check * 2
                check_made_material(num_to_check)

        elif product_to_check > 499:
            num_to_check = product_to_check / 2
            check_made_material(num_to_check)
        else:
            continue

if success_in_crafting():
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials_for_presents:
    print(f"Materials left: {', '.join(list(map(str, materials_for_presents)))}")

if genie_magic_level:
    print(f"Magic left: {', '.join(list(map(str, genie_magic_level)))}")

sorted_gift_info = dict(sorted(gifts.items()))

for k in sorted_gift_info:
    if sorted_gift_info[k]["made"] > 0:
        print(f"{k}: {sorted_gift_info[k]['made']}")

