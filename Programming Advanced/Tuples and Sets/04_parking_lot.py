number_of_instructions = int(input())
plates = set()
for _ in range(number_of_instructions):
    command, plate = input().split(", ")
    if command == "IN":
        plates.add(plate)
    else:
        plates.remove(plate)

if len(plates) > 0:
    print("\n".join(plates))
else:
    print("Parking Lot is Empty")
