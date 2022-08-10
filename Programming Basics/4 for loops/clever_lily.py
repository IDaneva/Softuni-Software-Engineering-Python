age = int(input())
washing_machine_price = float(input())
price_per_toy = int(input())

toys = 0
savings = 0

for i in range(1, age + 1):
    if i % 2 != 0:
        toys += 1
    elif i % 2 == 0:
        savings += 10 * i/2 - 1

sold_toys = toys * price_per_toy

total_savings = savings + sold_toys

diff = abs(washing_machine_price - total_savings)

if total_savings >= washing_machine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
    