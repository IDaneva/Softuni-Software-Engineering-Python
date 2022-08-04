budget = int(input())
season = input()
fishermen = int(input())

costs = 0

if season == "Spring":
    costs = 3000
elif season == "Summer" or season == "Autumn":
    costs = 4200
elif season == "Winter":
    costs = 2600

if fishermen <= 6:
    costs -= costs * 0.10
elif 6 < fishermen <= 11:
    costs -= costs * 0.15
elif fishermen > 11:
    costs -= costs * 0.25

if fishermen % 2 == 0 and season != "Autumn":
    costs -= costs * 0.05

diff = abs(budget - costs)

if budget >= costs:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
