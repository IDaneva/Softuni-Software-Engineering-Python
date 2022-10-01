animals = input()
list_of_animals = animals.split(", ")

sheep_count = 0

if list_of_animals[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for item in range(len(list_of_animals)):
        if list_of_animals[item] == "sheep":
            sheep_count += 1
        elif list_of_animals[0] == "wolf":
            print(f"Oi! Sheep number {len(list_of_animals) - 1}! You are about to be eaten by a wolf!")
        elif list_of_animals[item] == "wolf":
            print(f"Oi! Sheep number {len(list_of_animals) - sheep_count -1}! You are about to be eaten by a wolf!")
