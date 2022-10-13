number_of_lines = int(input())
plant_info = {}


def plant_data_base_generator(plant_info):
    for _ in range(number_of_lines):
        name_of_plant, rarity = input().split("<->")
        if name_of_plant not in plant_info:
            plant_info[name_of_plant] = {"rarity": 0}
        plant_info[name_of_plant] = {"rarity": int(rarity), "rating": []}
    return plant_info


def things_to_do_with_plants(plant_info):
    while True:
        command = input()
        if command == "Exhibition":
            print("Plants for the exhibition:")
            for plant in plant_info:
                if len(plant_info[plant]["rating"]) == 0:
                    print(f"- {plant}; Rarity: {plant_info[plant]['rarity']}; Rating: 0.00")
                else:
                    print(f"- {plant}; Rarity: {plant_info[plant]['rarity']}; Rating: {(sum(plant_info[plant]['rating'])/ len(plant_info[plant]['rating'])):.2f}")

            break
        command = command.split(": ")
        instructions = command[0]
        information = command[1]

        if instructions == "Rate":
            plant_name, rating = information.split(" - ")
            if plant_name in plant_info:
                plant_info[plant_name]["rating"].append(int(rating))
            else:
                print("error")

        elif instructions == "Update":
            plant_name, new_rarity = information.split(" - ")
            if plant_name in plant_info:
                plant_info[plant_name]["rarity"] = int(new_rarity)
            else:
                print("error")

        elif instructions == "Reset":
            if information in plant_info:
                plant_info[information]["rating"] = []
            else:
                print("error")
    return plant_info


plant_data_base_generator(plant_info)
things_to_do_with_plants(plant_info)
