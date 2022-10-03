def order_calculator(item, quantity):
    price = 0
    if item == "coffee":
        price = 1.5
    elif item == "water":
        price = 1
    elif item == "coke":
        price = 1.4
    elif item == "snacks":
        price = 2
    return price * quantity


product = input()
number_of_products = int(input())
print(f"{order_calculator(product, number_of_products):.2f}")
