def shopping_list(budget: int, **things_to_buy):
    result = ""
    if budget < 100:
        return "You do not have enough budget.\n"

    types_of_products = 0

    for thing, price_and_quantity in things_to_buy.items():
        multiplication = price_and_quantity[0] * price_and_quantity[1]
        if multiplication <= budget:
            result += f"You bought {thing} for {multiplication:.2f} leva.\n"
            types_of_products += 1
            budget -= multiplication

            if types_of_products >= 5:
                return result
    return result


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
