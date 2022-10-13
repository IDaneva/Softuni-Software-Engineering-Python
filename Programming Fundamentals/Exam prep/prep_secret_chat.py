concealed_message = input()

while True:
    command = input()
    if command == "Reveal":
        print(f"You have a new text message: {concealed_message}")
        break
    command = command.split(":|:")
    instructions = command[0]

    if instructions == "InsertSpace":
        index = int(command[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)

    elif instructions == "Reverse":
        substring = command[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, "", 1)
            concealed_message = concealed_message + substring[::-1]
            print(concealed_message)

        else:
            print("error")

    elif instructions == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, replacement)
            print(concealed_message)
