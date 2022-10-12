miner_items = {}

while True:
    item = input()
    if item == "stop":
        break
    quantity = int(input())
    if item not in miner_items:
        miner_items[item] = 0
    miner_items[item] += quantity

for key, value in miner_items.items():
    print(f"{key} -> {value}")

