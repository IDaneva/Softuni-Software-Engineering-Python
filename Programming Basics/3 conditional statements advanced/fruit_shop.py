product = input()
day = input()
amount = float(input())

price = 0

if day in "Monday Tuesday Wednesday Thursday Friday":
    if product not in "banana apple orange grapefruit kiwi pineapple grapes":
        print("error")
    elif product == "banana":
        price = 2.50
    elif product == "apple":
        price = 1.20
    elif product == "orange":
        price = 0.85
    elif product == "grapefruit":
        price = 1.45
    elif product == "kiwi":
        price = 2.70
    elif product == "pineapple":
        price = 5.50
    elif product == "grapes":
        price = 3.85
elif day in "Saturday Sunday":
    if product == "banana":
        price = 2.70
    elif product == "apple":
        price = 1.25
    elif product == "orange":
        price = 0.90
    elif product == "grapefruit":
        price = 1.60
    elif product == "kiwi":
        price = 3
    elif product == "pineapple":
        price = 5.60
    elif product == "grapes":
        price = 4.20
else:
    print("error")

total_price = price * amount

if price != 0:
    print(f"{total_price:.2f}")
