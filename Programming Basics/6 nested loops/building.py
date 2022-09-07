number_of_floors = int(input())
number_of_apartments_per_floor = int(input())

apartment_name = ""
for floors in range(number_of_floors, 0, -1):
    for apartments in range(0, number_of_apartments_per_floor):
        if floors == number_of_floors:
            print(f"L{floors}{apartments}", end=" ")
        elif floors % 2 == 0:
            print(f"O{floors}{apartments}", end=" ")
        elif floors % 2 != 0:
            print(f"A{floors}{apartments}", end=" ")
    print()
