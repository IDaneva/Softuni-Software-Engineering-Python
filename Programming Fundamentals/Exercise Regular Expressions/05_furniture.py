import re

searched_pattern = r">{2}(\w+)<{2}(\d+(\.\d+)*)!(\d+)"
bought_furniture = []
total_cost = 0

while True:
    command = input()
    if command == "Purchase":
        break
    matches = re.findall(searched_pattern, command)
    for match in matches:
        bought_furniture.append(match[0])
        total_cost += float(match[1]) * int(match[3])


print(f"Bought furniture:")
for s in bought_furniture:
    print(s)
print(f"Total money spend: {total_cost:.2f}")