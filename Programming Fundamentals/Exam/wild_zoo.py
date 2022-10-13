def daily_zoo_tasks(animal_information):
    while True:
        command = input()
        if command == "EndDay":
            print("Animals:")
            for animal in animal_information:
                print(f"{animal} -> {animal_information[animal][0]}g")
            print("Areas with hungry animals:")
            area_info = {}
            for name, full_info in animal_information.items():
                current_area = full_info[1]
                if current_area not in area_info:
                    area_info[current_area] = 0
                area_info[current_area] += 1

            for reg, num in area_info.items():
                print(f"{reg}: {num}")
            break

        command = command.split(": ")
        instructions = command[0]
        info = command[1]

        if instructions == "Add":
            animal_name, needed_food_quantity, area = info.split("-")
            if animal_name not in animal_information:
                animal_information[animal_name] = [int(needed_food_quantity), area]
            else:
                animal_information[animal_name][0] += int(needed_food_quantity)

        elif instructions == "Feed":
            animal_name, given_food = info.split("-")
            if animal_name not in animal_information:
                continue
            else:
                if animal_information[animal_name][0] - int(given_food) <= 0:
                    del animal_information[animal_name]
                    print(f"{animal_name} was successfully fed")

                else:
                    animal_information[animal_name][0] -= int(given_food)

    return animal_information


animal_information = {}
daily_zoo_tasks(animal_information)
