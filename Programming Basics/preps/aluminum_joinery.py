ammount = int(input())
type = input()
delivery = input()
price = 0

if type == "90X130":
    price = 110
    if ammount > 60:
        price -= 0.08 * price
    elif ammount > 30:
        price -= 0.05 * price

elif type == "100X150":
    price = 140
    if ammount > 80:
        price -= 0.1 * price
    elif ammount > 40:
        price -= 0.06 * price

elif type == "130X180":
    price = 190
    if ammount > 50:
        price -= 0.12 * price
    elif ammount > 20:
        price -= 0.07 * price

elif type == "200X300":
    price = 250
    if ammount > 50:
        price -= 0.14 * price
    elif ammount > 25:
        price -= 0.09 * price

total = price * ammount

if delivery == "With delivery":
    total += 60

if ammount > 99:
    total -= 0.04 * total
if ammount < 10:
    print("Invalid order")
else:
    print(f"{total:.2f} BGN")
