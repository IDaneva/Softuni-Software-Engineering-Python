trip_price = float(input())
puzzle_amount = int(input())
doll_amount = int(input())
teddies_amount = int(input())
minions_amount = int(input())
trucks_amount = int(input())

toys_price = puzzle_amount * 2.60 + doll_amount * 3 + teddies_amount * 4.10 + minions_amount * 8.20 + trucks_amount * 2

toys_amount = puzzle_amount + doll_amount + teddies_amount + minions_amount + trucks_amount

if toys_amount >= 50:
    toys_price = toys_price - (0.25 * toys_price)

rent = toys_price * 0.10
profit = toys_price - rent

diff = abs(profit - trip_price)

if profit >= trip_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")
