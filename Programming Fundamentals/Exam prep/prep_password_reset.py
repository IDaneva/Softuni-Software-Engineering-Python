text = input()

while True:
    command = input()
    if command == "Done":
        print(f"Your password is: {text}")
        break
    command = command.split()
    instructions = command[0]
    if instructions == "TakeOdd":
        text = "".join([text[i] for i in range(len(text)) if i % 2 != 0])
        print(text)

    elif instructions == "Cut":
        index = int(command[1])
        length = int(command[2])
        text = text[:index] + text[index + length:]
        print(text)

    elif instructions == "Substitute":
        substring = command[1]
        replacement = command[2]
        if substring in text:
            text = text.replace(substring, replacement)
            print(text)
        else:
            print("Nothing to replace!")