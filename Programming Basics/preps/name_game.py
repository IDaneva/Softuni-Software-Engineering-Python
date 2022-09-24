max_points = 0
current_player = ""

while True:
    name_of_player = input()

    if name_of_player == "Stop":
        break
    else:
        points = 0
        for ch in name_of_player:
            guessed_number = int(input())

            if guessed_number == (ord(ch)):
                points += 10
            else:
                points += 2

            if points >= max_points:
                max_points = points
                current_player = name_of_player

print(f"The winner is {current_player} with {max_points} points!")