width = int(input("Width"))
length = int(input("Length"))

number_of_pieces = width * length

while True:
    taken_pieces = input("Taken pieces?")

    if taken_pieces == "STOP":
        break

    if int(taken_pieces) >= number_of_pieces:
        number_of_pieces -= int(taken_pieces)
        break

    number_of_pieces -= int(taken_pieces)


if number_of_pieces >= 0:
    print(f"{number_of_pieces} pieces are left.")
else:
    print(f"No more cake left! You need {abs(number_of_pieces)} pieces more.")