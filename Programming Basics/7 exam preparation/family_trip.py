budget = float(input())
number_of_nights = float(input())
price_per_night = float(input())
percentent_of_additional_costs = int(input()) / 100

if number_of_nights > 7:
    price_per_night -= price_per_night * 0.05
total_for_stay = price_per_night * number_of_nights

additional_costs = percentent_of_additional_costs * budget

total = total_for_stay + additional_costs

if budget >= total:
    print(f"Ivanovi will be left with {(budget - total):.2f} leva after vacation.")
else:
    print(f"{(abs(budget - total)):.2f} leva needed.")