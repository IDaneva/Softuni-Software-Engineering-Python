number_of_messages = int(input())

for _ in range(number_of_messages):
    command = int(input())

    if command == 88:
        print("Hello")
    elif command == 86:
        print("How are you?")
    elif command < 88:
        print("GREAT!")
    elif command > 88:
        print("Bye.")