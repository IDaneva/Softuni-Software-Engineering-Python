encrypted_message = input()

while True:
    command = input()
    if command == "Decode":
        print(f"The decrypted message is: {encrypted_message}")
        break
    command = command.split("|")
    instructions = command[0]
    if instructions == "Move":
        number_of_letters = int(command[1])
        encrypted_message = encrypted_message[number_of_letters:] + encrypted_message[:number_of_letters]
    elif instructions == "Insert":
        index = int(command[1])
        value = command[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif instructions == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        if substring in encrypted_message:
            encrypted_message = encrypted_message.replace(substring, replacement)

