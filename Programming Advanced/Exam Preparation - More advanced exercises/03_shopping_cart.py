def shopping_cart(*args):
    products_dict = {"Soup": {"product_limit": 3, "bought_products": []},
                     "Pizza": {"product_limit": 4, "bought_products": []},
                     "Dessert": {"product_limit": 2, "bought_products": []}}

    for current_info in args:
        if current_info == "Stop":
            if len(products_dict["Soup"]["bought_products"]) == 0 and len(products_dict["Pizza"]["bought_products"]) == 0 and len(products_dict["Dessert"]["bought_products"]) == 0:
                return "No products in the cart!"
            break
        food = current_info[0]
        product = current_info[1]
        if len(products_dict[food]["bought_products"]) < products_dict[food]["product_limit"] and product not \
                in products_dict[food]["bought_products"]:
            products_dict[food]["bought_products"].append(product)
    sorted_info = dict(sorted(products_dict.items(), key=lambda x: (-len(x[1]["bought_products"]), x[0])))
    result = ""
    for meal, ingredients in sorted_info.items():
        result += f'{meal}:\n'
        for i in sorted(ingredients["bought_products"]):
            result += f" - {i}\n"
    return result


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
