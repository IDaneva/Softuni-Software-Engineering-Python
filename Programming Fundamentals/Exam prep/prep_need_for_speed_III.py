def car_data_base_generator(number_of_cars, garage_info):
    for _ in range(number_of_cars):
        car, mileage, fuel = input().split("|")
        if car not in garage_info:
            garage_info[car] = [int(mileage), int(fuel)]
    return garage_info


def things_to_do_with_cars(garage_info):
    while True:
        command = input()
        if command == "Stop":
            for car in garage_info:
                print(f"{car} -> Mileage: {garage_info[car][0]} kms, Fuel in the tank: {garage_info[car][1]} lt.")
            break
        command = command.split(" : ")
        instructions = command[0]
        car_name = command[1]

        if instructions == "Drive":
            distance = int(command[2])
            fuel = int(command[3])

            if garage_info[car_name][1] >= fuel:
                garage_info[car_name][1] -= fuel
                garage_info[car_name][0] += distance
                print(f"{car_name} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

                if garage_info[car_name][0] >= 100000:
                    print(f"Time to sell the {car_name}!")
                    del garage_info[car_name]
            else:
                print("Not enough fuel to make that ride")

        elif instructions == "Refuel":
            wanted_litres_to_refuel = int(command[2])
            capacity_to_refuel = 75 - garage_info[car_name][1]
            if wanted_litres_to_refuel > capacity_to_refuel:
                garage_info[car_name][1] += capacity_to_refuel
                print(f"{car_name} refueled with {capacity_to_refuel} liters")
            else:
                garage_info[car_name][1] += wanted_litres_to_refuel
                print(f"{car_name} refueled with {wanted_litres_to_refuel} liters")

        elif instructions == "Revert":
            kilometers_to_decrease = int(command[2])
            if garage_info[car_name][0] - kilometers_to_decrease <= 10000:
                garage_info[car_name][0] = 10000
            else:
                garage_info[car_name][0] -= kilometers_to_decrease
                print(f"{car_name} mileage decreased by {kilometers_to_decrease} kilometers")

    return garage_info


number_of_cars = int(input())
garage_info = {}
car_data_base_generator(number_of_cars, garage_info)
things_to_do_with_cars(garage_info)
