budget = float(input())

costs = 0
product_counter = 0

condition = True

while True:
    product = input()

    if product == "Stop":
        break

    product_counter += 1
    price_of_product = float(input())

    if product_counter % 3 == 0:
        price_of_product /= 2

    costs += price_of_product
    budget -= price_of_product

    if price_of_product > budget:
        condition = False
        product_counter -= 1
        break


if not condition:
    print("You don't have enough money!")
    print(f"You need {(abs(budget)):.2f} leva!")
else:
    print(f"You bought {product_counter} products for {costs:.2f} leva.")