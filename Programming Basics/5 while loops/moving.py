width = int(input())
length = int(input())
height = int(input())

available_space = width * height * length

while True:
    boxes = input()

    if boxes == "Done":
        break

    else:
        available_space -= int(boxes)
        if available_space < 0:
            break

if available_space < 0:
    print(f"No more free space! You need {abs(available_space)} Cubic meters more.")
else:
    print(f"{available_space} Cubic meters left.")
