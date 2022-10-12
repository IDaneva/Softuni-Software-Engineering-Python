number_of_cars = int(input())

data_base = {}

for _ in range(number_of_cars):
    command = input()
    if "unregister" in command:
        event, username = command.split()
        if username not in data_base:
            print(f"ERROR: user {username} not found")
        else:
            del data_base[username]
            print(f"{username} unregistered successfully")
    else:
        event, username, license_plate = command.split()
        if username not in data_base:
            data_base[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {data_base[username]}")

print(data_base)

for key, value in data_base.items():
    print(f"{key} => {value}")
