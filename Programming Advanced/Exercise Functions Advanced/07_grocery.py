def grocery_store(**kwargs):
    receipt = {}
    result = ""
    for key, value in kwargs.items():
        receipt[key] = value
    receipt_sort = dict(sorted(receipt.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    for product, quantity in receipt_sort.items():
        result += f"{product}: {quantity}" + "\n"
    return result


print(grocery_store(

bread=5,

pasta=12,

eggs=12,

))