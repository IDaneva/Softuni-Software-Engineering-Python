import os

while True:
    command = input().split("-")
    instructions = command[0]

    if instructions == "End":
        break

    file_name = command[1]

    if instructions == "Create":
        with open(f"{file_name}", "w") as file:
            pass

    elif instructions == "Add":
        content = command[2]
        with open(f"{file_name}", "a") as file:
            file.write(f"{content}\n")

    elif instructions == "Replace":
        try:
            old_string = command[2]
            new_string = command[3]
            with open(f"{file_name}", "r+") as new_file:
                text = new_file.read().replace(old_string, new_string)
                new_file.seek(0)
                new_file.truncate()
                new_file.write(text)
        except FileNotFoundError:
            print("An error occurred")

    elif instructions == "Delete":
        try:
            os.remove(f"{file_name}")
        except FileNotFoundError:
            print("An error occurred")
    else:
        break

