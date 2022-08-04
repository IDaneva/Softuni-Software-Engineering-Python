days = int(input())
room_type = input()
review = input()

nights = days - 1
costs = 0
price = 0

if room_type == "room for one person":
    price = 18
    costs = nights * price

elif room_type == "apartment":
    price = 25
    if days < 10:
        costs = nights * price - 0.3 * nights * price
    elif 10 <= days <= 15:
        costs = nights * price - 0.35 * nights * price
    elif days > 15:
        costs = nights * price - 0.5 * nights * price
elif room_type == "president apartment":
    price = 35
    if days < 10:
        costs = nights * price - 0.1 * nights * price
    elif 10 <= days <= 15:
        costs = nights * price - 0.15 * nights * price
    elif days > 15:
        costs = nights * price - 0.2 * nights * price

if review == "positive":
    costs += 0.25 * costs
else:
    costs -= 0.10 * costs

print(f"{costs:.2f}")

