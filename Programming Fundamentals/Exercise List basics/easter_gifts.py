gift_names = input().split()

while True:
    commands = input().split(" ")
    if commands[0] == "No" and commands[1] == "Money":
        break
    elif commands[0] == "OutOfStock":
        for index, digit in enumerate(gift_names):
            if digit == commands[1]:
                gift_names[index] = "None"
    elif commands[0] == "Required":
        if 0 <= int(commands[2]) < len(gift_names):
            gift_names[int(commands[2])] = commands[1]
            # gift_names.pop(int(commands[2]))
            # gift_names.insert(int(commands[2]), commands[1])
    elif commands[0] == "JustInCase":
        gift_names[-1] = commands[1]
        # gift_names.pop(-1)
        # gift_names.append(commands[1])

for gift in range(len(gift_names)):
    if "None" in gift_names:
        gift_names.remove("None")
print(gift_names)

# print(" ".join(str(element) for element in gift_names if element != "None"))
