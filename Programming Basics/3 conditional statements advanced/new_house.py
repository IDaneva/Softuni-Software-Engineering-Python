flowers_type = input()
flowers_amount = int(input())
budget = int(input())

costs = 0

if flowers_type == "Roses":
    costs = 5
    final_price = flowers_amount * costs
    if flowers_amount > 80:
        final_price -= final_price * 0.10
elif flowers_type == "Dahlias":
    costs = 3.80
    final_price = flowers_amount * costs
    if flowers_amount > 90:
        final_price -= final_price * 0.15
elif flowers_type == "Tulips":
    costs = 2.80
    final_price = flowers_amount * costs
    if flowers_amount > 80:
        final_price -= final_price * 0.15
elif flowers_type == "Narcissus":
    costs = 3
    final_price = flowers_amount * costs
    if flowers_amount < 120:
        final_price += final_price * 0.15
elif flowers_type == "Gladiolus":
    costs = 2.50
    final_price = flowers_amount * costs
    if flowers_amount < 80:
        final_price += final_price * 0.20

diff = abs(budget - final_price)

if budget >= final_price:
    print(f"Hey, you have a great garden with {flowers_amount} {flowers_type} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
