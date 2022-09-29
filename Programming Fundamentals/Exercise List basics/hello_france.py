ticket_cost = 150
items_and_prices = input().split("|")
budget = int(input())
bought_items = []
costs = 0
for element in items_and_prices:
    split_info = element.split("->")
    if split_info[0] == "Clothes":
        if float(split_info[1]) > 50:
            continue
        else:
            if budget >= float(split_info[1]):
                costs += float(split_info[1])
                bought_items.append(split_info[1])
                budget -= float(split_info[1])
    elif split_info[0] == "Shoes":
        if float(split_info[1]) > 35:
            continue
        else:
            if budget >= float(split_info[1]):
                costs += float(split_info[1])
                bought_items.append(split_info[1])
                budget -= float(split_info[1])
    elif split_info[0] == "Accessories":
        if float(split_info[1]) > 20.50:
            continue
        else:
            if budget >= float(split_info[1]):
                costs += float(split_info[1])
                bought_items.append(split_info[1])
                budget -= float(split_info[1])
total_earnings = 0

for item in bought_items:
    earnings = float(item) * 0.4 + float(item)
    total_earnings += earnings
    print(f"{earnings:.2f}", end=" ")
print("")
profit = total_earnings - costs
print(f'Profit: {profit:.2f}')

if total_earnings + budget >= ticket_cost:
    print("Hello, France!")
else:
    print("Not enough money.")
