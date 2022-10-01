command = ""

while command != "End":
    command = input()

    if command == "End":
        break

    if command == "SoftUni":
        continue

    for ch in command:
        print(ch * 2, end="")
    print(" ")
