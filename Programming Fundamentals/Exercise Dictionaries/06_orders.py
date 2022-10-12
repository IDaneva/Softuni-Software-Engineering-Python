order_information = {}

while True:
    command = input()
    if command == "buy":
        break
    item, price, quantity = command.split()
    if item not in order_information:
        order_information[item] = [float(price), int(quantity)]
    else:
        if price not in order_information[item]:
            order_information[item][0] = float(price)
        order_information[item][1] += int(quantity)

print(order_information)

for item, price in order_information.items():
    print(f"{item} -> {(price[0] * price[1]):.2f}")