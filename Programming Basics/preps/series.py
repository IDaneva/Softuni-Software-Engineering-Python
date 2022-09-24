budget = float(input())
number_of_series = int(input())

total_costs = 0

for series in range(number_of_series):
    name_of_serie = input()
    price_of_serie = float(input())

    if name_of_serie == "Thrones":
        price_of_serie -= price_of_serie * 0.5

    elif name_of_serie == "Lucifer":
        price_of_serie -= price_of_serie * 0.4

    elif name_of_serie == "Protector":
        price_of_serie -= price_of_serie * 0.3

    elif name_of_serie == "TotalDrama":
        price_of_serie -= price_of_serie * 0.2

    elif name_of_serie == "Area":
        price_of_serie -= price_of_serie * 0.1

    total_costs += price_of_serie

diff = abs(budget - total_costs)

if budget >= total_costs:
    print(f"You bought all the series and left with {diff:.2f} lv.")
else:
    print(f"You need {diff:.2f} lv. more to buy the series!")
