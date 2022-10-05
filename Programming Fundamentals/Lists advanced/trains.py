number = int(input())
wagons = [0] * number

while True:
    command = input()
    if command == "End":
        break
    else:
        data = command.split()

        if data[0] == "add":
            people_to_add = data[1]
            wagons[-1] += int(people_to_add)
        elif data[0] == "insert":
            index = int(data[1])
            people = int(data[2])
            wagons[index] += people
        elif data[0] == "leave":
            index = int(data[1])
            people = int(data[2])
            wagons[index] -= people

print(wagons)