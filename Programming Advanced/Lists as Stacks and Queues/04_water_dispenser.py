from collections import deque

start_quantity_in_litres = int(input())
people_in_queue = deque()

while True:
    command = input()
    if command == "Start":
        break
    else:
        name = command
        people_in_queue.append(name)

while True:
    command = input()
    if command == "End":
        break
    else:
        command = command.split()
        if command[0] == "refill":
            start_quantity_in_litres += int(command[1])
        else:
            wanted_liters = int(command[0])
            name = people_in_queue.popleft()
            if start_quantity_in_litres >= wanted_liters:
                start_quantity_in_litres -= wanted_liters
                print(f"{name} got water")
            else:
                print(f"{name} must wait")

print(f"{start_quantity_in_litres} liters left")
