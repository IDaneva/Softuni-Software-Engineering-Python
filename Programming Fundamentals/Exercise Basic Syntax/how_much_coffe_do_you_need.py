coffee = 0

while True:
    command = input()

    if command.upper() == "END":
        break
    if command.lower() in ["dog", "cat", "coding", "movie"]:
        if command.islower():
            coffee += 1
        elif command.isupper():
            coffee += 2


if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)
