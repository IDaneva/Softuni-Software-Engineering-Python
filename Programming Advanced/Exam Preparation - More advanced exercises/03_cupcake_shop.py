from collections import deque


def stock_availability(inventory_list, deliver_or_sell, *args):
    inventory_list = deque(inventory_list)
    if deliver_or_sell == "delivery":
        inventory_list.extend(x for x in args)
    elif deliver_or_sell == "sell":
        if not args:
            inventory_list.popleft()
        else:
            for thing in args:
                if str(thing).isdigit():
                    for _ in range(thing):
                        inventory_list.popleft()
                else:
                    inventory_list = [x for x in inventory_list if x != thing]

    return list(inventory_list)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
