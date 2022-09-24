name_of_football_team = input()
number_of_games = int(input())

wins = 0
draws = 0
loses = 0

if number_of_games < 1:
    print(f"{name_of_football_team} hasn't played any games during this season.")
else:
    for _ in range(number_of_games):
        result_of_game = input()

        if result_of_game == "W":
            wins += 1
        elif result_of_game == "D":
            draws += 1
        elif result_of_game == "L":
            loses += 1

    win_points = wins * 3
    print(f"{name_of_football_team} has won {win_points + draws} points during this season.")
    print("Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {draws}")
    print(f"## L: {loses}")
    print(f"Win rate: {(wins / number_of_games * 100):.2f}%")
