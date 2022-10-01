number_of_orders = int(input())
overall = 0

for _ in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if price_per_capsule < 0.01 or price_per_capsule > 100 or days < 1 or days > 31 or capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    else:
        total = (price_per_capsule * capsules_per_day) * days
        overall += total
        print(f"The price for the coffee is: ${total:.2f}")

print(f"Total: ${overall:.2f}")