all_stops = input()


def index_validator(index, all_stops):
    if 0 <= index < len(all_stops):
        return True
    else:
        return False


while True:
    command = input()
    if command == "Travel":
        print(f"Ready for world tour! Planned stops: {all_stops}")
        break
    command = command.split(":")
    instructions = command[0]
    if instructions == "Add Stop":
        index = int(command[1])
        string = command[2]
        if index_validator(index, all_stops):
            all_stops = all_stops[:index] + string + all_stops[index:]
        print(all_stops)

    elif instructions == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if index_validator(start_index, all_stops) and index_validator(end_index, all_stops):
            all_stops = all_stops[:start_index] + all_stops[end_index + 1:]
        print(all_stops)

    elif instructions == "Switch":
        old_string = command[1]
        new_string = command[2]
        if old_string in all_stops:
            all_stops = all_stops.replace(old_string, new_string)
        print(all_stops)

