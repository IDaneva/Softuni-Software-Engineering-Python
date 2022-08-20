tournaments = int(input())
starting_points = int(input())

points = 0
wins = 0

for _ in range(tournaments):
    ending_in_tournament = input()
    if ending_in_tournament.upper() == "W":
        points += 2000
        wins += 1
    elif ending_in_tournament.upper() == "F":
        points += 1200
    elif ending_in_tournament.upper() == "SF":
        points += 720

total = points + starting_points

average = (total - starting_points) / tournaments

percentage = wins / tournaments * 100

print(f"Final points: {total}")
print(f"Average points: {int(average)}")
print(f"{percentage:.2f}%")
