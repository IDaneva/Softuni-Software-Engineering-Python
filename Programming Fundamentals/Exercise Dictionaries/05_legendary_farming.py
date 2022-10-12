def item_return(my_dict):
    for x, y in my_dict.items():
        print(f"{x}: {y}")


item_dict = {"shards": 0, "fragments": 0, "motes": 0}

obtained = False
while not obtained:
    items = input().split()
    for index_in_items in range(0, len(items), 2):
        quantity = int(items[index_in_items])
        material = items[index_in_items + 1].lower()
        if material not in item_dict:
            item_dict[material] = 0
        item_dict[material] += quantity
        if item_dict[material] >= 250 and (material == "shards" or material == "fragments" or material == "motes"):
            obtained = True
            item_dict[material] -= 250
            if material == "shards":
                print("Shadowmourne obtained!")
            elif material == "fragments":
                print("Valanyr obtained!")
            elif material == "motes":
                print("Dragonwrath obtained!")
            break

item_return(item_dict)