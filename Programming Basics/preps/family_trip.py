budget = float(input())
number_of_nights = int(input())
price_per_night = float(input())
percent_for_additional_expenses = int(input())

if number_of_nights > 7:
    price_per_night -= price_per_night * 0.05

accomodation_total = price_per_night * number_of_nights

additional_expenses = (percent_for_additional_expenses / 100) * budget

total = accomodation_total + additional_expenses

diff = abs(budget - total)

if budget >= total:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")

