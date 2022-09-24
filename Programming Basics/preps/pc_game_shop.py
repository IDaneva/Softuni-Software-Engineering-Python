number_of_sold_games = int(input())

hearthstone_games = 0
fortnite_games = 0
overwatch_games = 0
other_games = 0


for games in range(number_of_sold_games):
    name_of_game = input()

    if name_of_game == "Hearthstone":
        hearthstone_games += 1
    elif name_of_game == "Fornite":
        fortnite_games += 1
    elif name_of_game == "Overwatch":
        overwatch_games += 1
    else:
        other_games += 1

print(f"Hearthstone - {(hearthstone_games / number_of_sold_games * 100):.2f}%")
print(f"Fornite - {(fortnite_games / number_of_sold_games * 100):.2f}%")
print(f"Overwatch - {(overwatch_games / number_of_sold_games * 100):.2f}%")
print(f"Others - {(other_games / number_of_sold_games * 100):.2f}%")