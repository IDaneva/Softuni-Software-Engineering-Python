raw_activation_key = input()

while True:
    command = input()
    if command == "Generate":
        print(f"Your activation key is: {raw_activation_key}")
        break
    command = command.split(">>>")
    instructions = command[0]
    if instructions == "Contains":
        substring = command[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif instructions == "Flip":
        up_low = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        if up_low == "Upper":
            raw_activation_key = raw_activation_key[:start_index] + (raw_activation_key[start_index:end_index]).upper() + raw_activation_key[end_index:]
        else:
            raw_activation_key = raw_activation_key[:start_index] + (raw_activation_key[start_index:end_index]).lower() + raw_activation_key[end_index:]
        print(raw_activation_key)

    elif instructions == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[end_index:]
        print(raw_activation_key)