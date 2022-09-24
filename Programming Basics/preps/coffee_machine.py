drink_type = input()
sugar = input()
number_of_drinks = int(input())

price = 0
total = 0

if drink_type == "Espresso":
    if sugar == "Without":
        price = 0.90
    elif sugar == "Normal":
        price = 1
    elif sugar == "Extra":
        price = 1.20

    total = number_of_drinks * price
    if sugar == "Without":
        total -= total * 0.35

    if number_of_drinks > 5:
        total -= total * 0.25

elif drink_type == "Cappuccino":
    if sugar == "Without":
        price = 1
    elif sugar == "Normal":
        price = 1.20
    elif sugar == "Extra":
        price = 1.60

    total = number_of_drinks * price

    if sugar == "Without":
        total -= total * 0.35

elif drink_type == "Tea":
    if sugar == "Without":
        price = 0.50
    elif sugar == "Normal":
        price = 0.60
    elif sugar == "Extra":
        price = 0.70

    total = number_of_drinks * price

    if sugar == "Without":
        total -= total * 0.35

if total > 15:
    total -= total * 0.2

print(f"You bought {number_of_drinks} cups of {drink_type} for {total:.2f} lv.")